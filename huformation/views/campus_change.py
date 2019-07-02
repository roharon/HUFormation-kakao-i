# -*- coding: utf8 -*-
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def campus_change(request):
    """
    :param request:
    :return: 캠퍼스 변경 알림 텍스트
    """
    received_json_data = json.loads(request.body)
    user_request = received_json_data['userRequest']

    user_data = dict()
    user_data['time_zone'] = user_request['timezone']
    user_data['utterance'] = user_request['utterance']
    user_data['lang'] = user_request['lang']
    user_data['user_id'] = user_request['user']['id']


    #TODO DJANGO DB연결 및 사용자 캠퍼스 정보 UPDATE

    return JsonResponse({
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "simpleText": {
                        "text": "캠퍼스를 선택하세요"
                    }
                }
            ],
            "quickReplies": [
                {
                    "action": "message",
                    "label": "서울캠퍼스",
                    "messageText": "서울캠퍼스"
                },
                {
                    "action": "message",
                    "label": "글로벌캠퍼스",
                    "messageText": "글로벌캠퍼스"
                }
            ]
        }
    })
