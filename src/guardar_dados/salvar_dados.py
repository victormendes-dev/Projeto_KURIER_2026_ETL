import pandas as pd
import os
import json
import ast

from variaveis_globais.variaveis  import var_strCaminhoRepositorio, var_DateHoje


class Salvar_Dados:
    def __init__(self, json: json, nomeArquivo: str):
        self.json = json
        self.nomeArquivo = nomeArquivo

    def dados_Excel(self) -> pd.DataFrame:
        """
        salva os dados brutos em um arquivo excel para inserção, além de servir para auditoria dos dados.
        return: Dataframe contendo todos os dados da API não tratados
    
        """
        # Nome do arquivo de histórico:
        var_strNomeDt = f"{self.nomeArquivo}_Dados_ETL_{var_DateHoje}.xlsx"

        # Transforma o Json em um DataFrame:
        var_DfDadosKurier = pd.DataFrame(self.json)

        # Trata o dataframe:
        var_DfDadosKurierTratado: pd.DataFrame = self.normalizar_colunas_dict(var_DfDadosKurier)

        # Adiciona o caminho do repositorio para salvar os dados para a inserção:
        var_objCaminhoExcel = os.path.join(var_strCaminhoRepositorio, var_strNomeDt)

        # Transforma em excel e salva o excel dentro da pasta:
        var_DfDadosKurierTratado.to_excel(var_objCaminhoExcel, index=False)

        # Lendo o arquivo preparado para inserção dos dados:
        var_dictDadosInsert = pd.read_excel(f'{var_strCaminhoRepositorio}/{var_strNomeDt}')

        return var_dictDadosInsert
    
    def normalizar_colunas_dict(self, var_DfDadosKurier: pd.DataFrame) -> pd.DataFrame:
        """
        Detecta colunas que contêm dicionários (ou strings de dicionários),
        expande essas colunas em novas colunas e remove as colunas originais.
        """

        var_DfDadosKurier = var_DfDadosKurier.copy()

        for coluna in var_DfDadosKurier.columns:

            serie = var_DfDadosKurier[coluna].dropna()
            if serie.empty:
                continue

            valor = serie.iloc[0]

            # verifica se é dict ou string de dict
            try:
                eh_dict = isinstance(valor, dict) or isinstance(ast.literal_eval(valor), dict)
            except Exception:
                eh_dict = False

            if not eh_dict:
                continue

            # expande para colunas
            var_DfDadosKurier_expandido = var_DfDadosKurier[coluna].apply(pd.Series)

            # prefixa nomes
            var_DfDadosKurier_expandido.columns = [f"{coluna}_{c}" for c in var_DfDadosKurier_expandido.columns]

            # concatena e remove coluna original
            var_DfDadosKurier = pd.concat(
                [var_DfDadosKurier.drop(columns=[coluna]), var_DfDadosKurier_expandido],
                axis=1
            )

        return var_DfDadosKurier
