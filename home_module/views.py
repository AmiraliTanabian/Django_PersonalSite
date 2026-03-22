from django.shortcuts import render
from django.views.generic import TemplateView, View
from django.http import HttpRequest, HttpResponseRedirect
from .models import InfoModel, SkillModel, CommentModels, StatsModel, EducationModel, WorkExperience, AttributeModel, \
    PortfolioCategoryModel, PortfolioModel, NewsLetterModel
from django.urls import reverse_lazy
from django.core.validators import validate_email
from django.core.exceptions import ValidationError

from django.contrib import messages

class HomeView(View):
    def get(self, request: HttpRequest):
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
            "info": info,
            "skills": skills,
            "comments": comments,
            "stats": stats,
            "educations": educations,
            "experiences": experiences,
            "attributes": attributes,
            "portfolio_cats": portfolio_cats,
            "portfolios": portfolios
        })

    def post(self, request: HttpRequest):
        # use for newsletter
        email = request.POST.get("email")

        try:
            validate_email(email)
            db_email = NewsLetterModel.objects.filter(email=email)

            if not db_email.exists():
                NewsLetterModel.objects.create(email=email)
                messages.success(request, "ایمیل شما ثبت شد")
                return HttpResponseRedirect(reverse_lazy("home_url"))

            else:
                messages.error(request, "این ایمیل قبلا در خبرنامه ثبت شده است")
                return HttpResponseRedirect(reverse_lazy("home_url"))

        except ValidationError:
            messages.error(request, "ایمیل شما نامعتبر است")
            return HttpResponseRedirect(reverse_lazy("home_url"))

