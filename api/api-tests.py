import api

# Test the vault apis for get/put of secret in vault api, 
# make sure that vault server is running.

# Path to insert the secrect
PATH_TO_SECRET = 'hello'

# SECRET
SECRET = ['db_name=mysql', 'user=root']

# SECRET FIELD 
SECRET_FIELD_1 = 'db_name'
SECRET_FIELD_2 = 'user'

# Def to test two details.
def _expect(arg1, arg2, test_no):
	if arg1 == arg2:
		print "Pass: Passed the test " + test_no
	else: 
		print "Fail: Test " + test_no + " failed" 
	pass

if api.check_vault_server():

	# Write the secret to the given path
	api.write_vault_secret(PATH_TO_SECRET, SECRET)

	# Get the secrect feild from the vault

	# First secrect pair is db_name=mysql
	SECRECT_VALUE_1 = api.get_vault_secret(SECRET_FIELD_1, PATH_TO_SECRET)
	_expect(SECRECT_VALUE_1, 'mysql', '1')

	# Second secrect pair is user=root
	SECRECT_VALUE_2 = api.get_vault_secret(SECRET_FIELD_2, PATH_TO_SECRET)
	_expect(SECRECT_VALUE_2, 'root', '2')

else:
	print "Error: vault server is not running."