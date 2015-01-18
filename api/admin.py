from django.contrib import admin
from api.models import Novel, Chapter, Token, NovelToken, FormattedNovelToken

admin.register(Novel)
admin.register(Chapter)
admin.register(Token)
admin.register(NovelToken)
admin.register(FormattedNovelToken)
