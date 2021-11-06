from rest_framework.generics import ListAPIView , RetrieveUpdateDestroyAPIView
from .models import Ish
from .serializers import IshSerializer

class IshListView(ListAPIView):
    queryset = Ish.objects.all()
    serializer_class = IshSerializer

class IshDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Ish.objects.all()
    serializer_class = IshSerializer