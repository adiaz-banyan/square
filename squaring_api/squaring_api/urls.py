from django.contrib import admin
from django.urls import path, include
from squaring.views import SquaringView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('squaring.urls')),
    path('square/<int:number>', SquaringView.as_view())
]
