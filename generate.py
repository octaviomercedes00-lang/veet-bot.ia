from fastapi import APIRouter
from fastapi.responses import StreamingResponse
from core.llm_stream import stream_bdfd

router = APIRouter(prefix="/generate")

@router.post("/stream")
def generate_stream(prompt: str):
    return StreamingResponse(stream_bdfd(prompt), media_type="text/plain")