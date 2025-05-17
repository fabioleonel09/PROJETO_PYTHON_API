# Conexão com o banco de dados
import mysql.connector
def conectar_banco():
    return mysql.connector.connect(
        host="127.0.0.1:3306",
        user="root",
        password="adm1030#$",
        database="ProdutosLoja"
    )