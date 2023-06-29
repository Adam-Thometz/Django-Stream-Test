from rest_framework.decorators import api_view
from django.http import StreamingHttpResponse
from .gen import test_gen

@api_view(['GET'])
def helloworld(request):
    print('hello!')
    response = StreamingHttpResponse(test_gen())
    response['Content-Type'] = 'text/event-stream'
    print(response)
    return response