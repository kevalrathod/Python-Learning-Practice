import requests
from PIL import Image
url = 'https://www.google.com/favicon.ico'
r = requests.get(url, allow_redirects=True)
open('imgg/google.ico', 'wb').write(r.content)
img=Image.open('google.ico')
img.show()

