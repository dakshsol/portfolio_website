from django.shortcuts import render

# Create your views here.
# from django.shortcuts import render
# from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# import json
from .models import ContactMessage
from django.shortcuts import render,redirect
from django.http import JsonResponse
from django.contrib import admin
from django.urls import path
from django.db import models
from django.views.decorators.csrf import csrf_exempt
import json
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.decorators import login_required, user_passes_test
import json
from .models import ContactMessage,ResumeUpload

# Home Page
def home(request):
    return render(request, 'home.html')


# Projects Page
def projects(request):
    return render(request, 'projects.html')

def is_admin(user):
    return user.is_superuser

def resume(request):
    print(f"User: {request.user}, Is Superuser: {request.user.is_superuser}")  # Debugging
    uploaded_resumes = ResumeUpload.objects.all()
    return render(request, 'resume.html', {'resumes': uploaded_resumes})


@login_required
@user_passes_test(is_admin)
def upload_resume(request):
    if request.method == 'POST' and request.FILES.get('resume'):
        uploaded_file = request.FILES['resume']
        fs = FileSystemStorage()
        file_name = fs.save(f'resumes/{uploaded_file.name}', uploaded_file)
        ResumeUpload.objects.create(resume=file_name)
        return redirect('resume')  # Updated: Redirect to refresh the page after upload
    return render(request, 'upload_resume.html')  # Updated: Render the upload page

# Contact Form Handling
def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        ContactMessage.objects.create(name=name, email=email, message=message)
        return JsonResponse({'status': 'Message Sent'})
    return render(request, 'contact.html')

# AI Model API Example
def sample_ai_model(input_text):
    return f"AI Response for: {input_text}"

@csrf_exempt
def ai_model_api(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        input_text = data.get('input_text', '')
        response = sample_ai_model(input_text)
        return JsonResponse({'response': response})
    return render(request, 'ai_model.html')
