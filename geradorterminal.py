from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import generetor


conquistas = list()
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
        conquistas.append('andar100')
    if sel == 2:
        conquistas.append('caravan')
    if sel == 3:
        conquistas.append('elzellion')
    if sel == 4:
        conquistas.append('boga')
    if sel == 5:
        conquistas.append('disu')
    if sel == 6:
        conquistas.append('guard')
    if sel == 7:
        conquistas.append('gwan')
    if sel == 8:
        conquistas.append('mama')
    if sel == 9:
        conquistas.append('miru')
    if sel == 10:
        conquistas.append('pari')
    if sel == 11:
        conquistas.append('quem')
    if sel == 12:
        conquistas.append('zeru')
    if sel == 13:
        conquistas.append('jino')
    if sel == 14:
        conquistas.append('rajang')
    if sel == 15:
        conquistas.append('narga')
    if sel == 16:
        conquistas.append('jho')
    if sel == 0:
        break
    elif sel > 16 and sel < 0:
        print("Opção invalida!")
    print(conquistas)

print(conquistas, sel)
generetor.generate_guild_card('Tsugami', 'ARCA', 118, conquistas)