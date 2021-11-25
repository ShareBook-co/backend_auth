from rest_framework                          import status, views
from rest_framework.response                 import Response
from rest_framework_simplejwt.serializers    import TokenObtainPairSerializer
from auth_example.models.user                import User
from rest_framework                          import generics
from auth_example.serializers.userSerializer import UserSerializer


class UserCreateView(views.APIView):
    def post(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        tokenData = {"username":request.data["username"],
                     "password":request.data["password"]}
        tokenSerializer = TokenObtainPairSerializer(data=tokenData)
        tokenSerializer.is_valid(raise_exception=True)
        
        return Response(tokenSerializer.validated_data, status=status.HTTP_201_CREATED)
    

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