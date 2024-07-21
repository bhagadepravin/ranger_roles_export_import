import json
from requests import get
import requests
import time
from getpass import getpass
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

try:
    input = raw_input  # For Python 2 compatibility
except NameError:
    pass  # For Python 3, raw_input doesn't exist, use input

EXPORT_RANGER_URL = input("SOURCE_RANGER URL:- ")
ROLES_API = "/service/roles/roles/"
EXPORT_RANGER_ADMIN_USER = input("SOURCE_RANGER ADMIN USER:- ")
EXPORT_RANGER_ADMIN_PASSWORD = getpass(prompt='SOURCE_RANGER ADMIN PASSWORD:- ', stream=None)
headers = {'Accept': 'application/json'}

# Exporting roles with all the configured users and groups
response = get(EXPORT_RANGER_URL + ROLES_API, headers=headers, verify=False,
               auth=(EXPORT_RANGER_ADMIN_USER, EXPORT_RANGER_ADMIN_PASSWORD))
roles_convert = json.loads(response.content)

ROLES = roles_convert['roles']
TOTAL_ROLES = len(ROLES)

print("Total number of roles " + str(TOTAL_ROLES) + " will be exported.")

# Saving the roles to a JSON file
with open('exported_roles.json', 'w') as outfile:
    json.dump(ROLES, outfile, indent=4)

print("Roles have been successfully exported to 'exported_roles.json'.")
