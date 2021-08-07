from django.shortcuts import render,redirect
from testapp.models import Empmobnumbers
from testapp.forms import EmpmobnumbersForm
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.db.models import Q

# Create your views here.

def create_view(request):
    #edept_id=request.GET.get('edept')
    empmobnumber=Empmobnumbers.objects.filter(Q(edept="PR") | Q(edept="APSHCL") |Q(edept="RWS") )

    return  render(request,'testapp/create.html',{'empmobnumber':empmobnumber})

def logout_view(request):
    return render(request,'testapp/logout.html')

@login_required
def create_pr(request):
    empmobnumber=Empmobnumbers.objects.filter(edept="PR")
    paginator=Paginator(empmobnumber,5)
    page_number=request.GET.get('page')
    try:
        empmobnumber=paginator.page(page_number)
    except PageNotAnInteger:
        empmobnumber=paginator.page(1)
    except EmptyPage:
        empmobnumber=paginator.page(paginator.num_pages)

    return  render(request,'testapp/create.html',{'empmobnumber':empmobnumber})

def create_rws(request):
    empmobnumber=Empmobnumbers.objects.filter(edept="RWS")
    paginator=Paginator(empmobnumber,5)
    page_number=request.GET.get('page')
    try:
        empmobnumber=paginator.page(page_number)
    except PageNotAnInteger:
        empmobnumber=paginator.page(1)
    except EmptyPage:
        empmobnumber=paginator.page(paginator.num_pages)

    return  render(request,'testapp/create.html',{'empmobnumber':empmobnumber})
def create_ap(request):
    empmobnumber=Empmobnumbers.objects.filter(edept="APSHCL")
    paginator=Paginator(empmobnumber,5)
    page_number=request.GET.get('page')
    try:
        empmobnumber=paginator.page(page_number)
    except PageNotAnInteger:
        empmobnumber=paginator.page(1)
    except EmptyPage:
        empmobnumber=paginator.page(paginator.num_pages)

    return  render(request,'testapp/create.html',{'empmobnumber':empmobnumber})
def insert_view(request):
    form=EmpmobnumbersForm()
    if request.method=="POST":
        form =EmpmobnumbersForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    return render(request,'testapp/insert.html',{'form':form})

def delete_view(request,id):
    id=int(id)
    empmobnumber=Empmobnumbers.objects.get(id=id)
    empmobnumber.delete()
    return redirect("/")

def update_view(request,id):
    employee=Empmobnumbers.objects.get(id=id)
    if request.method=="POST":
        form=EmpmobnumbersForm(request.POST,instance=employee)
        if form.is_valid():
            form.save()
        return redirect('/')
    return render(request,'testapp/update.html',{'employee':employee})
