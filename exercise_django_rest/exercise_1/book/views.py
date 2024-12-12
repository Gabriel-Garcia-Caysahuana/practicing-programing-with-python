from .models import Book
from rest_framework import permissions, viewsets
from .serializers import BookSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    # permission_classes = [permissions.IsAuthenticated]

