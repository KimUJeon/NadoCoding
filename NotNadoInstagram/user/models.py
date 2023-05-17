from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models

# Create your models here.
class User(AbstractBaseUser):
    '''
        프로필 이미지
        유저 아이디(닉네임)
        유저 이름
        유저 이메일주소 -> 회원가입시 사용하는 아이디
        유저 비밀번호 -> 디폴트 이용
    '''

    profile_image = models.TextField()
    nickname = models.CharField(max_length=24, unique=True)
    user_name = models.CharField(max_length=24)
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'nickname'

    class Meta:
        db_table = "User"

