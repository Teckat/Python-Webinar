from PIL import Image, ImageDraw, ImageFont
import os


def certificate(certiNum, name):

    print(os.getcwd())

    # join the cwd path
    path = os.path.join(os.getcwd(), 'day8')

    # open the image
    image = Image.open(r''+path + '\certificate\certificate.jpg')

    draw = ImageDraw.Draw(image)

    # font style and size

    fontCerti = ImageFont.truetype(r''+path+'\style\DancingScript.ttf', 80)
    fontName = ImageFont.truetype(r''+path+'\style\DancingScript.ttf', 150)

    # draw certificate no.
    (x, y) = (2500, 100)
    color = 'rgb(0,0,0)'

    w, h = draw.textsize(certiNum, font=fontCerti)

    draw.text((x-(w/2), y), certiNum, fill=color, font=fontCerti)

    # draw name.
    (x, y) = (1700, 1100)
    color = 'rgb(0,0,0)'

    w, h = draw.textsize(name, font=fontName)

    draw.text((x-(w/2), y), name, fill=color, font=fontName)

    # saving image
    image.save(r''+path+'\certificate\\'+name+'.jpg')


certificate("C-no. : teckat123abc1516256121626121", "Akash Biswal Misra Rai")
