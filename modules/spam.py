import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from colorama import Fore, Style

def send_spam_email(smtp_server, smtp_port, sender_email, sender_password, target_email, subject, message, count):
    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender_email, sender_password)
        
        for _ in range(count):
            msg = MIMEMultipart()
            msg['From'] = sender_email
            msg['To'] = target_email
            msg['Subject'] = subject
            msg.attach(MIMEText(message, 'plain'))
            server.sendmail(sender_email, target_email, msg.as_string())
            print(f"{Fore.GREEN}[+] Sent spam email to {target_email}{Style.RESET_ALL}")
        
        server.quit()
    except Exception as e:
        print(f"{Fore.RED}[-] Error: {e}{Style.RESET_ALL}")

def start_spam(config):
    print(f"{Fore.CYAN}=== Spam Email Tool ==={Style.RESET_ALL}")
    sender_email = input(f"{Fore.GREEN}Enter Your Email > {Style.RESET_ALL}")
    sender_password = input(f"{Fore.GREEN}Enter Your Password (App Password Recommended) > {Style.RESET_ALL}")
    target_email = input(f"{Fore.GREEN}Enter Target Email > {Style.RESET_ALL}")
    subject = input(f"{Fore.GREEN}Enter Email Subject > {Style.RESET_ALL}")
    message = input(f"{Fore.GREEN}Enter Email Message > {Style.RESET_ALL}")
    count = int(input(f"{Fore.GREEN}Enter Number of Emails to Send > {Style.RESET_ALL}"))

    smtp_server = 'smtp.gmail.com'
    smtp_port = 587

    send_spam_email(smtp_server, smtp_port, sender_email, sender_password, target_email, subject, message, count)
    input(f"{Fore.GREEN}Press Enter to Return to Menu > {Style.RESET_ALL}")
