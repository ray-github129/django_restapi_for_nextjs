from django.contrib import admin
from .models import Task, Post

# PostとTaskのモデルをジャンゴで見れるように設定する
# Register your models here.

admin.site.register(Post)
admin.site.register(Task)