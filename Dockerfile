FROM python:3.11

WORKDIR /app

COPY *.py /app
COPY requirements.txt /app

RUN pip install --no-cache-dir -r requirements.txt
RUN python weights_download.py

EXPOSE 7860

ENV GRADIO_SERVER_NAME="0.0.0.0"

CMD ["python", "app.py"]