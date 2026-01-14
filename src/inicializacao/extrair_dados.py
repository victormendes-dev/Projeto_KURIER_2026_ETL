# Imports da função:
import json
import requests
from loguru                      import logger

# Retornando valor pela area com o arquivo relacionado:
from variaveis_globais.variaveis import var_dictParametrosAPI


def retornarDados() -> dict : 
    """

    objetivo: retornar informações através da API de dados fornecidos pela Kurier.

    """
    var_dictJsonDados = {}

    for area, arquivo in var_dictParametrosAPI.items():
        try:
            if area == 'marketing':
                for arquivo in arquivo:
                 var_dictJsonDados["Leads"] = retornaJson(area, arquivo)
                 

            if area == 'crm':
                for nomeArquivo in arquivo:
                    if nomeArquivo == 'clientes':
                        var_dictJsonDados["Clientes"] = retornaJson(area, nomeArquivo)
                        
                    if nomeArquivo == 'vendas':
                      var_dictJsonDados["Vendas"] = retornaJson(area, nomeArquivo)

        except requests.exceptions.RequestException as e:
            logger.error(f"Erro ao retornar dados via API. Status de retorno: {e}")
    logger.info("Dados via API foram retornados com sucesso")

    return var_dictJsonDados

def retornaJson(area: str , arquivo : str):
    var_jsonRequest = requests.get(f"http://127.0.0.1:8000/v1/{area}/{arquivo}")
    if var_jsonRequest.status_code == 200:
        var_jsonDados = var_jsonRequest.json()
    return var_jsonDados