export BUCKET             := $(TF_BUCKET)
export ROOTDIR            := $(ROOTDIR)

#/ clean .terraform and old state
clean-terraform:
	@find "$(ROOTDIR)" -type f -name terraform.tfstate -exec rm -v {} +
	@find "$(ROOTDIR)" -type f -name terraform.tfstate.backup -exec rm -v {} +

## terraform plan
plan: clean-terraform
	cd "terraform" ; \
	terraform init \
		-backend-config="path=state_config.tf" \
		-get=true -get-plugins=true -force-copy=true -input=false
	cd "terraform" ; \
	terraform plan \
		-detailed-exitcode \
		-var-file=config.tfvars

## terraform apply
apply: clean-terraform
	cd "terraform" ; \
	terraform init \
		-backend-config="path=state_config.tf" \
		-get=true -get-plugins=true -force-copy=true -input=false
	cd "terraform" ; \
	terraform apply -auto-approve \
		-var-file=config.tfvars

## preview what terraform will destroy
destroy-plan: clean-terraform
	cd "terraform" ; \
	terraform init \
		-backend-config="path=state_config.tf" \
		-get=true -get-plugins=true -force-copy=true -input=false
	cd "terraform" ; \
	terraform plan -destroy \
		-var-file=config.tfvars


## destroy infrastructure with terraform
destroy-apply: clean-terraform
	cd "terraform" ; \
	terraform init \
		-backend-config="path=state_config.tf" \
		-get=true -get-plugins=true -force-copy=true -input=false
	cd "terraform" ; \
	terraform destroy -force \
		-var-file=config.tfvars

# Bring up api locally
compose-up:
	docker-compose -f devops/docker-compose.yml up --build -d

# Stop all local resources 
compose-stop:
	docker-compose -f devops/docker-compose.yml stop

# Stop and start all containers
compose-restart: compose-stop compose-up

# Delete all local resources apart from postgres data volume 
compose-down:
	docker-compose -f devops/docker-compose.yml down

# Delete all local resources 
compose-clean:
	docker-compose -f devops/docker-compose.yml down && \
	docker volume rm postgres-data
