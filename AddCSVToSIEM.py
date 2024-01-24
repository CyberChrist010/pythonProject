import pandas as pd
# import requests
import json

# Add SIEM's API endpoint
SIEM_API_ENDPOINT = 'https://siem.example.com/api/logs'
API_KEY = 'your_api_key_here'


def send_logs_to_siem(csv_file):
    # Read logs from CSV
    logs = pd.read_csv(csv_file)

    # Convert logs to JSON
    logs_json = logs.to_json(orient='records')
    log_records = json.loads(logs_json)

    # Local testing: Print each log record
    for record in log_records:
        print("Log Record:", record)

    # # Uncomment the following code to interact with the SIEM
    # for record in log_records:
    #     response = requests.post(
    #         SIEM_API_ENDPOINT,
    #         headers={
    #             'Content-Type': 'application/json',
    #             'Authorization': f'Bearer {API_KEY}'
    #         },
    #         json=record
    #     )
    #     if response.status_code == 200:
    #         print("Log successfully sent")
    #     else:
    #         print(f"Failed to send log: {response.text}")


# Call the function with the CSV file path
send_logs_to_siem('user_data.csv')
