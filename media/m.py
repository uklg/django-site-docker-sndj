#!/usr/bin/python3

from PIL import Image, ImageFont, ImageDraw

new = Image.new(mode="RGBA", size=(1920,1080))


draw = ImageDraw.Draw(new) 

#font = ImageFont.load_default().font

font = ImageFont.truetype("/usr/share/fonts/truetype/freefont/FreeMono.ttf", 64, encoding="unic")


#help(ImageFont.truetype)



text = 'Saturday Night DJ'


draw.text((5, 5), text, font=font, align ="left")
draw.text((6, 6), text, font=font, align ="left",fill=(255,0,0,255))
draw.text((7, 7), text, font=font, align ="left",fill=(255,255,0,255))


help(draw.text)


new.show()

