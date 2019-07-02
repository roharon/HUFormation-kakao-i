# -*- coding: utf8 -*-
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .shortcut import *

@csrf_exempt
def library_reservation(request):
    return JsonResponse({
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "basicCard": {
                        "title": "도서관 열람실 연장",
                        "description": "도서관 좌석 연장을 온라인으로 하세요",
                        "buttons": [
                            {
                                "action": "webLink",
                                "label": "연장하기",
                                "webLinkUrl": library_reservation_link
                            },
                            {
                                "action": "share",
                                "label": "공유하기"
                            }
                        ]

                    }
                }
            ],
            "quickReplies": quickReplies
        }
    })