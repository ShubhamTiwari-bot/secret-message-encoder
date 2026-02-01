from fastapi import APIRouter, HTTPException
from models.request_model import MessageRequest
from core.encoder_factory import EncoderFactory

router = APIRouter()

@router.post("/encode")
def encode_message(request: MessageRequest):
    try:
        encoder = EncoderFactory.get_encoder(request.type)
        result = encoder.encode(request.message)
        return {"result": result}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/decode")
def decode_message(request: MessageRequest):
    try:
        encoder = EncoderFactory.get_encoder(request.type)
        result = encoder.decode(request.message)
        return {"result": result}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
