from django.conf.urls import url
from . import views

urlpatterns = [
    # 匹配`kyc/`成功就调用`views`中的`kyc`函数
    url(r'^kyc/$', views.kyc),
]