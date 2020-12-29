from rest_framework import status
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .models import Cart, Orders
from backend import custom_status_codes, responses
from .serializers import CartSerializer, OrderSerializer
from nursery.models import Plant
from django.core.exceptions import ValidationError, ObjectDoesNotExist


# cart: where a user can add,update,delete .only user have the permission to do so.

class UserCart(viewsets.ViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = CartSerializer

    def create(self, request, *args, **kwargs):

        if request.user.has_perm('orders.add_cart'):
            request.data['user'] = request.user.id

            serializer = CartSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(responses.generate_success_response(custom_status_codes.ADD_ITEMS_SUCCESS,
                                                                    payload={'data': serializer.data}),
                                status=status.HTTP_201_CREATED)
            else:
                return Response(responses.generate_success_response(custom_status_codes.ADD_ITEMS_FAILURE,
                                                                    payload={'errors': serializer.errors}),
                                status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(responses.generate_failure_response(custom_status_codes.AUTHORIZATION_FAILURE, payload={}),
                            status=status.HTTP_401_UNAUTHORIZED)

    def partial_update(self, request, pk, *args, **kwargs):
        if request.user.has_perm('orders.change_cart'):
            try:
                instance = Cart.objects.get(id=pk, user=request.user)
                if instance is None or 'user' in request.data:
                    return Response(responses.generate_failure_response(custom_status_codes.UPDATE_ITEM_FAILURE),
                                    status=status.HTTP_400_BAD_REQUEST)
                serializer = CartSerializer(instance, data=request.data, partial=True)
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
            return Response(
                responses.generate_failure_response(
                    custom_status_codes.AUTHORIZATION_FAILURE, payload={}),
                status=status.HTTP_401_UNAUTHORIZED)

    def destroy(self, request, pk):
        if request.user.has_perm('orders.delete_cart'):
            queryset = Cart.objects.filter(id=pk, user=request.user)

            if len(queryset) == 0:
                return Response(responses.generate_failure_response(custom_status_codes.UPDATE_ITEM_FAILURE),
                                status=status.HTTP_400_BAD_REQUEST)
            queryset.delete()

            return Response(responses.generate_success_response(custom_status_codes.UPDATE_ITEM_SUCCESS,
                                                                payload={}),
                            status=status.HTTP_200_OK)

        else:
            return Response(
                responses.generate_failure_response(
                    custom_status_codes.AUTHORIZATION_FAILURE, payload={}),
                status=status.HTTP_401_UNAUTHORIZED)


class PlaceOrder(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        if request.user.has_perm('orders.change_cart'):

            orderset = Cart.objects.filter(user=request.user)
            if len(orderset) != 0:
                for data in orderset:
                    nursery = Plant.objects.get(id=data.plant_id)
                    nursery_user = nursery.user_id
                    total_amount = nursery.price * data.quantity

                    order = Orders(status="placed", quantity=data.quantity, nursery_id=nursery_user,
                                   plant_id=data.plant_id, user_id=data.user_id, total=total_amount)

                    order.save()
                orderset.delete()
                return Response(responses.generate_success_response(custom_status_codes.ORDER_PLACED_SUCCESS,
                                                                    payload={}),
                                status=status.HTTP_200_OK)
            else:
                return Response(
                    responses.generate_failure_response(
                        custom_status_codes.NO_ITEM_ERROR, payload={}),
                    status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(
                responses.generate_failure_response(
                    custom_status_codes.AUTHORIZATION_FAILURE, payload={}),
                status=status.HTTP_401_UNAUTHORIZED)


class ViewOrder(viewsets.ViewSet):
    permission_classes = (IsAuthenticated,)

    def list(self, request, *args, **kwargs):
        try:
            if request.user.has_perm('orders.view_orders'):
                queryset = Orders.objects.filter(nursery_id=request.user.id)
                serializer = OrderSerializer(queryset, many=True)
                return Response(responses.generate_success_response(custom_status_codes.LIST_ITEMS_SUCCESS,
                                                                    payload={'data': serializer.data}),
                                status=status.HTTP_200_OK)
            else:
                return Response(
                    responses.generate_failure_response(
                        custom_status_codes.AUTHORIZATION_FAILURE, payload={}),
                    status=status.HTTP_401_UNAUTHORIZED)
        except:
            return Response(responses.generate_failure_response(custom_status_codes.LIST_ITEMS_FAILURE, payload={}),
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)
