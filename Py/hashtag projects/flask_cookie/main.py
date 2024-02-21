from flask import Flask, request, make_response

app = Flask(__name__)

@app.route("/")
def homepage():
    return "Meu site está no ar"

@app.route("/criar-cookie")
def criar_cookie():
    resposta = make_response("Cookie criado")
    resposta.set_cookie("user", "vini")
    return resposta

@app.route("/ver-cookie")
def ver_cookie():
    cookies = request.cookies
    #nome_user = cookies["user"]
    return cookies

if __name__ =="__main__":
    app.run(debug=True)