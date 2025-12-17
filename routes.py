from fastapi import APIRouter

router = APIRouter(prefix="/projects")
projects = {}

@router.post("/save")
def save(name: str, code: str, user: str):
    projects.setdefault(user, {})[name] = code
    return {"saved": True}

@router.get("/list")
def list_projects(user: str):
    return projects.get(user, {})