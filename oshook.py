import platform, psutil, requests, socket, subprocess, os, re
from datetime import datetime

def get_processor_name():
    if platform.system() == "Windows":
        return platform.processor()
    elif platform.system() == "Darwin":
        os.environ['PATH'] = os.environ['PATH'] + os.pathsep + '/usr/sbin'
        command ="sysctl -n machdep.cpu.brand_string"
        return subprocess.check_output(command).strip()
    elif platform.system() == "Linux":
        command = "cat /proc/cpuinfo"
        all_info = subprocess.check_output(command, shell=True).decode().strip()
        for line in all_info.split("\n"):
            if "model name" in line:
                return re.sub( ".*model name.*:", "", line,1)
    return ""

def send_discord_webhook(webhook_url):
    computer_name = socket.gethostname()
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    ip_address = socket.gethostbyname(socket.gethostname())
    operating_system = platform.platform()
    cpu_info = get_processor_name()
    cpu_cores = psutil.cpu_count(logical=False)
    cpu_architecture = platform.machine()
    cpu_usage = psutil.cpu_percent(interval=1)
    memory_info = psutil.virtual_memory().total / (1024 ** 3)
    memory_used = psutil.virtual_memory().used / (1024 ** 3)
    disk_info = psutil.disk_usage('/').total / (1024 ** 3)
    disk_used = psutil.disk_usage('/').used / (1024 ** 3)
    battery_info = psutil.sensors_battery()

    # Embedding
    embed = {
        "color": 0xfff,
        "author": {"name": "System Information", "icon_url": "https://www.pngall.com/wp-content/uploads/2/Windows-Logo.png"},
        "thumbnail": {"url": "https://www.pngall.com/wp-content/uploads/2/Windows-Logo.png"},
        "fields": [
            {"name": "Computer Name", "value": computer_name, "inline": True},
            {"name": "Current Time", "value": current_time, "inline": True},
            {"name": "IP Address", "value": ip_address, "inline": True},
            {"name": "Operating System", "value": operating_system, "inline": False},
            {"name": "CPU", "value": cpu_info, "inline": True},
            {"name": "CPU Architecture", "value": cpu_architecture, "inline": True},
            {"name": "Number of CPU Cores", "value": cpu_cores, "inline": True},
            {"name": "Total CPU Usage", "value": f"{cpu_usage}%", "inline": True},
            {"name": "Memory", "value": f"{memory_info:.2f} GB", "inline": True},
            {"name": "Memory Used", "value": f"{memory_used:.2f} GB", "inline": True},
            {"name": "Total Disk Space", "value": f"{disk_info:.2f} GB", "inline": True},
            {"name": "Disk Used Space", "value": f"{disk_used:.2f} GB", "inline": True},
            {"name": "Battery Information", "value": str(battery_info), "inline": True}
        ]
    }

    # Create payload
    payload = {
        "embeds": [embed]
    }

    # Post request
    response = requests.post(webhook_url, json=payload)
    
    # Checks for successful response (Status Code 204)
    if response.status_code == 204:
        print("Webhook sent successfully.")
    else:
        print(f"Failed to send webhook. Status code: {response.status_code}")

if __name__ == "__main__":
    webhook_url = 'https://discord.com/api/webhooks/1232383567720480780/LLg0QP4yZadG2M52Ih02ULNhZWTOa49beOfsqStE-PBC6e03AnNGgXw67T7c5aBB93lv' # Replace with Webhook URL
    send_discord_webhook(webhook_url)
