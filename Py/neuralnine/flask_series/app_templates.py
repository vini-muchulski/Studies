from flask import Flask,request , make_response, render_template,redirect,url_for

app = Flask(__name__,template_folder="templates")


@app.route("/")
def index():
    my_value = 4
    result = "Vini"
    vini_lista= ["1","3","5"]
    return render_template("index.html", my_value= my_value,result = result, my_list=vini_lista)


@app.route("/other")
def other():
    texto = "filtro to upper"
    return render_template("other.html",texto=texto )

@app.template_filter('reverse_string')
def reverse(s):
    return s[::-1]

@app.route("/redirect_endpoint")
def redirect_endpoint(): 
    return redirect(url_for("other"))

if __name__ =="__main__":
    app.run(debug=True,host="0.0.0.0")