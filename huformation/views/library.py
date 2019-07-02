# -*- coding: utf8 -*-
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

def library(request):
    """
    도서관 열람실 좌석현황
    :param request: 도서관,열람실 고유번호
    :return: 도서관 열람실 좌석 json 카드 템플릿
    """
    #TODO 도서관 크롤러 연결 후 뿌리기
    pass