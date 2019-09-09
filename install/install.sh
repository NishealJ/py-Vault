# MacOs Starter Installation scripts for vault

# Download Vault into some temp directory
curl -L "https://releases.hashicorp.com/vault/1.2.2/vault_1.2.2_darwin_amd64.zip" > /tmp/vault.zip

# Unzip vault to the temp directory
cd /tmp
sudo unzip vault.zip
sudo mv vault /usr/local/bin

# Export the vault devserer Address
export VAULT_ADDR='http://127.0.0.1:8200'

