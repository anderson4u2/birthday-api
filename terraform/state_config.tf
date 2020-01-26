terraform {
  backend "gcs" {
    bucket  = "encoded-pointer-265615-terraform"
    prefix  = "terraform/state"
  }
}
