import oracledb
import traceback

def recupera_por_id(id: int):
    pass

def apaga_por_id(id: int):
    pass

def inclui(carro: dict):
    pass

def atualiza(carro: dict):
    pass

def recupera_todos():
    sql = "select id, ano, montadora, modelo, placa from carro"
    try:
        with oracledb.connect(
            user="pf0313", password='professor#23',
            dsn="oracle.fiap.com.br/orcl"                     
        ) as conexao:

            with conexao.cursor() as cur:
                cur.execute(sql)
                dados = cur.fetchall()
                return dados
            
    except Exception as erro:
        #print(erro)
        traceback.print_exc()
        raise erro

if __name__ == '__main__':
    registros = recupera_todos()
    for reg in registros:
        print(reg)
