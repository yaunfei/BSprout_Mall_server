import io
import json

from rest_framework import viewsets
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.merchandise.models import SpuInfo
from apps.merchandise.serializers import SpuSerializer
from core.utls import Pagination
from django.core import serializers


# Create your views here.
class SpuInfoView(viewsets.ReadOnlyModelViewSet):
    # queryset = models.SpuInfo.objects.filter(id="2").first()
    queryset = SpuInfo.objects.all()
    serializer_class = SpuSerializer
    pagination_class = Pagination  # 分页


class SpuInfoList(APIView):
    def get(self, request, *args, **kwargs):
        res = {"code": 200}
        # 全查
        # spuInfoList = SpuInfo.objects.all()
        # serializer = SpuSerializer(spuInfoList, many=True)
        # res["data"] = serializer.data
        # return Response(res)

        # 条件查询

        # key = request.GET.get("name")
        # spuInfoList = SpuInfo.objects.filter(name=key)
        # paginationInfo = Pagination()
        # paginationSpuInfoList = paginationInfo.paginate_queryset(spuInfoList, request, view=self)
        # serializer = SpuSerializer(paginationSpuInfoList, many=True)
        # res["data"] = serializer.data
        #
        # return paginationInfo.get_paginated_response(res)

        # if not request.user.is_authenticated:
        #     return Response('请先登录')

        key = request.GET.get("name")
        spuInfoList = SpuInfo.objects.filter(name=key).values()  # 这样处理不要序列化

        paginationInfo = Pagination()
        paginationSpuInfoList = paginationInfo.paginate_queryset(spuInfoList, request, view=self)
        res["data"] = paginationSpuInfoList

        return Response(res)

    def post(self, request):
        # if not request.user.is_authenticated:
        #     return Response('请先登录')
        res = SpuSerializer(data=request.data)
        if res.is_valid():
            res.save()
            return Response({"code": "200", "data": '保存成功'}, status=200)
        return Response(res.errors)
