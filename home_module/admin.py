from django.contrib import admin
from .models import InfoModel,SkillModel, CommentModels, StatsModel

admin.site.register(InfoModel)
admin.site.register(SkillModel)
admin.site.register(CommentModels)
admin.site.register(StatsModel)