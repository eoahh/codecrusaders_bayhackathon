from fastapi import FastAPI, File, UploadFile
import uvicorn
from app import process_image

app = FastAPI()

@app.post("/analyze_image")
async def analyze_image(file: UploadFile = File(...)):
    # Read the file data
    image_data = await file.read()
    
    # Process the image and get mean and std deviation
    result = process_image(image_data)

    return result