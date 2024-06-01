import sqlite3
import csv

def ler_csv(cad_cia_aberta):
    dados = []
    with open(cad_cia_aberta, mode='r', newline='') as arquivo_csv:
        leitor_csv = csv.DictReader(arquivo_csv, delimiter=';')
        for linha in leitor_csv:
            dados_linha = [linha[coluna] for coluna in linha]
            dados.append(dados_linha)
    return dados

def criar_banco():
    banco = sqlite3.connect('informacoes.db')
    cursor = banco.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS informacoes (
        CNPJ_CIA VARCHAR(20) NOT NULL,
        DENOM_SOCIAL VARCHAR(100) NOT NULL,
        SIT VARCHAR(40) NOT NULL,
        DT_INI_SIT DATE NOT NULL
    )
    ''')

    banco.commit()
    banco.close()

def inserir_informacoes(cnpj_cia, denom_social, sit, dt_ini_sit):
    try:
        banco = sqlite3.connect('informacoes.db')
        cursor = banco.cursor()
        
        cursor.execute('''
        INSERT INTO informacoes (CNPJ_CIA, DENOM_SOCIAL, SIT, DT_INI_SIT)
        VALUES (?, ?, ?, ?)
        ''', (cnpj_cia, denom_social, sit, dt_ini_sit))
        
        banco.commit()
    except sqlite3.Error as e:
        print(f"Erro ao inserir dados: {e}")
    finally:
        if banco:
            banco.close()

def consulta_informacoes(dt_ini_sit):
    rows = []
    try:
        banco = sqlite3.connect('informacoes.db')
        cursor = banco.cursor()
        
        cursor.execute('''
        SELECT CNPJ_CIA, DENOM_SOCIAL, SIT
        FROM informacoes
        WHERE DT_INI_SIT = ?
        ''', (dt_ini_sit,))
        
        rows = cursor.fetchall()
    except sqlite3.Error as e:
        print(f"Erro ao consultar dados: {e}")
    finally:
        if banco:
            banco.close()
    return rows

def inserir_csv(cad_cia_aberta):
    dados = ler_csv(cad_cia_aberta)
    for linha in dados:
        inserir_informacoes(linha[0], linha[1], linha[7], linha[8])

criar_banco()

cad_cia_aberta = './cad_cia_aberta.csv'
inserir_csv(cad_cia_aberta)

print(consulta_informacoes ('#'))