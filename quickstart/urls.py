



from django.urls import path
from . import views


urlpatterns = [
    # path('test/',views.test, name='test'),
    path('test/<int:id>',views.delete_test),
	path("foo/", views.foo)
    
]

