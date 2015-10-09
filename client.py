
import http
import operations
import resources
import json
import config


class Omnivore(object):
    '''Main client class for Omnivore API'''
    def __init__(self):
        api_key = config.api_key
        self.version            = '0.1'
        self.request_container  = http.RequestContainer()
        self.request_sender     = http.RequestSender(api_key=api_key)
        self.resource_provider  = resources.ResourcesProvider(self.version)
        self.operation_provider = operations.OperationsProvider(self._begin_request)
        self.base_url           = 'https://api.omnivore.io'

    def __getattr__(self, attr):
        self.request_container.resource = attr
        return self.operation_provider

    def _begin_request(self, op, args):
        '''callback for operations provider'''
        self.request_container.operation = op
        self.request_container.args = args
        resource  = self.request_container.resource
        operation = self.request_container.operation
        request   = self.resource_provider.get_path(resource, operation)
        self.request_container.action = request.action

        # Builds complete URL -> base_url/version/path
        url = "/".join([self.base_url, self.version, request.url])
        self.request_container.url = url

        # If request container cant build the request, we abort
        if self.request_container.create_request():
            return self._send_request()

    def _send_request(self):
        '''injects request sender into request container
           and attempts the request
        '''
        response = self.request_container.send(self.request_sender)
        return {'status': response[0], 'body': response[1]}


if __name__=='__main__':
    c = Omnivore()

