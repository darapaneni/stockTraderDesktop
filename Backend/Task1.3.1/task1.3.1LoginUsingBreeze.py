import requests

# Replace with your actual API key, secret key, and session token
API_KEY = "975~_9970R!56H3y7Inp2519029Rl648"
API_SECRET = "741252)^983$1579162137NnU59^233C"
SESSION_ID = "39999072"

# API endpoints
BASE_URL = "https://api.icicidirect.com/apiuser"
LOGIN_URL = f"{BASE_URL}/login?api_key={API_KEY}"

def main():
    session_token = SESSION_ID
    if session_token:
        url = LOGIN_URL
        payload = {
            "api_secret": API_SECRET
        }
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                print("Login successful!")
            else:
                print(f"Error Logging in. Status code: {response.status_code}")
        except Exception as e:
            print(f"Error: {e}")
    else:
        print("Check your API credentials.")

if __name__ == "__main__":
    main()