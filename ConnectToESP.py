import requests

ESP32_IP = "192.168.4.1"

while 1:
    choice = input("LED On or Off ")

    if choice.lower() == "on":
        requests.get(f"http://{ESP32_IP}/H")  # ON
    elif choice.lower() == "off":
        requests.get(f"http://{ESP32_IP}/L")  # OFF
