# Hash Cracker

Hash Cracker is a simple Python tool designed to crack hashes using dictionary attacks. It supports popular hash algorithms like MD5, SHA-1, and SHA-256.

## Features

- Supports cracking **MD5**, **SHA-1**, and **SHA-256** hashes.
- Uses a wordlist file for dictionary-based cracking.
- Easy to use and customizable.

## How It Works

The tool reads a hash value and compares it with the hashes of words in a given wordlist file. If a match is found, the original word (password) is displayed.

## Requirements

- Python 3.x
- A wordlist file (e.g., `rockyou.txt` or a custom wordlist).

## Usage

1. Run the script:
   ```bash
   python hash_cracker.py
   ```
2. Follow the prompts to:
   - Enter the hash to crack.
   - Specify the hash type (`md5`, `sha1`, or `sha256`).
   - Provide the path to your wordlist file.

### Example

```plaintext
===== Hash Cracker =====
Enter the hash to crack: 5d41402abc4b2a76b9719d911017c592
Enter the hash type (md5/sha1/sha256): md5
Enter the path to the wordlist file: wordlist.txt
[+] Hash found: hello
```

## Disclaimer

This tool is intended for educational and ethical purposes only. Use it to test the security of your own systems or with explicit permission. The author is not responsible for any misuse of this tool.
