__author__ = 'churley'
import requests
import json

class Headers(object):
    @classmethod
    def prep_headers(self, api_key):
        ''' builds and returns HTTP headers
            with security credentials
        '''
        headers = {
            'content-type': 'application/json',
            'Api-Key': '%s'%api_key.strip()
        }
        return headers

class RequestSender(object):
    def __init__(self, api_key=''):
        self.api_key = api_key
    def send(self, url, action, payload, resource, operation):
        '''
        sends the HTTP request
        :param url: complete url with https://, etc.
        :param action: post, get, delete, patch, put
        :param payload: post data in json format
        :return: http response code, response text
        '''
        if action == 'get':
            response = requests.get(url, headers=Headers.prep_headers(self.api_key))
        elif action == 'post':
            response = requests.post(url,
                                     payload,
                                     headers=Headers.prep_headers(self.api_key))
        data = json.loads(response.text)
        #removing HAL data for now
        if operation == 'list':
            data = data['_embedded'][resource]
            for r in data:
                if '_embedded' in r:
                    del r['_embedded']
                if '_links' in r:
                    del r['_links']
        elif operation in ('getOne', 'create'):
            if '_embedded' in data:
                del data['_embedded']
            if '_links' in data:
                del data['_links']



        return [response.status_code, data]
