from django.shortcuts import render, redirect
from django.http import HttpResponse
from apps.plan.models import Plan
from apps.plan.forms import PlanForm


# Create your views here.

def index(request):
    return render(request, 'plan/index.html')

def quienesSomos(request):
    return render(request, 'plan/quienesSomos.html')

def contacto(request):
    return render(request, 'plan/contacto.html')

def plan_view(request):
    if request.method == 'POST':
        form = PlanForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect(plan_listar)
    else:
        form = PlanForm()

    return render(request, 'plan/plan_form.html', {'form':form}) 

def plan_listar(request):
    plan = Plan.objects.all().order_by('id')
    contexto = {'planes':plan}
    return render(request, 'plan/plan_list.html', contexto)

def plan_editar(request, id_plan):
    plan = Plan.objects.get(id=id_plan)
    if request.method == 'GET':
        form = PlanForm(instance=plan)
    else:
        form = PlanForm(request.POST, instance=plan)
        if form.is_valid():
            form.save()
        return redirect(plan_listar) 
    return render(request, 'plan/plan_form.html', {'form':form})     

def plan_eliminar(request, id_plan):
    plan = Plan.objects.get(id=id_plan)
    if request.method =='POST':
        plan.delete()
        return redirect(plan_listar)
    return render(request, 'plan/plan_delete.html', {'plan':plan})    
         