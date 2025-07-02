import asyncio
from datetime import datetime


async def animate_param(ws, param_id: int, from_value: float, to_value: float, duration_ms: int, steps: int = 30,
                        db=None, path=""):
  print(
    f"[animate_param] Called with: param_id={param_id}, from={from_value}, to={to_value}, duration={duration_ms}, path={path}")

  await ws.send_json({
    "action": "set",
    "parameter": param_id,
    "value": to_value
  })
  print(f"[animate_param] Sent: param_id={param_id}, value={to_value}")

  if db is not None and path is not None:
    await log_param_change(db, param_id, path, from_value, to_value)


def path_to_human(path: str) -> str:
  # Remove a primeira barra e capitaliza cada parte
  parts = path.strip('/').split('/')
  return ' '.join(part.capitalize() if not part.isdigit() else part for part in parts)


async def log_param_change(db, param_id: int, path: str, old_value: float, new_value: float, origin: str = "mockai"):
  message = f"{path_to_human(path)} set to {round(new_value * 100)}%"
  await db['param_changes'].insert_one({
    "timestamp": datetime.utcnow(),
    "param_id": param_id,
    "path": path,
    "old_value": old_value,
    "new_value": new_value,
    "message": message,
    "origin": origin
  })
