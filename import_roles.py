import json
from requests import post
import requests
from getpass import getpass
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
import time

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

ROLES = roles_convert['roles']
TOTAL_ROLES = len(ROLES)

print("Total number of roles " + str(TOTAL_ROLES) + " will be imported.")

FAILED_ROLES = []
IMPORTED_ROLES = []

# Importing roles with all the configured users and groups
for ROLE in ROLES:
    time.sleep(5)
    del ROLE['id']
    response = post(IMPORT_RANGER_URL + ROLES_API, headers=headers, json=ROLE, verify=False,
                    auth=(IMPORT_RANGER_ADMIN_USER, IMPORT_RANGER_ADMIN_PASSWORD))
    STATUS = response.status_code
    ROLENAME = ROLE['name']
    if STATUS == 200:
        print("Successfully Imported Role " + ROLENAME + " with status " + str(STATUS))
        IMPORTED_ROLES.append(ROLENAME)
    else:
        print("Import for role " + ROLENAME + " failed with status " + str(STATUS))
        FAILED_ROLES.append(ROLENAME)

print("\n" + str(len(FAILED_ROLES)) + " roles failed to import.")
print(str(len(IMPORTED_ROLES)) + " roles were imported successfully.")

if FAILED_ROLES:
    print("\nCould not import the following roles:- ")
    for FAILED_ROLE in FAILED_ROLES:
        print(FAILED_ROLE)
