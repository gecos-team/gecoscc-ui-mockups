import os

from pyramid.config import Configurator
from .models import get_root


def read_setting_from_env(settings, key, default=None):
    env_variable = key.upper()
    if env_variable in os.environ:
        return os.environ[env_variable]
    else:
        return settings.get(key, default)


def route_config(config):
    config.add_static_view('static', 'static')
    config.add_route('admins', '/admins/')
    config.add_route('groups', '/groups/')
    config.add_route('reports', '/reports/')
    config.add_route('login', '/login/')
    config.add_route('logout', 'logout/')

    config.add_route('home', '/')
    config.add_route('users', '/users/')
    config.add_route('ous', '/ous/')
    config.add_route('policies_wallpaper', '/ous/policies-wallpaper/')
    config.add_route('policies_software', '/ous/policies-software/')
    config.add_route('policies_storage', '/ous/policies-storage/')
    config.add_route('computers', '/computers/')
    config.add_route('printers', '/printers/')


def jinja2_config(config):
    settings = config.registry.settings
    settings.setdefault('jinja2.i18n.domain', 'gecoscc')
    settings.setdefault('jinja2.newstyle', True)

    settings.setdefault('jinja2.extensions', ['jinja2.ext.with_'])

    settings.setdefault('jinja2.directories', 'gecoscc:templates')
    settings.setdefault('jinja2.undefined', 'strict')
    settings.setdefault('jinja2.filters', """
        route_url = pyramid_jinja2.filters:route_url_filter
        static_url = pyramid_jinja2.filters:static_url_filter
    """)


def main(global_config, **settings):
    """ This function returns a WSGI application.
    """
    settings = dict(settings)

    config = Configurator(root_factory=get_root, settings=settings)

    config.add_translation_dirs('locale/')

    jinja2_config(config)

    config.include('pyramid_jinja2')

    route_config(config)

    config.scan('gecosccmockups.views')

    return config.make_wsgi_app()
