

from app.src.repository.proposta_repository import AtualizarProposta, PropostaCriarPayload


class PropostaRepositoryMock:
    def gerar_id_proposta(self, proposta_criar_payload: PropostaCriarPayload):
        return{
            "id_proposta": str(uuid.uuid4()),
            "id_cliente": proposta_criar_payload['id_cliente'],
            "segmento": proposta_criar_payload['segmento'],
            "funcional_officer_operador": proposta_criar_payload['funcional_officer_operador']
        }

    def patch_id_proposta(self, atualizar_proposta_payload: AtualizarProposta, id_proposta: str):
        return{
            "id_proposta": atualizar_proposta_payload['id_proposta']
        }
    
    def listar_propostas(self, buscarProposta: BuscarProposta):
        return "xpto"