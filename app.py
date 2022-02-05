###Nuevo

import streamlit as st

import requests

#import numpy as np
#import tensorflow as tf
#from PIL import Image

st.markdown("""
    # Diabetic Retinopathy

    ## Kaggle: https://www.kaggle.com/amanneo/diabetic-retinopathy-resized-arranged
""")

image = st.file_uploader("Upload an image", type=["jpeg", 'jpg', 'png'])

if st.button("Make Prediction"):
    if image is not None:

        api_url = "http://localhost:8000/predict/"
        params = {"img_file": image.getvalue()}
        response = requests.get(api_url, files=params)
        prediction = response.json()

        st.image(image, caption=prediction, use_column_width=True)

        #image = Image.open(image)
        #img = np.asarray(image.resize((224, 224)))[..., :3]
        #img = np.expand_dims(img, 0)

    ##fp = f'{path}/{ls_4[0]}'
    ##img = cv2.imread(image)
    ##img = cv2.resize(img, (224, 224))
    ##img = np.expand_dims(img, 0)

    ## Load the TFLite model and allocate tensors.
    #interpreter = tf.lite.Interpreter("model.tflite")
    #interpreter.allocate_tensors()

    ## Get input and output tensors.
    #input_details = interpreter.get_input_details()
    #output_details = interpreter.get_output_details()

    ## Test the model on random input data.
    #input_shape = input_details[0]['shape']
    #input_data = np.array(img, dtype=np.uint8)  #NN: + img
    #interpreter.set_tensor(input_details[0]['index'], input_data)
    #interpreter.invoke()

    ## The function `get_tensor()` returns a copy of the tensor data.
    ## Use `tensor()` in order to get a pointer to the tensor.
    #output_data = interpreter.get_tensor(output_details[0]['index'])
    ##print(output_data)

    #output_probs = tf.math.softmax(output_data / 255)

    ##labels = [2, 0, 4]

    #d = {
    #    "0": np.round(output_probs.numpy()[0][1], 2),
    #    "2": np.round(output_probs.numpy()[0][0], 2),
    #    "4": np.round(output_probs.numpy()[0][2], 2)
    #}

    #c = max(d, key=d.get)

    #st.image(image, caption=c, use_column_width=True)


###make streamlit
