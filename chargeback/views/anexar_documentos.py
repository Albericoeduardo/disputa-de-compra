from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response


class AnexarDocumentosView(APIView):
    def post(self, request):
        return Response({"msg": "Funcionalidade de anexar documentos ainda não implementada"}, status=status.HTTP_501_NOT_IMPLEMENTED)