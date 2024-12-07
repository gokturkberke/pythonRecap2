from flask import Flask
#sunucumuzu kurmak
app = Flask(__name__) # create an instance of the Flask class

@app.route("/")
def anasayfa():
    return "Sayfama Hosgeldiniz"

@app.route("/Hakkimizda")
def hakkimizda():
    return "Hakkimizda Sayfasi"

@app.route("/Hakkimizda/iletisim")
def iletisim():
    return "Iletisim tel no : 123456789"

if(__name__ == '__main__'):
    app.run(debug=True) # run the app in debug mode
    #surekli ac kapat yapmak yerine sunucuyu guncel tutuyo acik tutuyo
    
    
