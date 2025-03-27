from flask import Flask, request, jsonify
import requests
import hashlib
from flask_cors import CORS  # Import CORS

app = Flask(__name__)

# Enable CORS for all routes and origins
CORS(app)

# Nodes of the distributed database
nodes = ["http://localhost:5001", "http://localhost:5002"]

def get_node_url(key):
    """Simple hash to choose the node for a key"""
    hash = int(hashlib.md5(key.encode()).hexdigest(), 16) % len(nodes)
    return nodes[hash]

@app.route('/set', methods=['POST'])
def set_value():
    """Sets a key-value pair in the distributed database"""
    req = request.json
    key = req.get('key')
    value = req.get('value')
    
    if not key or not value:
        return jsonify({"message": "Key and value are required."}), 400
    
    node_url = get_node_url(key)  # Get the correct node based on the key
    response = requests.post(f"{node_url}/set", json={"key": key, "value": value})
    
    if response.status_code == 200:
        return jsonify({"message": "Value stored successfully"})
    return jsonify({"message": "Error storing value"}), 500

@app.route('/get/<key>', methods=['GET'])
def get_value(key):
    """Retrieves the value of a key from the distributed database"""
    node_url = get_node_url(key)  # Get the correct node based on the key
    response = requests.get(f"{node_url}/get/{key}")
    
    if response.status_code == 200:
        return jsonify(response.json())
    return jsonify({"value": "Key not found"}), 404


if __name__ == '__main__':
    app.run(debug=True, port=5000)  # Run the Flask server on port 5000
