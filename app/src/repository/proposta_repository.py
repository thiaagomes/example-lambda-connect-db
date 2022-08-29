

from calendar import c
from unittest import result


class PropostaCriarPayload:
    id_cliente: str
    segment: str
    funcional_officer_operador: str

class AtualizarProposta:
    id_proposta: str
    finalidade: str
    valor_operacao: str
    data_abertura: str
    forma_pagamento: str
    tipo_taxa: str
    iof_financiado: str
    liquido_liberar: str
    nome_completo: str
    produto: str


class BuscarProposta:
    id_proposta: str


class PropostaRepository:
    _conn = []

    def __init__(self, connection: Connection, logger: AppLogger):
        self._conn = connection
        self.logger = logger

    def __execute_query(self, query):

        with self._conn.cursor() as cur:
            cur.execute(query)
            self.logger.info("Comando executado: %s", query)
            result = cur.fetchall()

        self._conn.commit()
        cur.close()

        return result
    
    def gerar_id_proposta(self, proposta_criar_payload: PropostaCriarPayload):
        self.logger.info("gerando id proposta...")
        query = "INSERT INTO proposta"

        result = self.__execute_query(query)

        for proposta in result:
            self.logger.info("Proposta encontrada: [%s] %s", proposta[0], proposta[1])

    def patch_id_proposta(self, atualizar_proposta_payload: AtualizarProposta, id_proposta: str):
        self.logger.info("Gerando id_proposta ...")
        query = "UPDATE"

        self.__execute_query(query)

        return "Proposta Atualizada com Sucesso!"
    
    def buscar_proposta_por_id(self, buscar_proposta_payload: BuscarProposta):
        self.logger.info("Buscando proposta...")
        query = "SELECT"

        self.__execute_query(query)

        return "Busca da Proposta OK!"
