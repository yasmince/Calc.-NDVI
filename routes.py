from flask import Flask, request

##from main import insertUsuario

app = Flask(__name__)

@app.route("/olamundo", methods=["GET"])
def olaMundo():
    return {"planta": "Necessita de agua"}

#@app.route("/cadastra/usuario", methods=["POST"])
#def cadastraUsuario():

 #   body = request.get_json()

  #  usuario = insertUsuario(body["nome"], body["email"], body["senha"])

   # return usuario
if __name__ == "__main__":
    app.run(debug=True)

