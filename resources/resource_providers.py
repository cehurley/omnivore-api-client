__author__ = 'churley'

from resources import resources as api_resources

class RequestData(object):
    ''' a container for request data'''
    @property
    def resource(self):
        return self.__resource

    @resource.setter
    def resource(self, resource):
        self.__resource = resource

    @property
    def op(self):
        return self.__op

    @op.setter
    def op(self, op):
        self.__op = op

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


class ResourcesProvider(object):
    ''' reads resource file and retrieves the correct
        resource information for selected version.
        subclass this to make new resource map readers.
        i.e., pull from DB, another API, etc.
    '''
    def __init__(self, version):
        self.resources = api_resources['versions'][version]

    def get_path(self, resource_name, op):
        '''create an object with resource object '''
        rd = self.resources[resource_name][op]
        ep = RequestData()
        ep.url = rd['url']
        ep.action = rd['action']
        ep.op = op
        ep.resource = resource_name
        return ep

