# API client for Omnivore
The start of an Python API client for Omnivore.io

put your api key in the config file and...
replace anything in a {...} with your ids

c = Omnivore()
c.locations.list()
c.locations.getOne(location_id={a location id})
c.tickets.list()
data= {
          "employee": "{employee id}",
          "order_type": "{order_type id}",
          "revenue_center": "{revenue_center id}",
        }
        
c.tickets.create(location_id='{location id}', data = data)
