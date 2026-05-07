from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from chargeback.aplication.casos_de_uso.anexar_documento_caso_de_uso import AnexarDocumentoCasoDeUso
from chargeback.aplication.serializers.anexo_serializer import AnexoContestacaoSerializer
from chargeback.infra.repositorios.contestacoes_repo_impl import ContestacaoRepo


def _ok(data, http_status=status.HTTP_200_OK):
    return Response({"success": True, "data": data}, status=http_status)


def _erro(code: str, message: str, http_status: int):
    return Response(
        {
            "success": False,
            "error": {
                "code": code,
                "message": message,
            },
        },
        status=http_status,
    )


class AnexarDocumentosView(APIView):
    def post(self, request, contestacao_id: int):
        serializer = AnexoContestacaoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        caso_de_uso = AnexarDocumentoCasoDeUso(repo_contestacao=ContestacaoRepo())
        resultado = caso_de_uso.executar(
            contestacao_id=contestacao_id,
            tipo=serializer.validated_data["tipo"],
            nome_arquivo=serializer.validated_data["nome_arquivo"],
            url=serializer.validated_data["url"],
            observacao=serializer.validated_data.get("observacao"),
        )

        if not resultado["ok"]:
            http_status = status.HTTP_409_CONFLICT
            if resultado["code"] == "NAO_ENCONTRADO":
                http_status = status.HTTP_404_NOT_FOUND
            return _erro(code=resultado["code"], message=resultado["msg"], http_status=http_status)

        return _ok(resultado["anexo"], status.HTTP_201_CREATED)

    def get(self, request, contestacao_id: int):
        repo = ContestacaoRepo()
        contestacao = repo.buscar_por_id(contestacao_id)
        if not contestacao:
            return _erro(
                code="NAO_ENCONTRADO",
                message="Contestacao nao encontrada",
                http_status=status.HTTP_404_NOT_FOUND,
            )

        anexos = repo.listar_anexos(contestacao_id=contestacao_id)
        return _ok(anexos)
