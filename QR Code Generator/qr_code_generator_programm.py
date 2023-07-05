import qrcode

def generate_qrcode(text):
    qr = qrcode.QRCode(
        version = 1,
        error_correction = qrcode.constants.ERROR_CORRECT_L,
        box_size = 15,
        border = 5,
    )
    
    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill_color = "black", back_color = "white")
    img.save("Muqumov Samandarbek")
    
url = input("Enter yout URL link too create QR Code version: ")
generate_qrcode(url)
    