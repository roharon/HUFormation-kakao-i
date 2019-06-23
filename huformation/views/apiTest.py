from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def apiTest(request):

    print(request.body)
    return JsonResponse({
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "simpleImage": {
                        "imageUrl": "https://t1.daumcdn.net/friends/prod/category/M001_friends_ryan2.jpg",
                        "altText": " Image"
                    }
                }
            ]
        }
    })