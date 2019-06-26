# -*- coding: utf8 -*-
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

def get_haksik(request):
    """
    학식 메뉴 로드 관리
    :param date: 날짜 (오늘, 내일, 다음주 등)
    :return: 학식 json 카드 템플릿 포맷
    """