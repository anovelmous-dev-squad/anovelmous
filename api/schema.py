import graphene
from graphene import resolve_only_args, relay
from graphene.contrib.django import DjangoNode

from . import models
from datetime import datetime

schema = graphene.Schema(name='Anovelmous Schema')

class Connection(relay.Connection):
    total_count = graphene.Int()

    def resolve_total_count(self, args, info):
        return len(self.get_connection_data())


class VocabTerm(DjangoNode):
    class Meta:
        model = models.Token

    connection_type = Connection

class Token(DjangoNode):
    class Meta:
        model = models.NovelToken

    connection_type = Connection


class Chapter(DjangoNode):
    vocabulary = relay.ConnectionField(VocabTerm)

    def resolve_vocabulary(self, *args):
        return models.Token.objects.all() # Eventually add filter based on chapter

    def resolve_tokens(self, *args):
        return self.instance.tokens.all()

    class Meta:
        model = models.Chapter

    connection_type = Connection


class Novel(DjangoNode):
    latest_chapter = graphene.Field(Chapter)

    def resolve_latest_chapter(self, *args):
        return self.instance.chapters.last()

    def resolve_chapters(self, *args):
        return self.instance.chapters.all()

    class Meta:
        model = models.Novel

    connection_type = Connection


class Vote(DjangoNode):
    class Meta:
        model = models.Vote

    connection_type = Connection


class Stage(DjangoNode):
    class Meta:
        model = models.Stage

    connection_type = Connection


class Plot(DjangoNode):
    class Meta:
        model = models.Plot

    connection_type = Connection


class Place(DjangoNode):
    class Meta:
        model = models.Place

    connection_type = Connection


class PlotItem(DjangoNode):
    class Meta:
        model = models.PlotItem

    connection_type = Connection


class Character(DjangoNode):
    class Meta:
        model = models.Character

    connection_type = Connection


class Contributor(DjangoNode):

    def resolve_votes(self, *args):
        return self.instance.votes.all()

    def resolve_plots(self, *args):
        return self.instance.plots.all()

    def resolve_places(self, *args):
        return self.instance.places.all()

    def resolve_plot_items(self, *args):
        return self.instance.plot_items.all()

    def resolve_characters(self, *args):
        return self.instance.characters.all()

    class Meta:
        model = models.Contributor

    connection_type = Connection


class Query(graphene.ObjectType):
    contributors = relay.ConnectionField(Contributor)
    vocabulary = relay.ConnectionField(VocabTerm)
    novels = relay.ConnectionField(Novel)
    chapters = relay.ConnectionField(Chapter)
    tokens = relay.ConnectionField(Token)
    votes = relay.ConnectionField(Vote)
    stages = relay.ConnectionField(Stage)
    plots = relay.ConnectionField(Plot)
    places = relay.ConnectionField(Place)
    plot_items = relay.ConnectionField(PlotItem)
    characters = relay.ConnectionField(Character)

    contributor = relay.NodeField(Contributor)
    vocab_term = relay.NodeField(VocabTerm)
    novel = relay.NodeField(Novel)
    chapter = relay.NodeField(Chapter)
    token = relay.NodeField(Token)
    vote = relay.NodeField(Vote)
    stage = relay.NodeField(Stage)
    plot = relay.NodeField(Plot)
    place = relay.NodeField(Place)
    plot_item = relay.NodeField(PlotItem)
    character = relay.NodeField(Character)
    node = relay.NodeField()
    viewer = graphene.Field('self')

    @resolve_only_args
    def resolve_contributors(self, **kwargs):
        return models.Contributor.objects.all()

    @resolve_only_args
    def resolve_vocabulary(self, **kwargs):
        return models.Token.objects.all()

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

    @resolve_only_args
    def resolve_characters(self, **kwargs):
        return models.Character.objects.all()

    def resolve_viewer(self, *args, **kwargs):
        return self

schema.query = Query


import json

introspection_dict = schema.introspect()

print(json.dumps(introspection_dict))
