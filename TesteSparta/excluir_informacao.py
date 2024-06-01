import sqlite3

try:

    banco = sqlite3.connect('informacoes.db')

    cursor = banco.cursor()
    cursor.execute("DELETE from pessoas WHERE date = #")

    banco.commit()
    banco.close()
    print("os dados foram removidos com sucesso!!")

except sqlite3.Error as erro:
    print("Erro ao remover dados do banco de dados", erro)