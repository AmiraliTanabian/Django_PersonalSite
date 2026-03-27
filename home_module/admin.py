from django.contrib import admin
from .models import InfoModel, SkillModel, CommentModels, StatsModel, EducationModel, WorkExperience, AttributeModel, \
    PortfolioCategoryModel, PortfolioModel, NewsLetterModel, ServicesModel, CVModel, SkillLogoModel


class CVAdminClass(admin.ModelAdmin):
    list_display = ["is_active", "__str__"]
    list_filter = ["is_active"]
    list_editable = ["is_active"]
    list_display_links = ["__str__"]

class PortfolioAdmin(admin.ModelAdmin):
    list_display = ["title", "url", "banner", "category"]
    list_filter = ["category"]


admin.site.register(InfoModel)
admin.site.register(SkillModel)
admin.site.register(CommentModels)
admin.site.register(StatsModel)
admin.site.register(EducationModel)
admin.site.register(WorkExperience)
admin.site.register(AttributeModel)
admin.site.register(PortfolioCategoryModel)
admin.site.register(PortfolioModel, PortfolioAdmin)
admin.site.register(NewsLetterModel)
admin.site.register(ServicesModel)
admin.site.register(CVModel, CVAdminClass)
admin.site.register(SkillLogoModel)
