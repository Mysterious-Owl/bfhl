from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


class EmptyArray(Exception):
    def __repr__(self):
        return "Empty Request Body"


@api_view(['POST'])
def odd_even(request):
    user_id = "tanishq_gupta_25072001"
    try:
        data = map(int, JSONParser().parse(request)['numbers'])
        odd = []
        even = []
        for i in data:
            if i & 1:
                odd.append(i)
            else:
                even.append(i)
        if len(odd) == 0 and len(even) == 0:
            raise EmptyArray
        return Response({'is_success': True, 'user_id': user_id, "odd": odd, "even": even}, status.HTTP_200_OK)

    except Exception as e:
        return Response({'is_success': False, 'user_id': user_id}, status.HTTP_400_BAD_REQUEST)
