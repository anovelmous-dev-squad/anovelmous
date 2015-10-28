from .models import Contributor, Novel, Chapter, Token, Vote, Stage, Plot, Character, Place, PlotItem

def getViewer():
    return Contributor.objects.first()

def getContributor(_id):
    return Contributor.objects.get(_id)

def getNovel(_id):
    return Novel.objects.get(_id)

def getChapter(_id):
    return Chapter.objects.get(_id)

def getToken(_id):
    return Token.objects.get(_id)

def getVote(_id):
    return Vote.objects.get(_id)

def getStage(_id):
    return Stage.objects.get(_id)

def getPlot(_id):
    return Plot.objects.get(_id)

def getCharacter(_id):
    return Character.objects.get(_id)

def getPlace(_id):
    return Place.objects.get(_id)

def getPlotItem(_id):
    return PlotItem.objects.get(_id)
