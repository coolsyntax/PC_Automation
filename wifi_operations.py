import subprocess
import re
from voice_engine import speak, takeCommand


def connect_to_wifi():
    devices = subprocess.check_output(['netsh', 'wlan', 'show', 'network'])
    devices = devices.decode('utf8').replace("\r", "")
    wifi_names = re.findall("(?:Profile\s*:\s)(.*)", devices)

    speak("Available Wi-Fi networks are:")
    for i, name in enumerate(wifi_names, 1):
        speak(f"{i} for {name}")

    speak("Which network would you like to connect to?")
    choice = int(takeCommand()) - 1
    name = wifi_names[choice]

    speak("Please say the password")
    password = takeCommand()

    config = f"""<?xml version=\"1.0\"?>
    <WLANProfile xmlns="http://www.microsoft.com/networking/WLAN/profile/v1">
        <name>{name}</name>
        <SSIDConfig>
            <SSID>
                <name>{name}</name>
            </SSID>
        </SSIDConfig>
        <connectionType>ESS</connectionType>
        <connectionMode>auto</connectionMode>
        <MSM>
            <security>
                <authEncryption>
                    <authentication>WPA2PSK</authentication>
                    <encryption>AES</encryption>
                    <useOneX>false</useOneX>
                </authEncryption>
                <sharedKey>
                    <keyType>passPhrase</keyType>
                    <protected>false</protected>
                    <keyMaterial>{password}</keyMaterial>
                </sharedKey>
            </security>
        </MSM>
    </WLANProfile>"""

    with open(f"{name}.xml", 'w') as file:
        file.write(config)

    command = f"netsh wlan add profile filename=\"{name}.xml\" interface=Wi-Fi"
    subprocess.run(command, shell=True)

    connect_command = f"netsh wlan connect name=\"{
        name}\" ssid=\"{name}\" interface=Wi-Fi"
    subprocess.run(connect_command, shell=True)

    speak(f"Attempting to connect to {name}")


def enable_wifi():
    subprocess.run(['netsh', 'interface', 'set',
                   'interface', "Wi-Fi", "ENABLED"])
    speak("Wi-Fi has been enabled")


def disable_wifi():
    subprocess.run(['netsh', 'interface', 'set',
                   'interface', "Wi-Fi", "DISABLED"])
    speak("Wi-Fi has been disabled")
