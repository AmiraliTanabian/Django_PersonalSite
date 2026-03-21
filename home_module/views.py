from django.shortcuts import render
from django.views.generic import TemplateView, View
from django.http import HttpRequest
from .models import InfoModel, SkillModel, CommentModels, StatsModel, EducationModel, WorkExperience, AttributeModel, PortfolioCategoryModel, PortfolioModel

class HomeView(View):
    def get(self, request:HttpRequest):
        info = InfoModel.objects.filter(is_active=True).last()
        skills = SkillModel.objects.all()
        comments = CommentModels.objects.all()
        educations = EducationModel.objects.all()
        experiences = WorkExperience.objects.all()
        try:
            stats = StatsModel.objects.all()[4]
        except IndexError:
            stats = StatsModel.objects.all()

        try:
            attributes = AttributeModel.objects.all()[3]
        except IndexError:
            attributes = AttributeModel.objects.all()

        portfolio_cats = PortfolioCategoryModel.objects.all()
        portfolios = PortfolioModel.objects.all()
        return render(request, "index.html", {
            "info":info,
            "skills":skills,
            "comments":comments,
            "stats":stats,
            "educations":educations,
            "experiences":experiences,
            "attributes":attributes,
            "portfolio_cats":portfolio_cats,
            "portfolios":portfolios
        })
