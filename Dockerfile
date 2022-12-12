FROM python:3.9.15

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./predict.py /code/predict.py

COPY ./models/pipeline.bin /code/models/pipeline.bin

CMD ["uvicorn", "predict:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]