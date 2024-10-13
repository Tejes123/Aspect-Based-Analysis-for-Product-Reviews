from flask import Flask, jsonify, request, render_template
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_values', methods=['POST', 'GET'])
def get_values():
    # Example values; replace this with your logic to compute these values
    values = [10, 20, 30]  # Replace with logic to get values dynamically

    count ={}
    with open(r"C:\Tejeswar\product Review\Aspect Based Product Analysis\Aspect Based Sentiment Analysis\reviews\count.json", 'r') as file:
        count = json.load(file)

    return count

@app.route('/get_response', methods=['POST', 'GET'])
def get_response():
    # Example values; replace this with your logic to compute these values
    
    responseData ={}
    with open(r"C:\Tejeswar\product Review\Aspect Based Product Analysis\Aspect Based Sentiment Analysis\reviews\topicExtractedNew.json", 'r') as file:
        responseData = json.load(file)

    return responseData

if __name__ == '__main__':
    app.run(debug=True)
