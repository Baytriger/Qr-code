import qrcode
from PIL import Image

website_link = 'https://github.com/'

qr = qrcode.QRCode(version=4, box_size=5, border=5)
qr.add_data(website_link)
qr.make(fit=True)

img = qr.make_image(fill_color='green', back_color='white')
img.save('nnpc_qr.png')
img.show()

