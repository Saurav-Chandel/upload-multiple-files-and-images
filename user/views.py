from django.shortcuts import render
from rest_framework import viewsets
from .serializers import *
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.response import Response
from rest_framework import  status


# Create your views here.


class BlogViewSet(viewsets.ModelViewSet):
    serializer_class = BlogsSerializer
    parser_classes = (MultiPartParser, FormParser,)
    queryset=Blogs.objects.all()

class PhotoViewSet(viewsets.ModelViewSet):
    serializer_class = PhotoSerializer
    parser_classes = (MultiPartParser, FormParser,)
    queryset=Photo.objects.all()


    #get a single photo by input a blog_id.
    def list(self,request,pk=None):
        blog_id=request.data.get('blog_id')
        if blog_id:
            photo=Photo.objects.filter(blogs=blog_id)
            return Response({"data":photo.values()})
        return Response({"data":Photo.objects.all().values()})    

    # def update(self,request,pk=None):
    #     print("__________")
    #     data=request.data
    #     print(data)

    #     serializer=self.serializer_class(data=data)
    #     print("SSSSSSSS")
    #     if serializer.is_valid():
    #         serializer.save()
    #     #    return super().update(instance, validated_data)   
    #     return Response({"msg":serializer.data})

        # instance.image = validated_data.get('image', instance.image)
        # print(instance)
        # instance.save()
        # return instance
        
       








# class ImagesViewSet(viewsets.ModelViewSet):
#     queryset = Images.objects.all()
#     serializer_class = ImageSerializer

#     # overwrite create method from the CreateModelMixin
#     def create(self, request, *args, **kwargs):
#         data = request.data
#         images = data.getlist('image')
          
#         # if no images call parent method it will return error
#         if not images:
#             return super().create(request, *args, **kwargs)

#         # verify only without creating the images
#         serializer_lst = []
#         for image in images:
#             data['image'] = image
#             serializer = self.get_serializer(data=data)
#             serializer.is_valid(raise_exception=True)
#             serializer_lst.append(serializer)
        
#         serializers_data = [] # this is to collect data for all created images and return as list in the response
#         for serializer in serializer_lst:
#             self.perform_create(serializer)
#             serializers_data.append(serializer.data)
#             headers = self.get_success_headers(serializer.data)
        
#         return Response({"data":serializers_data}, status=status.HTTP_201_CREATED, headers=headers)

#     def update(self,request,pk):
#         image=self.get_object(pk)

#         data=request.data   
#         images=data.FILES.getlist('image')

#         def clear_existing_images(self, instance):
#             for image in instance.images():
#                image.images.delete()
#                image.delete()

#         def update(self,)       





