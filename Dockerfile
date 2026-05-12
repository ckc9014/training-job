FROM nvidia/cuda:12.1-base-ubuntu22.04


RUN apt-get update && apt-get install -y python3 python3-pip && rm -rf /var/lib/apt/lists/*


WORKDIR /app


COPY requirements.txt .


RUN pip3 install --no-cache-dir -r requirements.txt


COPY src/ .


EXPOSE 8080


ENTRYPOINT ["python3", "train.py"]
CMD ["--epochs", "10"]