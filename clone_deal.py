import requests
import json
import os

import format_payload
from dotenv import load_dotenv, find_dotenv

load_dotenv()

# API BATCH associations and JSON information

HS_API_KEY = os.getenv('HS_API_KEY')

headers = {'Content-Type': "application/json"}

cwd = os.getcwd()

def clone_deal(json_data):
    contact_ids = []
    company_ids = []
    orig_deal_id = json_data["objectId"]

    # Get associations
    orig_url = f"https://api.hubapi.com/crm/v3/objects/deals/{orig_deal_id}?associations=contacts&associations=companies&archived=false&hapikey={HS_API_KEY}"

    response = requests.get(orig_url, headers=headers)
    if response.status_code != 200:
        return "Error getting request" 
    print("GETTING DEAL INFO:", response)
    assoc_data = response.json()
    print(assoc_data)
    print('-' * 50)

    for id in assoc_data.get("associations").get("companies",{}).get("results",{}):
        company_ids.append(id.get('id', ""))

    for id in assoc_data.get("associations").get("contacts",{}).get("results",{}):
        contact_ids.append(id.get('id', ""))

    # Clone Deal
    clone_deal_id = create_deal(json_data)

    # Make Associations
    deal_assoc(clone_deal_id, contact_ids, "contact", "deal_to_contact")
    deal_assoc(clone_deal_id, company_ids, "company", "deal_to_company")

def create_deal(json_data):
    url = f"https://api.hubapi.com/crm/v3/objects/deals?hapikey={HS_API_KEY}"
    # filename = "deals_log.txt"
    payload = format_payload.make_payload(json_data)
    response = requests.post(url, data=json.dumps(payload), headers=headers)
    print("CLONING DEAL:", response)
    print(response.text)
    if response.status_code != 201:
        quit()
    # log(response, filename)
    return json.loads(response.text)["id"]

def deal_assoc(deal_id, contact_or_company_ids, assoc_obj, type):
    url = f"https://api.hubapi.com/crm/v3/associations/deal/{assoc_obj}/batch/create?hapikey={HS_API_KEY}"

    for i in range(0, len(contact_or_company_ids), 100):
        # List to send request
        hundred_associations = []
        # Add the appropriate format for each association
        for id in contact_or_company_ids[i:i+100]:
            hundred_associations.append(make_assoc_api(deal_id, id, type))
        payload = {"inputs": hundred_associations}
        response = requests.post(url, data=json.dumps(payload), headers=headers)
        print("CLONING ASSOCIATIONS:", response)
        print(response.text)
        if response.status_code != 201:
            quit()
        # log(response, filename)
        return response

def make_assoc_api(clone_deal_id, contact_or_company_id, assoc_type):
    """ 
    The make_assoc_api function takes a table with the hubspot id in the 0th index and database id in the 1st index along with the type to return the format ready for the Hubspot id 
    for ASSOCIATIONS
    :param type: the type of association to create
    :return: a dictionary with the appropriate API format for Hubspot
    """
    return {
        "from": {
        "id": clone_deal_id
    },
        "to": {
        "id": contact_or_company_id
    },
        "type": assoc_type
    }

# def log(response, filename):
#     print(response)
#     print(response.text)
#     print("-" * 50)
#     complete_path = os.path.join(cwd + "/logs", filename)
#     with open(complete_path, 'a') as file:
#         if response.status_code != 201:
#             file.write('\n')
#             file.write(f"ERROR: {response} - {response.text}")
#             file.write('\n')
#             file.write('*' * 100)
#             file.write('\n')
#             file.close()
#             quit()
#         else:
#             # Write the current row number successfully uploaded
#             file.write('\n')
#             file.write(f"{response} - {response.text}")
#             file.write('\n')
#             file.write('-' * 100)
#             file.write('\n')
#     file.close()
