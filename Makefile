include .env

PATH_TF=./iac
define tfdir
	-chdir="${PATH_TF}"
endef

define tf_backend
	-backend-config="bucket=${TF_BUCKET}" -backend-config="key=${PROJECT_NAME}/${ENV}/terraform.tfstate"
endef

define tf_vars
	-var="PROJECT_NAME=${PROJECT_NAME}" -var="ENV=${ENV}"
endef

tf-init:
	@terraform ${tfdir} init -upgrade ${tf_backend} -reconfigure

tf-plan:
	@terraform ${tfdir} plan -out=tf_planned ${tf_vars}

tf-apply:
	@terraform ${tfdir} apply --auto-approve tf_planned