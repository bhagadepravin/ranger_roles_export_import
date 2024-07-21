import json
from requests import post
import requests
from getpass import getpass
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from concurrent.futures import ThreadPoolExecutor, as_completed
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

try:
    input = raw_input  # For Python 2 compatibility
except NameError:
    pass  # For Python 3, raw_input doesn't exist, use input

IMPORT_JSON_FILE = input("Path to exported roles JSON file:- ")
IMPORT_RANGER_URL = input("DEST_RANGER URL:- ")
ROLES_API = "/service/roles/roles/"
IMPORT_RANGER_ADMIN_USER = input("DEST_RANGER ADMIN USER:- ")
IMPORT_RANGER_ADMIN_PASSWORD = getpass(prompt='DEST_RANGER ADMIN PASSWORD:- ', stream=None)
headers = {'Accept': 'application/json'}

# Loading roles from the JSON file
with open(IMPORT_JSON_FILE, 'r') as infile:
    roles_convert = json.load(infile)

# Since roles are directly in the JSON root
ROLES = roles_convert
TOTAL_ROLES = len(ROLES)

print("Total number of roles " + str(TOTAL_ROLES) + " will be imported.")

FAILED_ROLES = []
IMPORTED_ROLES = []

def import_role(role):
    del role['id']
    response = post(IMPORT_RANGER_URL + ROLES_API, headers=headers, json=role, verify=False,
                    auth=(IMPORT_RANGER_ADMIN_USER, IMPORT_RANGER_ADMIN_PASSWORD))
    status = response.status_code
    rolename = role['name']
    if status == 200:
        return rolename, True
    else:
        return rolename, False

# Use ThreadPoolExecutor to import roles concurrently
with ThreadPoolExecutor(max_workers=10) as executor:
    future_to_role = {executor.submit(import_role, role): role for role in ROLES}
    for future in as_completed(future_to_role):
        rolename, success = future.result()
        if success:
            print("Successfully Imported Role " + rolename)
            IMPORTED_ROLES.append(rolename)
        else:
            print("Import for role " + rolename + " failed")
            FAILED_ROLES.append(rolename)

print("\n" + str(len(FAILED_ROLES)) + " roles failed to import.")
print(str(len(IMPORTED_ROLES)) + " roles were imported successfully.")

if FAILED_ROLES:
    print("\nCould not import the following roles:- ")
    for FAILED_ROLE in FAILED_ROLES:
        print(FAILED_ROLE)
