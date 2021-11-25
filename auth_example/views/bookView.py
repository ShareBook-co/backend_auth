from rest_framework                          import generics
from rest_framework.permissions              import IsAuthenticated
from auth_example.models.book                import Book
from auth_example.serializers.bookSerializer import BookSerializer

class BookListCreateView(generics.ListCreateAPIView):
    queryset           = Book.objects.all()
    serializer_class   = BookSerializer
    permission_classes = (IsAuthenticated,)

class BookDetailView(generics.RetrieveAPIView):
    queryset           = Book.objects.all()
    serializer_class   = BookSerializer
#    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
            
#        token        = request.META.get('HTTP_AUTHORIZATION')[7:]
#        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
#        valid_data   = tokenBackend.decode(token,verify=False)
#
#        if valid_data['user_id'] != kwargs['pk']:
#            stringResponse = {'detail':'Acceso no autorizado.'}
#            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)

        return super().get(request, *args, **kwargs)

class BookUpdateView(generics.UpdateAPIView):
    queryset           = Book.objects.all()
    serializer_class   = BookSerializer

    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

class BookDeleteView(generics.DestroyAPIView):
    queryset           = Book.objects.all()
    serializer_class   = BookSerializer

    def delete(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

