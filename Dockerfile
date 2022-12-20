FROM python:3.10-slim-buster
WORKDIR /app
COPY requirements.txt .
ENV PYTHONDONTWRITEBYTECODE 1
RUN pip install --upgrade pip \
    && pip install -r requirements.txt
ENTRYPOINT ["uvicorn"]
CMD ["main:app", "--reload", "--host=0.0.0.0"]
