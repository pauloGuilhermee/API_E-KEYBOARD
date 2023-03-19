from flask import Flask, jsonify, request

app = Flask(__name__)

# Dicionário de emoções e seus respectivos unicodes

emojis_por_sentimmento = {
    'raiva': ['\U0001F620', '\U0001F621', '\U0001F612', '\U0001F624', '\U0001F4A9', '\U0001F975'],
    'nojo': ['\U0001F92E', '\U0001F92F', '\U0001F974', '\U0001F635', '\U0001F616', '\U0001F922'],
    'medo': ['\U0001F632', '\U0001F628', '\U0001F626', '\U0001F631', '\U0001F630', '\U0001F628'],
    'alegria': ['\U0001F601', '\U0001F604', '\U0001F606', '\U0001F917', '\U0001F600', '\U0001F602'],
    'neutro': ['\U0001F636', '\U0001F611', '\U0001F610', '\U0001F914', '\U0001F642', '\U0001F643'],
    'triste': ['\U0001F62B', '\U0001F613', '\U0001F614', '\U0001F629', '\U0001F622', '\U0001F62D'],
    'surpreso': ['\U0001F626', '\U0001F627', '\U0001F631', '\U0001F633', '\U0001F62C', '\U0001F92F']
}

@app.route("/")
def hello():
    return "Bem-vindeee a nossa aplicação flask"

@app.route('/receber_dados', methods=['POST'])
def receber_dados():
    dados = request.get_json()
    texto = dados['texto']

    #data = dados['data']
    #hora = dados['hora']
    #dia_da_semana = dados['dia_da_semana']

    sucesso = {'mensagem': 'Dados recebidos com sucesso!'}

    #Chamando a rede neural e armazenando resultado na variável 'emocao'
    emocao = chamar_aqui_rede_neural(texto) # Retornar uma das emoções do dicionário 🙏

    #Selecionando os emojis correnspondentes a emoção identificada
    emojis = emojis_por_sentimmento[emocao]

    #Transformando unicodes em strings
    emojis_em_string = [emoji.encode('unicode_escape').decode() for emoji in emojis]

    # Envia os emojis devolta para o APP
    resposta = {'emojis': emojis_em_string}
    return jsonify(resposta)

if __name__ == "__main__":
    app.run()