from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont



def select():
    guildcard = Image.open(r'.\guildcard\base.png')
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
    awards = []
    provisorio = guildcard.copy()
    user = input('Entre com o Usuario :')
    guild = input('Entre com a Guild :')
    record = input('Recorde de Andares : ')
    myFont = ImageFont.truetype(r'.\fonts\monsterhunter.ttf', 50)
    FontUSER = ImageFont.truetype(r'.\fonts\monsterhunter.ttf', 72)
    print("Selecione uma conquista ou 0 pra sair\n"
                    "Andar 100 da ROAD[1]\n"
                    "MAX UP Esfera Caravan[2]\n"
                    "Elzellion[3]\n"
                    "Boga[4]\n"
                    "Disufiora[5]\n"
                    "Guardião[6]\n"
                    "Gwanzorm[7]\n"
                    "Rajang + Voljang[8]\n"
                    "Miru[9]\n"
                    "Extreme Pariapuria[10]\n"
                    "Quem ?[11]\n"
                    "Zerureuso[12]\n"
                    "Jinouga[13]\n"
                    "2Rajang[14]\n"
                    "Narga[15]\n"
                    "Deviljho[16]\n")
    while True:
        sel = int(input("Escolha uma Award: "))
        if sel == 1:
            provisorio.paste(imgroad, (613, 211))
            print("Award Adicionado")
        if sel == 2:
            provisorio.paste(imgcaravan, (931, 211))
            print("Award Adicionado")
        if sel == 3:
            provisorio.paste(imgelzellion, (1250, 211))
            print("Award Adicionado")
        if sel == 4:
            provisorio.paste(imgboga, (1568, 211))
            print("Award Adicionado")
        if sel == 5:
            provisorio.paste(imgdisufiora, (613, 442))
            print("Award Adicionado")
        if sel == 6:
            provisorio.paste(imgguard, (931, 442))
            print("Award Adicionado")
        if sel == 7:
            provisorio.paste(imggwan, (1250, 442))
            print("Award Adicionado")
        if sel == 8:
            provisorio.paste(imgmama, (1568, 442))
            print("Award Adicionado")
        if sel == 9:
            provisorio.paste(imgmiru, (613, 673))
            print("Award Adicionado")
        if sel == 10:
            provisorio.paste(imgpari, (931, 673))
            print("Award Adicionado")
        if sel == 11:
            provisorio.paste(imgquem, (1250, 673))
            print("Award Adicionado")
        if sel == 12:
            provisorio.paste(imgzeru, (1568, 673))
            print("Award Adicionado")
        if sel == 13:
            provisorio.paste(imgjino, (613, 906))
            print("Award Adicionado")
        if sel == 14:
            provisorio.paste(imgrajang, (931, 906))
            print("Award Adicionado")
        if sel == 15:
            provisorio.paste(imgnarga, (1250, 906))
            print("Award Adicionado")
        if sel == 16:
            provisorio.paste(imgdeviljho, (1568, 906))
            print("Award Adicionado")
        if sel == 0:
            provisorio.save(fr".\gcdownload\{user}.png")
            infos = ImageDraw.Draw(provisorio)
            infos.text((205, 885), f'{guild}', font=myFont, fill=(0, 0, 0))
            infos.text((450, 940), f'{record}', font=myFont, fill=(0, 0, 0))
            infos.text((105, 200), f'{user}', font=FontUSER, fill=(0, 0, 0))
            provisorio.save(fr".\gcdownload\{user}.png")


            break
        elif sel>16 and sel<0:
            print("Opção invalida!")



    return provisorio

gc = select()