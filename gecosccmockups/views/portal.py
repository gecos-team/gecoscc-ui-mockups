from pyramid.httpexceptions import HTTPFound

from pyramid.view import view_config

from . import BaseView


@view_config(route_name='home', renderer='templates/home.jinja2')
def home(context, request):
    return {}


@view_config(route_name='admins', renderer='templates/admins.jinja2')
def admins(context, request):
    return {}


@view_config(route_name='groups', renderer='templates/groups.jinja2')
def groups(context, request):
    return {}


@view_config(route_name='reports', renderer='templates/reports.jinja2')
def reports(context, request):
    return {}


#;;;;;;;;;;;
# TO DELETE
#;;;;;;;;;;;
@view_config(route_name='users', renderer='templates/users.jinja2')
def users(context, request):
    return {}


@view_config(route_name='ous', renderer='templates/ous.jinja2')
def ous(context, request):
    return {}


@view_config(route_name='policies_wallpaper', renderer='templates/policies-wallpaper.jinja2')
def policies_wallpaper(context, request):
    return {}


@view_config(route_name='policies_software', renderer='templates/policies-software.jinja2')
def policies_software(context, request):
    return {}


@view_config(route_name='policies_storage', renderer='templates/policies-storage.jinja2')
def policies_storage(context, request):
    return {}


@view_config(route_name='computers', renderer='templates/computers.jinja2')
def computers(context, request):
    return {}


@view_config(route_name='printers', renderer='templates/printers.jinja2')
def printers(context, request):
    return {}


class LoginViews(BaseView):

    @view_config(route_name='login', renderer='templates/login.jinja2')
    def login(self):
        if self.request.POST:
            return HTTPFound(location=self.request.route_path('home'))

    @view_config(route_name='logout')
    def logout(self):
        return HTTPFound(location=self.request.route_path('login'))
