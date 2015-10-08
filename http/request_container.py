__author__ = 'churley'

import json

class RequestContainer(object):
    ''' holds information from which to build a request '''
    def __init__(self):
        self.resource = None
        self.operation = None
        self.args = {}
        self.action = None
        self.url = None

    def set_resource(self, resource):
        self.resource = resource

    def set_operation(self, op, args):
        self.operation = op
        self.args = args

    def set_action(self, action):
        self.action = action

    def set_url(self, url):
        self.url = url

    def get_resource_name(self):
        return self.resource

    def get_operation_name(self):
        return self.operation

    def create_request(self):
        '''
        called to perform final formatting on request
        data and plug ids into the url.
        also converts post data to json
        :return: boolean: true is successful
        '''
        try:
            if 'data' in self.args.keys():
                payload = self.args.pop('data')
            else:
                payload = {}
            self.url = self.url%self.args
            self.payload = json.dumps(payload)
        except:
            return False
        return True

    def send(self, sender):
        '''
        :param sender: object of type RequestSender
        :return: the raw API response
        '''
        return sender.send(self.url, self.action, self.payload,
                           self.resource, self.operation)

