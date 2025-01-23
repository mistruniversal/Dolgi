class WomenAPIList(generics.ListCreateAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer


class WomenAPIUpdate(generics.UpdateAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer


class WomenAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer











from rest_framework import viewsets


class WomenViewSet(viewsets.ModelViewSet):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer









urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/womenlist/', WomenViewSet.as_view({'get': 'list'})),
    path('api/v1/womenlist/<int:pk>/', WomenViewSet.as_view({'put': 'update'})),
]










from rest_framework import routers
router = routers.SimpleRouter()


router.register(r'women', WomenViewSet)







urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),   # http://127.0.0.1:8000/api/v1/women/
]



class WomenViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer


class ReadOnlyModelViewSet(mixins.RetrieveModelMixin,
                           mixins.ListModelMixin,
                           GenericViewSet):
    pass


class ModelViewSet(mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
                   mixins.ListModelMixin,
                   GenericViewSet):
    pass




class WomenViewSet(mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
                   mixins.ListModelMixin,
                   viewsets.GenericViewSet):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer