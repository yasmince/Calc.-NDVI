# -*- coding: UTF-8 -*-
import numpy as np 
import cv2
import cmapy
import json
from flask import Flask
from flask_ngrok import run_with_ngrok

# Inicia a aplicação para que o túnel e a URL sejam gerados
app = Flask(__name__)
run_with_ngrok(app)  

# Função para o cálculo do NDVI
def NDVI(img):

    # Separação dos canais vermelhos para a realização do cálculo NDVI
    img_c = cv2.applyColorMap(img, cmapy.cmap('Reds')).astype(np.int)
    _, R, NIR = cv2.split(img_c)

    # Fórmua do cálculo NDVI
    ndvi = (NIR-R)/(NIR+R+0.01)

    # Amazenamento do maior resultado obtido
    max = ndvi.max()

    # Retorno do resultado do cálculo
    return max;

@app.route("/")

# Função para captura de imagens e API de comunicação com a assistente virtual
def home():

    # Inicia a câmera e faz a captura de imagem
    camera = cv2.VideoCapture(0)
    retval, img = camera.read()
    
    # Armazena a imagem em uma váriavel para que seja feito cálculo
    ndvi_image = NDVI(img)

    # Faz um comparativo do resultado obtido para saber qual mensagem a assistente virtual irá emitir
    if ndvi_image >= 0.90:
        json_return = json.loads(f"{{\"valor_max\":\"{('não necessita de irrigação')}\"}}")
    
    elif ndvi_image >= 0.80 and ndvi_image <= 0.89:
        json_return = json.loads(f"{{\"valor_max\":\"{('necessita de irrigação')}\"}}")

    else:
        json_return = json.loads(f"{{\"valor_max\":\"{('está com os níveis de clorofila abaixo do normal considerado para uma planta viva')}\"}}")

    # Retorna a mensagem que a assistente irá transmitir ao usuário
    return json_return;

# Mantém a aplicação rodando até que a compilação seja finalizada pelo usuário
app.run()