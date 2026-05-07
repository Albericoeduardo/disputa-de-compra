from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from chargeback.aplication.casos_de_uso.abrir_contestacao_caso_de_uso import AbrirContestacaoCasoDeUso
from chargeback.aplication.casos_de_uso.atualizar_status_contestacao_caso_de_uso import AtualizarStatusContestacaoCasoDeUso
from chargeback.aplication.casos_de_uso.buscar_contestacao_caso_de_uso import BuscarContestacaoCasoDeUso
from chargeback.aplication.casos_de_uso.listar_contestacoes_caso_de_uso import ListarContestacoesCasoDeUso
from chargeback.aplication.serializers.contestacao_serializer import (
    AtualizarStatusContestacaoSerializer,
    ContestacaoOutputSerializer,
    ContestacaoViewSerializer,
    FiltroContestacaoSerializer,
)
from chargeback.domain.services.contestacao_service import ContestacaoService
from chargeback.domain.services.prazo_service import PrazoService
from chargeback.infra.repositorios.clientes_repo_impl import ClienteRepo
from chargeback.infra.repositorios.contestacoes_repo_impl import ContestacaoRepo
from chargeback.infra.repositorios.prazo_repo_impl import PrazoRepo


class ContestacaoCollectionView(APIView):
    def post(self, request):
        serializer = ContestacaoViewSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        contestacao_repo = ContestacaoRepo()
        prazo_service = PrazoService(prazo_repo=PrazoRepo())
        caso_de_uso = AbrirContestacaoCasoDeUso(
            repo_contestacao=contestacao_repo,
            repo_cliente=ClienteRepo(),
            unicidade_service=ContestacaoService(contestacao_repo),
            prazo_service=prazo_service,
        )

        resultado = caso_de_uso.executar(serializer.validated_data)
        if not resultado["ok"]:
            return Response(
                {
                    "success": False,
                    "error": {
                        "code": resultado["code"],
                        "message": resultado["msg"],
                    },
                },
                status=status.HTTP_409_CONFLICT,
            )

        payload = ContestacaoOutputSerializer(resultado["contestacao"]).data
        return Response({"success": True, "data": payload}, status=status.HTTP_201_CREATED)

    def get(self, request):
        serializer = FiltroContestacaoSerializer(data=request.query_params)
        serializer.is_valid(raise_exception=True)

        caso_de_uso = ListarContestacoesCasoDeUso(ContestacaoRepo())
        resultado = caso_de_uso.executar(**serializer.validated_data)
        data = ContestacaoOutputSerializer(resultado["contestacoes"], many=True).data
        return Response({"success": True, "data": data}, status=status.HTTP_200_OK)


class ContestacaoDetailView(APIView):
    def get(self, request, contestacao_id: int):
        caso_de_uso = BuscarContestacaoCasoDeUso(ContestacaoRepo())
        resultado = caso_de_uso.executar(contestacao_id)

        if not resultado["ok"]:
            return Response(
                {
                    "success": False,
                    "error": {
                        "code": resultado["code"],
                        "message": resultado["msg"],
                    },
                },
                status=status.HTTP_404_NOT_FOUND,
            )

        payload = ContestacaoOutputSerializer(resultado["contestacao"]).data
        return Response({"success": True, "data": payload}, status=status.HTTP_200_OK)

    def patch(self, request, contestacao_id: int):
        serializer = AtualizarStatusContestacaoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        contestacao_repo = ContestacaoRepo()
        caso_de_uso = AtualizarStatusContestacaoCasoDeUso(
            repo_contestacao=contestacao_repo,
            prazo_service=PrazoService(prazo_repo=PrazoRepo()),
        )

        resultado = caso_de_uso.executar(
            contestacao_id=contestacao_id,
            novo_status=serializer.validated_data["status"],
            observacao=serializer.validated_data.get("observacao"),
        )

        if not resultado["ok"]:
            status_code = status.HTTP_409_CONFLICT
            if resultado["code"] == "NAO_ENCONTRADO":
                status_code = status.HTTP_404_NOT_FOUND
            return Response(
                {
                    "success": False,
                    "error": {
                        "code": resultado["code"],
                        "message": resultado["msg"],
                    },
                },
                status=status_code,
            )

        payload = ContestacaoOutputSerializer(resultado["contestacao"]).data
        return Response({"success": True, "data": payload}, status=status.HTTP_200_OK)
