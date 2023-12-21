from flask import Flask, render_template, request

app = Flask(__name__)

# Sample data for demonstration purposes
# In a real application, you would likely use a database
# to store and retrieve search results.
data = [
    {'id': 1, 'title': 'Flask Introduction'},
    {'id': 2, 'title': 'Building Web Apps with Flask'},
    {'id': 3, 'title': 'Flask Templates'},
    # Add more sample data as needed
]

@app.route('/')
def index():
    return render_template('index.html', data=data)

@app.route('/search', methods=['GET'])
def search():
    # Get the search query parameter from the URL
    query = request.args.get('query', '')

    # Perform a simple search based on the query
    results = [item for item in data if query.lower() in item['title'].lower()]

    return render_template('search_results.html', query=query, results=results)

if __name__ == '__main__':
    app.run(debug=True)
