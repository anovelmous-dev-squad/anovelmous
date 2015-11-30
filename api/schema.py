import graphene
from graphene import resolve_only_args, relay
from graphene.contrib.django import DjangoNode
from graphql_relay.node.node import from_global_id

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
    text = graphene.String()

    def resolve_text(self, *args):
        return ' '.join(models.FormattedNovelToken.objects.filter(chapter=self.instance).values_list('content', flat=True))

    def resolve_tokens(self, *args):
        return self.instance.tokens.all()

    class Meta:
        model = models.Chapter

    connection_type = Connection


class Novel(DjangoNode):
    latest_chapter = graphene.Field(Chapter)
    vocabulary = relay.ConnectionField(VocabTerm)

    def resolve_vocabulary(self, *args):
        return models.Token.objects.all() # Eventually add filter based on Novel

    def resolve_latest_chapter(self, *args):
        return self.instance.chapters.last()

    def resolve_chapters(self, *args):
        return self.instance.chapters.all()

    def resolve_places(self, *args):
        return self.instance.places.all()

    def resolve_characters(self, *args):
        return self.instance.characters.all()

    def resolve_plot_items(self, *args):
        return self.instance.plot_items.all()

    def resolve_proposed_plots(self, *args):
        return self.instance.proposed_plots.all()

    def resolve_proposed_places(self, *args):
        return self.instance.proposed_places.all()

    def resolve_proposed_characters(self, *args):
        return self.instance.proposed_characters.all()

    def resolve_proposed_plotitems(self, *args):
        return self.instance.proposed_plotitems.all()

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

    def resolve_plotitems(self, *args):
        return self.instance.plotitems.all()

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


class CastVote(relay.ClientIDMutation):
    class Input:
        resource_id = graphene.String(required=True)
        chapter_id = graphene.String(required=True)
        ordinal = graphene.Int(required=True)
        contributor_id = graphene.String(required=True)

    vote = graphene.Field(Vote)
    contributor = graphene.Field(Contributor)

    @classmethod
    def mutate_and_get_payload(cls, input, info):
        resource_id = input.get('resource_id')
        chapter_id = input.get('chapter_id')
        ordinal = input.get('ordinal')
        contributor_id = input.get('contributor_id')

        res_global = from_global_id(resource_id)
        res_global_type = res_global.type
        resource, relation_name = None, None
        if (res_global_type == 'VocabTerm'):
            relation_name = 'token'
            resource = models.Token.objects.get(id=res_global.id)
        elif (res_global_type == 'Place'):
            relation_name = 'place'
            resource = models.Place.objects.get(id=res_global.id)
        elif (res_global_type == 'Character'):
            relation_name = 'character'
            resource = models.Character.objects.get(id=res_global.id)
        elif (res_global_type == 'PlotItem'):
            relation_name = 'plot_item'
            resource = models.PlotItem.objects.get(id=res_global.id)

        chapter = models.Chapter.objects.get(id=from_global_id(chapter_id).id)
        contributor = models.Contributor.objects.get(id=from_global_id(contributor_id).id)
        createArgs = {'ordinal': ordinal, 'chapter': chapter, 'contributor': contributor}
        createArgs[relation_name] = resource

        vote = models.Vote.objects.create(**createArgs)
        return CastVote(vote=vote, contributor=contributor)


class CreatePlot(relay.ClientIDMutation):
    class Input:
        summary = graphene.String(required=True)
        novel_id = graphene.String(required=True)
        contributor_id = graphene.String(required=True)

    plot = graphene.Field(Plot)

    @classmethod
    def mutate_and_get_payload(cls, input, info):
        summary = input.get('summary')
        novel_id = input.get('novel_id')
        contributor_id = input.get('contributor_id')

        contributor = models.Contributor.objects.get(id=from_global_id(contributor_id).id)
        novel = models.Novel.objects.get(id=from_global_id(novel_id).id)

        plot = models.Plot.objects.create(
            summary=summary,
            novel=novel,
            contributor=contributor
        )

        return CreatePlot(plot=plot)


class CreateCharacter(relay.ClientIDMutation):
    class Input:
        first_name = graphene.String(required=True)
        last_name = graphene.String()
        bio = graphene.String(required=True)
        novel_id = graphene.String(required=True)
        contributor_id = graphene.String(required=True)

    character = graphene.Field(Character)

    @classmethod
    def mutate_and_get_payload(cls, input, info):
        first_name = input.get('first_name')
        last_name = input.get('last_name', '')
        bio = input.get('bio')
        novel_id = input.get('novel_id')
        contributor_id = input.get('contributor_id')

        contributor = models.Contributor.objects.get(id=from_global_id(contributor_id).id)
        novel = models.Novel.objects.get(id=from_global_id(novel_id).id)

        character = models.Character.objects.create(
            first_name=first_name,
            last_name=last_name,
            bio=bio,
            novel=novel,
            contributor=contributor
        )

        return CreateCharacter(character=character)


class CreatePlace(relay.ClientIDMutation):
    class Input:
        name = graphene.String(required=True)
        description = graphene.String(required=True)
        novel_id = graphene.String(required=True)
        contributor_id = graphene.String(required=True)

    place = graphene.Field(Place)

    @classmethod
    def mutate_and_get_payload(cls, input, info):
        name = input.get('name')
        description = input.get('description')
        novel_id = input.get('novel_id')
        contributor_id = input.get('contributor_id')

        contributor = models.Contributor.objects.get(id=from_global_id(contributor_id).id)
        novel = models.Novel.objects.get(id=from_global_id(novel_id).id)

        place = models.Place.objects.create(
            name=name,
            description=description,
            novel=novel,
            contributor=contributor
        )

        return CreatePlace(place=place)


class CreatePlotItem(relay.ClientIDMutation):
    class Input:
        name = graphene.String(required=True)
        description = graphene.String(required=True)
        novel_id = graphene.String(required=True)
        contributor_id = graphene.String(required=True)

    plot_item = graphene.Field(PlotItem)

    @classmethod
    def mutate_and_get_payload(cls, input, info):
        name = input.get('name')
        description = input.get('description')
        novel_id = input.get('novel_id')
        contributor_id = input.get('contributor_id')

        contributor = models.Contributor.objects.get(id=from_global_id(contributor_id).id)
        novel = models.Novel.objects.get(id=from_global_id(novel_id).id)

        plot_item = models.PlotItem.objects.create(
            name=name,
            description=description,
            novel=novel,
            contributor=contributor
        )

        return CreatePlotItem(plot_item=plot_item)


class Mutation(graphene.ObjectType):
    cast_vote = graphene.Field(CastVote)
    create_plot = graphene.Field(CreatePlot)
    create_character = graphene.Field(CreateCharacter)
    create_place = graphene.Field(CreatePlace)
    create_plot_item = graphene.Field(CreatePlotItem)

schema.query = Query
schema.mutation = Mutation


import json

introspection_dict = schema.introspect()

print(json.dumps(introspection_dict))
