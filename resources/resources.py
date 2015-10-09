''' This is the resource map for the Omnivore API
    Todo: need to create validation class
'''
resources = {
'versions':
  {'0.1':{'locations':{
		    'list': {'url':'locations', 'action':'get'},
		    'getOne': {'url':'locations/%(location_id)s', 'action':'get'}
		    },
          'tickets':{
		    'list'  : {'url':'locations/%(location_id)s/tickets', 'action':'get'},
		    'getOne': {'url':'locations/%(location_id)s/tickets/%(ticket_id)s', 'action':'get'},
                    'create': {'url':'locations/%(location_id)s/tickets', 'action':'post'},
                    'delete': {'url':'locations/%(location_id)s/tickets/%{ticket_id}s', 'action':'delete'},
		   }
		  }
	}
}
