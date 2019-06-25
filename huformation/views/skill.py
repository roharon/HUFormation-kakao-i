# -*- coding: utf8 -*-
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
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

    #사용자 발화
    return JsonResponse({
    "version": "2.0",
    "template": {
        "outputs": [
            {
                "simpleText": {
                    "text": user_data['utterance'] + " 를 눌렀습니다."
                }
            }
        ]
    }
})
