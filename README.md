# OS/System Information Discord Webhook Generator

This Python script collects system information and sends it to a Discord webhook. It provides details about the user's computer hardware, operating system, and resource usage.

## Features

- Simple webhook generator that displays information about your system sent through a webhook.
- Highly configurable allowing for new information by experimenting with the [psutil]([https://docs.python.org/3/library/platform.html) and [platform](https://docs.python.org/3/library/platform.html) modules.

## Requirements

- Python 3.x 
- `platform`, `psutil`, `requests`, `socket`, `datetime`, `subprocess`, `re`, `os` Python modules.

## Installation

1. Clone this repository to your machine (or download it for that matter):

   ```bash
   git clone https://github.com/Kermit1246/oshook.git

2. Install the required Python modules:

   ```bash
    pip install -r requirements.txt

3. Replace 'webhook_goes_here' with your Discord webhook URL in the send_discord_webhook() function.

## Usage
Run the script:

   ```bash
    python oshook.py
