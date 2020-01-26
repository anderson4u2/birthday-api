provider "google" {
  project = var.project
  region  = var.region
  version = "~> 2"
}

resource "google_service_account" "gke-service-account" {
  account_id   = "gke-nodes"
  display_name = "Service account for GKE nodes"
}

data "google_iam_policy" "gke-nodes" {
  binding {
    role = "roles/cloudsql.client"
    members = [
      "serviceAccount:${google_service_account.gke-service-account.email}",
    ]
  }

  binding {
    role = "roles/monitoring.metricWriter"
    members = [
      "serviceAccount:${google_service_account.gke-service-account.email}",
    ]
  }

  binding {
    role = "roles/logging.logWriter"
    members = [
      "serviceAccount:${google_service_account.gke-service-account.email}",
    ]
  }
}

resource "google_service_account_iam_policy" "gke-nodes-account-iam" {
  service_account_id = google_service_account.gke-service-account.name
  policy_data        = data.google_iam_policy.gke-nodes.policy_data
}

module "gke" {
  source                     = "terraform-google-modules/kubernetes-engine/google"
  project_id                 = var.project
  name                       = var.cluster_name
  region                     = var.region
  regional                   = true
  zones                      = var.zones
  network                    = var.network
  subnetwork                 = var.subnetwork
  # ip_range_pods              = var.subnetwork
  # ip_range_services          = var.subnetwork
  http_load_balancing        = true
  horizontal_pod_autoscaling = true
  network_policy             = true
  remove_default_node_pool   = true
  create_service_account     = false

  node_pools = [
    {
      name               = "backend-node-pool"
      machine_type       = "n1-standard-2"
      min_count          = 1
      max_count          = 2
      local_ssd_count    = 0
      disk_size_gb       = 20
      disk_type          = "pd-standard"
      image_type         = "COS"
      auto_repair        = true
      auto_upgrade       = false
      service_account    = "gke-nodes@${var.project}.iam.gserviceaccount.com"
      service_account    = google_service_account.gke-service-account.email
      preemptible        = false
      initial_node_count = 1
    },
  ]

  node_pools_oauth_scopes = {
    all = [
      "https://www.googleapis.com/auth/sqlservice.admin",
      "https://www.googleapis.com/auth/logging.write",
      "https://www.googleapis.com/auth/monitoring.write",
    ]
  }

  node_pools_labels = {
    all = {
      service = "backend"
    }
  }
}
