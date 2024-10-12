import requests
import json

# Define the API endpoint URL
api_url = 'https://api.example.com/endpoint'

# Define your API key
api_key = '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'

# Load the JSON data from the file containing the scraped subtitles
json_file_path = './yt-subtitles.json'

try:
    with open(json_file_path, 'r') as json_file:
        data_to_send = json.load(json_file)

    # Set up the headers with the API key
    headers = {
        'Authorization': f'Bearer {api_key}',
        'Content-Type': 'application/json'
    }

    # Send a POST request to the API endpoint
    response = requests.post(api_url, json=data_to_send, headers=headers)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Process the response data
        response_data = response.json()
        print("Response from the API:")
        print(response_data)
        
    else:
        print(f"Error: {response.status_code} - {response.reason}")

except FileNotFoundError:
    print(f"Error: File '{json_file_path}' not found")

except Exception as e:
    print(f"Error occurred: {e}")
