from flask import Flask, render_template

app = Flask(__name__)

class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria = categoria
        self.console = console

@app.route("/home")
def hello():
    bloodbourne = Jogo("Bloodbourne", "RPG", "PS4")
    gears_of_war = Jogo("Gears of War", "Third-Person Shooter", "Xbox 360")
    god_of_war = Jogo("God of War", "Action", "Playstation 4")
    the_last_of_us = Jogo("The Last of Us", "Survival", "Playstation 4")
    pokemon = Jogo("Pokemon Gold", "RPG", "Gameboy")

    lista = [bloodbourne, gears_of_war, god_of_war, the_last_of_us, pokemon]
    return render_template("/home/lista.html", jogos=lista, titulo="Playstation Network")

@app.route("/cadastro")
def cadastro():
    return render_template("/cadastro/cadastro.html")

    
app.run()