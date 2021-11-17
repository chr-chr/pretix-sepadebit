from django.conf.urls import re_path

from . import views

urlpatterns = [
    re_path(r'^control/organizer/(?P<organizer>[^/]+)/sepa/exports/$', views.OrganizerExportListView.as_view(),
        name='export'),
    re_path(r'^control/organizer/(?P<organizer>[^/]+)/sepa/exports/(?P<id>\d+).xml$', views.OrganizerDownloadView.as_view(),
        name='download'),
    re_path(r'^control/organizer/(?P<organizer>[^/]+)/sepa/exports/(?P<id>\d+)/orders/$',
        views.OrganizerOrdersView.as_view(),
        name='orders'),

    re_path(r'^control/event/(?P<organizer>[^/]+)/(?P<event>[^/]+)/sepa/exports/$', views.EventExportListView.as_view(),
        name='export'),
    re_path(r'^control/event/(?P<organizer>[^/]+)/(?P<event>[^/]+)/sepa/exports/(?P<id>\d+).xml$', views.EventDownloadView.as_view(),
        name='download'),
    re_path(r'^control/event/(?P<organizer>[^/]+)/(?P<event>[^/]+)/sepa/exports/(?P<id>\d+)/orders/$',
        views.EventOrdersView.as_view(),
        name='orders'),
]
