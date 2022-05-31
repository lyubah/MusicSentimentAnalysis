FROM lyubah/musicsentiment:1
WORKDIR /app
COPY . .

RUN pip install -r requirements.txt


CMD ["python3", "app.py"]



