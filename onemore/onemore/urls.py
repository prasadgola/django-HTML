from django.contrib import admin
from django.urls import path
from onemoreapp import views

admin.site.site_header = 'jvt connect admin'
admin.site.site_title = 'jvt connect admin'
admin.site.index_title = 'jvt connect adminstration'


urlpatterns = [
    path('login',views.user_login, name = 'nobulshit'),
    path('ppl',views.ppl, name = 'ppl'),
    # path('show',views.show, name = 'show'),
    path('signin',views.signin, name = 'signin'),
    path('admin/', admin.site.urls),
    path('signup',views.signup, name = 'signup'),
    path('logout',views.signout, name = 'logout'),
    path('jvtconnect',views.jvtconnect, name = 'jvtconnect'),

]