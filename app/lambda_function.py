import traceback


logger = AppLogger().create_logger(__name__)

class FunctionsMock:
    def gerar_id_proposta(self):
        return "proposta"

def obterRepository():
    if os.environ.get('ENVIORNMENT', None) in ["hom", "prod"]:
        CONN = configSetup(logger).connect()
        return PropostaRepository(CONN, logger)
    return PropostaRepositoryMock()


def lambda_post_id_proposta(event, context):
    try:
        logger.info(event)
        proposta_repository = obterRepository()
        body = json.loads(event['body'])
        proposta_gerada = proposta_repository.gerar_id_proposta(body)
        logger.info(proposta_gerada)
        return proposta_gerada
        
    except Exception as e:
        message_error = "lambda_handler Error: %s" + str(e)
        logger.error(message_error)
        traceback.print_exc()
        raise Exception(message_error)

def lambda_patch_proposta(event, context):
    try:
        logger.info(event)
        proposta_repository = obterRepository()
        body: AtualizarProposta = json.loads(event['body'])
        id_proposta = event['pathParameters']['id_proposta']
        proposta_atualizada = proposta_repository.patch_id_proposta(body, id_proposta)
        logger.info(proposta_atualizada)
        return {'statusCode': 200, 'body': "Atualizacao da Proposta"}

    except Exception as e:
        message_error = "lambda_handler Error: %s" + str(e)
        logger.error(message_error)
        traceback.print_exc()
        raise Exception(message_error)