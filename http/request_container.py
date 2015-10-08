__author__ = 'churley'

import json

class RequestContainer(object):
    ''' holds information from which to build a request '''
    @property
    def resource(self):
        return self.__resource

    @resource.setter
    def resource(self, resource):
        self.__resource = resource

    @property
    def operation(self):
        return self.__operation

    @operation.setter
    def operation(self, op):
        self.__operation = op

    @property
    def args(self):
        return self.__args

    @args.setter
    def args(self, args):
        self.__args = args

    @property
    def action(self):
        return self.__action

    @action.setter
    def action(self, action):
        self.__action = action

    @property
    def url(self):
        return self.__url

    @url.setter
    def url(self, url):
        self.__url = url


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

