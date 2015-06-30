from django.contrib import admin
from .models import Novel, Chapter, Token, NovelToken, FormattedNovelToken, Vote, Contributor, Guild

admin.site.register(Novel)
admin.site.register(Chapter)
admin.site.register(Token)
admin.site.register(NovelToken)
admin.site.register(FormattedNovelToken)
admin.site.register(Vote)
admin.site.register(Contributor)
admin.site.register(Guild)
