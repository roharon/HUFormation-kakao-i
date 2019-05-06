from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.
def keyboard(request):
    userRequest = JsonResponse(request)
    #userRequest.content

    return JsonResponse({
  "version": "2.0",
  "context": {
    "values": [
      {
        "name": "abc",
        "lifeSpan": 10,
        "params": {
          "key1": "val1",
          "key2": "val2"
        }
      },
      {
        "name": "def",
        "lifeSpan": 5,
        "params": {
          "key3": "1",
          "key4": "true",
          "key5": "{\"jsonKey\": \"jsonVal\"}"
        }
      },
      {
        "name": "ghi",
        "lifeSpan": 0
      }
    ]
  }
})