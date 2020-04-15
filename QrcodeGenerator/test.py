import qrcode

url = input('Enter url : ')
image = qrcode.make(url)
image.save('1.png')
