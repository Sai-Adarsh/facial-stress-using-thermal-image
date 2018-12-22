from django.shortcuts import render
from .forms import GetPictureForm
from .predict import predict
from django.core.files.storage import FileSystemStorage
from thermalai.settings import BASE_DIR
from django.http import JsonResponse
import os
# Create your views here.


from django.views.decorators.csrf import csrf_exempt

@csrf_exempt

def index(request):
	form = GetPictureForm()
	print (request.method)
	result = None
	if request.method == 'POST':
		print (request.POST, request.FILES)
		file = request.FILES['file']
		fs = FileSystemStorage()
		filename = fs.save('images/'+file.name, file)
		uploaded_file_url = fs.url(filename)
		image_dir = os.path.join(BASE_DIR, 'images')
		result = predict (image_dir+'\\'+file.name)
		#return (result)
	return render(request, 'index.html', {'form':form, 'result':result})
	