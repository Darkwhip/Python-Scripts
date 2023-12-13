from PIL import Image

img = Image.new('RGB', (100, 100), color='green')
img.save('pil_green.png')
