class Entry:

    # def __init__(self, lat, lng, address):
    #     self.address = address

    def __init__(self, lat, lng, address, vic_id=None, vic_name=None, contactID=None, eventID=None):
        self.lat = lat
        self.long = lng
        self.address = address
        if vic_id is not None: self.victim_id = vic_id
        if vic_name is not None: self.victim_name = vic_name
        if contactID is not None: self.contact_id = contactID
        if eventID is not  None: self.event_id = eventID

    # def __init__(self, vic_name, lat, lng, address, contactID, eventID):
    #     self.victim_name = vic_name
    #     self.lat = lat
    #     self.long = lng
    #     self.address = address
    #     self.contact_id = contactID
    #     self.event_id = eventID