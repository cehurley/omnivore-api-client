__author__ = 'churley'
import requests

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
    def send(self, url, action, payload):
        '''
        sends the HTTP request
        :param url: complete url with https://, etc.
        :param action: post, get, delete, patch, put
        :param payload: post data in json format
        :return: http response code, response text
        '''
        try:
            response = requests.get(url, headers=Headers.prep_headers(self.api_key))
        except:
            return []
        return [response.status_code, response.text]
