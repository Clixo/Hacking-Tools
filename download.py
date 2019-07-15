import requests

def download(url):
    get_response = requests.get(url)
    file_name = url.split("/")[-1]
    print(file_name)
    with open(file_name, "wb") as out_file:
        out_file.write(get_response.content)

download("https://vignette.wikia.nocookie.net/horrormovies/images/9/90/Pinhead-0.png/revision/latest?cb=20170318002557")