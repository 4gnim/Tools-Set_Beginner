import hashlib

def crack_hash(hash_to_crack, hash_type, wordlist_file):
    try:
        # Open the wordlist file
        with open(wordlist_file, 'r', encoding='utf-8', errors='ignore') as file:
            for word in file:
                word = word.strip()
                
                # Select hash type
                if hash_type == "md5":
                    hashed_word = hashlib.md5(word.encode()).hexdigest()
                elif hash_type == "sha1":
                    hashed_word = hashlib.sha1(word.encode()).hexdigest()
                elif hash_type == "sha256":
                    hashed_word = hashlib.sha256(word.encode()).hexdigest()
                else:
                    print(f"Hash type {hash_type} is not supported.")
                    return
                
                # Compare the hash
                if hashed_word == hash_to_crack:
                    print(f"[+] Hash cracked: {word}")
                    return
                
        print("[-] Hash not found in the wordlist.")
    except FileNotFoundError:
        print("Wordlist file not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    print("===== Hash Cracker =====")
    hash_to_crack = input("Enter the hash to crack: ")
    hash_type = input("Enter the hash type (md5/sha1/sha256): ").lower()
    wordlist_file = input("Enter the path to the wordlist file: ")
    
    crack_hash(hash_to_crack, hash_type, wordlist_file)
