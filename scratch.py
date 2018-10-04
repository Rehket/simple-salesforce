# Just here to manually call some of the code...

from os import environ
from simple_salesforce import login
import requests
import json

SANDBOX_TYPES = ['DEVELOPER', 'DEVELOPER_PRO', 'PARTIAL', 'FULL']

def create_sandbox(name, org_url, token):
    my_req_url = 'https://' + org_url + '/services/data/v43.0/tooling/sobjects/SandBoxInfo'
    print(my_req_url)

    headers = {'Authorization': 'Bearer ' + token,
               'Content-Type': 'application/json'}

    body = {'AutoActivate': True,
            'Description': 'Test sandbox made with the tooling API',
            'HistoryDays': 0,
            'LicenseType': 'DEVELOPER',
            'SandboxName': name,
            }
    print(body)
    my_request = requests.post(url=my_req_url, headers=headers, data=json.dumps(body))
    body = my_request.content

    return json.loads(body)

if __name__ == '__main__':
    print(environ.get('SFDC_USER'))

    token, url = login.SalesforceLogin(username=environ.get('SFDC_USER'),
                                       password=environ.get('SFDC_PASS'),
                                       security_token=environ.get('SFDC_TOKEN'),)

    headers = {'Authorization': 'Bearer ' + token,
               'Content-Type': 'application/json'}

    job_info = 'https://' + url + '/services/data/v43.0/jobs/ingest'

    jobs = requests.get(url=job_info, headers=headers)

    print(json.loads(jobs.content))

    org_info = 'https://' + url + '/services/data/v43.0/'

    info = requests.get(url=org_info, headers=headers)

    info = json.loads(info.content)['identity']
    info = info.split('/')
    user_id = info.pop()
    org_id = info.pop()

    create_sandbox('APISBTwo', url, token)

    # SELECT Id, SandBoxName FROM SandboxInfo WHERE SandBoxName='APISBTwo'