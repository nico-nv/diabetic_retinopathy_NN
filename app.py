#Nuevo

import numpy as np
import streamlit as st
from PIL import Image
#import requests

#import cv2
import tensorflow as tf

st.markdown("""
    # title
    ## subtitles
""")

img_file_buffer = st.file_uploader("Upload an image", type=["jpeg"])

if img_file_buffer is not None:
    image = Image.open(img_file_buffer)
    #img_array = np.array(image) # if you want to pass it to OpenCV

    #url = "http://localhost:8000/predict"
    #params = dict(imagen=1010)
    #response = requests.get(url, params=img_array)
    #prediction = response.json()

    img = np.asarray(image.resize((224, 224)))[..., :3]
    img = np.expand_dims(img, 0)

    #fp = f'{path}/{ls_4[0]}'
    #img = cv2.imread(image)
    #img = cv2.resize(img, (224, 224))
    #img = np.expand_dims(img, 0)

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

    st.image(image, caption=c, use_column_width=True)


#make streamlit

#params
#'imagen': array([[[0, 0, 0], [0, 0, 0], [0, 0, 0], ..., [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], ..., [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], ..., [0, 0, 0], [0, 0, 0], [0, 0, 0]], ..., [[0, 0, 0], [0, 0, 0], [0, 0, 0], ..., [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], ..., [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], ..., [0, 0, 0], [0, 0, 0], [0, 0, 0]]], dtype=uint8)}
#= img = cv2.imread(fp)