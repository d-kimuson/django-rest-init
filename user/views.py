from rest_framework import viewsets
from rest_framework.response import Response
# from rest_framework.decorators import action
from django.db.utils import IntegrityError

from .serializer import UserSerializer
from .models import User


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_fields = ('email',)

    def update(self, request, *args, **kwargs):
        pk = kwargs['pk']
        try:
            user = User.objects.get(pk=pk)
        except User.DoesNotExist as e:
            print(e)
            return Response({
                "error_message": f"ユーザー: pk={pk} は存在しません"
            })

        if user != request.user:
            return Response({
                "error_message": "他ユーザーのパラメータの書き換えはできません"
            })

        serializer = self.get_serializer()

        required_keys = set(self.get_serializer_class().Meta.fields) - {'pk'}
        if set(request.data.keys()) - required_keys != set():
            return Response({
                "error_message": f"Keyを確認してください. 必要なKey: {required_keys}"
            })

        try:
            return Response(
                serializer.update(instance=user, validated_data=request.data).to_dict()
            )
        except IntegrityError as e:
            print(e)
            return Response({
                "error_message": f"パラメータの更新に失敗. パラメータが適切であることを確認してください. Error: {e.__cause__}"
            })
