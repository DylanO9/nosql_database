import requests
import hashlib
import random

nodes = ["http://localhost:5001", "http://localhost:5002"]  # Multiple database nodes

def hash_key(key):
    return int(hashlib.md5(key.encode()).hexdigest(), 16) % len(nodes)


replica_nodes = {
    "http://localhost:5001": ["http://localhost:5002"],  # Node 1 replicates to Node 2
    "http://localhost:5002": ["http://localhost:5001"]   # Node 2 replicates to Node 1
}

def replicate_value(node, key, value):
    for replica in replica_nodes[node]:
        requests.post(f"{replica}/set", json={"key": key, "value": value})

def set_value(key, value):
    node = nodes[hash_key(key)]
    response = requests.post(f"{node}/set", json={"key": key, "value": value})
    replicate_value(node, key, value)  # Replicates to backup nodes
    return response.json()


def get_value(key):
    node = nodes[hash_key(key)]
    response = requests.get(f"{node}/get/{key}")
    return response.json()


def get_value_quorum(key):
    values = []
    for node in nodes:
        try:
            response = requests.get(f"{node}/get/{key}").json()
            values.append(response['value'])
        except:
            pass  # Ignore failed nodes
    
    return max(set(values), key=values.count)  # Return the most frequent value


if __name__ == "__main__":
    print(set_value("user1", "Alice"))  # Stores in a shard
    print(get_value("user1"))  # Retrieves from the correct shard
