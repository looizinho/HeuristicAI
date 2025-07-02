# HeusristicAI Python Backend
> By Luizinho & Wilker

## Função principal


```python
from app import connect
```


```python
  await connect()
```

## Conectar ao MongoDB


```python
import motor.motor_asyncio
from app import mongo_connect

```


```python
  async def mongo_connect():
    mongo_client = motor.motor_asyncio.AsyncIOMotorClient('mongodb://localhost:27017')
    # db = mongo_client['arena']
    print('Conectado ao MongoDB')
  await mongo_connect()
```

  ## Conectar ao WebSocket


```python
import asyncio
import aiohttp
```


```python
session = aiohttp.ClientSession()
ws = await session.ws_connect('ws://localhost:8080/api/v1')
print('Conectado ao WebSocket')
```

## Exibir _callback_ de conexão


```python
import aiohttp
import asyncio
import json


async def get_composition():
  async with aiohttp.ClientSession() as session:
    async with session.get('http://localhost:8080/api/v1/composition') as resp:
      data = await resp.json()
      print(json.dumps(data, indent=2))


await get_composition()
```

  ## Mudar nome do Projeto


```python
import asyncio
from functions import alterar_nome_projeto
```


      Cell In[4], line 1
        SELECT *
                ^
    SyntaxError: invalid syntax




```python
idProjeto = 1751228434013
novoNome = "ARENA TESTE"
```


```python
asyncio.run(alterar_nome_projeto(novoNome, idProjeto))
```


---

## 📊 Relatórios possíveis

### 🧠 Atividade da IA (MockAI)
- Quantos parâmetros alterados
- Quais foram os mais alterados
- Porcentagem de projeto modificado pela IA

### 🕐 Timeline interativa
- Mostrar num gráfico as alterações ao longo do tempo
- Filtros por layer, clip, tipo de parâmetro…

### 🧩 Diagnóstico de performance
- Detectar valores que voltam constantemente (oscilações)
- Cruzar com snapshots e ver impacto

### 🔁 Histórico de sessões
- Sessões de uso da IA
- Parâmetros alterados por sessão
- Estado antes/depois com mini-preview

---

### 🚀 Ferramentas que podemos integrar depois
- Exportação `.csv` ou `.pdf`
- Visualização no frontend via gráficos
- API para consulta e filtragem (`/history`, `/report?param=opacity`…)


# Promtp vs Código

---

## Prompt vs Código: O que cada um faz?

**Resumindo:**
- Prompt: É legal pra comportamento de linguagem, personalidade, contexto imediato, e respostas baseadas no histórico da conversa atual.
- Programação/Script: Essencial pra lógica de timing, persistência de dados, estatísticas personalizadas, gatilhos baseados em tempo real, e memória de longo prazo.

⸻

### 🟢 O que dá pra resolver só com prompt?
- Personalidade (ex: “fale como Wilker, seja brincalhão”)
- Relembrar coisas ditas na conversa (“como falei agora há pouco, Luizinho…”)
- Sugerir ações (“Você quer que eu faça isso pra você?”)
- Algumas noções vagas de tempo (ex: “Você está sumido!” se houver um gap grande de mensagens)

### 🔴 O que PRECISA programar/scriptar?
- Medir tempos reais de interação (em segundos/minutos)
- Aprender padrões específicos do usuário ao longo de muitas sessões
- Decidir, no back, quando disparar alertas (ex: timeout, atraso, pausa anormal)
- Salvar e carregar dados históricos (“Wilker, lembra quanto tempo demorei ontem?”)
- Fazer cálculos, comparações, disparar automações

⸻

### 💡 Resumo prático
- Prompt: Comportamento, jeito de falar, “pano de fundo”.
- Código: Controle de fluxo, decisões temporais, persistência, aprendizado real.

A magia tá na junção dos dois.
Exemplo:
- Código percebe que você tá devagar →
- Chama o modelo com um prompt tipo:

> “Seu operador, Luizinho, está 30% mais lento do que o habitual ao mexer em opacidade de layer. Sugira uma dica ou pergunte se precisa de ajuda, mas de maneira informal e leve.”

- O Wilker manda aquele papo “Ei Luizinho, deu ruim aí ou foi só o café que bateu errado? 😅”.

⸻

**Resumindo:**
Prompt sozinho não consegue “sentir” o tempo real, mas é ótimo pra dar o toque humano na resposta.
Pra IA ser “proativa”, tem que ter uma camada de código/automação rodando junto, monitorando e guiando os prompts.
