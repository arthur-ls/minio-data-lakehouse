from minio import Minio
from task.extract.get_data import ImportData
from pandas import DataFrame
from utils.yaml.yaml_reader import get_yaml_paths, read_yaml_file
from io import BytesIO
import pyarrow as pa
import pyarrow.parquet as pq
import os

YAML_FOLDER = os.path.dirname(__file__) + "/*.yml"

print('connecting minio')
client = Minio(
    "localhost:9000",
    access_key="abcd",
    secret_key="abcd2345",
    secure=False
)
print('connected minio')

print('getting yml path')
print(get_yaml_paths(yaml_folder=YAML_FOLDER))
for file in get_yaml_paths(yaml_folder=YAML_FOLDER):
    print('saved yml path')
    print('getting yml data')
    yaml_data = read_yaml_file(file_path=file)
    print('saved yml data')

    print('getting data')
    kaggle_project_path = yaml_data['kaggle_project']
    kaggle_file_paths = yaml_data['file_path']

    import_data = ImportData(kaggle_project=kaggle_project_path)

    for kaggle_files in kaggle_file_paths:
        df = import_data.get_kaggle_data(file_path=kaggle_files)
        print('got data')

        table = pa.Table.from_pandas(df)
        parquet_buffer = BytesIO()
        pq.write_table(table, parquet_buffer)
        parquet_buffer.seek(0)

        bucket_name = "teste-bucket"
        object_name = "year=2025/month=10/day=22/teste.parquet"

        if not client.bucket_exists(bucket_name):
            client.make_bucket(bucket_name)

        client.put_object(
            bucket_name,
            object_name,
            data=parquet_buffer,
            length=len(parquet_buffer.getvalue()),
            content_type="application/octet-stream"
        )
        print(f"DataFrame uploaded as Parquet to MinIO: {bucket_name}/{object_name}")