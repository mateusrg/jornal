from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/noticias")
def noticias():
    return render_template("noticias.html")

@app.route("/reportagens")
def reportagens():
    return render_template("reportagens.html")

@app.route("/classificados")
def classificados():
    return render_template("classificados.html")

@app.route("/poema")
def poema():
    return render_template("poema.html")

@app.route("/arte")
def arte():
    return render_template("arte.html")

@app.route("/coluna-de-opiniao")
def coluna_de_opiniao():
    return render_template("coluna-de-opiniao.html")

@app.route("/carta_dos_leitores")
def carta_dos_leitores():
    return render_template("carta_dos_leitores.html")



@app.route("/noticia-mateus")
def noticia_mateus():
    return render_template("noticia-mateus.html")

@app.route("/noticia-isabelle")
def noticia_isabelle():
    return render_template("noticia-isabelle.html")

@app.route("/noticia-pedro")
def noticia_pedro():
    return render_template("noticia-pedro.html")

@app.route("/noticia-nicolas")
def noticia_nicolas():
    return render_template("noticia-nicolas.html")

@app.route("/reportagem-saude-mental")
def reportagem_saude_mental():
    return render_template("reportagem-saude-mental.html")

@app.route("/reportagem-aleph-farms")
def reportagem_aleph_farms():
    return render_template("reportagem-aleph-farms.html")



if __name__ == "__main__":
    app.run(debug=True)
