import os
import json
import time
import sys
from colorama import Fore, Style, init
from pystyle import Colors, Center
from modules import phishing, ddos, spam, recon

init(autoreset=True)

# Memuat konfigurasi
def load_config():
    try:
        with open('config.json', 'r') as f:
            return json.load(f)
    except Exception as e:
        print(f"{Fore.RED}Error loading config: {e}{Style.RESET_ALL}")
        sys.exit(1)

config = load_config()

# Menampilkan banner
def display_banner():
    with open('assets/logo.txt', 'r') as f:
        logo = f.read()
    os.system('clear' if os.name == 'posix' else 'cls')
    print(Center.XCenter(Colors.gold_to_red(logo)))
    print(Center.XCenter(f"{Fore.CYAN}0xGolip-Team | RedOps Elite | Premium Toolkit v1.0{Style.RESET_ALL}"))
    print(Center.XCenter(f"{Fore.YELLOW}Hacking Made Simple for Elite Users - Rp 23 Juta Exclusive{Style.RESET_ALL}"))
    print(f"{Fore.MAGENTA}{'='*80}{Style.RESET_ALL}")

# Animasi loading yang menarik
def loading_animation(text):
    for i in range(3):
        for char in ['|', '/', '-', '\\']:
            sys.stdout.write(f"\r{Fore.YELLOW}[{char}] {text}...{Style.RESET_ALL}")
            sys.stdout.flush()
            time.sleep(0.1)
    print()

# Menu Utama
def main_menu():
    while True:
        display_banner()
        print(f"{Fore.CYAN}=== 0xGolip-Toolkit Menu ==={Style.RESET_ALL}")
        print(f"{Fore.YELLOW}1. Phishing Module{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}2. DDoS Attack Tool{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}3. Spam Email Tool{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}4. Information Gathering{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}5. Utilities{Style.RESET_ALL}")
        print(f"{Fore.RED}6. Exit{Style.RESET_ALL}")
        print(f"{Fore.MAGENTA}{'='*80}{Style.RESET_ALL}")

        choice = input(f"{Fore.GREEN}Select Option > {Style.RESET_ALL}")
        if choice == '1':
            loading_animation("Loading Phishing Module")
            phishing.start_phishing(config)
        elif choice == '2':
            loading_animation("Loading DDoS Attack Tool")
            ddos.start_ddos(config)
        elif choice == '3':
            loading_animation("Loading Spam Email Tool")
            spam.start_spam(config)
        elif choice == '4':
            loading_animation("Loading Information Gathering")
            recon.start_recon(config)
        elif choice == '5':
            loading_animation("Loading Utilities")
            utilities_menu()
        elif choice == '6':
            print(f"{Fore.RED}Exiting 0xGolip-Toolkit. Stay Elite!{Style.RESET_ALL}")
            break
        else:
            print(f"{Fore.RED}Invalid Option! Please try again.{Style.RESET_ALL}")
            time.sleep(1)

# Menu Utilities
def utilities_menu():
    while True:
        display_banner()
        print(f"{Fore.CYAN}=== Utilities Menu ==={Style.RESET_ALL}")
        print(f"{Fore.YELLOW}1. Hash Generator{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}2. Encoder/Decoder{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}3. Banner Maker Premium{Style.RESET_ALL}")
        print(f"{Fore.RED}4. Back to Main Menu{Style.RESET_ALL}")
        choice = input(f"{Fore.GREEN}Select Utility > {Style.RESET_ALL}")
        if choice == '1':
            hash_generator()
        elif choice == '2':
            encoder_decoder()
        elif choice == '3':
            banner_maker()
        elif choice == '4':
            break
        else:
            print(f"{Fore.RED}Invalid Option! Please try again.{Style.RESET_ALL}")
            time.sleep(1)

if __name__ == "__main__":
    main_menu()
