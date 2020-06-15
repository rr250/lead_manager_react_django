from rest_framework import generics, viewsets, permissions
from rest_framework.response import Response
from fuzzywuzzy import fuzz
from leads.models import Lead
from .serializers import LeadSerializer

# Lead Viewset


class LeadViewSet(viewsets.ModelViewSet):
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    serializer_class = LeadSerializer

    def get_queryset(self):
        print(Lead.objects.all().values())
        leads = Lead.objects.all()
        return leads


    def perform_create(self, serializer):
        serializer.save()

class Search(generics.GenericAPIView):
    # permission_classes = [
    #     permissions.IsAuthenticated,
    # ]
    serializer_class = LeadSerializer
    def get(self, request):
        str1 = request.GET.get('search')
        leads = Lead.objects.all()
        res = []
        for lead in leads:
            if(fuzz.ratio(str1.lower(),lead.name.lower())>80 or fuzz.partial_ratio(str1.lower(),lead.name.lower())>80 or fuzz.token_sort_ratio(str1,lead.name)>80 or fuzz.token_set_ratio(str1,lead.name)>80):
                res.append(lead)
        res = sorted(res,key = lambda lead: fuzz.ratio(str1.lower(),lead.name.lower()) + fuzz.partial_ratio(str1.lower(),lead.name.lower()) + fuzz.token_sort_ratio(str1,lead.name) + fuzz.token_set_ratio(str1,lead.name))
        return Response(LeadSerializer(res,many=True).data)

