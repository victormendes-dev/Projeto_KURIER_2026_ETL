import psycopg2
from configparser import ConfigParser

class Connect_PgAdmin:
    @classmethod
    def __init__(self):
        # Carregar o arquivo de configuração dentro do método init
        self.config = ConfigParser()
        self.config.read(r'src\database\conn_POSTGRES\config.ini')

        # Recuperar as credenciais a partir do arquivo .ini
        self.user = self.config.get('POSTGRES', 'username')
        self.password = self.config.get('POSTGRES', 'password')

    def connect_postgres(self, dbname: str):
        try:
            # Estabelecendo a conexão com o banco de dados
            connection = psycopg2.connect(
                user=self.user,
                password=self.password,
                dbname=dbname
            )
            return connection  # Retorne a conexão para uso posterior
        except Exception as error:
            print(f"Erro ao conectar ao PostgreSQL: {psycopg2.DatabaseError}")
      
    def reconnect_postgres(self):
        connection = self.connect_postgres()
        return connection



