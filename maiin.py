from fastapi import FastAPI, UploadFile, File
from tensorflow.keras.models import load_model
import cv2
import numpy as np

app = FastAPI()

model = load_model(r"C:\Users\Lenovo\deepfake_model.h5")

@app.get("/")
def home():
    return {"message": "Model Loaded Successfully"}

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    contents = await file.read()

    np_img = np.frombuffer(contents, np.uint8)

    img = cv2.imdecode(np_img, cv2.IMREAD_COLOR)

    img = cv2.resize(img, (128,128))

    img = img / 255.0

    img = img.reshape(1,128,128,3)

    prediction = model.predict(img)

    if prediction[0][0] > 0.5:
        result = "REAL"
    else:
        result = "FAKE"

    return {
        "prediction": result,
        "confidence": float(prediction[0][0])
    }