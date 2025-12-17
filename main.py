from fastapi import FastAPI
from routes.generate import router as gen
from auth.routes import router as auth
from projects.routes import router as projects

app = FastAPI(title="VEET IA ULTIMATE")
app.include_router(gen)
app.include_router(auth)
app.include_router(projects)