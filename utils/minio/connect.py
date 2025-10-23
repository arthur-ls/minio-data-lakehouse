from minio import Minio

def minio_connect(access_key, secret_key, host='localhost', port='9000', secure=False):
    return Minio(
        f"{host}:{port}",
        access_key=access_key,
        secret_key=secret_key,
        secure=secure
    )