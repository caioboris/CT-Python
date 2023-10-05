from flask import Flask, request, jsonify
import traceback
import carro_oracle as bd
from flask_cors import CORS 

app = Flask(__name__)
CORS(app)

@app.route("/carros", methods=["GET"])
def get_all():
    try:
        dados = bd.recupera_todos()
        retorno = []
        for reg in dados:
            car_dic = {}
            car_dic['id'] = reg[0]
            car_dic['ano'] = reg[1]
            car_dic['montadora'] = reg[2]
            car_dic['modelo'] = reg[3]
            car_dic['placa'] = reg[4]
            retorno.append(car_dic)

        return jsonify(retorno), 200
    
    except Exception as erro:
        traceback.print_exc()
        info = {"msg": "erro na consulta"}
        return info, 406


app.run(debug=True)