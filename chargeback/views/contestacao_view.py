from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

from chargeback.chargeback.aplication.contestacao_serializer import (
    ContestacaoViewSerializer,
)
from chargeback.chargeback.domain.casos_de_uso.contestacao_caso_de_uso import (
    AbrirContestacaoCasoDeUso,
)
from chargeback.chargeback.infra.models.contestacao import Contestacao


class CriarContestacaoView(APIView):
    def post(self, request):
        try:
            data = ContestacaoViewSerializer(data=request.data)
            data.is_valid(raise_exception=True)

            contestacao = AbrirContestacaoCasoDeUso.executar(data.validated_data)
            if isinstance(contestacao, Contestacao):
                return Response(
                    {
                        "message": "Contestação recebida com sucesso!",
                        "status": contestacao.status,
                    },
                    status=status.HTTP_201_CREATED,
                )

            return Response(
                {"message": f"{contestacao['msg']}"},
                status=status.HTTP_409_CONFLICT,
            )
        except Exception:
            return Response(
                {"error": "Error ao receber contestação"},
                status=status.HTTP_400_BAD_REQUEST,
            )
