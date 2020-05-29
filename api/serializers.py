from rest_framework import serializers

from home.models import MySkills


class MySkillSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=20, required=True)
    icon_class = serializers.CharField(max_length=30, required=True)
    description = serializers.CharField(required=True, style={'base_template': 'textarea.html'})
    skills = serializers.CharField(max_length=200, required=True)
    created_at = serializers.DateField(read_only=True)
    updated_at = serializers.DateField(read_only=True)

    def create(self, validated_data):
        return MySkills.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.icon_class = validated_data.get('icon_class', instance.icon_class)
        instance.description = validated_data.get('description', instance.description)
        instance.skills = validated_data.get('skills', instance.skills)
        instance.save()
        return instance
