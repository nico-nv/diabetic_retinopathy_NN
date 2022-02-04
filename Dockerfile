FROM python:3.8.6-buster

COPY model.tflite /model.tflite
COPY diabetic_retinopathy_NN /diabetic_retinopathy_NN
COPY api /api
COPY requirements.txt /requirements.txt

RUN pip install -r requirements.txt

CMD uvicorn api.fast:app --host 0.0.0.0 --port $PORT
