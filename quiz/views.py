from django.shortcuts import render
from django.db.models import Max
import random
from .serializers import *
from .models import *
from rest_framework.generics import ListAPIView
from rest_framework.generics import RetrieveAPIView
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.core.cache import cache
# Create your views here.


def get_random():
    cached_result = cache.get('random_quiz')
    
    if cached_result is not None:
        # 캐시에 값이 존재하면 그 값을 반환합니다.
        return cached_result
    
    max_id = Quiz.objects.all().aggregate(max_id=Max("id"))['max_id']
    while 1:
        # pk = random.randint(1,max_id)
        random_list = random.sample(range(1,max_id+1),2)
        queryset = Quiz.objects.filter(pk=random_list[0])
        for temp_pk in random_list[1:]:
            temp_qs = Quiz.objects.filter(pk=temp_pk)
            queryset = queryset.union(temp_qs)
        # queryset = Quiz.objects.filter(pk=pk)
        if queryset:
            return queryset


class QuizListAPIView(ListAPIView):
    serializer_class = QuizSerializer
    
    def get_queryset(self):
        return get_random()
    
class QuizRetrieveAPIView(RetrieveAPIView):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer
    