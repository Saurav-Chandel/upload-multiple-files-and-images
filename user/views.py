from django.shortcuts import render
from rest_framework import viewsets
from .serializers import *
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.response import Response
from rest_framework import  status


# Create your views here.


# class PhotoViewSet(viewsets.ModelViewSet):
#     serializer_class = BlogsSerializer
#     parser_classes = (MultiPartParser, FormParser,)
#     queryset=Blogs.objects.all()





class ImagesViewSet(viewsets.ModelViewSet):
    queryset = Images.objects.all()
    serializer_class = ImageSerializer
    
    # overwrite create method from the CreateModelMixin
    def create(self, request, *args, **kwargs):
        data = request.data
        images = data.getlist('image')
        
        # if no images call parent method it will return error
        if not images:
            return super().create(request, *args, **kwargs)

        # verify only without creating the images
        serializer_lst = []
        for image in images:
            data['image'] = image
            serializer = self.get_serializer(data=data)
            serializer.is_valid(raise_exception=True)
            serializer_lst.append(serializer)
        
        serializers_data = [] # this is to collect data for all created images and return as list in the response
        for serializer in serializer_lst:
            self.perform_create(serializer)
            serializers_data.append(serializer.data)
            headers = self.get_success_headers(serializer.data)
        
        return Response({"data":serializers_data}, status=status.HTTP_201_CREATED, headers=headers)