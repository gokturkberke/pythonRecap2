from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def index():
    ad = "Berke"
    soyad = "Korkut"
    return render_template('index.html',name = ad , surname = soyad)
    #return render_template("hakkimizda.html") #miras aldigimiz html dosyasini cagirdik
#python verilerini kullandik
if __name__ == '__main__':
    app.run(debug=True)