import aiohttp
from aiohttp import web
import asyncio

RESOLUME_API_BASE = "http://192.168.0.158:8888/api/v1"

async def fetch_compositions():
  async with aiohttp.ClientSession() as session:
    async with session.get(f"{RESOLUME_API_BASE}/composition") as resp:
      if resp.status == 200:
        return await resp.json()
      else:
         return {"error": f"Status {resp.status}"}


async def compositions_handler(request):
  data = await fetch_compositions()
  return web.json_response(data)

app = web.Application()
app.router.add_get('/composition', compositions_handler)

if __name__ == '__main__':
  web.run_app(app, port=3000)
