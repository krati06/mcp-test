import requests
import json
import sys

if len(sys.argv) < 2:
    print("Usage: python test_cloud.py <cloud-run-url>")
    print("Example: python test_cloud.py https://mcp-server-abcde123-uc.a.run.app")
    sys.exit(1)

cloud_url = sys.argv[1]

# Define the MCP request format
request_data = {
    "inputs": "Say hello from Cloud Run!",
    "parameters": {}
}

# Send the request to the deployed MCP server
response = requests.post(
    f"{cloud_url}/v1/generate",
    headers={"Content-Type": "application/json"},
    data=json.dumps(request_data)
)

# Print the response
print("Status code:", response.status_code)
print("Response:")
print(json.dumps(response.json(), indent=2))

# Test the health check endpoint
health_response = requests.get(f"{cloud_url}/health")
print("\nHealth check status code:", health_response.status_code)
print("Health check response:", health_response.json())
