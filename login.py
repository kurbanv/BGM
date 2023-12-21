from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient

app = Flask(__name__)

# MongoDB Configuration
app.config['MONGO_URI'] = 'mongodb://localhost:27017/Members'
mongo = MongoClient(app.config['MONGO_URI'])
db = mongo.members
members_collection = db.member
db=mongo.notes
notes_collection=db.note



@app.route('/')
def home():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    email = request.form.get('email')
    password = request.form.get('password')

    # Check if the user exists in the database
    user = members_collection.find_one({'email': email, 'password': password})

    if user:
        # Successful login, redirect to a dashboard or home page
        return redirect(url_for('page'))
    else:
        # Display a message that the account doesn't exist
        return render_template('login.html', message='Account does not exist')

@app.route('/signup', methods=['POST'])
def signup():
    name = request.form.get('name')
    email = request.form.get('email')
    password = request.form.get('password')

    # Check if the email already exists in the database
    if members_collection.find_one({'email': email}):
        return render_template('login.html', message='Account with this email already exists')

    # Add the new user to the database
    members_collection.insert_one({'name': name, 'email': email, 'password': password})

    # Redirect to the login page after successful signup
    return redirect(url_for('home'))



@app.route('/page')
def page():
    
    return render_template('page.html')

@app.route('/contact', methods=['GET'])
def contact():
    name = request.form.get('name')
    email = request.form.get('email')
    Your_opinion = request.form.get('Your opinion')

    if notes_collection.find_one({'email': email, 'Your opinion': Your_opinion , 'name' : name}):
        
        return render_template('contact.html', message='This message already exists')

    notes_collection.insert_one({'name': name, 'email': email, 'Your opinion': Your_opinion})

    
    return redirect(url_for('contact'))

@app.route('/TVSeries')
def TVSeries():
    
    return render_template('TVseries.html')



@app.route('/Home')
def Home():

    return render_template('page.html')



if __name__ == '__main__':
    app.run(debug=True)
