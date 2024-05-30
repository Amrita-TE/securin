from flask import Flask, render_template, jsonify
import requests

app = Flask(__name__)
if __name__ == '__main__':
    app.run(debug=True)
@app.route('/')
def index():
    print("Received request for index page")
    try:
        # URL of the local API (replace with your actual local API URL)
        api_url = 'http://localhost:5000/api/data'
        print(f"Fetching data from API: {api_url}")
        
        # Fetch data from the API
        response = requests.get(api_url)
        response.raise_for_status()
        data = response.json()
        print(f"Data received: {data}")
        
        return render_template('index.html', data=data)
    except requests.exceptions.RequestException as e:
        print(f"Error occurred: {e}")
        return f"An error occurred: {e}", 500
