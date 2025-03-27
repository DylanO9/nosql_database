# Distributed NoSQL Database

Welcome to the Distributed NoSQL Database project! This repository provides a robust, scalable, and high-performance NoSQL database solution designed for modern distributed systems.

## Features

- **Scalability**: Seamlessly scale horizontally to handle growing data and traffic.
- **High Availability**: Built-in replication and fault tolerance for uninterrupted service.
- **Flexible Schema**: Supports schema-less data models for maximum flexibility.
- **Fast Performance**: Optimized for low-latency read and write operations.
- **Distributed Architecture**: Designed to work efficiently across multiple nodes.

## Getting Started

Follow these steps to set up and run the database:

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/your-username/nosql_database.git
    cd nosql_database
    ```

2. **Install Dependencies**:
    Ensure you have the required dependencies installed. Refer to the `requirements.txt` or `package.json` file for details.

3. **Run the Database**:
    Use the following command to start a database node on a specific port:
    ```bash
    py database_node.py --port 5001
    ```
    Repeat the command with different port numbers to create additional nodes.

4. **Start the Frontend**:
    Navigate to the `distributed-db-frontend` directory and run:
    ```bash
    npm run start
    ```
    This will launch the frontend interface for interacting with the database.

4. **Connect to the Database**:
    Use the client library or REST API to interact with the database. Once the frontend is running, open your browser and navigate to `http://localhost:3000` to access the database's user interface.
