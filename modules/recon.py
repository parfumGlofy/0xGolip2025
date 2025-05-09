import whois
import dns.resolver
from colorama import Fore, Style

def whois_lookup(domain):
    try:
        w = whois.whois(domain)
        print(f"{Fore.YELLOW}[+] WHOIS Information for {domain}:{Style.RESET_ALL}")
        print(w)
    except Exception as e:
        print(f"{Fore.RED}[-] Error during WHOIS lookup: {e}{Style.RESET_ALL}")

def dns_lookup(domain):
    try:
        result = dns.resolver.resolve(domain, 'A')
        print(f"{Fore.YELLOW}[+] DNS Records for {domain}:{Style.RESET_ALL}")
        for ipval in result:
            print(f"IP Address: {ipval.to_text()}")
    except Exception as e:
        print(f"{Fore.RED}[-] Error during DNS lookup: {e}{Style.RESET_ALL}")

def start_recon(config):
    print(f"{Fore.CYAN}=== Information Gathering ==={Style.RESET_ALL}")
    domain = input(f"{Fore.GREEN}Enter Domain to Recon > {Style.RESET_ALL}")
    print(f"{Fore.YELLOW}[*] Performing WHOIS Lookup...{Style.RESET_ALL}")
    whois_lookup(domain)
    print(f"{Fore.YELLOW}[*] Performing DNS Lookup...{Style.RESET_ALL}")
    dns_lookup(domain)
    input(f"{Fore.GREEN}Press Enter to Return to Menu > {Style.RESET_ALL}")
