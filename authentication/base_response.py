from rest_framework import status
from rest_framework.response import Response


def s_404(reason):

    return Response({'error':f'{reason} Does not Exist'},status=status.HTTP_404_NOT_FOUND)


def s_406(reason):

    return Response({'error':f'Except {reason} into Request Body'},status=status.HTTP_406_NOT_ACCEPTABLE)



def s_200(ser):

    return Response(ser.data, status=status.HTTP_200_OK)