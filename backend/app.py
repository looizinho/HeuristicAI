import aiohttp
from aiohttp import web
import aiohttp_cors
import asyncio
import motor.motor_asyncio
from datetime import datetime

MONGO_URI = "mongodb://localhost:27017"
MONGO_DB = "arena"
MONGO_COLLECTION = "composition_snapshots"

mongo_client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_URI)
db = mongo_client[MONGO_DB]
collection = db[MONGO_COLLECTION]

# RESOLUME_API_BASE = "http://192.168.0.158:8888/api/v1"
RESOLUME_API_BASE = "http://localhost:8888/api/v1"


async def fetch_compositions():
    async with aiohttp.ClientSession() as session:
        async with session.get(f"{RESOLUME_API_BASE}/composition") as resp:
            if resp.status == 200:
                data = await resp.json()
                # Inserir no MongoDB
                await collection.insert_one({
                    "timestamp": int(datetime.utcnow().timestamp()),
                    "composition": data
                })
                return data
            else:
                return {"error": f"Status {resp.status}"}


async def compositions_handler(request):
    data = await fetch_compositions()
    return web.json_response(data)


async def snapshots_handler(request):
    cursor = collection.find().sort("timestamp", -1)
    snapshots = []
    async for doc in cursor:
        doc["_id"] = str(doc["_id"])
        if isinstance(doc["timestamp"], datetime):
            doc["timestamp"] = doc["timestamp"].isoformat()
        snapshots.append(doc)
    return web.json_response(snapshots)


async def log_change(event: dict):
    event['actor'] = 'user'
    event['timestamp'] = int(datetime.utcnow().timestamp())
    await db["changes"].insert_one(event)


async def register_command(command: dict):
    command['actor'] = 'system'
    command['timestamp'] = int(datetime.utcnow().timestamp())
    await db["commands"].insert_one(command)
    await send_to_resolume(command)  # Se tiver envio imediato


# --- summary_handler ---
async def summary_handler(request):
    latest = await collection.find_one(sort=[("timestamp", -1)])
    if not latest:
        return web.json_response({"error": "No composition data available"}, status=404)

    composition = latest.get("composition", {})
    layers = composition.get("layers", [])
    columns = composition.get("columns", [])

    total_clips = sum(len(layer.get("clips", [])) for layer in layers)
    autopilot_layers = [
        layer.get("name", {}).get("value", f"Layer {i}")
        for i, layer in enumerate(layers)
        if layer.get("autopilot", {}).get("enabled", False)
    ]

    looping_clips = []
    for i, layer in enumerate(layers):
        for clip in layer.get("clips", []):
            autopilot = clip.get("autopilot", {})
            if autopilot.get("action") in ["Play First Clip", "Play Specific Clip"]:
                looping_clips.append({
                    "layer": layer.get("name", {}).get("value", f"Layer {i}"),
                    "clip": clip.get("name", {}).get("value", "Unnamed Clip"),
                    "loop_type": autopilot["action"]
                })

    summary = {
        "project_name": composition.get("name", {}).get("value", "Unknown"),
        "layers": len(layers),
        "columns": len(columns),
        "total_clips": total_clips,
        "autopilot_layers": len(autopilot_layers),
        "idle_duration_seconds": 0,  # Placeholder, calcularemos depois
        "pip_layers": [],  # Placeholder
        "looping_clips": looping_clips
    }

    return web.json_response(summary)


app = web.Application()
app.router.add_get('/composition', compositions_handler)
app.router.add_get('/snapshots', snapshots_handler)
app.router.add_get('/summary', summary_handler)

async def websocket_handler(request):
    ws = web.WebSocketResponse()
    await ws.prepare(request)
    try:
        async for msg in ws:
            if msg.type == aiohttp.WSMsgType.TEXT:
                # Aqui você pode processar mensagens recebidas
                await ws.send_str(f"Echo: {msg.data}")
            elif msg.type == aiohttp.WSMsgType.ERROR:
                print(f'WebSocket connection closed with exception {ws.exception()}')
    finally:
        print('WebSocket connection closed')
    return ws

app.router.add_get('/ws', websocket_handler)

cors = aiohttp_cors.setup(app, defaults={
    "*": aiohttp_cors.ResourceOptions(
        allow_credentials=True,
        expose_headers="*",
        allow_headers="*",
    )
})

for route in list(app.router.routes()):
    cors.add(route)

if __name__ == '__main__':
    web.run_app(app, port=3000)
