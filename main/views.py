from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from simple_project import GlobalClass


################################## BUSSINES ACCOUNT ENDPOINTS ####################################


@api_view(['GET'])
def test(request):
    # is_request_valid, request_check_message = GlobalClass.is_request_valid(request)
    # if not is_request_valid:
    #     return Response(GlobalClass.IResponse(ok=False, message=request_check_message).to_dict(), status.HTTP_400_BAD_REQUEST)

    return Response(GlobalClass.IResponse(ok=True, message='endpoint test work', data=None).to_dict(), status.HTTP_200_OK)