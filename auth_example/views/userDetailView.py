#from django.conf                             import settings
from rest_framework                          import generics#, status
#from rest_framework.response                 import Response
#from rest_framework_simplejwt.backends       import TokenBackend
#from rest_framework.permissions              import IsAuthenticated

from auth_example.models.user                import User
from auth_example.serializers.userSerializer import UserSerializer

class UserDetailView(generics.RetrieveAPIView):
    queryset           = User.objects.all()
    serializer_class   = UserSerializer
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

class UserUpdateView(generics.UpdateAPIView):
    queryset           = User.objects.all()
    serializer_class   = UserSerializer

    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

class UserDeleteView(generics.DestroyAPIView):
    queryset           = User.objects.all()
    serializer_class   = UserSerializer

    def delete(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)