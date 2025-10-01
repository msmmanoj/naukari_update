import requests
import urllib3

# Disable SSL warnings when verify=False is used
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# --- API 1: Login to get token ---
login_url = "https://www.naukri.com/central-login-services/v1/login"
login_payload = {
    "username": "malepatimanoj6@gmail.com",
    "password": "Mtrgsm@123"
}
login_headers = {
    "accept": "application/json",
    "appid": "103",
    "clientid": "d3skt0p",
    "content-type": "application/json",
    "origin": "https://www.naukri.com",
    "referer": "https://www.naukri.com/",
    "systemid": "jobseeker",
    "user-agent": "Mozilla/5.0"
}

login_response = requests.post(login_url, json=login_payload, headers=login_headers, verify=False)
login_response.raise_for_status()
login_data = login_response.json()

# Extract access token from cookies
access_token = None
if 'cookies' in login_data:
    for cookie in login_data['cookies']:
        if cookie['name'] == 'nauk_at':
            access_token = cookie['value']
            print(f"Found access token in cookies: {access_token[:50]}...")
            break

# Fallback: try to get token from JSON body
if not access_token:
    access_token = login_data.get("accessToken") or login_data.get("token") or login_data.get("data", {}).get("accessToken")
    if access_token:
        print(f"Found access token in JSON body: {access_token[:50]}...")

if not access_token:
    print("Login response structure:", login_data.keys())
    raise Exception("Could not find access token in response: " + str(login_data))

# --- API 2: Use token to update profile ---
profile_url = "https://www.naukri.com/cloudgateway-mynaukri/resman-aggregator-services/v1/users/self/fullprofiles"
profile_json = {
    "profile": {
        "resumeHeadline": "Advanced Software Engineer with expertise in Software Development,Software Design,Software Debugging,Software Deployment,Application Development,Web Development,Web Application,Design Patterns,Code Development,Fullstack Development,System Design,SDLC"
    },
    "profileId": "b0592d9202756c4246da4e1993a01d02be70713db7750e82fcc93b141dd0abb8"
}
profile_headers = {
    "accept": "application/json",
    "appid": "105",
    "authorization": f"Bearer {access_token}",
    "clientid": "d3skt0p",
    "content-type": "application/json",
    "origin": "https://www.naukri.com",
    "referer": "https://www.naukri.com/mnjuser/profile?id=&altresid&action=modalOpen",
    "systemid": "Naukri",
    "user-agent": "Mozilla/5.0",
    "x-http-method-override": "PUT",
    "x-requested-with": "XMLHttpRequest"
}

profile_response = requests.post(profile_url, json=profile_json, headers=profile_headers, verify=False)
profile_response.raise_for_status()
print("Profile update response:", profile_response.json())

# Alternative approach using session (commented out):
# import ssl
# session = requests.Session()
# session.verify = False  # or set to path of certificate bundle
# # Then use: session.post() instead of requests.post()
