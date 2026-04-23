from fastapi import APIRouter
import time

router = APIRouter()

@router.post("/ingest_message")
async def ingest_message(payload: dict):
    intake_id = f"intake_{int(time.time()*1000)}"

    return {
        "ok": True,
        "intake_id": intake_id,
        "ack_text": "✅ 已收到，可繼續輸入"
    }
