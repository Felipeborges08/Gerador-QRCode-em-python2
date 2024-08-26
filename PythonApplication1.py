
import qrcode

# Dados que você quer codificar no QR Code
data = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQC3rfJrKWyXB02JJADPgFRtXKGbabn0GMq4g&s"

# Criação do QR Code
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

qr.add_data(data)
qr.make(fit=True)

# Criação da imagem do QR Code
img = qr.make_image(fill_color="black", back_color="white")

# Salvando a imagem do QR Code
img.save("qrcode.png")
