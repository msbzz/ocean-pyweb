from flask import Flask, render_template, request, redirect, url_for, session,flash,g

app = Flask(__name__)

# KEY
SECRET_KEY = 'max'
app.config.from_object(__name__)
# POST MOCK

posts = [

    {
        "titulo": "Post 1",
        "texto": "Meu primerio post"
    },

    {

        "titulo": "Post 2",
        "texto": "Meu segubndo post",
    },

    {

        "titulo": "Post 3",
        "texto": "Meu terceiro post",
    }


]

# USER MOCKS

USERNAME = "admin"
PASSWORD = "12345"


@app.route("/", methods=["GET", "POST"])
def main():
    return render_template("exibir_entradas.html", entradas=posts)


@app.route("/quaqua", methods=["GET", "POST"])
def login():
    erro = ""
    if request.method == "POST":
        if request.form['username'] == USERNAME and request.form['password'] == PASSWORD:
            session['logado'] = True
            return redirect(url_for('main'))

        erro = "usuario ou senha invalidos"
    return render_template("login.html", erro=erro)


@app.route("/inserir",methods=["POST"])
def inserir_entrada():
    
    novo_post = {
        
        "titulo": request.form['titulo'],
        "texto": request.form['texto'],
         
    }
 
    posts.append(novo_post)
    #return posts
    return redirect(url_for('main'))


@app.route("/logout")
def logout():
    session.pop('logado', None)
    flash('Logout feito')
    return redirect(url_for('main'))
