
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime
import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# internal imports
#from demo_engine.demo import place_demo_bet, ai_generate_ticket, cleanup_old_demo

app = FastAPI(title="Analises Esportivas Pro - Backend (FINAL)")
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])

@app.get("/")
def root():
    return {"status":"online", "time": datetime.utcnow().isoformat()}

@app.get("/api/health")
def health():
    return {"status":"ok"}

@app.post("/api/bet/demo")
def bet_demo(account_id: str, payload: dict):
    return place_demo_bet(account_id, payload)

@app.post("/api/ai/generate")
def gen(matches: list):
    return ai_generate_ticket(matches)

@app.delete("/api/cleanup")
def cleanup():
    return cleanup_old_demo()
