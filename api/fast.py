#NN: Nuevo

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

#from diabetic_retinopathy_NN.predict import predict

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

#@app.get("/predict")
#def predict():
#    return {"greeting": "Hello world 2"}

import numpy as np
import pandas as pd
#import os
import cv2
import tensorflow as tf

@app.get("/predict")
def predict(imagen):

    #fp = f'{path}/{ls_4[0]}'
    img = cv2.imread(imagen)
    img = cv2.resize(img, (224, 224))
    img = np.expand_dims(img, 0)

    # Load the TFLite model and allocate tensors.
    interpreter = tf.lite.Interpreter("model.tflite")
    interpreter.allocate_tensors()

    # Get input and output tensors.
    input_details = interpreter.get_input_details()
    output_details = interpreter.get_output_details()

    # Test the model on random input data.
    input_shape = input_details[0]['shape']
    input_data = np.array(img, dtype=np.uint8)  #NN: + img
    interpreter.set_tensor(input_details[0]['index'], input_data)
    interpreter.invoke()

    # The function `get_tensor()` returns a copy of the tensor data.
    # Use `tensor()` in order to get a pointer to the tensor.
    output_data = interpreter.get_tensor(output_details[0]['index'])
    #print(output_data)

    output_probs = tf.math.softmax(output_data / 256)

    #labels = [2, 0, 4]

    d = {
        "0": np.round(output_probs.numpy()[0][1], 2),
        "2": np.round(output_probs.numpy()[0][0], 2),
        "4": np.round(output_probs.numpy()[0][2], 2)
    }

    c = max(d, key=d.get)

    return c

#make run_api
#http://localhost:8000/
#http://localhost:8000/docs
