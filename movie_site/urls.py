from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from movies import views as movie_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', movie_views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='movies/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='movies/logout.html'), name='logout'),
    path('', movie_views.home, name='home'),
    path('asia/', movie_views.asia_movies, name='asia_movies'),
    path('europe/', movie_views.europe_movies, name='europe_movies'),
    path('china/', movie_views.china_movies, name='china_movies'),
    path('movies/', include('movies.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)