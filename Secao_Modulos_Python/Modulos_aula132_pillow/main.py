from PIL import Image
from pathlib import Path

ROOT_FOLDER = Path(__file__).parent
ORIGINAL_IMAGE = ROOT_FOLDER / 'teste.jpg'
NEW_IMAGE = ROOT_FOLDER / 'new_teste.jpg'

pil_image = Image.open(ORIGINAL_IMAGE)
width, heigth = pil_image.size

new_width = 640
new_heigth = round(heigth * new_width / width)

new_image = pil_image.resize((new_width, new_heigth))
new_image.save(
    NEW_IMAGE,
    optimize=True,
    quality=70,
)
