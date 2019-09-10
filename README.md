# py-Vault

Foobar is a Python library for dealing with word pluralization.

## Installation

You can use the below script to install Vault in MacOS

```bash
bash install/install.sh
```
Further I recommend to see the vault installation guide here https://www.vaultproject.io/docs/install/

## Usage

Before using the Apis please make sure that the vault is up and running use ```start/start```,

you can use the vault api by importing the api file ```import api/api```

To check the vault status use ```check_vault_server()``` and to get the vault server details use ```vault_server_details()```

To insert the secrets in Vault pass the Secret path & Secret data to the api ```write_vault_secret(path, data)``` you can check the inserted vault secrect access the Vault UI in the Vault Address

To get the data from the fault use ```get_vault_secret(feild, path)```

See ```api/api-tests``` to know more about the usage of this library.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
