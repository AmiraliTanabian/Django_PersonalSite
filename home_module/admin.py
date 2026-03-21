from django.contrib import admin
from .models import InfoModel,SkillModel, CommentModels, StatsModel,EducationModel

admin.site.register(InfoModel)
admin.site.register(SkillModel)
admin.site.register(CommentModels)
admin.site.register(StatsModel)
admin.site.register(EducationModel)