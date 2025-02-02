# Tor Proxy Rotator 🕵️‍♂️🔄

Tor Proxy Rotator is a Python-based tool that automatically rotates your IP address using the **Tor network**. It allows you to send web requests through different Tor exit nodes, providing anonymity and security.

## Features 🚀

- Automatically rotates IP addresses via the **Tor network**.
- Uses **Stem** to control Tor and issue new identity requests.
- Sends HTTP(S) requests through Tor-protected proxies.
- Interactive CLI with real-time IP updates.

## How It Works ⚙️

1. The script connects to the **Tor network**.
2. It periodically requests a new identity from Tor.
3. All web requests are routed through different Tor exit nodes.
4. The current Tor IP is displayed after each rotation.

## Requirements 🛠️

Ensure you have Python and the following dependencies installed:

- **Tor** (Make sure the Tor service is running)
- **Requests**
- **Stem**

Install the dependencies using the following command:

```bash
sudo apt install tor  # For Linux
brew install tor      # For macOS
choco install tor     # For Windows (Chocolatey)
pip install requests stem
```
