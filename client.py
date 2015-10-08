
import http
import operations
import resources
import json


class Omnivore(object):
    '''Main client class for Omnivore API'''
    def __init__(self):
        self.version            = '0.1'
        self.request_container  = http.RequestContainer()
        self.request_sender     = http.RequestSender(api_key='[YOUR API KEY]')
        self.resource_provider  = resources.ResourcesProvider(self.version)
        self.operation_provider = operations.OperationsProvider(self._set_operation)
        self.base_url           = 'https://api.omnivore.io'

    def __getattr__(self, attr):
        self.request_container.set_resource(attr)
        return self.operation_provider

    def _set_operation(self, op, args):
        '''callback for operations provider'''
        self.request_container.set_operation(op, args)
        resource  = self.request_container.get_resource_name()
        operation = self.request_container.get_operation_name()
        request   = self.resource_provider.get_path(resource, operation)
        self.request_container.action = request.action

        # Builds complete URL -> base_url/version/path
        url = "/".join([self.base_url, self.version, request.url])
        self.request_container.set_url(url)

        # If request container cant build the request, we abort
        if self.request_container.create_request():
            return self._send_request()
        else:
            return None

    def _send_request(self):
        '''injects request sender into request container
           and attempts the request
        '''
        response = self.request_container.send(self.request_sender)
        return [response[0], response[1]]





if __name__=='__main__':
    c = Omnivore()
    print c.locations.list()
    print c.locations.getOne(location_id='Mi8y7jcL')
    print c.tickets.list(location_id='Mi8y7jcL')
    #c.locations.create(data={'asdasdasd': 'asdadasd'})
