# from fastapi import FastAPI, UploadFile, Form
# from fastapi.middleware.cors import CORSMiddleware
# from fastapi.responses import StreamingResponse
# import uvicorn
# from io import BytesIO
# from PIL import Image
# import json
# import sys
# import os
# sys.path.append(os.path.dirname(os.path.abspath(__file__)))


# from src.models.dior_model import DIORModel

# app = FastAPI()

# Allow frontend (React Native) to access the backend
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],  # Replace * with your actual domain in production
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# # Load the DIOR model (placeholder)
# model = DIORModel()

# @app.post("/virtual_tryon")
# async def virtual_tryon(user_image: UploadFile, gid: str = Form(...)):
#     gid_data = json.loads(gid)

#     image_data = await user_image.read()
#     user_img = Image.open(BytesIO(image_data)).convert("RGB")

#     output_image = model.try_on(user_img, gid_data)

#     buffer = BytesIO()
#     output_image.save(buffer, format="JPEG")
#     buffer.seek(0)

#     return StreamingResponse(buffer, media_type="image/jpeg")
# if __name__ == "__main__":
#     uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from inference import run_tryon_from_urls
from utils import pose_utils
from skimage.draw import disk, line_aa, polygon




app = FastAPI()

# CORS to allow frontend to connect
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change to your frontend domain in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Request body model
class TryOnRequest(BaseModel):
    person_url: str
    cloth_url: str

# Main try-on endpoint
@app.post("/tryon")
def tryon(data: TryOnRequest):
    result_url = run_tryon_from_urls(data.person_url, data.cloth_url)
    return {"result_url": result_url}
