from django.shortcuts import render
from rest_framework.views import APIView
from .models import Feed

# Create your views here.
class Main(APIView):
    def get(self, request):
        feed_list = Feed.objects.all().order_by('-id') # select * from content_feed 랑 동일한 동작

        return render(request, "notnadocoding/main.html", context=dict(feeds=feed_list))

