class Entry:

    def __init__(self, lat, lng, address):
        self.address = address

    def __init__(self, vic_id, vic_name, lat, lng, address, contactID, eventID):
        self.victim_id = vic_id
        self.victim_name = vic_name
        self.lat = lat
        self.long = lng
        self.address = address
        self.contact_id = contactID
        self.event_id = eventID

    def __init__(self, vic_name, lat, lng, address, contactID, eventID):
        self.victim_id
        self.victim_name = vic_name
        self.lat = lat
        self.long = lng
        self.address = address
        self.contact_id = contactID
        self.event_id = eventID