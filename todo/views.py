from django.shortcuts import get_object_or_404, redirect, render
from .models import Ish
from .forms import IshForm

def todo(request):
    ishlar = Ish.objects.all()
    if request.method == 'POST':
        form = IshForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = IshForm()
    context = {
        "ishlar":ishlar,
        'form': form
    }
    return render(request, 'todo/home.html', context)


def delete(request,id):
    ish = get_object_or_404(Ish,id=id)
    ish.delete()
    return redirect("home")

def bajarildi(request,id):
    ish = get_object_or_404(Ish,id=id)
    ish.bajarish = True
    ish.save()
    return redirect("home")

def edit(request,id):
    ish = get_object_or_404(Ish,id=id)
    if request.method == 'POST':
        form = IshForm(request.POST,instance=ish)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = IshForm(instance=ish)

    return render(request, 'todo/edit.html',{"ish":ish,"form":form})
