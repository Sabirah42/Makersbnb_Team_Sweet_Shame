class Listing:

    def __init__(self, id, listing_name, description, bedrooms, price, user_id):
        self.id = id 
        self.listing_name = listing_name 
        self.description = description 
        self.bedrooms = bedrooms 
        self.price = price 
        self.user_id = user_id  

    def __eq__(self, other):
        return self__dict__ == other.__dict__

    def __repr__(self):
        return f'Listing({self.id}, {self.listing_name}, {self.description}, {self.bedrooms}, {self.price}, {self.user_id})'