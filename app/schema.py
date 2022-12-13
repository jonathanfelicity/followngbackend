from .models import User
from . import ma



class UserSchema(ma.Schema):
    class Meta:
        fields = ('id', 'username', 'created_At','is_Banned', 'wallet')


single_user = UserSchema()
all_users = UserSchema(many=True)