##NN: Nuevo

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi import UploadFile, File

from diabetic_retinopathy_NN.read import read_imagen
from diabetic_retinopathy_NN.predict import predict_imagen

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)


@app.get("/")
def index():
    return {"greeting": "Hello world"}


@app.post("/predict/image")
async def predict_api(file: UploadFile = File(...)):
    extension = file.filename.split(".")[-1] in ("jpeg", "jpg", "png")
    if not extension:
        return "Image must be jpeg, jpg or png format!"
    image = read_imagen(await file.read())
    prediction = predict_imagen(image)

    return prediction


##make run_api
##http://localhost:8000/
##http://localhost:8000/docs
