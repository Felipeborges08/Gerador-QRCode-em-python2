
import qrcode

# Dados que voc� quer codificar no QR Code
data = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQC3rfJrKWyXB02JJADPgFRtXKGbabn0GMq4g&s"

# Cria��o do QR Code
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

qr.add_data(data)
qr.make(fit=True)

# Cria��o da imagem do QR Code
img = qr.make_image(fill_color="black", back_color="white")

# Salvando a imagem do QR Code
img.save("qrcode.png")
