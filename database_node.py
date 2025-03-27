from flask import Flask, request, jsonify
import argparse

app = Flask(__name__)
data_store = {}  # In-memory key-value store

@app.route('/set', methods=['POST'])
def set_value():
    req = request.json
    key, value = req['key'], req['value']
    data_store[key] = value
    return jsonify({'message': 'Value stored successfully'})

@app.route('/get/<key>', methods=['GET'])
def get_value(key):
    return jsonify({'value': data_store.get(key, 'Key not found')})

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Run the Flask app.')
    parser.add_argument('--port', type=int, default=5001, help='Port to run the server on')
    args = parser.parse_args()

    app.run(port=args.port)  # Runs on the specified port
