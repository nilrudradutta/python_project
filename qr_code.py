from importlib.metadata import version
import qrcode as qr
img=qr.make("https://www.marvel.com/movies/avengers-endgame")
img.save("A great news for u.png")


from PIL import Image
qr=qr.QRCode(version=3,error_correction=qr.constants.ERROR_CORRECT_H,box_size=10,border=4,)
qr.add_data("https://www.marvel.com/movies/avengers-endgame")
qr.make(fit=True)
img=qr.make_image(fill_color="red",back_color="blue")
img.save("A great news for u.png")