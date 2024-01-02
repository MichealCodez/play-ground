# import urllib.request
from PIL import Image
#
# # Retrieving the resource located at the URL
# # and storing it in the file name a.png
# for i in range(72):
#     i += 1
#     url = f"https://imgd-ct.aeplcdn.com/1280x720/cw/360/hyundai/1287/closed-door/ad1b2f/{i}.jpg"
#     urllib.request.urlretrieve(url, f"images/image{i}.png")
#
# # Opening the image and displaying it (to confirm its presence)
# # img = Image.open(r"geeksforgeeks.png")
# # img.show()
# import requests
#
# for i in range(72):
#     i += 1
#     img_data = requests.get(f"https://imgd-ct.aeplcdn.com/1280x720/cw/360/hyundai/1287/closed-door/ad1b2f/{i}.jpg", stream=True)
#     with open(f'images/image{i}.jpg', 'wb') as handler:
#         handler.write(img_data)
#         print(f"saved: image{i}.jpg")
#         img = Image.open(f"images/image{i}.jpg")
#         img.show()
import os
url1 = 'https://imgd-ct.aeplcdn.com/1280x720/cw/360/hyundai/1287/closed-door/ad1b2f/1.jpg'
os.system('wget {}'.format(url1))
