from PIL import Image, ImageDraw, ImageFont

img = Image.new('RGB', (200,100), color = (55, 200, 144))

fnt = ImageFont.truetype('/fonts/BebasNeue Bold.ttf',10)
d = ImageDraw.Draw(img)
d.text((2,2), "Glimmer did nothing wrong", font = fnt, spacing=1, fill = (212, 98, 142))

img.save('pil_text.png')
img.show()
