import axios from "axios";

// Backend service URL (this will now be the Python Flask service)
const backendUrl = "http://localhost:5000";

// Set a key-value pair in the distributed database
export const setKeyValue = async (key, value) => {
  try {
    const response = await axios.post(`${backendUrl}/set`, { key, value });
    return response.data;
  } catch (error) {
    console.error("Error setting value:", error);
    return { message: "Error storing value." };
  }
};

// Get a value by key from the distributed database
export const getKeyValue = async (key) => {
  try {
    const response = await axios.get(`${backendUrl}/get/${key}`);
    return response.data;
  } catch (error) {
    console.error("Error getting value:", error);
    return { value: "Error retrieving value." };
  }
};
