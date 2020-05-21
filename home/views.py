from django.shortcuts import render, redirect, get_object_or_404
from django.http.response import HttpResponse

from .forms import MySkillsForm
from .models import MySkills


# Create your views here.

def landing_page(request):
    data = {
        'name': 'Kalyan',
        'nums': [1, 2, 3],
        'test': 'TEST'
        }
    return render(request, "home.html", data)

def skills_add(request):
    context = {}
    if request.method == 'POST':
        form = MySkillsForm(request.POST)
        if form.is_valid():
            skill = form.save()
            print(skill)
            return redirect('skills_edit', pk=skill.pk)
    else:
        form = MySkillsForm()
    context['form'] = form
    return render(request, 'skill_edit.html', context)


def skills_edit(request, pk):
    context = {}
    skill = get_object_or_404(MySkills, pk=pk)
    if request.method == 'POST':
        form = MySkillsForm(request.POST , instance=skill)
        if form.is_valid():
            skill = form.save(commit=False)
            skill.save()
            print(skill)
            return redirect('skills_edit', pk=skill.pk)
    else:
        form = MySkillsForm(instance=skill)
    context['form'] = form
    return render(request, 'skill_edit.html', context)
