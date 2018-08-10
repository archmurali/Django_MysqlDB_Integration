# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from rest_framework import generics
from .models import OcCart
from .serializers import CartSerializer

from django.http import HttpResponse
from django.views.generic import View


class ListSongsView(generics.ListAPIView):
    """
    Provides a get method handler.
    """
    queryset = OcCart.objects.all()
    serializer_class = CartSerializer


class MyView(View):
  	def get(self,request,*args, **kwargs):
  		result = OcCart.objects.get(cart_id=13)
  		return HttpResponse("hello,world" +  " " + str(result))
