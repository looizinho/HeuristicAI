import aiohttp
import asyncio
import motor.motor_asyncio
from datetime import datetime


# Conectar ao Banco de Dados
async def mongo_connect():
  mongo_client = motor.motor_asyncio.AsyncIOMotorClient('mongodb://localhost:27017')
  db = mongo_client['arena']
  print('Conectado ao MongoDB')
  return db


# Abrir Conexão WebSocket
async def ws_connect():
  session = aiohttp.ClientSession()
  ws = await session.ws_connect('ws://localhost:8080/api/v1')
  print('Conectado ao WebSocket')
  return ws


# Subscrever em parametro
async def subscribe_parameter(ws, param_id):
  sub_msg = {"action": "subscribe", "parameter": f"/parameter/by-id/{param_id}"}
  await ws.send_json(sub_msg)
  print(f"Subscrito parâmetro {param_id}")


# Localizar parametro
def find_params(obj):
  ids = []
  if isinstance(obj, dict):
    if 'id' in obj:
      ids.append(obj['id'])
    for v in obj.values():
      ids.extend(find_params(v))
  elif isinstance(obj, list):
    for item in obj:
      ids.extend(find_params(item))
  return ids


# Criar snapshot no Banco de Dados
async def create_snapshot(db, project_id, data):
  snapshot = {
    'project_id': project_id,
    'snapshot_data': data
  }
  await db['snapshots'].insert_one(snapshot)


# Atualizar nome do projeto no Banco de Dados
async def update_project_name(db, project_id, new_name):
  await db['projects'].update_one(
    {'name.id': project_id},
    {'$set': {'name.value': new_name}}
  )


# Criar projeto no Banco de Dados
async def create_project(db, project_id, name_obj):
  await db['projects'].insert_one({
    'name': name_obj,
    'created_at': datetime.utcnow()
  })


# Alterar nome do projeto no Arena
async def alterar_nome_projeto(novo_nome, id_param):
  async with aiohttp.ClientSession() as session:
    url = f"http://localhost:8080/api/v1/parameter/by-id/{id_param}"
    payload = {
      "value": novo_nome
    }
    async with session.put(url, json=payload) as resp:
      print(f"Status: {resp.status}")
      print("Resposta:", await resp.text())

  # Exemplo de uso (substitua pelo ID real do parâmetro de nome do projeto):
  # asyncio.run(alterar_nome_projeto("ARENA TESTE 2", 1751314738451))


# Subscrever em múltiplos caminhos de composição
async def subscribe_all_paths(paths: list[str], ws):
  async with aiohttp.ClientSession() as session:
    async with session.get('http://localhost:8080/api/v1/composition') as base_resp:
      if base_resp.status != 200:
        print("Erro ao acessar /composition")
        return

      base_data = await base_resp.json()

      for path in paths:
        items = base_data.get(path, [])
        print(f"Encontrados {len(items)} itens em '{path}'.")

        for idx in range(1, len(items) + 1):
          async with session.get(f'http://localhost:8080/api/v1/composition/{path}/{idx}') as item_resp:
            if item_resp.status != 200:
              print(f"Erro ao acessar /composition/{path}/{idx}")
              continue
            item_data = await item_resp.json()
            param_ids = find_params(item_data)
            for param_id in param_ids:
              await subscribe_parameter(ws, param_id)


# Monitorar alterações no Arena
async def handle_composition_update(data, db, ws):
  from copy import deepcopy

  project_id = data.get('name', {}).get('id')
  if not project_id:
    print("ID do projeto não encontrado.")
    return

  last_snapshot = await db['snapshots'].find_one(
    {'project_id': project_id},
    sort=[('_id', -1)]
  )

  new_ids = set(find_params(data))
  old_ids = set(find_params(last_snapshot['snapshot_data'])) if last_snapshot else set()

  added_ids = new_ids - old_ids
  print(f"Encontrados {len(added_ids)} novos parâmetros para subscrição.")

  for param_id in added_ids:
    await subscribe_parameter(ws, param_id)

  await create_snapshot(db, project_id, deepcopy(data))


# Alterar valor de um parâmetro do Arena via HTTP
async def set_param_value(param_id, value):
  async with aiohttp.ClientSession() as session:
    url = f"http://localhost:8080/api/v1/parameter/by-id/{param_id}"
    payload = {"value": value}
    async with session.put(url, json=payload) as resp:
      print(f"[Set Opacity] Param ID {param_id}: Status {resp.status}")


# Definir opacidade de todas as layers para 100%
async def set_all_layers_opacity(ws):
  async with aiohttp.ClientSession() as session:
    for idx in range(1, len(layers) + 1):
      async with session.get(f'http://localhost:8080/api/v1/composition/layers/{idx}') as layer_resp:
        if layer_resp.status != 200:
          continue
        layer_data = await layer_resp.json()
        opacity = layer_data.get("video", {}).get("opacity", {})
        param_id = opacity.get("id")
        if param_id:
          await set_param_value(param_id, 1.0)


from fx import animate_param


async def set_all_layers_opacity_from_composition(ws, composition_data, db=None):
  layers = composition_data.get("layers", [])
  print(f"[MockAI] Corrigindo opacidade de {len(layers)} layers...")

  for layer in layers:
    opacity = layer.get("video", {}).get("opacity", {})
    param_id = opacity.get("id")
    current_value = opacity.get("value", 0.5)
    path = f"/composition/layers/{layers.index(layer) + 1}/video/opacity"

    print(f"[Debug] Layer Opacity -> ID: {param_id}, Current: {current_value}, Path: {path}")

    if param_id:
      await set_param_value(param_id, 1.0)
