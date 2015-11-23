import graphene
from graphene import resolve_only_args, relay
from graphene.contrib.django import DjangoNode, DjangoConnectionField

from . import models

schema = graphene.Schema(name='Anovelmous Schema')


class Contributor(DjangoNode):
    class Meta:
        model = models.Contributor

class Novel(DjangoNode):
    class Meta:
        model = models.Novel

class Chapter(DjangoNode):
    class Meta:
        model = models.Chapter

class Token(DjangoNode):
    class Meta:
        model = models.NovelToken

class Vote(DjangoNode):
    class Meta:
        model = models.Vote

class Stage(DjangoNode):
    class Meta:
        model = models.Stage

class Plot(DjangoNode):
    class Meta:
        model = models.Plot

class Place(DjangoNode):
    class Meta:
        model = models.Place

class PlotItem(DjangoNode):
    class Meta:
        model = models.PlotItem

class Query(graphene.ObjectType):
    contributors = relay.ConnectionField(Contributor)
    novels = relay.ConnectionField(Novel)
    chapters = relay.ConnectionField(Chapter)
    tokens = relay.ConnectionField(Token)
    votes = relay.ConnectionField(Vote)
    stages = relay.ConnectionField(Stage)
    plots = relay.ConnectionField(Plot)
    places = relay.ConnectionField(Place)
    plot_items = relay.ConnectionField(PlotItem)

    contributor = relay.NodeField(Contributor)
    novel = relay.NodeField(Novel)
    chapter = relay.NodeField(Chapter)
    token = relay.NodeField(Token)
    vote = relay.NodeField(Vote)
    stage = relay.NodeField(Stage)
    plot = relay.NodeField(Plot)
    place = relay.NodeField(Place)
    plot_item = relay.NodeField(PlotItem)
    node = relay.NodeField()
    viewer = graphene.Field('self')

    @resolve_only_args
    def resolve_contributors(self, **kwargs):
        return models.Contributor.objects.all()

    @resolve_only_args
    def resolve_novels(self, **kwargs):
        return models.Novel.objects.all()

    @resolve_only_args
    def resolve_chapters(self, **kwargs):
        return models.Chapter.objects.all()

    @resolve_only_args
    def resolve_tokens(self, **kwargs):
        return models.Token.objects.all()

    @resolve_only_args
    def resolve_votes(self, **kwargs):
        return models.Vote.objects.all()

    @resolve_only_args
    def resolve_stages(self, **kwargs):
        return models.Stage.objects.all()

    @resolve_only_args
    def resolve_plots(self, **kwargs):
        return models.Plot.objects.all()

    @resolve_only_args
    def resolve_places(self, **kwargs):
        return models.Place.objects.all()

    @resolve_only_args
    def resolve_plot_items(self, **kwargs):
        return models.PlotItem.objects.all()

    def resolve_viewer(self, *args, **kwargs):
        return self

schema.query = Query
