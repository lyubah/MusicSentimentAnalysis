FROM pytorch/pytorch

WORKDIR /app

COPY . .

EXPOSE 8080

RUN python3 -m pip install -r requirements.txt

CMD ["python", "app.py"]