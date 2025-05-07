from django.urls import path
from .views import (
    home, signup_view, login_view, logout_view,
    upload_file, my_files, download_file,
    upload_file_api, user_files_api, public_files_api
)

urlpatterns = [
    path('', home, name='home'),
    path('signup/', signup_view, name='signup'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('upload/', upload_file, name='upload'),
    path('my-files/', my_files, name='my_files'),
    path('download/<int:file_id>/', download_file, name='download'),  # Changed name here
    path('api/upload/', upload_file_api, name='upload_file_api'),
    path('api/my-files/', user_files_api, name='user_files_api'),
    path('api/public-files/', public_files_api, name='public_files_api'),
]
