# HeuristicAI

Assistente inteligente para operação audiovisual em tempo real com foco em eventos ao vivo.

## Estrutura do Projeto
HeuristicAI/
├── backend/   # Servidor Python (API, persistência, análise)
├── frontend/  # Interface Vue (Vite)
├── .venv/     # Ambiente virtual local (ignorado)

## Requisitos

- Python 3.11 (via mise)
- Node.js (via mise)
- MongoDB local
- `poetry` (opcional)
- `adev` para live reload

## Como rodar

### Backend

```bash
cd backend
source ../.venv/bin/activate
adev run app.py

Frontend
cd frontend
npm install
npm run dev

Desenvolvimento
	•	Monorepo (backend + frontend)
	•	MongoDB para persistência de snapshots
	•	API REST via aiohttp
	•	Live reload com adev

Autor

