import subprocess

# This command is used to get the vault status.
VAULT_SERVER_START = ['vault', 'server', '-dev']

process = subprocess.Popen(VAULT_SERVER_START, stdout=subprocess.PIPE)
output, error = process.communicate()

