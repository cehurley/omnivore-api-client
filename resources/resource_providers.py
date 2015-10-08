__author__ = 'churley'

from resources import resources as api_resources

class ResourceData(object):
    ''' a container for resource data '''
    def __init__(self):
        self.url = None
        self.action = None
        self.op = None
        self.resource = None
    def get_url(self):
        return self.url
    def get_action(self):
        return self.action
    def set(self, k, v):
        setattr(self, k,v)

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
        ep = ResourceData()
        ep.set('url', rd['url'])
        ep.set('action' , rd['action'])
        ep.set('op' , op)
        ep.set('resource' , resource_name)
        return ep

