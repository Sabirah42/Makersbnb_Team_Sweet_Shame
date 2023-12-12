from lib.listing import Listing 

def test_initiate_listing():
    listing = Listing(1, 'space', 'description', 3, 10, 1)
    assert listing.id == 1
    assert listing.listing_name == 'space'
    assert listing.description == 'description'
    assert listing.bedrooms == 3
    assert listing.price == 10
    assert listing.user_id == 1

