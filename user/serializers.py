from re import S
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


class PhotoSerializer(serializers.ModelSerializer):
    # image = serializers.ListField(child=serializers.ImageField(allow_empty_file=True))

    class Meta:
        model = Photo
        fields=['id','blogs','image']
        # read_only_fields = ("blogs",)


    #updates single image (inpirt:--blogs_id)
    def update(self,instance,validated_data):
        instance.image=validated_data.get('image',instance.image)
        instance.save()
        return instance
        


        # serializer=self.serializer_class(data=data)
        # print("SSSSSSSS")
        # if serializer.is_valid():
        #     serializer.save()
        # #    return super().update(instance, validated_data)   
        # return Response({"msg":serializer.data})


class BlogsSerializer(serializers.ModelSerializer):
    blogs_img=PhotoSerializer(many=True, required=False)
    # images=serializers.ListField(child=PhotoSerializer(many=True, required=False))
    # images_data = dict((self.context['request'].FILES).lists()).get('blogs_img', None)

    class Meta:
        model = Blogs
        fields=['id','name','blogs_img']
        # read_only_fields = ("blogs",)

    def create(self, validated_data):   
        print("________")  
        blog = Blogs.objects.create(**validated_data)
        print(blog)
        try:
            # try to get and save images (if any)
            images_data = dict((self.context['request'].FILES).lists()).get('blogs_img', None)
            print(images_data)
            for img in images_data:
                print(img)
                Photo.objects.create(blogs=blog, image=img)
        except:
            # if no images are available - create using default image
            Photo.objects.create(blogs=blog)
        return blog   


    # def clear_existing_images(self, instance):
    #         for post_image in instance.blogs_img:
    #             post_image.images.delete()
    #             post_image.delete()


    def update(self,instance,validated_data):
        print(instance)
        # images_data = dict((self.context['request'].FILES).lists()).get('blogs_img', None)
        # b=validated_data.pop('images_data',None)
        images = dict((self.context['request'].FILES).lists()).get('blogs_img', None)
        print(images)
        if images:
            print("___________")
            # self.clear_existing_images(instance)
            post_image_model_instance = [Photo(blogs=instance, image=img) for img in images]
            Photo.objects.bulk_create(
                post_image_model_instance
            )
        return super().update(instance, validated_data)    


        



    




       








#Another Serializers Approach


# class ProductSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Product
#         fields = '__all__'

# class ImageSerializer(serializers.ModelSerializer):
#     # product=ProductSerializer(read_only=True)
#     class Meta:
#         model = Images
#         fields = '__all__'


    # def clear_existing_images(self, instance):
    #     for image in instance.images():
    #        image.images.delete()
    #        image.delete()    

    # def update(self,instance,valiated_data):
    #     images = validated_data.pop('images', None)
    #     if images:
    #         self.clear_existing_images



