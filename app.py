import hashlib
import os
import json

HASH_FILE = "file_hashes.json"

def calculate_hash(file_path, algorithm='sha256'):
    """Calculate the hash of a file."""
    hasher = hashlib.new(algorithm)
    try:
        with open(file_path, 'rb') as f:
            while chunk := f.read(4096):
                hasher.update(chunk)
        return hasher.hexdigest()
    except FileNotFoundError:
        return None

def load_hashes():
    """Load stored hash values from the JSON file."""
    if os.path.exists(HASH_FILE):
        with open(HASH_FILE, 'r') as f:
            return json.load(f)
    return {}

def save_hashes(hashes):
    """Save hash values to the JSON file."""
    with open(HASH_FILE, 'w') as f:
        json.dump(hashes, f, indent=4)

def generate_hashes(directory):
    """Generate and store file hashes."""
    hashes = {}
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            hashes[file_path] = calculate_hash(file_path)
    save_hashes(hashes)
    print("Hashes generated and saved.")

def check_files(directory):
    """Check files for modifications."""
    stored_hashes = load_hashes()
    current_hashes = {}
    modified_files = []
    
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            current_hash = calculate_hash(file_path)
            current_hashes[file_path] = current_hash
            
            if file_path in stored_hashes:
                if stored_hashes[file_path] != current_hash:
                    modified_files.append(file_path)
            else:
                print(f"[NEW] File added: {file_path}")
    
    for file_path in stored_hashes:
        if file_path not in current_hashes:
            print(f"[DELETED] File missing: {file_path}")
    
    if modified_files:
        print("[MODIFIED] The following files were changed:")
        for file in modified_files:
            print(f" - {file}")
    else:
        print("No modifications detected.")
    
    save_hashes(current_hashes)

def main():
    directory = input("Enter the directory path: ")
    action = input("Generate new hashes or check files? (generate/check): ").strip().lower()
    if action == "generate":
        generate_hashes(directory)
    elif action == "check":
        check_files(directory)
    else:
        print("Invalid option. Please enter 'generate' or 'check'.")

if __name__ == "__main__":
    main()
