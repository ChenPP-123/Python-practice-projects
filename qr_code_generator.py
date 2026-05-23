import qrcode

data = input("Enter some data or URL:").strip()
filename = input("Enter the filename:").strip()

qr = qrcode.QRCode(box_size=10, border=4)
qr.add_data(data)
image = qr.make_image(fill_color="black", back_color="white")
image.save(f"QRcode/{filename}")
print(f"QRcode has been saved as {filename}")
