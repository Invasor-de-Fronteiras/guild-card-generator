from flask import Flask, request, render_template, send_file
from PIL import Image, ImageDraw, ImageFont

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    guildcard = Image.open(r'.\guildcard\base.png')
    imgroad = Image.open(r".\awards\Andar 100.png")  # road
    imgcaravan = Image.open(r".\awards\Max. Caravan.png")  # caravan
    imgelzellion = Image.open(r".\awards\Elzelion.png")  # elzellion
    imgboga = Image.open(r".\awards\Boga.png")  # Boga
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
    provisorio = guildcard.copy()
    if request.method == 'POST':
        if request.form.get('road'):
            provisorio.paste(imgroad, (613, 211))

        return send_file(provisorio, mimetype='image/jpg')
    return render_template('index.html')

app.run()
