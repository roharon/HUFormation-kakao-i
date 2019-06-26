# -*- coding: utf8 -*-
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

def lib(request):
    """
    도서관 열람실 좌석현황
    :param request: 도서관,열람실 고유번호
    :return: 도서관 열람실 좌석 json 카드 템플릿
    """