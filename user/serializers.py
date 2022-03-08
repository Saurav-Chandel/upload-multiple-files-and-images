from rest_framework import serializers
from .models import *


# # class FileListSerializer ( serializers.Serializer ) :
# #     image = serializers.ListField(
# #                        child=serializers.FileField( max_length=100000,
# #                                          allow_empty_file=False,
# #                                          use_url=False )
# #                                 )
# #     def create(self, validated_data):
# #         print("_________")
# #         blogs=Blogs.objects.latest('created_at')
# #         image=validated_data.pop('image')
# #         for img in image:
# #             photo=Photo.objects.create(image=img,blogs=blogs,**validated_data)
# #         return photo


# class PhotoSerializer(serializers.ModelSerializer):
    
#     class Meta:
#         model = Photo
#         fields=['id','blogs','image']
#         read_only_fields = ("blogs",)


# class BlogsSerializer(serializers.ModelSerializer):
#     blogs_img=PhotoSerializer(many=True, required=False)
    
#     class Meta:
#         model = Blogs
#         fields=['id','name','blogs_img']
#         read_only_fields = ("blogs",)

#     def create(self, validated_data):      
#         print("________")  
#         blog = Blogs.objects.create(**validated_data)
#         print(blog)
#         try:
#             # try to get and save images (if any)
#             images_data = dict((self.context['request'].FILES).lists()).get('blogs_img', None)
#             print(images_data)
#             for img in images_data:
#                 print(img)
#                 Photo.objects.create(blogs=blog, image=img)
#         except:
#             # if no images are available - create using default image
#             Photo.objects.create(blogs=blog)
#         return blog    





#Another Serializers Approach


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class ImageSerializer(serializers.ModelSerializer):
    # product=ProductSerializer(read_only=True)
    class Meta:
        model = Images
        fields = '__all__'