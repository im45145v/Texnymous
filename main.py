import os
from twilio.rest import Client
from PIL import Image, ImageDraw, ImageFont
import requests
import deso
import var
desoSocial = deso.Social(var.PUBLIC_KEY,var.SEED_HEX)
desoMedia = deso.Media(var.PUBLIC_KEY,var.SEED_HEX)
a = int(input("To number : \n"))
c = input("Your confession\n")

client = Client(var.account_sid, var.auth_token)
message = client.messages.create(
                              from_='whatsapp:+14155238886',
                              body=c,
                              to='whatsapp:+'+str(a)
                          )
print(message.sid)

width = 400
height = 150
img = Image.new('RGB', (width, height), color='black')
imgDraw = ImageDraw.Draw(img)
imgDraw.text((15, 15), c,  fill=(255, 255, 0))
img.save('img.png')
imageFileList = [('file',('screenshot.jpg',open("img.png","rb"),'image/png'))] 
urlResponse = desoMedia.uploadImage(fileList=imageFileList)
y = urlResponse.json()
z = y['ImageURL']
q = desoSocial.submitPost(body=c, imageURLs=[z])
