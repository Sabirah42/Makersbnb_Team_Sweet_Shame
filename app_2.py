from lib.user import User
from lib.user_repository import UserRepository 
from lib.listing import Listing 
from lib.listing_repository import ListingRepository 
import os
from flask import Flask, request, render_template, redirect, session 
from lib.database_connection import get_flask_database_connection

app = Flask(__name__)
app.secret_key = 'secretkey'

with app.app_context():
    connection = get_flask_database_connection(app)


@app.route('/', methods=['GET'])
def get_index():
    user_repo = UserRepository(connection)
    repo = ListingRepository(connection)
    all_listings = repo.all()
    if 'logged_in' in session and session['logged_in']:
        
        if user_repo.retrieve_last_viewed(session['current_id']) is not None:
            session['last_viewed'] = user_repo.retrieve_last_viewed(session['current_id'])
        if 'last_viewed' in session: 
            last_viewed_listing = repo.get_listing_from_id(session['last_viewed'])
            return render_template('index_in.html', listings=all_listings[::-1], last_viewed_listing=last_viewed_listing, current_username=session['current_username'])
        else:
            return render_template('index_in.html', listings=all_listings[::-1], current_username=session['current_username'])
    return render_template('index_out.html', listings=all_listings[::-1])

@app.route('/listings', methods=['POST'])
def add_listing():
    # connection = get_flask_database_connection(app)
    listing_repo = ListingRepository(connection)
    listing_name, description, bedrooms, price = request.form['listing_name'], request.form['description'], request.form['bedrooms'], request.form['price']
    listing = Listing(None, listing_name, description, bedrooms, price, session['current_id'])
    listing_repo.create(listing)
    return redirect('/')
    
@app.route('/add_listing')
def show_listing_sumbission_form():
    return render_template('add_listing.html')

@app.route('/logout')
def logout():
    session.pop('logged_in')
    session.pop('current_username')
    session.pop('current_id')
    if 'last_viewed' in session:
        del session['last_viewed']
    return redirect('/')

@app.route('/login')
def login_form():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def attempt_login():
    email, password = request.form['email'], request.form['password']
    user_repo = UserRepository(connection)
    try:
        user = user_repo.get_user_from_email(email)
        if user:
            if user.password == password:
                session['logged_in'] = True
                session['current_username'] = user.username
                session['current_id'] = user.id 
                return redirect('/')
            else:
                raise Exception('Password is incorrect')
    except Exception as e:
        return render_template('/login.html', error=e)
    
@app.route('/listings/<id>')
def show_single_listing(id):
    user_repo = UserRepository(connection)
    session['last_viewed'] = user_repo.set_last_viewed(session['current_id'], id)
    listing_repo = ListingRepository(connection)
    listing = listing_repo.get_listing_from_id(id) 
    user = user_repo.get_user_from_id(listing.user_id)
    return render_template('individual_listing.html', listing=listing, user=user)

@app.route('/signup')
def show_sign_up_form():
    return render_template('signup.html')

@app.route('/signup', methods=['POST'])
def create_new_user():
    username, email, password, confirm_password = request.form['username'], request.form['email'], request.form['password'], request.form['confirm_password']
    try: 
        user_repo = UserRepository(connection)
        if password != confirm_password:
            raise Exception('Passwords do not match.')
        else:
            user = User(None, username, email, password)
            new_user_id = user_repo.create(user)
            session['current_id'] = new_user_id
            session['current_username'] = username 
            session['logged_in'] = True 
            return redirect('/')
    except Exception as e:
        return render_template('signup.html', error=e)

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))
