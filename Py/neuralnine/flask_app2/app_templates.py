from flask import Flask, render_template,request

app = Flask(__name__,template_folder="templates")


@app.route(rule="/", methods=["GET", "POST"] )
def index():
    if request.method  == "GET":
        return render_template("index.html")
    
    elif request.method  == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        
        if username == "vini" and password == "password":
            return "Sucesso"
        
        else:
            return f"Failure {username} {password}"
        
    


if __name__ =="__main__":
    app.run(debug=True,host="0.0.0.0")