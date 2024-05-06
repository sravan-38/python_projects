import qrcode

def generate_qrcode(text):
    # Initialize QRCode object
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    # Add data to QRCode
    qr.add_data(text)
    qr.make(fit=True)

    # Create PIL Image object
    img = qr.make_image(fill_color="black", back_color="white")

    # Save image
    img.save("qrimg001.png")

url = input("Enter your URL: ")
generate_qrcode(url)
