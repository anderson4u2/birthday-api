variable "project" {
  default = "undefined"
}

variable "region" {
  default = "europe-west1"
}

variable "zones" {
  default = [
    "europe-west1-b",
    "europe-west1-c",
    "europe-west1-d",
  ]
}

variable "zone" {
  default = "undefined"
}

variable "master_k8s_version" {
  default = "undefined"
}

variable "initial_node_count" {
  default = "1"
}

variable "remove_default_node_pool" {
  default = true
}

variable "logging_service" {
  default = "none"
}

variable "monitoring_service" {
  default = "none"
}

variable "network" {
  default = "default"
}

variable "subnetwork" {
  default = "default"
}

variable "cluster_name" {
}
