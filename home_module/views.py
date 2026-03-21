from django.shortcuts import render
from django.views.generic import TemplateView, View
from django.http import HttpRequest
from .models import InfoModel, SkillModel, CommentModels

class HomeView(View):
    def get(self, request:HttpRequest):
        info = InfoModel.objects.filter(is_active=True).last()
        skills = SkillModel.objects.all()
        comments = CommentModels.objects.all()
        return render(request, "index.html", {
            "info":info,
            "skills":skills,
            "comments":comments
        })
