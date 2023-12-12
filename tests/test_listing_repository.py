from lib.listing import Listing
from lib.listing_repository import ListingRepository 

def test_create_new_listing(db_connection):
    db_connection.connect()
    db_connection.seed('seeds/bnb_tables.sql')
    repo = ListingRepository(db_connection)
    listing = Listing(None, 'house', 'a house', 3, 10, 1)
    result = repo.create(listing)
    all_listings = repo.all()
    assert result == 4
    assert all_listings[3] == Listing(4, 'house', 'a house', 3, 10, 1)