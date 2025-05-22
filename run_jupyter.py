import keyring
import requests
import os
import threading
import time
import subprocess

client_id = "wdanielsclient"
username = "wdaniels"
url = "https://cs.trendminer.net"
token_refresh_interval = 240  # seconds (4 minutes)

def fetch_token():
    response = requests.post(
        url=f"{url}/auth/realms/trendminer/protocol/openid-connect/token",
        headers={"Content-Type": "application/x-www-form-urlencoded"},
        data={
            "grant_type": "password",
            "client_id": client_id,
            "client_secret": keyring.get_password(url, client_id),
            "username": username,
            "password": keyring.get_password(url, username)
        },
    )
    response.raise_for_status()
    return response.json()["access_token"]

def token_refresher():
    while True:
        try:
            token = fetch_token()
            os.environ["KERNEL_USER_TOKEN"] = token
            print("[INFO] Refreshed token.")
        except Exception as e:
            print(f"[ERROR] Token refresh failed: {e}")
        time.sleep(token_refresh_interval)

# Initial token
os.environ["KERNEL_SERVER_URL"] = url
os.environ["KERNEL_USER_TOKEN"] = fetch_token()

# Start token refresher thread
threading.Thread(target=token_refresher, daemon=True).start()

# Launch Jupyter
subprocess.run(["jupyter", "notebook"])


# import keyring
# import requests
# import os
#
# client_id = "wdanielsclient"
# url = "https://cs.trendminer.net"
#
# # Authenticate
# response = requests.post(
#     url=f"{url}/auth/realms/trendminer/protocol/openid-connect/token",
#     headers={"Content-Type": "application/x-www-form-urlencoded"},
#     data={
#         "grant_type": "client_credentials",
#         "client_id": client_id,
#         "client_secret": keyring.get_password(url, client_id),
#     },
# )
#
# # Initialize environment
# os.environ["KERNEL_SERVER_URL"] = url
# os.environ["KERNEL_USER_TOKEN"] = response.json()["access_token"]
#
# os.system("jupyter notebook")
