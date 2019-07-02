# -*- coding: utf8 -*-
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .shortcut import *
from .today_cafeteria import today_cafeteria
from .library_reservation import library_reservation
# quickReplies
import json

@csrf_exempt
def skill(request):
    received_json_data = json.loads(request.body)
    user_request = received_json_data['userRequest']

    user_data = dict()
    user_data['time_zone'] = user_request['timezone']
    user_data['utterance'] = user_request['utterance']
    user_data['lang'] = user_request['lang']
    user_data['user_id'] = user_request['user']['id']

    if "오늘의 학식" in user_data['utterance']:
        return today_cafeteria(request)

    elif "열람실 좌석 연장" in user_data['utterance']:
        return library_reservation(request)
    else:
        return JsonResponse({
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "simpleText": {
                            "text": "명령어를 이해하지 못했습니다.\n다시 눌러주세요"
                        }
                    }
                ],
                "quickReplies": quickReplies
            }
        })
