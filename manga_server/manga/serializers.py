from rest_framework import serializers
from .models import Manga, Chapter
from user.models import CustomUser


class MangaSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    owner_id = serializers.IntegerField(required=True, write_only=True)

    class Meta:
        model = Manga
        fields = ["id", "name", "owner_id"]

        extra_kwargs = {
            "name": {"required": True}, 
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

    class Meta:
        model = Chapter
        fields = ["id", "name", "num_of_page", "order", "manga_id"]

        extra_kwargs = {
            "name": {"required": True},
            "num_of_page": {"required": True},
            "order": {"required": True},
            "manga_id": {"required": True},
        }

    def create(self, validated_data):
        chapter = Chapter()
        manga = Manga.objects.get(id=validated_data["manga_id"])

        chapter.name = validated_data["name"]
        chapter.num_of_page = validated_data["num_of_page"]
        chapter.order = validated_data["order"]
        chapter.manga = manga

        return chapter
