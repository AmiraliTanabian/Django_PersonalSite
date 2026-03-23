from django.contrib import admin
from .models import InfoModel, SkillModel, CommentModels, StatsModel, EducationModel, WorkExperience, AttributeModel, \
    PortfolioCategoryModel, PortfolioModel, NewsLetterModel, ServicesModel, CVModel

admin.site.register(InfoModel)
admin.site.register(SkillModel)
admin.site.register(CommentModels)
admin.site.register(StatsModel)
admin.site.register(EducationModel)
admin.site.register(WorkExperience)
admin.site.register(AttributeModel)
admin.site.register(PortfolioCategoryModel)
admin.site.register(PortfolioModel)
admin.site.register(NewsLetterModel)
admin.site.register(ServicesModel)
admin.site.register(CVModel)
