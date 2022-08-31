from PIL import ImageDraw
from PIL import Image
from PIL import ImageFont



def generate_guild_card(user, guild, record, conquistas):
    template = guildcard.copy()

    for i in conquistas:
        if i == 'andar100':
            template.paste(imgroad, (613, 211))
            print("Award Adicionado")
        if i == 'caravan':
            template.paste(imgcaravan, (931, 211))
            print("Award Adicionado")
        if i == 'elzellion':
            template.paste(imgelzellion, (1250, 211))
            print("Award Adicionado")
        if i == 'boga':
            template.paste(imgboga, (1568, 211))
            print("Award Adicionado")
        if i == 'disu':
            template.paste(imgdisufiora, (613, 442))
            print("Award Adicionado")
        if i == 'guard':
            template.paste(imgguard, (931, 442))
            print("Award Adicionado")
        if i == 'gwan':
            template.paste(imggwan, (1250, 442))
            print("Award Adicionado")
        if i == 'mama':
            template.paste(imgmama, (1568, 442))
            print("Award Adicionado")
        if i == 'miru':
            template.paste(imgmiru, (613, 673))
            print("Award Adicionado")
        if i == 'pari':
            template.paste(imgpari, (931, 673))
            print("Award Adicionado")
        if i == 'quem':
            template.paste(imgquem, (1250, 673))
            print("Award Adicionado")
        if i == 'zeru':
            template.paste(imgzeru, (1568, 673))
            print("Award Adicionado")
        if i == 'jino':
            template.paste(imgjino, (613, 906))
            print("Award Adicionado")
        if i == 'rajang':
            template.paste(imgrajang, (931, 906))
            print("Award Adicionado")
        if i == 'narga':
            template.paste(imgnarga, (1250, 906))
            print("Award Adicionado")
        if i == 'jho':
            template.paste(imgdeviljho, (1568, 906))
            print("Award Adicionado")

    infos = ImageDraw.Draw(template)
    infos.text((205, 885), f'{guild}', font=myFont, fill=(0, 0, 0))
    infos.text((450, 940), f'{record}', font=myFont, fill=(0, 0, 0))
    infos.text((105, 200), f'{user}', font=FontUSER, fill=(0, 0, 0))
    template.save(fr".\guildcard\{user}.png")




guildcard = Image.open(r'.\guildcard\base.png')
myFont = ImageFont.truetype(r'.\fonts\monsterhunter.ttf', 50)
FontUSER = ImageFont.truetype(r'.\fonts\monsterhunter.ttf', 72)
imgroad = Image.open(r".\awards\Andar 100.png")#road
imgcaravan = Image.open(r".\awards\Max. Caravan.png")  # caravan
imgelzellion = Image.open(r".\awards\Elzelion.png")  # elzellion
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
imgdeviljho = Image.open(r".\awards\Deviljho.png")  # deviljho

#generate_guild_card('tsugami', 'ARCA', 122, ['andar100', 'jho', 'narga'])

#    guildcard = Image.open(r'.\guildcard\base.png')


