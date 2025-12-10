
Analises Esportivas Pro - FINAL COMPLETE (Scaffold)
--------------------------------------------------

This package is a complete scaffold integrating backend (FastAPI), engine placeholders,
frontend scaffold (Next.js), and deployment files. **It does NOT contain your secrets.**

IMPORTANT:
- Do NOT commit your secrets to git.
- Use Railway/Render/Heroku environment variables or secret stores to provide keys.

To run locally:
1. Copy .env.example to .env and fill real credentials (or set environment variables).
2. pip install -r requirements.txt
3. uvicorn backend.main:app --reload --port 8080
4. Visit http://localhost:8080/api/health

To deploy to Railway:
- Create project -> upload repo or use GitHub integration
- Set environment variables in Railway settings (SUPABASE_URL, SUPABASE_SERVICE_ROLE_KEY, etc)
- Use start command: sh start.sh

