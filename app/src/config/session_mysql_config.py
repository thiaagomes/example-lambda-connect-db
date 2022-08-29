

import traceback
from webbrowser import get


class ConfigSetup:
    _client = []

    def __init__(self, logger: AppLogger):
    self.logger = logger
    self._client = boto3.session.Session().client(
        service_name = 'secretsmanager',
        region_name = 'sa-east-1'
    )

    def __get_secret(self, secret_name):
        try:
            get_secret_value_response = self._client.get_secret_value(
                SecretId=secret_name
            )
        except Exception as e:
            message_error = "Falha no get_secret. Error: "+ str(e)
            self.logger.error(message_error)
            traceback.print_exc()
            raise e
        else:
            secret = get_secret_value_response['SecretString']
            return secret
    
    def rds_connect(self, rds_host, user, passwd, db_name, port):
        try:
            ssl = None
            conn = pymysql.connect(
                rds_host,
                user,
                password=passwd,
                database=db_name,
                port=port,
                ssl=ssl,
                connect_timeout=5,
                autocommit=1,
                client_flag=CLIENT.MULTI_STATEMENTS)

        except pymysql.MySQLError as e:
            self.logger.error(message_error)
            traceback.print_exc()
            raise pymsql.MySQLError(message_error)

        return conn
    
    def get_secrets(self):
        return dict(
            RDSEndpoint=self.__get_secret('credencial-RDSInstanceEndpointSecret',
            RDSInstancePasswordSecret=self.__get_secret('credencial-RDSInstancePasswordSecret'),
            RDSInstanceUserScret=self.__get_secret('credencial-RDSInstanceUserScret')
            )
        )
    
    def connect(self):
        secrets = self.get_secrets()
        db_passwd = secrets.get('RDSInstancePasswordSecret')
        db_user = secrets.get('RDSInstanceUserScret')
        endpoint = secrets.get('RDSEndpoint')

        host_port_db_name = endpoint.split('//')[1]
        db_name = host_port_db_name.split('/')[1]
        host_port = host_port_db_name.split('/')[0]
        db_host = host_port.split(':')[0]
        db_port = int(host_port.split(':')[1])

        return self.rds_connect(db_host, db_user, db_passwd, db_name, db_port)