import os
from datetime import datetime, timedelta, timezone
from rest_framework import serializers
from .models import Image
from auth_app.models import CustomUser
from PIL import Image as Img


class ImageSerializers(serializers.ModelSerializer):
    image_small = serializers.SerializerMethodField()
    image_medium = serializers.SerializerMethodField()

    class Meta:
        model = Image
        fields = ['id', 'image', 'user', 'image_medium', 'image_small']
        read_only_fields = ['image_medium', 'image_small']

    def get_image_small(self, obj):
        request = self.context.get('request')
        small_path = obj.image.name.replace('.', '_small.')
        image_small = request.build_absolute_uri('/media/') + small_path
        return image_small

    def get_image_medium(self, obj):
        if obj.user.user_plan != CustomUser.USER_PLAN_BASIC:
            request = self.context.get('request')
            medium_path = obj.image.name.replace('.', '_medium.')
            image_medium = request.build_absolute_uri('/media/') + medium_path
            return image_medium
        return 'Move to Premium plan.'

    def to_representation(self, instance):
        data = super(ImageSerializers, self).to_representation(instance)
        if instance.user.user_plan != CustomUser.USER_PLAN_ENTERPRISE:
            data['image'] = 'Move to Enterprise plan.'
            return data
        return data


class ImageDetailSerializers(serializers.ModelSerializer):
    image_small = serializers.SerializerMethodField()
    image_medium = serializers.SerializerMethodField()
    lifetime_link = serializers.SerializerMethodField()

    class Meta:
        model = Image
        fields = ['id', 'image', 'user', 'link_lifetime_in_seconds', 'link_lifetime_created',
                  'image_medium', 'image_small', 'lifetime_link']
        read_only_fields = ['image_medium', 'image_small']

    def get_lifetime_link(self, obj):
        request = self.context.get('request')
        time_change = timedelta(seconds=obj.link_lifetime_in_seconds)
        time_date = obj.link_lifetime_created + time_change
        date = datetime.now().replace(tzinfo=timezone.utc)
        date.isoformat()
        current_day = date.replace(microsecond=0)
        current_day.isoformat()
        image_path = obj.image.path

        lifetime_image_path = obj.image.name.replace('.', f'_lifetime_{obj.link_lifetime_in_seconds}.')
        image_exist = os.path.exists(image_path.replace('.', f'_lifetime_{obj.link_lifetime_in_seconds}.'))
        if current_day < time_date and not image_exist:
            image = Img.open(image_path)
            lifetime_image = image.copy()
            lifetime_image.save(image_path.replace('.', f'_lifetime_{obj.link_lifetime_in_seconds}.'))
            lifetime_link = request.build_absolute_uri('/media/') + lifetime_image_path
            return lifetime_link

        if image_exist:
            os.remove(image_path.replace('.', f'_lifetime_{obj.link_lifetime_in_seconds}.'), dir_fd=None)
        return 'Set time'

    def get_image_small(self, obj):
        request = self.context.get('request')
        small_path = obj.image.name.replace('.', '_small.')
        image_small = request.build_absolute_uri('/media/') + small_path
        return image_small

    def get_image_medium(self, obj):
        if obj.user.user_plan != CustomUser.USER_PLAN_BASIC:
            request = self.context.get('request')
            medium_path = obj.image.name.replace('.', '_medium.')
            image_medium = request.build_absolute_uri('/media/') + medium_path
            return image_medium
        return 'Move to Premium plan.'

    def to_representation(self, instance):
        data = super(ImageDetailSerializers, self).to_representation(instance)
        if instance.user.user_plan != CustomUser.USER_PLAN_ENTERPRISE:
            data['image'] = 'Move to Enterprise plan.'
            return data
        return data
