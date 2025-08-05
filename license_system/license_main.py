import os
import uuid
import hashlib
import time
from datetime import datetime, timedelta

# Function to get unique device ID
def get_device_id():
    return hashlib.md5(str(uuid.getnode()).encode()).hexdigest()

# Generate license key
def generate_license(days):
    expiry = datetime.now() + timedelta(days=days)
    device_id = get_device_id()
    return f"{device_id}|{expiry.strftime('%Y-%m-%d')}"

# Save license file
def save_license_file(license_key):
    with open("license.txt", "w") as f:
        f.write(license_key)

# Check license validity
def is_license_valid():
    try:
        with open("license.txt", "r") as f:
            content = f.read().strip()
        device_id, expiry = content.split("|")
        if device_id != get_device_id():
            return False
        if datetime.now() > datetime.strptime(expiry, '%Y-%m-%d'):
            return False
        return True
    except:
        return False

# License prompt for user
def ask_license():
    print("""
📅 Select License Duration:
[1] 7 Days
[2] 30 Days
[3] 90 Days
""")
    option = input("👉 Type 1/2/3: ").strip()
    if option == "1":
        license_key = generate_license(7)
    elif option == "2":
        license_key = generate_license(30)
    elif option == "3":
        license_key = generate_license(90)
    else:
        print("❌ Invalid selection.")
        exit()

    print("\n✅ Copy this LICENSE KEY and send to Admin (Ajmal 👑) for approval:\n")
    print(f"🔐 {license_key}")
    print("\n📩 Jab license.txt mil jaaye, script dobara run karein.\n")
    exit()

# 🔧 MAIN FUNCTION
def main():
    if not is_license_valid():
        ask_license()

    print("\n✅ License Verified! Welcome 💖\n")
    print("🎯 Starting Facebook Account Creator Tool...")

    # 👇 Yahan aapka actual Facebook creator code aayega:
    print("\n🔧 (Facebook Account Creator Running...)")
    print("👤 Account created successfully!")

# 🔥 START
if __name__ == "__main__":
    main()
