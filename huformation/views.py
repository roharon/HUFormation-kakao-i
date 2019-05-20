from django.shortcuts import render
from django.http import JsonResponse

def show_test(request):
    if request.method == "POST":
      userRequest = request.data
      userRequest = userRequest.body
      print(userRequest)
      return JsonResponse({
  "version": "2.0",
  "context": {
    "version": "2.0",
    "template": {
        "outputs": [
            {
                "simpleText": {
                    "text": userRequest
                }
            }
        ]
    }
}
})

    if request.method == "POST":
      return JsonResponse({'status':200})