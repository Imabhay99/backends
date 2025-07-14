# routes/cloth_routes.py
from fastapi import APIRouter, UploadFile, File, Form
from controllers.cloth_controller import process_virtual_tryon

router = APIRouter()

@router.post("/tryon")
async def tryon_cloth(
    prompt: str = Form(...),
    image: UploadFile = File(...)
):
    return await process_virtual_tryon(image, prompt)
