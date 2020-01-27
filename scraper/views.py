from rest_framework.views import APIView
from rest_framework.response import Response

from .Email import Email


"""
author : Domngang Eric Faycal, Essongo joel Stephane
description : endpoints for getting email when we entry a domain 
"""
class FindEmailsView(APIView): 
    def post(self, request):
        url = request.data.get('url', None)
        p = request.data.get('p', None)
        final_data = Email.main(Email, url, p) # p = nomber of email to back
        Jsonfinal = {"data": final_data}

        return Response(Jsonfinal)