from django.urls import path
from .views import home, projects, resume, contact, ai_model_api,upload_resume

urlpatterns = [
    path('', home, name='home'),
    path('projects/', projects, name='projects'),
    path('resume/', resume, name='resume'),
    path('resume/upload/', upload_resume, name='upload_resume'),
    path('contact/', contact, name='contact'),
    path('api/ai_model/', ai_model_api, name='ai_model_api'),
]
