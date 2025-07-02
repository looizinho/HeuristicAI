import asyncio
import random
import sys
import os
import shutil

os.system('clear && printf "\\e[3J"')

def print_user_input(text):
    columns = shutil.get_terminal_size((80, 20)).columns
    formatted = text.rjust(columns)
    print(f"\033[1;32m{formatted}\033[0m")

def print_header():
  print("\033[1;35m" + "=" * 38)
  print("🤖  HeuristicAI - MockAI Chat (Wilker)")
  print("=" * 38 + "\033[0m\n")
os.system('clear && printf "\\e[3J"')
print_header()

falas = [
  "Bom dia, Luizinho.",
  "Ué Luizinho, tu já me conhece. Sou Wilker, a inteligência artificial através da HeuristicAI, uma plataforma de boa, bla bla...",
  "Manda ver, tamo junto!",
  # Essa fala faz a ação junto!
  "Luizinho, identifiquei aqui que tinham duas Layers em 50%… já ajustei aqui.",
  "Valeu. Obrigado.",
  "Sim, é pra já!",
  "Prontinho, tá na mão. Já deixei um Solid Color em cada camada aqui.",
  "Precisar, tamo aê.",
]

# Índices em que Wilker espera input do Luizinho antes de responder:
INPUT_BEFORE = {0, 1, 2, 4, 5}


async def main(ws=None, composition_data=None, db=None):
  for idx, fala in enumerate(falas):
    if idx in INPUT_BEFORE:
      user_text = input("\033[1;32mL: \033[0m")
      print_user_input(f"L: {user_text}")
    await asyncio.sleep(random.uniform(1.5, 3.0))
    print(f"\033[1;36mW: {fala}\033[0m")  # Wilker em azul
    if "Solid Color" in fala:
      user_text = input("\033[1;32mL: \033[0m")
      print_user_input(f"L: {user_text}")

    # Se for o momento de corrigir as opacidades:
    if "identifiquei aqui" in fala and ws and composition_data:
      # await set_all_layers_opacity_from_composition(ws, composition_data, db)
      print("\033[1;33m[MockAI] Opacidades corrigidas!\033[0m")
  while True:
    user = input("\033[1;32mL: \033[0m")
    print_user_input(f"L: {user}")
    user = user.strip().lower()
    if user in ["encerrar conversa", "encerrar", "sair", "exit", "fim"]:
      print("\033[1;36mW: Valeu demais, Luizinho! Até a próxima. 👋\033[0m")
      sys.exit(0)
    else:
      print("\033[1;36mW: Só encerrar quando quiser, viu? 😉\033[0m")


if __name__ == '__main__':
  asyncio.run(main())
