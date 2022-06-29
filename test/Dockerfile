FROM python:3.8.7

WORKDIR /test

ENV PATH="/test/bin:${PATH}"

COPY requirements.txt .
RUN pip install --upgrade --no-cache-dir -r requirements.txt

COPY bin bin
COPY main.py .
