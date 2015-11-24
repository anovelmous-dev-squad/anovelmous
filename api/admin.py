from django.contrib import admin
from .models import (
    Novel,
    Chapter,
    Token,
    NovelToken,
    FormattedNovelToken,
    Vote,
    Contributor,
    Guild,
    Stage,
    Plot,
    Place,
    PlotItem,
    Character
)

admin.site.register(Novel)
admin.site.register(Chapter)
admin.site.register(Token)
admin.site.register(NovelToken)
admin.site.register(FormattedNovelToken)
admin.site.register(Vote)
admin.site.register(Contributor)
admin.site.register(Guild)
admin.site.register(Stage)
admin.site.register(Plot)
admin.site.register(Place)
admin.site.register(PlotItem)
admin.site.register(Character)
