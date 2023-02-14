from flask import Flask,render_template

app = Flask(__name__)

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


@app.route("/")
def helloPovu():
    return render_template("exibir_entradas.html",entradas=posts)
