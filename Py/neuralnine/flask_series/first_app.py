from flask import Flask,request , make_response

app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>hello world</h1>"

@app.route('/hello', methods=["GET","POST"])
def hello():
    response = make_response()
    
    if request.method == "GET":
        return f"ola mundo -> REQUISICAO GET status {response.status_code} \n"
    
    elif request.method == "POST":
        return f"ola mundo -> REQUISICAO POST {response.status_code} \n"
    
    else:
        return "nao usada"

@app.route('/greet/<name>')
def greet(name):
    return f"ola {name}"

@app.route('/add/<int:n1>/<int:n2>')
def add(n1,n2):
    
    return f"{n1} + {n2} = {n1 + n2}"

@app.route('/handle_url_parms')
def handle_params():
    if "greeting" in request.args.keys() and "name" in request.args.keys():
        saudacao = request.args.get("greeting")
        name = request.args.get("name")
        return f"{saudacao}, {name}"
    else:
        return "sem parametros"
    

if __name__ =="__main__":
    app.run(debug=True,host="0.0.0.0",port=5555)