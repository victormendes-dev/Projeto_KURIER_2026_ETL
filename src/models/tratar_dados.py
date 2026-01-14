import pandas as pd
from datetime import date
from loguru import logger
from models.models import Models

class Tratamento:
    def __init__(self,var_dfDadosETL: pd.DataFrame, nomeArquivo):
            self.var_dfDadosETL = var_dfDadosETL
            self.nomeArquivo    = nomeArquivo
                
    def tratamento_de_dados(self):
            """
            Trata todos os dados retornados via API
            return: Retorna uma lista com os dados tratados prontos para serem inseridos em banco

            """
            var_objModels = Models()
            var_ListDadosTratados = [colunas for _, colunas in self.var_dfDadosETL.iterrows()]
            var_dbtabelaInsert = []
            for itens in var_ListDadosTratados:
                # Padronização de dados da tabela relacionada aos Leads:
                if self.nomeArquivo == "Leads":
                    tabela_insert_values = var_objModels.LEADS(itens[0], itens[1], itens[2], itens[3], itens[4], itens[5], itens[6]
                                                            , itens[7], itens[8], itens[9])
                    var_dbtabelaInsert.append(tabela_insert_values.to_tuple())
                # Padronização de dados da tabela relacionada aos Clientes:
                elif self.nomeArquivo == "Clientes":
                    tabela_insert_values = var_objModels.CLIENTES(itens[0], itens[1], itens[2], itens[3], itens[4], itens[5], itens[6]
                                                            , itens[7], itens[8], itens[9])
                    var_dbtabelaInsert.append(tabela_insert_values.to_tuple())
                # Padronização de dados da tabela relacionada as Vendsa:
                elif self.nomeArquivo == "Vendas":
                    tabela_insert_values = var_objModels.VENDAS(itens[0], itens[1], itens[2], itens[3], itens[4], itens[5], itens[6]
                                                            , itens[7], itens[8])
                    var_dbtabelaInsert.append(tabela_insert_values.to_tuple())
                
            logger.info(f"Irão ser inseridas: {len(var_ListDadosTratados)} linhas em banco!")   
                
            return var_dbtabelaInsert
         
        