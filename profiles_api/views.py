from rest_framework.views import APIView
from rest_framework.response import Response



class HelloApiView(APIView):
    """Test API View"""

    def get(self, request, format=None):
        """Returns a list of APIView features"""
        an_apiview = [
        'this is a test ',
        'this is a test ',
        'this is a test ',
        'this is a test ',
        ]

        return Response({'message': 'Hello!', 'an_apiview': an_apiview})
