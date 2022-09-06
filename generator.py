from PIL import ImageDraw, Image, ImageFont, ImageOps
import requests
from io import BytesIO




def generate_guild_card(user, guild, record, conquistas, background):
    if len(user) >= 15 :
        FontUSER = ImageFont.truetype(r'.\fonts\ReggaeOne-Regular.ttf', 50)
    else:
        FontUSER = ImageFont.truetype(r'.\fonts\ReggaeOne-Regular.ttf', 72)

    template = background
    rank = 0
    for i in conquistas:
        if i == 'andar100':
            rank += 10
            template.paste(imgroad, (613, 211), imgroad)
        if i == 'caravan':
            template.paste(imgcaravan, (931, 211), imgcaravan)
            rank += 10
        if i == 'elzellion':
            template.paste(imgelzellion, (1250, 211), imgelzellion)
            rank += 15
        if i == 'boga':
            template.paste(imgboga, (1568, 211), imgboga)
            rank += 10
        if i == 'disu':
            template.paste(imgdisufiora, (613, 442), imgdisufiora)
            rank += 10
        if i == 'guard':
            template.paste(imgguard, (931, 442), imgguard)
            rank += 10
        if i == 'gwan':
            template.paste(imggwan, (1250, 442), imggwan)
            rank += 10
        if i == 'mama':
            template.paste(imgmama, (1568, 442), imgmama)
            rank += 5
        if i == 'miru':
            template.paste(imgmiru, (613, 673), imgmiru)
            rank += 5
        if i == 'pari':
            template.paste(imgpari, (931, 673), imgpari)
            rank += 5
        if i == 'quem':
            template.paste(imgquem, (1250, 673), imgquem)
            rank += 10
        if i == 'zeru':
            template.paste(imgzeru, (1568, 673), imgzeru)
            rank += 20
        if i == 'jino':
            template.paste(imgjino, (613, 906), imgjino)
            rank += 10
        if i == 'rajang':
            template.paste(imgrajang, (931, 906), imgrajang)
            rank += 5
        if i == 'narga':
            template.paste(imgnarga, (1250, 906), imgnarga)
            rank += 10
        if i == 'jho':
            template.paste(imgdeviljho, (1568, 906), imgdeviljho)
            rank += 5

    infos = ImageDraw.Draw(template)
    infos.text((205, 882), f'{guild}', font=myFont, fill=(0, 0, 0))
    infos.text((450, 940), f'{record}', font=myFont, fill=(0, 0, 0))
    infos.text((105, 200), f'{user}', font=FontUSER, fill=(0, 0, 0))
    if rank == 0:
        infos.text((350, 990), f'D', font=FontRank, fill=(195, 123, 252), stroke_width=8,
        stroke_fill="black")
    if rank >= 5 and rank < 30 :
        infos.text((350, 990), f'C', font=FontRank, fill=(0, 26, 255), stroke_width=8,
        stroke_fill="black")
    if rank >= 30 and rank < 75:
        infos.text((350, 990), f'B', font=FontRank, fill=(38, 255, 2), stroke_width=8,
        stroke_fill="black" )
    if rank >= 75 and rank < 150:
        infos.text((350, 990), f'A', font=FontRank, fill=(250, 255, 0), stroke_width=8,
        stroke_fill="black")
    if rank >= 150:
        infos.text((350, 990), f'S', font=FontRank, fill=(255, 0, 0), stroke_width=8,
        stroke_fill="black")

    return template



def user_image(urlimage):
    urlimage = urlimage.resize((417, 417));
    bigsize = (urlimage.size[0] * 3, urlimage.size[1] * 3)
    mask = Image.new('L', bigsize, 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0) + bigsize, fill=255)
    mask = mask.resize(urlimage.size, Image.ANTIALIAS)
    urlimage.putalpha(mask)

    output = ImageOps.fit(urlimage, mask.size, centering=(0.5, 0.5))
    output.putalpha(mask)

    background = Image.open('./guildcard/base.png', mode='r')
    background.paste(urlimage, (101, 335), urlimage)
    return background
def generator_jpg(url):
    imgurl = requests.get(url)
    urlimg = Image.open(BytesIO(imgurl.content))
    return urlimg







FontRank = ImageFont.truetype(r'.\fonts\DMC5Font.otf',150)
myFont = ImageFont.truetype(r'.\fonts\monsterhunter.ttf', 50)
guildcard = Image.open(r'.\guildcard\base.png')
imgroad = Image.open(r".\awards\Andar 100.png")#road
imgcaravan = Image.open(r".\awards\Max. Caravan.png")
imgelzellion = Image.open(r".\awards\Elzelion.png")
imgboga = Image.open(r".\awards\Boga.png") # Boga
imgdisufiora = Image.open(r".\awards\Disufiora.png")
imgguard = Image.open(r".\awards\Duremudira.png")
imggwan = Image.open(r".\awards\Gwanzorm.png")
imgmama = Image.open(r".\awards\Rajang + Voljang.png")
imgmiru = Image.open(r".\awards\MiRu.png")
imgpari = Image.open(r".\awards\Pariapuria.png")
imgzeru = Image.open(r".\awards\Zerureusu.png")
imgquem = Image.open(r".\awards\Unkown.png")
imgjino = Image.open(r".\awards\Jinouga.png")
imgrajang = Image.open(r".\awards\Rajang.png")
imgnarga = Image.open(r".\awards\Nargacuga.png")
imgdeviljho = Image.open(r".\awards\Deviljho.png")