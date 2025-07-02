from pythonosc.dispatcher import Dispatcher
from pythonosc.osc_server import AsyncIOOSCUDPServer
import asyncio
import json
from functions import mongo_connect
from functions import ws_connect
from functions import subscribe_parameter
from functions import find_params, create_snapshot, update_project_name, create_project
from functions import subscribe_all_paths
from functions import set_all_layers_opacity_from_composition
from fx import animate_param


# def handler(address, *args):
#   print(f"[OSC] Recebido: {address}, argumentos: {args}")
  # Aqui você chama suas funções, ex:
  # if address == "/corrigir_opacidade":
  #     corrigir_opacidade()


async def connect():
  # Conecta no MongoDB e ao WebScoket
  db = await mongo_connect()
  ws = await ws_connect()

  subscriptions = []

  for sub in subscriptions:
    await ws.send_json(sub)
    print(f"Enviada subscrição para {sub['parameter']}")

  first_message = True
  project_id = None

  async for msg in ws:
    data = json.loads(msg.data)

    if first_message:
      first_message = False

      with open('composition_dump.json', 'w') as f:
        json.dump(data, f, indent=2)
      print('Primeira composition salva em composition_dump.json')

      await subscribe_all_paths(["layers"], ws)
      param_ids = find_params(data)
      print(f"Encontrados {len(param_ids)} parâmetros para subscrição.")
      for param_id in param_ids[:1]:
          await subscribe_parameter(ws, param_id)

      project_id = data.get('name', {}).get('id')

      if project_id is None:
        print('ID do projeto não encontrado na mensagem.')
        continue

      project = await db['projects'].find_one({'name.id': project_id})

      if project is None:
        await create_project(db, project_id, data.get('name'))
        await create_snapshot(db, project_id, data)
        print('Projeto e snapshot criados no Mongo')
    else:
      # Processa qualquer alteração recebida após a inicialização
      # 1. Se for alteração em layers
      if 'path' in data and isinstance(data['path'], str) and data['path'].startswith('/composition/layers'):
        print("Alteração na layer detectada!")
        print("Mensagem recebida:", data)
        # Aqui pode salvar snapshot, atualizar Mongo, etc.

      # 2. Alteração de nome do projeto
      elif 'path' in data and '/name' in data['path']:
        project_id_update = data.get('id') or data.get('parameterId')
        if project_id_update:
          project = await db['projects'].find_one({'name.id': project_id_update})
          if project:
            old_name = project['name'].get('value')
            new_name = data.get('value')
            await update_project_name(db, project_id_update, new_name)
            await create_snapshot(db, project_id_update, data)
            print(f"Nome do projeto foi alterado de {old_name} para {new_name}.")
      # 3. Debug geral (ativar se quiser ver todas as mensagens)
      # print(f"Mensagem recebida: {data}")


if __name__ == '__main__':
  asyncio.run(connect())
