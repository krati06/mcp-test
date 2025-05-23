import requests
import json

# Define the MCP request format
request_data = {
    "inputs": "Say hello!",
    "parameters": {}
}

# Send the request to the MCP server
response = requests.post(
    "http://localhost:8000/v1/generate",
    headers={"Content-Type": "application/json"},
    data=json.dumps(request_data)
)

# Print the response
print("Status code:", response.status_code)
print("Response:")
print(json.dumps(response.json(), indent=2))

# Test the health check endpoint
health_response = requests.get("http://localhost:8000/health")
print("\nHealth check status code:", health_response.status_code)
print("Health check response:", health_response.json())
