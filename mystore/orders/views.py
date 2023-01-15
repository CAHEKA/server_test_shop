from rest_framework import viewsets, status
from rest_framework.response import Response

from .serializers import OrderSerializers
from .models import Orders

from mystore.store.models import Products, Feedbacks


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Orders.objects.all().order_by('-created_at')
    serializer_class = OrderSerializers

    def create(self, request):
        if request.method == 'POST':
            order = request.data.get('order')
            cart = request.data.get('order')['cart']
            rating = request.data.get('order')['rating']

            for i in cart:
                # Product inventory subtraction
                i.pop('image')
                item_id = i.get('itemId')
                qty = i.get('qty')
                p = Products.objects.get(pk=item_id)

                if p.inventory == 0:
                    return Response(status=status.HTTP_409_CONFLICT)

                p.inventory = p.inventory - qty
                p.save()

            if rating:
                for i in rating:
                    item_id = i.get('itemId')
                    value = i.get('value')
                    r = Feedbacks.objects.get(products=item_id)

                    if value == 1:
                        r.one += 1
                    elif value == 2:
                        r.two += 1
                    elif value == 3:
                        r.three += 1
                    elif value == 4:
                        r.four += 1
                    elif value == 5:
                        r.five += 1
                    r.save()

            serializer = self.serializer_class(data=order, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
