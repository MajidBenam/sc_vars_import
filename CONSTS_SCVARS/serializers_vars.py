SERIALIZERS_FUNCTION_DEFINITIONS = """
################ Beginning of Base Serializers
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class ReferenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reference
        fields = ['id', 'title', 'year', 'creator', 'zotero_link', 'long_name']
        
################ End of Base Serializers
"""
