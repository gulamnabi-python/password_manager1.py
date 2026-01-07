import base64
import os

FILE_NAME = "passwords.txt"
MASTER_PASSWORD = "admin123"

def encrypt(text):
    return base64.b64encode(text.encode()).decode()

def decrypt(text):
    return base64.b64decode(text.encode()).decode()

def save_password():
    website = input("Website: ")
    username = input("Username: ")
    password = input("Password: ")

    enc_pass = encrypt(password)

    with open(FILE_NAME, "a") as f:
        f.write(f"{website}|{username}|{enc_pass}\n")

    print("✅ Password saved")

def view_passwords():
    if not os.path.exists(FILE_NAME):
        print("❌ No passwords found")
        return

    with open(FILE_NAME, "r") as f:
        for line in f:
            website, username, enc_pass = line.strip().split("|")
            print("Website:", website)
            print("Username:", username)
            print("Password:", decrypt(enc_pass))
            print("-" * 30)

def main():
    master = input("Enter Master Password: ")
    if master != MASTER_PASSWORD:
        print("❌ Wrong Master Password")
        return

    while True:
        print("\n1. Save Password")
        print("2. View Passwords")
        print("3. Exit")

        choice = input("Choose: ")

        if choice == "1":
            save_password()
        elif choice == "2":
            view_passwords()
        elif choice == "3":
            print("👋 Bye")
            break
        else:
            print("❌ Invalid choice")

main()
