from rest_framework_mongoengine.serializers import DocumentSerializer
from .models import Tool

class ToolSerializer(DocumentSerializer):

    class Meta:
        model = Tool
        fields = '__all__' 

