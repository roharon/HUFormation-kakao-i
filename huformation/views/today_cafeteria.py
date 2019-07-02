# -*- coding: utf8 -*-
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .shortcut import *

@csrf_exempt
def today_cafeteria(request):
    """
    :param request:
    :return: 오늘의 학식 메뉴
    """
    return JsonResponse({
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "simpleText": {
                        "text": "오늘의 학식"
                    }
                }
            ],
            "quickReplies": quickReplies
        }
    })