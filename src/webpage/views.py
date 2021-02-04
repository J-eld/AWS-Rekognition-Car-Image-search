from django.shortcuts import render, redirect
from .models import Document
from .forms import DocumentForm
from .Rekog import Rekog
from random import randint

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

def lucky_view(request):

    sedans = ['https://www.turners.co.nz/Cars/Used-Cars-for-Sale/subaru/legacy/20257257',
    'https://www.turners.co.nz/Cars/Used-Cars-for-Sale/mazda/mazda6/21051761',
    'https://www.turners.co.nz/Cars/Used-Cars-for-Sale/mazda/mazda6/21075790',
    'https://www.turners.co.nz/Cars/Used-Cars-for-Sale/toyota/sai/20003512',
    'https://www.turners.co.nz/Cars/Used-Cars-for-Sale/mazda/axela/20237023',
    'https://www.turners.co.nz/Cars/Used-Cars-for-Sale/nissan/teana/21048186',
    'https://www.turners.co.nz/Cars/Used-Cars-for-Sale/nissan/sunny/21113032']


    coupes = ['https://www.turners.co.nz/Cars/Used-Cars-for-Sale/bmw/3-series/21113176', 
    'https://www.turners.co.nz/Cars/Used-Cars-for-Sale/bmw/320i/20239287', 
    'https://www.turners.co.nz/Cars/Used-Cars-for-Sale/peugeot/407/21001135', 
    'https://www.turners.co.nz/Cars/Used-Cars-for-Sale/toyota/86/21098687', 
    'https://www.turners.co.nz/Cars/Used-Cars-for-Sale/mercedes-benz/cls/20326229' , 
    'https://www.turners.co.nz/Cars/Used-Cars-for-Sale/hyundai/tiburon/21140447' , 
    'https://www.turners.co.nz/Cars/Used-Cars-for-Sale/audi/tt/21116671' , 
    'https://www.turners.co.nz/Cars/Used-Cars-for-Sale/peugeot/307/21072241' , 
    'https://www.turners.co.nz/Cars/Used-Cars-for-Sale/audi/tt/21130719', 
    'https://www.turners.co.nz/Cars/Used-Cars-for-Sale/volvo/c70/21130774']


    vans = ['https://www.turners.co.nz/Cars/Used-Cars-for-Sale/mercedes-benz/sprinter/19317851', 
    'https://www.turners.co.nz/Cars/Used-Cars-for-Sale/nissan/caravan/19953293', 
    'https://www.turners.co.nz/Cars/Used-Cars-for-Sale/toyota/hiace/20230894', 
    'https://www.turners.co.nz/Cars/Used-Cars-for-Sale/nissan/caravan/21045946', 
    'https://www.turners.co.nz/Cars/Used-Cars-for-Sale/nissan/e-nv200/20259632', 
    'https://www.turners.co.nz/Cars/Used-Cars-for-Sale/mazda/titan/21078613', 
    'https://www.turners.co.nz/Cars/Used-Cars-for-Sale/nissan/e-nv200/19179059']


    convertibles = ['https://www.turners.co.nz/Cars/Used-Cars-for-Sale/toyota/mr-s/20986428', 
    'https://www.turners.co.nz/Cars/Used-Cars-for-Sale/mercedes-benz/slk350/21140343', 
    'https://www.turners.co.nz/Cars/Used-Cars-for-Sale/ford/mustang/21152463', 
    'https://www.turners.co.nz/Cars/Used-Cars-for-Sale/bmw/z4/21150476']


    suvs = ['https://www.turners.co.nz/Cars/Used-Cars-for-Sale/hyundai/santa-fe/21045399',
    'https://www.turners.co.nz/Cars/Used-Cars-for-Sale/honda/crv/21055672',
    'https://www.turners.co.nz/Cars/Used-Cars-for-Sale/toyota/rav4/20279253',
    'https://www.turners.co.nz/Cars/Used-Cars-for-Sale/subaru/forester/20277536',
    'https://www.turners.co.nz/Cars/Used-Cars-for-Sale/volkswagen/touareg/21019328',
    'https://www.turners.co.nz/Cars/Used-Cars-for-Sale/nissan/qashqai/21051669',
    'https://www.turners.co.nz/Cars/Used-Cars-for-Sale/volkswagen/tiguan/19879618',]


    trucks = ['https://www.turners.co.nz/Cars/Used-Cars-for-Sale/holden/commodore/20989410',
    'https://www.turners.co.nz/Cars/Used-Cars-for-Sale/ssangyong/actyon-sport/21107085',
    'https://www.turners.co.nz/Cars/Used-Cars-for-Sale/foton/tunland/21113182',
    'https://www.turners.co.nz/Cars/Used-Cars-for-Sale/toyota/hilux/19461479',
    'https://www.turners.co.nz/Cars/Used-Cars-for-Sale/ford/ranger/21087004',
    'https://www.turners.co.nz/Cars/Used-Cars-for-Sale/holden/colorado/19415716',
    'https://www.turners.co.nz/Cars/Used-Cars-for-Sale/mitsubishi/canter/19192245']

    if analyse_view.TypeOfCar == 'Sedan':
        return redirect(sedans[randint(0, len(sedans) - 1)])

    elif analyse_view.TypeOfCar == 'Coupe':
        return redirect(coupes[randint(0, len(coupes) - 1)])
    
    elif analyse_view.TypeOfCar == 'Suv':
        return redirect(suvs[randint(0, len(suvs) - 1)])

    elif analyse_view.TypeOfCar == 'Convertible':
        return redirect(convertibles[randint(0, len(convertibles) - 1)])

    elif analyse_view.TypeOfCar == 'Truck':
        return redirect(trucks[randint(0, len(trucks) - 1)])

    elif analyse_view.TypeOfCar == 'Van':
        return redirect(vans[randint(0, len(vans) - 1)])

