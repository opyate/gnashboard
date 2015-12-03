# -*- coding: utf-8 -*-
from factory import Sequence, PostGenerationMethodCall
from factory.alchemy import SQLAlchemyModelFactory

from application.models.foo import Foo
from application.extensions import db


class BaseFactory(SQLAlchemyModelFactory):

    class Meta:
        abstract = True
        sqlalchemy_session = db.session


class FooFactory(BaseFactory):
    bar = Sequence(lambda n: n)
    baz = Sequence(lambda n: 'baz-%s' % n)

    class Meta:
        model = Foo
