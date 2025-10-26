import os
import shutil

print("📁 FILE & IMAGE ENCRYPTION TOOL")
print("=" * 40)

def encrypt_file(file_path, key):
    """Simple file encryption - works for ANY file type"""
    try:
        # Read file as binary
        with open(file_path, 'rb') as f:
            file_data = f.read()
        
        # Simple XOR encryption
        key_bytes = key.encode('utf-8')
        encrypted_data = bytearray()
        
        for i, byte in enumerate(file_data):
            encrypted_byte = byte ^ key_bytes[i % len(key_bytes)]
            encrypted_data.append(encrypted_byte)
        
        # Save encrypted file
        file_name = os.path.basename(file_path)
        encrypted_path = f"encrypted_{file_name}"
        
        with open(encrypted_path, 'wb') as f:
            f.write(encrypted_data)
        
        print(f"✅ Encrypted: {encrypted_path}")
        return encrypted_path
        
    except Exception as e:
        print(f"❌ Encryption failed: {e}")
        return None

def decrypt_file(file_path, key):
    """Simple file decryption - works for ANY file type"""
    try:
        # Read encrypted file
        with open(file_path, 'rb') as f:
            encrypted_data = f.read()
        
        # XOR decryption (same as encryption)
        key_bytes = key.encode('utf-8')
        decrypted_data = bytearray()
        
        for i, byte in enumerate(encrypted_data):
            decrypted_byte = byte ^ key_bytes[i % len(key_bytes)]
            decrypted_data.append(decrypted_byte)
        
        # Save decrypted file
        file_name = os.path.basename(file_path)
        decrypted_path = f"decrypted_{file_name.replace('encrypted_', '')}"
        
        with open(decrypted_path, 'wb') as f:
            f.write(decrypted_data)
        
        print(f"✅ Decrypted: {decrypted_path}")
        return decrypted_path
        
    except Exception as e:
        print(f"❌ Decryption failed: {e}")
        return None

def list_files():
    """Show all files in current folder"""
    print("\n📂 Files in current folder:")
    files = [f for f in os.listdir('.') if os.path.isfile(f)]
    for i, file in enumerate(files, 1):
        print(f"  {i}. {file}")
    return files

def upload_file():
    """Copy file from another location to current folder"""
    try:
        source_path = input("Enter full path of file to upload: ")
        
        if not os.path.exists(source_path):
            print("❌ File not found!")
            return None
            
        file_name = os.path.basename(source_path)
        dest_path = file_name
        
        # Copy file to current directory
        shutil.copy2(source_path, dest_path)
        print(f"✅ Uploaded: {file_name}")
        return dest_path
        
    except Exception as e:
        print(f"❌ Upload failed: {e}")
        return None

def main():
    while True:
        print("\n" + "="*50)
        print("1. 📂 List All Files")
        print("2. ⬆️  Upload File/Image")
        print("3. 🔒 Encrypt File/Image")
        print("4. 🔓 Decrypt File/Image")
        print("5. 🚪 Exit")
        print("="*50)
        
        choice = input("\nChoose (1-5): ").strip()
        
        if choice == "1":
            list_files()
            
        elif choice == "2":
            uploaded_file = upload_file()
            if uploaded_file:
                print(f"🎉 Ready to encrypt: {uploaded_file}")
            
        elif choice == "3":
            files = list_files()
            if not files:
                print("❌ No files found! Upload files first.")
                continue
                
            try:
                file_num = int(input("Enter file number to encrypt: "))
                if 1 <= file_num <= len(files):
                    file_to_encrypt = files[file_num - 1]
                    key = input("Enter encryption password: ")
                    encrypt_file(file_to_encrypt, key)
                else:
                    print("❌ Invalid file number!")
            except ValueError:
                print("❌ Please enter a valid number!")
                
        elif choice == "4":
            files = list_files()
            if not files:
                print("❌ No files found!")
                continue
                
            try:
                file_num = int(input("Enter file number to decrypt: "))
                if 1 <= file_num <= len(files):
                    file_to_decrypt = files[file_num - 1]
                    key = input("Enter decryption password: ")
                    decrypt_file(file_to_decrypt, key)
                else:
                    print("❌ Invalid file number!")
            except ValueError:
                print("❌ Please enter a valid number!")
                
        elif choice == "5":
            print("👋 Goodbye!")
            break
            
        else:
            print("❌ Please choose 1-5")

if __name__ == "__main__":
    # Create a sample text file for testing
    with open("sample.txt", "w") as f:
        f.write("This is a secret message!")
    print("✅ Created sample.txt for testing")
    
    main()