# controllers/cloth_controller.py
import os
import uuid
import subprocess
from fastapi import UploadFile
from fastapi.responses import JSONResponse

UPLOAD_DIR = "uploads/user_images"
os.makedirs(UPLOAD_DIR, exist_ok=True)

async def process_virtual_tryon(image: UploadFile, prompt: str):
    try:
        # Save image
        ext = os.path.splitext(image.filename)[-1]
        filename = f"{uuid.uuid4()}{ext}"
        filepath = os.path.join(UPLOAD_DIR, filename)

        with open(filepath, "wb") as f:
            f.write(await image.read())

        # Move to correct data location or simulate VITON-compatible input
        # Here, you should copy or generate correct input files your model needs
        # For now, we assume your model is already using `data/` directory.

        # Run the existing model pipeline (generate_all.py)
        cmd = [
            "python", "generate_all.py",
            "--model", "adgan",
            "--gpu_ids", "-1"
        ]
        process = subprocess.run(cmd, capture_output=True, text=True)

        if process.returncode != 0:
            return JSONResponse(status_code=500, content={
                "error": "Model execution failed",
                "details": process.stderr
            })

        return {
            "message": "Virtual try-on success",
            "logs": process.stdout,
            "input_image": filename,
            "prompt_used": prompt,
        }
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})
