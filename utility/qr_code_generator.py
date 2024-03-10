import qrcode


def qr_code_generator(link: str):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    qr.add_data(link)
    img = qr.make_image(fill_color="black", black_color="white")

    img.save("qrcode.png")

