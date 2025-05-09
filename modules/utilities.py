import hashlib
from colorama import Fore, Style

def hash_generator():
    print(f"{Fore.CYAN}=== Hash Generator ==={Style.RESET_ALL}")
    text = input(f"{Fore.GREEN}Enter text to hash > {Style.RESET_ALL}")
    hash_type = input(f"{Fore.GREEN}Enter hash type (md5, sha1, sha256) > {Style.RESET_ALL}").lower()
    
    if hash_type == 'md5':
        print(f"{Fore.YELLOW}MD5: {hashlib.md5(text.encode()).hexdigest()}{Style.RESET_ALL}")
    elif hash_type == 'sha1':
        print(f"{Fore.YELLOW}SHA1: {hashlib.sha1(text.encode()).hexdigest()}{Style.RESET_ALL}")
    elif hash_type == 'sha256':
        print(f"{Fore.YELLOW}SHA256: {hashlib.sha256(text.encode()).hexdigest()}{Style.RESET_ALL}")
    else:
        print(f"{Fore.RED}[-] Invalid hash type!{Style.RESET_ALL}")
    input(f"{Fore.GREEN}Press Enter to Return to Menu > {Style.RESET_ALL}")

def encoder_decoder():
    print(f"{Fore.CYAN}=== Encoder/Decoder ==={Style.RESET_ALL}")
    text = input(f"{Fore.GREEN}Enter text > {Style.RESET_ALL}")
    choice = input(f"{Fore.GREEN}Choose operation (encode/decode) > {Style.RESET_ALL}").lower()
    
    if choice == 'encode':
        encoded = text.encode('utf-8').hex()
        print(f"{Fore.YELLOW}Encoded: {encoded}{Style.RESET_ALL}")
    elif choice == 'decode':
        try:
            decoded = bytes.fromhex(text).decode('utf-8')
            print(f"{Fore.YELLOW}Decoded: {decoded}{Style.RESET_ALL}")
        except Exception as e:
            print(f"{Fore.RED}[-] Error decoding: {e}{Style.RESET_ALL}")
    else:
        print(f"{Fore.RED}[-] Invalid choice!{Style.RESET_ALL}")
    
    input(f"{Fore.GREEN}Press Enter to Return to Menu > {Style.RESET_ALL}")
