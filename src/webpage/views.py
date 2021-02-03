from django.shortcuts import render, redirect
from .models import Document
from .forms import DocumentForm
from .Rekog import Rekog

# Create your views here.


def home_view(request, *args, **kwargs):
    return render(request, 'homepage.html', {})


def analyse_view(request):
    print(f"Great! You're using Python 3.6+. If you fail here, use the right version.")
    message = 'Upload Image to search for similar vehicles'
    # Handle file upload
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Document(docfile=request.FILES['docfile'])
            newdoc.save()
            analyse_view.image = Document.objects.all()[0].docfile.name
            analyse_view.TypeOfCar = Rekog(analyse_view.image)
            Document.objects.all().delete()

            # Redirect to the document list after POST
            return redirect('my-view')

    else:
        form = DocumentForm()  # An empty, unbound form

    
    # Render list page with the documents and the form
    context = {'form': form, 'message': message}
    return render(request, 'analyse.html', context)



def my_view(request):

    # Render list page with the documents and the form
    context = {'TypeOfCar':analyse_view.TypeOfCar, "image": analyse_view.image,}
    return render(request, 'base.html', context)

def turners_view(request):
    if analyse_view.TypeOfCar == 'Coupe':
        return redirect('https://www.turners.co.nz/Cars/Used-Cars-for-Sale/?sortorder=7&pagesize=24&pageno=1&types=coupe')

    elif analyse_view.TypeOfCar == 'Sedan':
        return redirect('https://www.turners.co.nz/Cars/Used-Cars-for-Sale/?sortorder=7&pagesize=24&pageno=1&types=sedan')

    elif analyse_view.TypeOfCar == 'Suv':
        return redirect('https://www.turners.co.nz/Cars/Used-Cars-for-Sale/?sortorder=7&pagesize=24&pageno=1&types=suv')

    elif analyse_view.TypeOfCar == 'Truck':
        return redirect('https://www.turners.co.nz/Cars/Used-Cars-for-Sale/?sortorder=7&pagesize=24&pageno=1&types=utility')

    elif analyse_view.TypeOfCar == 'Convertible':
        return redirect('https://www.turners.co.nz/Cars/Used-Cars-for-Sale/?sortorder=7&pagesize=24&pageno=1&types=convertible')

    elif analyse_view.TypeOfCar == 'Van':
        return redirect('https://www.turners.co.nz/Cars/Used-Cars-for-Sale/?sortorder=7&pagesize=24&pageno=1&types=van')
