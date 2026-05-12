#!/usr/bin/env python3
import os
import time
import sys
import torch
import boto3
from prometheus_client import start_http_server, Gauge


if not torch.cuda.is_available():
    print("ERROR: No GPU found")
    sys.exit(1)

print(f"GPU found: {torch.cuda.get_device_name(0)}")


start_http_server(8080)
gpu_active = Gauge("gpu_active", "1 if GPU is available, else 0")
gpu_active.set(1)

print("Prometheus metrics on port 8080")


EPOCHS = int(os.environ.get("EPOCHS", 10))
for i in range(EPOCHS):
    print(f"Training step {i+1}/{EPOCHS} - GPU is working")
    time.sleep(1)


bucket = os.environ.get("MODEL_BUCKET", "your-bucket")
s3 = boto3.client("s3")
s3.put_object(Bucket=bucket, Key="result.txt", Body=b"GPU job finished")
print(f"Uploaded result to s3://{bucket}/result.txt")
print("All done.")