from django.conf import settings
from rest_framework.routers import DefaultRouter


class Router(DefaultRouter):
    include_root_view = settings.DEBUG
    include_format_suffixes = False

    def __init__(self, leading_slash=True, trailing_slash=False):
        if leading_slash:
            self.routes = self.routes.copy()
            for i in range(len(self.routes)):
                new_url = self.routes[i].url.replace('^', '^/')
                self.routes[i] = self.routes[i]._replace(url=new_url)
        super().__init__(trailing_slash=trailing_slash)
