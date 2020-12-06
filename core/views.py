from django.core.exceptions import ValidationError
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Sonda

from .serializers import SondaSerializer


class ReturnToInicialCoordinatesView(APIView):
    """ Reset probe´s coordinate to x=0, y=0 and face='D' """

    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def put(self, request, *args, **kwargs):
        sonda = Sonda.objects.first()

        sonda.return_to_inicial_coordinates()
        sonda.save()

        return Response(status=200)


class MoveView(APIView):
    """ Move probe based in a list of moviments passed by json """

    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def patch(self, request, pk=None, format=None):
        sonda = Sonda.objects.first()
        movements = dict(request.data)

        try:
            for movement in movements['movimentos']:
                if movement.upper() == 'GE':
                    sonda.rotate('left')
                elif movement.upper() == 'GD':
                    sonda.rotate('right')
                elif movement.upper() == 'M':
                    sonda.move()

                sonda.clean_fields()

        except ValidationError as err:
            message = {
                "erro": "Um movimento inválido foi detectado, infelizmente a sonda ainda não consegue ir tão longe."}

            return Response(data=message, status=400)

        sonda.save()

        serializers = SondaSerializer(sonda)
        return Response(serializers.data)


class GetCoordinatesView(APIView):
    """ Return current probe´s coordinate in json format """

    def get(self, request, format=None):
        sonda = Sonda.objects.first()

        serializers = SondaSerializer(sonda)
        return Response(serializers.data)
