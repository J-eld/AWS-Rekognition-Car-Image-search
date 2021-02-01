from django.shortcuts import render, redirect
from .models import Document
from .forms import DocumentForm
from .Rekog import Rekog

# Create your views here.
def home_view(request, *args, **kwargs):
    return render(request, 'homepage.html', {})

def my_view(request):
    print(f"Great! You're using Python 3.6+. If you fail here, use the right version.")
    message = 'Upload Image to search for similar vehicles'
    # Handle file upload
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            Document.objects.all().delete()
            newdoc = Document(docfile=request.FILES['docfile'])
            newdoc.save()

            # Redirect to the document list after POST
            return redirect('my-view')

    else:
        form = DocumentForm()  # An empty, unbound form

    # Load documents for the list page
    documents = Document.objects.all()
    
    for document in documents:
        TypeOfCar = Rekog(document.docfile.name)
        Document.objects.all().delete()

        if TypeOfCar == 'Coupe':
            return redirect(coupe_view)

        if TypeOfCar == 'Sedan':
            return redirect(sedan_view)
        
        if TypeOfCar == 'Suv':
            return redirect(suv_view)
        
        if TypeOfCar == 'Truck':
            return redirect(truck_view)
        
        if TypeOfCar == 'Convertible':
            return redirect(convertible_view)
        
        if TypeOfCar == 'Van':
            return redirect(van_view)
            
    
    
    

    # Render list page with the documents and the form
    context = {'documents': documents, 'form': form, 'message': message}
    return render(request, 'base.html', context)

def sedan_view(request, *args, **kwargs):
    return redirect('https://www.turners.co.nz/Cars/Used-Cars-for-Sale/?sortorder=7&pagesize=24&pageno=1&types=sedan')

def coupe_view(request, *args, **kwargs):
    return redirect('https://www.turners.co.nz/Cars/Used-Cars-for-Sale/?sortorder=7&pagesize=24&pageno=1&types=coupe')
    
def truck_view(request, *args, **kwargs):
    return redirect('https://www.turners.co.nz/Cars/Used-Cars-for-Sale/?sortorder=7&pagesize=24&pageno=1&types=utility')
    
def convertible_view(request, *args, **kwargs):
    return redirect('https://www.turners.co.nz/Cars/Used-Cars-for-Sale/?sortorder=7&pagesize=24&pageno=1&types=convertible')
    
def suv_view(request, *args, **kwargs):
    return redirect('https://www.turners.co.nz/Cars/Used-Cars-for-Sale/?sortorder=7&pagesize=24&pageno=1&types=suv')
    
def van_view(request, *args, **kwargs):
    return redirect('https://www.turners.co.nz/Cars/Used-Cars-for-Sale/?sortorder=7&pagesize=24&pageno=1&types=van')
    