provider "minio" {
  minio_server   = "localhost:9000"
  minio_user     = "abcd"
  minio_password = "abcd2345"
}

terraform {
  required_providers {
    minio = {
      source  = "aminueza/minio"
      version = ">= 3.0.0"
    }
  }
  backend "s3" {
    bucket                      = "tf-bucket"
    key                         = "state/terraform.tfstate"
    region                      = "main"
    endpoints                   = {s3: "http://localhost:9000"}
    access_key                  = "abcd"
    secret_key                  = "abcd2345"
    skip_credentials_validation = true
    skip_metadata_api_check     = true
    skip_region_validation      = true
    skip_requesting_account_id  = true
    use_path_style            = true
  }
}