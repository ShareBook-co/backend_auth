from rest_framework                          import generics
from rest_framework.permissions              import IsAuthenticated
from auth_example.models.book                import Book
from auth_example.serializers.bookSerializer import BookSerializer

class BookListCreateView(generics.ListCreateAPIView):
    queryset           = Book.objects.all()
    serializer_class   = BookSerializer
    permission_classes = (IsAuthenticated,)

class BooksView(generics.RetrieveUpdateDestroyAPIView):
    queryset           = Book.objects.all()
    serializer_class   = BookSerializer
    permission_classes = (IsAuthenticated,)