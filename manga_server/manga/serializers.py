from rest_framework import serializers
from .models import Manga, Chapter
from user.models import CustomUser

from . import utils

class MangaSerializer(serializers.ModelSerializer):
    owner_id = serializers.IntegerField(required=True, write_only=True)

    class Meta:
        model = Manga
        fields = "__all__"

        extra_kwargs = {
            "name": {"required": True}, 
            "owner" : {"read_only" : True},
            "owner_id": {"required": True}
        }

    def validate(self, attrs):
        if (attrs['owner_id'] is None) or (attrs['owner_id'] == ''):
            raise serializers.ValidationError("owner_id is required")
        
        return attrs

    def create(self, validated_data):
        manga = Manga()
        user = CustomUser.objects.get(id=validated_data["owner_id"])

        manga.name = validated_data["name"]
        manga.owner = user

        manga.save()

        return manga

class ChapterSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    manga_id = serializers.IntegerField(write_only=True, required=True)
    file = serializers.FileField(required=True, write_only=True)

    class Meta:
        model = Chapter
        fields = ["id", "name", "num_of_page", "order", "manga_id", "file"]

        extra_kwargs = {
            "name": {"required": True},
            "num_of_page": {"required": True},
            "order": {"required": True},
            "manga_id": {"required": True},
        }
        
    def validate(self, attrs):
        if not attrs["num_of_page"]:
            raise serializers.ValidationError("Num of page is required")
        return attrs
    
    def create(self, validated_data):
        chapter = Chapter()
        manga = Manga.objects.get(id=validated_data["manga_id"])
        
        chapter.name = validated_data["name"]
        chapter.num_of_page = validated_data["num_of_page"]
        chapter.order = validated_data["order"]
        chapter.manga = manga

        folder_name, folder_path = utils.get_and_save_upload_file(data=validated_data['file'])
        utils.extract_and_remove_compress_file(folder_path)

        chapter.save()
        
        utils.upload_png_from_local(chapter, folder_name)
        utils.remove_temp_folder(folder_name)

        return chapter
    
class MangaDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manga
        fields = '__all__'

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        chapters = instance.chapter_set.all()
        ret['chapters'] = ChapterSerializer(chapters, many=True).data
        
        return ret
    
class ChapterDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chapter
        fields = '__all__'

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret['public_href'] = utils.get_all_page_from_chapter(instance)
        return ret