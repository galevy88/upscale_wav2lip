import requests
import json
import base64

# URL to which the PUT request is to be sent
url = 'http://localhost:3003/video/sync'

# Path to your JSON file
file_path = 'body.json'

# Read the contents of the JSON file
with open(file_path, 'r') as file:
    data = json.load(file)

# Send a PUT request
response = requests.put(url, json=data)

# Check if the response is successful
if response.status_code == 200:
    # Parse the JSON response
    response_json = response.json()

    # Extract the base64 encoded video data
    b64data = response_json.get('base64_video')

    if b64data:
        # Ensure the base64 string is a multiple of 4 in length
        b64data += '=' * (-len(b64data) % 4)

        # Decode the base64 encoded video
        video_data = base64.b64decode(b64data)

        # Path where you want to save the video, e.g., 'output.mp4'
        output_file_path = 'output.mp4'

        # Write the video data to a file
        with open(output_file_path, 'wb') as file:
            file.write(video_data)
        print(f"Video saved as {output_file_path}")
    else:
        print("No video data found in the response.")
else:
    print('Status Code:', response.status_code)
    print('Response Body:', response.text)
