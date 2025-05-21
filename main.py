from flask import Flask, render_template, request, redirect, url_for, jsonify
from db import connection
from models import *

app = Flask(__name__)
create_table()


@app.route('/cadastrar', methods=['POST'])
def cadastrar_produtos():
    dados = request.get_json()

    motor = dados.get('motor')
    lado = dados.get('lado')
    quantidade = dados.get('quantidade')
    status = dados.get('status')

    try:
        insert_items((motor,lado,quantidade,status))
        return jsonify({'status':'sucesso'})
    except Exception as e:
        return jsonify({'status':'erro', 'mensagem': str(e)}), 500
    
@app.route('/fila', methods=['GET'])
def fila_montagem():


    try:
        items = get_items()
        return jsonify(items)
    except Exception as e:
        return jsonify({'status':'erro', 'mensagem': str(e)}), 500


    




if __name__ == '__main__':
    app.run(debug=True)