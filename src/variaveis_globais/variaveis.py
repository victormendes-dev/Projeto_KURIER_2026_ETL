from datetime import datetime

# Caminho do repositório aonde ficará o excel:
var_strCaminhoRepositorio = r'C:\Users\victo\OneDrive\Desktop\Projeto_KURIER_2026_ETL\src\repositorio'

var_dictParametrosAPI = {
                        'marketing': ['leads']
                      , 'crm': [ "clientes", "vendas"]
                    }

# Somente para indicar a data que foi inserido os dados:
var_DateHoje = datetime.now().date().strftime("%d-%m-%Y")

