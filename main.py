from encryptor import encrypt_file, decrypt_file

def main():
    print("=== CyberSafe File Encryption Tool ===")
    print("1. Encrypt a file")
    print("2. Decrypt a file")

    choice = input("Choose an option (1 or 2): ")

    file_path = input("Enter file path: ")
    password = input("Enter password: ")

    if choice == "1":
        encrypt_file(file_path, password)
        print("File encrypted successfully!")

    elif choice == "2":
        decrypt_file(file_path, password)
        print("File decrypted successfully!")

    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()
