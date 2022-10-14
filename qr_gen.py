import pyqrcode
import png
from pyqrcode import QRCode

#Now we will take link which will be generated as QR code
s=str(input("Enter The Url : "))

#Now we will generate QR code
url=pyqrcode.create(s)

#Now we will create and save the png file with Some Name
name=str(input("Enter the name of File : "))
url.png(name+".png", scale = 6)
#if you want your Qrcode in SVG then uncomment line 16
# url.svg(name+".svg",scale=8)