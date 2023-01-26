FROM tiangolo/uvicorn-gunicorn:python3.8-slim
WORKDIR .
COPY requirements.txt .
RUN pip3 install --no-cache-dir --upgrade -r requirements.txt

COPY . .
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]