from rest_framework import status
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Plant
from backend import custom_status_codes, responses
from .serializers import PlantSerializer
from django.core.exceptions import ValidationError, ObjectDoesNotExist


class PlantViewSet(viewsets.ViewSet):
    serializer_class = PlantSerializer
    permission_classes = (IsAuthenticated,)

    # POST METHOD
    def create(self, request):
        if request.user.has_perm('nursery.add_plant'):

            request.data._mutable = True
            request.data['user'] = request.user.id
            request.data._mutable = False
            serializer = PlantSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(responses.generate_success_response(custom_status_codes.ADD_ITEMS_SUCCESS,
                                                                    payload={'data': serializer.data}),
                                status=status.HTTP_201_CREATED)
            return Response(responses.generate_failure_response(custom_status_codes.ADD_ITEMS_FAILURE,
                                                                payload={'errors': serializer.errors}),
                            status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(responses.generate_failure_response(custom_status_codes.AUTHORIZATION_FAILURE, payload={}),
                            status=status.HTTP_401_UNAUTHORIZED)

        # GET METHOD
        # LIST ALL THE PLANTS AVAILABLE

    def list(self, request, *args, **kwargs):
        try:
            plantset = Plant.objects.filter(is_deleted=False)
            serializer = PlantSerializer(plantset, many=True)
            return Response(responses.generate_success_response(custom_status_codes.LIST_ITEMS_SUCCESS,
                                                                payload={'data': serializer.data}),
                            status=status.HTTP_200_OK)
        except:
            return Response(responses.generate_failure_response(custom_status_codes.LIST_ITEMS_FAILURE, payload={}),
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    # GET WITH ID METHOD
    def retrieve(self, request, pk, *args, **kwargs):
        try:
            query = Plant.objects.get(id=pk, is_deleted=False)
            if query is None:
                return Response(responses.generate_failure_response(custom_status_codes.VIEW_ITEM_FAILURE),
                                status=status.HTTP_400_BAD_REQUEST)

            serializer = PlantSerializer(query)
            return Response(responses.generate_success_response(custom_status_codes.VIEW_ITEM_SUCCESS,
                                                                payload={'data': serializer.data}),
                            status=status.HTTP_200_OK)
        except ValidationError:
            return Response(responses.generate_failure_response(custom_status_codes.LIST_ITEMS_FAILURE, payload={}),
                            status=status.HTTP_404_NOT_FOUND)

        except:
            return Response(responses.generate_failure_response(custom_status_codes.LIST_ITEMS_FAILURE, payload={}),
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    # PATCH METHOD
    # Partially update the record s
    def partial_update(self, request, pk):
        if request.user.has_perm('nursery.change_plant'):
            try:
                instance = Plant.objects.get(id=pk, user=request.user)
                if instance is None or 'user' in request.data:
                    return Response(responses.generate_failure_response(custom_status_codes.UPDATE_ITEM_FAILURE),
                                    status=status.HTTP_400_BAD_REQUEST)
                serializer = PlantSerializer(instance, data=request.data, partial=True)
                if serializer.is_valid():
                    serializer.save()
                    return Response(responses.generate_success_response(custom_status_codes.UPDATE_ITEM_SUCCESS,
                                                                        payload={'data': serializer.data}),
                                    status=status.HTTP_200_OK)
                else:
                    return Response(responses.generate_failure_response(custom_status_codes.UPDATE_ITEM_FAILURE,
                                                                        payload={"errors": serializer.errors}),
                                    status=status.HTTP_400_BAD_REQUEST)
            except ValidationError:
                return Response(responses.generate_failure_response(custom_status_codes.ID_IMPROPER),
                                status=status.HTTP_400_BAD_REQUEST)

            except ObjectDoesNotExist:
                return Response(
                    responses.generate_failure_response(custom_status_codes.AUTHORIZATION_FAILURE, payload={}),
                    status=status.HTTP_401_UNAUTHORIZED)


        else:
            return Response(responses.generate_failure_response(custom_status_codes.AUTHORIZATION_FAILURE, payload={}),
                            status=status.HTTP_401_UNAUTHORIZED)

    # SOFT DELETE OF A PLANT
    def destroy(self, request, pk):
        if request.user.has_perm('nursery.delete_plant'):
            try:
                object = Plant.objects.get(id=pk, user=request.user)
                object.is_deleted = True
                object.save()
                return Response(responses.generate_success_response(custom_status_codes.DELETE_ITEMS_SUCCESS,
                                                                    payload={}),
                                status=status.HTTP_200_OK)

            except ObjectDoesNotExist:

                return Response(
                    responses.generate_failure_response(custom_status_codes.AUTHORIZATION_FAILURE, payload={}),
                    status=status.HTTP_401_UNAUTHORIZED)

        else:
            return Response(responses.generate_failure_response(custom_status_codes.AUTHORIZATION_FAILURE, payload={}),
                            status=status.HTTP_401_UNAUTHORIZED)
