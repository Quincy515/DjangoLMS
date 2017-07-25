settings.py

项目的总配置文件

里面包含了数据库、Web应用、时间等各种配置

BASE_DIR 项目的根目录
SECRET_KEY 安全码，自动生成
DEBUG 调试
ALLOWED_HOSTS 外界只允许使用这个地址访问网站
INSTALLED_APPS 已经安装的应用
MIDDLEWARE 中间件，Django自带的工具集
ROOT_URLCONF URL的配置文件根文件
TEMPLATES 模版配置
WSGI_APPLICATION 和WSGI有关的，我们可以默认忽略
DATABASES 数据库配置
AUTH_PASSWORD_VALIDATORS 密码认证
LANGUAGE_CODE = 'en-us'
STATIC_URL = '/static/' 静态文件地址


setting文件的配置:
1. DATABASES:
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': "testdjango",
        'USER': "root",
        'PASSWORD': "root1234",
        'HOST': "127.0.0.1"
    }
}
```
2. TEMPLATES:
```
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```
3. 新建STATICFILES_DIRS
`
    静态文件路径配置
    STATICFILES_DIRS = [
        os.path.join(BASE_DIR, 'static')
    ]
`


