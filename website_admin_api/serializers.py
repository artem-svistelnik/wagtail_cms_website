# from rest_framework import serializers
# from .models import HomePage,HomeHeaderGalleryImage,AboutCompanyPage,Activities,NewsPublicationPage,NewsPublicationPageTag
# from wagtail.images.models import Image
# from taggit.models import TaggedItemBase
#
# #Gallery
# class ImageSerialier(serializers.ModelSerializer):
#     class Meta:
#         model=Image
#         # fields='__all__'
#         fields=('id','title','file','width','height')
# class HomeHeaderGalleryImageSerializer(serializers.ModelSerializer):
#     image=ImageSerialier()
#     class Meta:
#         model=HomeHeaderGalleryImage
#         fields='__all__'
# #Activities
# class ActivitiesSerializer(serializers.ModelSerializer):
#     activity_image=ImageSerialier()
#     class Meta:
#         model=Activities
#         # fields='__all__'
#         fields=('id','kind_of_activity_ru','kind_of_activity_uk',
#                 'activity_image','activity_image_caption_ru','activity_image_caption_uk',
#                 )
# class AboutCompanySerializer(serializers.ModelSerializer):
#     activities=ActivitiesSerializer(many=True,read_only=True)
#     class Meta:
#         model=AboutCompanyPage
#         # fields=('about_company_text_ru','about_company_text_uk','activities')/
#         # fields='__all__'
#         fields=('id','title_ru','title_uk','seo_title_ru','seo_title_uk','search_description_ru','search_description_uk',
#                 'about_company_text_ru','about_company_text_uk','activities')
# class HomePageSerializer(serializers.ModelSerializer):
#     gallery_images=HomeHeaderGalleryImageSerializer(many=True,read_only=True)
#     # about_company_page=AboutCompanySerializer()
#     class Meta:
#         model=HomePage
#         # fields='__all__'
#         fields=('title_ru','title_uk','seo_title_ru','seo_title_uk','company_position_ru','company_position_uk','gallery_images')#,'about_company_page')
# class TagsSerializer(serializers.ModelSerializer):
#     class Meta:
#         model=TaggedItemBase
#         fields='__all__'
#
# class NewsPublicationPageTagSerializer(serializers.ModelSerializer):
#     content_object=TagsSerializer()
#     class Meta:
#         model=NewsPublicationPageTag
#         fields='__all__'
#
# class Tag(serializers.ModelSerializer):
#     # tag=TagsSerializer(read_only=True)
#     # tag=serializers.StringRelatedField(many=True)
#     class Meta:
#         model=NewsPublicationPageTag
#         fields='__all__'
#         # abstract = False
#
# from .models import HeadingNewsPublicationsTypes
# class PublicationHeadingSerializer(serializers.ModelSerializer):
#     class Meta:
#         model=HeadingNewsPublicationsTypes
#         fields='__all__'
#
#
# class NewsPublicationPageSerializer(serializers.ModelSerializer):
#     publication_heading=PublicationHeadingSerializer()
#     publication_image=ImageSerialier()
#     class Meta:
#         model=NewsPublicationPage
#         fields='__all__'
#
# class TestTagSer(serializers.ModelSerializer):
#     class Meta:
#         model=TagsSerializer
#         fields='__all__'
#
#
