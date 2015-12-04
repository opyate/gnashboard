from flask.ext.sandboy import Sandboy

from .foo import Foo
from .basket import Basket
from .page import Page
from .kv import KV


class APIScaffold(object):
    def init_app(self, app, db, auth=None):
        decorators = [auth.login_required]
        sandboy = Sandboy(
            app, db,
            [Foo, Basket, Page, KV],
            decorators=decorators)
        return sandboy
