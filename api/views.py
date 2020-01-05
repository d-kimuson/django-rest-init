from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action

from .models import Sample
from .serializer import SampleSerializer


class SampleViewSet(viewsets.ModelViewSet):
    queryset = Sample.objects.all()
    serializer_class = SampleSerializer
    filter_fields = ('name', 'score',)

    @action(methods=['GET'], detail=False, url_path='search')
    def search(self, request):
        keyword = request.GET.get('keyword')
        return Response(Sample.to_list(name__icontains=keyword))

    @action(methods=['GET'], detail=True, url_path='more_detail')
    def more_detail(self, request, pk):
        try:
            s = self.get_queryset().get(pk=pk)
        except Sample.DoesNotExist as e:
            print(e)
            return Response({
                "error_message": f"Sample<pk={pk}> は存在しません."
            })

        return Response(s.to_dict())
