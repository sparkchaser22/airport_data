class Airport:
    def __init__(self, airport_identifier, name, country, state):
        self.airport_identifier = airport_identifier
        self.name = name
        self.country = country
        self.state = state
        
    def __str__(self):
        return "Airport id: " + self.airport_identifier + "\n" + \
                "Name: " + self.name + "\n" + \
                "Country: " + self.country + "\n" + \
                "State: " + self.state 