resource "minio_s3_bucket" "datalake-transient-bucket" {
  bucket = "datalake-transient"
  acl = "private"
}

resource "minio_s3_bucket" "datalake-bronze-bucket" {
  bucket = "datalake-bronze"
  acl = "private"
}

resource "minio_s3_bucket" "datalake-silver-bucket" {
  bucket = "datalake-silver"
  acl = "private"
}

resource "minio_s3_bucket" "datalake-gold-bucket" {
  bucket = "datalake-gold"
  acl = "private"
}