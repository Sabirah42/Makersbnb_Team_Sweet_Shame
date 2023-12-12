from lib.listing import Listing 

class ListingRepository:
    def __init__(self, connection):
        self.connection = connection 

    def all(self):
        rows = self.connection.execute('SELECT * from listings')
        listings = []
        for row in rows:
            item = Listing(row["id"], row["listing_name"], row["description"], row['bedrooms'], row['price'], row['user_id'])
            listings.append(item)
        return listings

    def create(self, listing):
        rows = self.connection.execute('INSERT INTO listings (listing_name, description, bedrooms, price, user_id) VALUES (%s, %s, %s, %s, %s) RETURNING id', [
                                listing.listing_name, listing.description, listing.bedrooms, listing.price, listing.user_id])
        return rows[0]['id']
