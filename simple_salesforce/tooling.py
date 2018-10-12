"""Tooling functions for simple-salesforce"""

import requests
import json


class Tooling:
    headers = {}
    url = ''

    def __init__(self, headers, org_url):
        self.headers = headers
        self.url = org_url

    def fetch_org_info(self, url):
        org_info = 'https://' + url + '/services/data/v43.0/'

        info = requests.get(url=org_info, headers=self.headers)

        info = json.loads(info.content)['identity']
        info = info.split('/')
        user_id = info.pop()
        org_id = info.pop()

        return user_id, org_id

    @staticmethod
    def query_builder(param_list):

        if len(param_list) == 0:
            raise ValueError('No parameters provided')

        params = (x + ',' for x in param_list)
        param_string = ''
        for param in params:
            param_string += param
        param_string = param_string[:-1]

        return param_string

    def get_sandbox_status(self, sand_box_name, url, params=None):
        if params is None:
            params = ['Id', 'ActivatedById', 'ApexClassId', 'AutoActivate', 'CopyChatter', 'CopyProgress',
                      'Description',
                      'EndDate', 'HistoryDays', 'LicenseType', 'RefreshAction', 'SandboxInfoId', 'SandboxName',
                      'SandboxOrganization', 'SourceId', 'StartDate', 'Status', 'TemplateId', ]

        sandbox_info_url = 'https://' + url + '/services/data/v44.0/tooling/query/?q='
        query = 'SELECT+' + self.query_builder(params) + '+FROM+SandBoxProcess+WHERE+SandboxName=\'' + sand_box_name + '\''

        print(query)
        result = requests.get(url=sandbox_info_url + query, headers=self.headers)

        result_dict = json.loads(result.content)
        print(json.dumps(result_dict))

    def create_sandbox(self, name, org_url, token):
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

