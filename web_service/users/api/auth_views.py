# -*- coding: utf-8 -*-

from django.contrib.auth import authenticate, login as auth_login
from utils.request_utils import pretreatment, response_as_json_without_auth

# Created by: guangda.lee
# Created on: 2019/3/20
# Function:


# 用户登录验证
@response_as_json_without_auth
@pretreatment
def login(request, data):
    auth_user = authenticate(username=data['username'], password=data['password'])
    if auth_user and auth_user.is_active:
        auth_login(request, auth_user)
        # 生成 token
        from utils.string_utils import generate_token
        user_item = auth_user.user
        user_item.token = generate_token()
        user_item.save()
        return {
            'category': {
                'id': user_item.category.category,
                'name': user_item.category.name,
                'isAdmin': user_item.category.name == u'管理员'
            },
            'id': user_item.id,
            'fullname': auth_user.last_name,
            'email': auth_user.email,
            'enable_tasks': user_item.enable_tasks,
            'token': user_item.token
        }, 200
    return {}, 401


# 退出登录状态
@response_as_json_without_auth
def logout(request):
    from users.common import user_by_token
    user = user_by_token(request)
    if user:
        user.token = ''
        user.save()
        return {}, 200
    return {'detail': 'You do not have permission to perform this action.'}, 403

