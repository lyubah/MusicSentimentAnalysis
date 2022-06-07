FROM huggingface/transformers-all-latest-gpu

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt


CMD ["python3", "app.py"]