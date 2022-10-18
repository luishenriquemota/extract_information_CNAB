
from transactions.models import Files, Transactions
from rest_framework import serializers

class UploadSerializer(serializers.ModelSerializer):

    class Meta:
        model= Files
        fields = ["id", "file", "description", "user"]
        read_only_fields = ["id", "user"]


class ConvertFileSerializer(serializers.ModelSerializer):
    class Meta:
        model= Transactions
        fields= "__all__"
        read_only_fields= ["type"]


