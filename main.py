
import qrcode
link = input("Enter the link of which you want to generate QR of :\n> ")
img = qrcode.make(link)
img.save("GeneratedQR.png")
