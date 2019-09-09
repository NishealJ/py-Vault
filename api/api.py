import subprocess
import json

# Constant Commands

# This command is used to get the vault status.
VAULT_STATUS_COMMAND = ['vault', 'status']

def check_vault_server():

	vault_status = subprocess.Popen(VAULT_STATUS_COMMAND, 
        stdout=subprocess.PIPE, 
        stderr=subprocess.STDOUT)
	stdout = vault_status.stdout.read()
	if "Error" in stdout:
		print "Error: Running the vault server.."
		print stdout
		return 0
	else:
		return 1

def vault_server_details():
	if check_vault_server():
		vault_details = subprocess.Popen(VAULT_STATUS_COMMAND, 
        stdout=subprocess.PIPE, 
        stderr=subprocess.STDOUT)
		stdout = vault_details.stdout.read()
		return stdout
	else:
		return 0

def write_vault_secret(path, pair = []):
	# The parameter path is the path to the secrect
	# it should be prefixed with secret.
	path = 'secret/' + path
	# The second parameter is of type list is the data pair
	# which you want to keep in the vault.
	# i.e user = xyz or db_name = xyz

	# This command is used to put secrets in vault.
	VAULT_SECRET_WRITE = ['vault', 'kv', 'put']

	VAULT_SECRET_WRITE.append(path)
	VAULT_SECRET_WRITE = VAULT_SECRET_WRITE + pair
	vault_status = subprocess.Popen(VAULT_SECRET_WRITE, 
        stdout=subprocess.PIPE, 
        stderr=subprocess.STDOUT)
	stdout = vault_status.stdout.read()

def get_vault_secret(field, path):
	# The parameter field is the key which you want to rer=trive
	# frome the vault example db_name or user.
	
	# This command is used to get secrets from vault.
	VAULT_SECRET_GET = ['vault', 'kv', 'get']

	VAULT_SECRET_GET.append('-field='+field)
	# The second parameter is the path of the secret
	path = 'secret/' + path
	VAULT_SECRET_GET.append(path)
	vault_status = subprocess.Popen(VAULT_SECRET_GET, 
        stdout=subprocess.PIPE, 
        stderr=subprocess.STDOUT)
	stdout = vault_status.stdout.read()
	return stdout
