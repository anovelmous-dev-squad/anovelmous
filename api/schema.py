import graphene
from graphene import resolve_only_args, relay
from graphene.contrib.django import (
    DjangoObjectType,
    DjangoNode
)

from .models import (
    Contributor as ContributorModel,
    Novel as NovelModel,
    Chapter as ChapterModel,
    Token as TokenModel,
    Vote as VoteModel,
    Stage as StageModel,
    Plot as PlotModel,
    Character as CharacterModel,
    Place as PlaceModel,
    PlotItem as PlotItemModel
)

from .data import (
    getViewer,
    getContributor,
    getNovel,
    getChapter,
    getToken
)

schema = graphene.Schema(name='Anovelmous Schema')


class Contributor(DjangoNode):
    class Meta:
        model = ContributorModel

    def get_node(cls, id):
        return Contributor(getContributor(id))


class Novel(DjangoNode):
    class Meta:
        model = NovelModel

    @classmethod
    def get_node(cls, id):
        return Novel(getNovel(id))



class Chapter(DjangoNode):
    class Meta:
        model = ChapterModel

    @classmethod
    def get_node(cls, id):
        return Chapter(getChapter(id))


class Token(DjangoNode):
    class Meta:
        model = TokenModel

    @classmethod
    def get_node(cls, id):
        return Token(getToken(id))


class Query(graphene.ObjectType):
    viewer = graphene.Field(Contributor)
    node = relay.NodeField()

    @resolve_only_args
    def resolve_viewer(self):
        return Contributor(getViewer())

schema.query = Query
