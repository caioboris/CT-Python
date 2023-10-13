from flask import Flask, request, jsonify
import oracledb
from datetime import datetime

app = Flask(__name__)

conn = oracledb.connect(user="rm552496", password="240103", dsn="oracle.fiap.com.br/orcl")
print("Database version:", conn.version)

@app.route('/livros', methods=['POST'])
def criar_livro():
    dados = request.get_json()
    if 'titulo' not in dados or 'autor' not in dados or 'preco' not in dados or 'data_publicacao' not in dados:
        return jsonify({"erro": "Campos obrigatórios faltando"}), 400
    novo_livro = (
        dados['titulo'],
        dados['autor'],
        float(dados['preco']),  
        datetime.strptime(dados['data_publicacao'], '%Y-%m-%d')  
    )
    try:
        with conn.cursor() as cursor:
            cursor.execute("""
                INSERT INTO Livros (titulo, autor, preco, data_publicacao)
                VALUES (:1, :2, :3, :4)
            """, novo_livro)
            conn.commit()
        return jsonify({"mensagem": "Livro criado com sucesso!"}), 201
    except oracledb.DatabaseError as error:
        return jsonify({"erro": "Erro ao criar o livro", "detalhes": str(error)}), 400

@app.route('/livros/<int:id>', methods=['GET'])
def obter_livro_por_id(id):
    try:
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM Livros WHERE id = :1", (id,))
            livro = cursor.fetchone()
            if livro:
                livro_dict = {
                    "id": livro[0],
                    "titulo": livro[1],
                    "autor": livro[2],
                    "preco": float(livro[3]),
                    "data_publicacao": livro[4].strftime('%Y-%m-%d')
                }
                return jsonify(livro_dict), 200
            else:
                return jsonify({"mensagem": "Livro não encontrado"}), 404
    except oracledb.DatabaseError as error:
        return jsonify({"erro": "Erro ao buscar o livro", "detalhes": str(error)}), 500

@app.route('/livros/por_autor', methods=['GET'])
def obter_livros_por_autor():
    autor = request.args.get('autor')
    if not autor:
        return jsonify({"erro": "Parâmetro 'autor' não fornecido"}), 400

    try:
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM Livros WHERE autor = :1", (autor,))
            livros = cursor.fetchall()
            if livros:
                livros_list = []
                for livro in livros:
                    livro_dict = {
                        "id": livro[0],
                        "titulo": livro[1],
                        "autor": livro[2],
                        "preco": float(livro[3]),
                        "data_publicacao": livro[4].strftime('%Y-%m-%d')
                    }
                    livros_list.append(livro_dict)
                return jsonify(livros_list), 200
            else:
                return jsonify({"mensagem": "Nenhum livro encontrado para o autor especificado"}), 404
    except oracledb.DatabaseError as error:
        return jsonify({"erro": "Erro ao buscar os livros", "detalhes": str(error)}), 500

@app.route('/livros/<int:id>', methods=['DELETE'])
def excluir_livro(id):
    try:
        with conn.cursor() as cursor:
            cursor.execute("DELETE FROM Livros WHERE id = :1",(id))
            conn.commit()
        return jsonify({"mensagem":"Livro excluido com sucesso!"}), 200
    except oracledb.DatabaseError as error:
        return jsonify({"erro": "Erro ao excluir o livro", "detalhes": str(error)}), 500

@app.route('/livros/<int:id>', methods=['PUT'])
def editar_livro(id):
    dados = request.get_json()
    if 'titulo' not in dados or 'autor' not in dados or 'preco' not in dados or 'data_publicacao' not in dados:
        return jsonify({"erro": "Campos obrigatórios faltando"}), 400
    novo_livro = (
        dados['titulo'],
        dados['autor'],
        float(dados['preco']),  
        datetime.strptime(dados['data_publicacao'], '%Y-%m-%d')  
    )
    try:
        with conn.cursor() as cursor:
            cursor.execute("""
                        UPDATE Livros
                        SET titulo = :1,
                        autor = :2,
                        preco = :3,
                        data_publicacao = :4
                        WHERE id = :5""", (novo_livro, id))
            conn.commit()
        return jsonify({"mensagem":"Livro atualizado com sucesso!"}), 200            
    except oracledb.DatabaseError as error:
        return jsonify({"erro": "Erro ao editar o livro", "detalhes": str(error)}), 400        
    
app.run(debug=True)
