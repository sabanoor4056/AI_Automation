from django.urls import path
from . import views


urlpatterns = [

    path("", views.home, name="home"),

    path("dashboard/", views.dashboard, name="dashboard"),

    path("chatboard/", views.chatboard, name="chatboard"),

    path("leads/", views.leads, name="leads"),
    path("automations/", views.automations, name="automations"),
path("automations/create/", views.create_automation, name="create_automation"),
path('leads/add/', views.add_lead, name='add_lead'),
path('leads/<int:lead_id>/', views.view_lead, name='view_lead'),
path('leads/<int:lead_id>/edit/', views.edit_lead, name='edit_lead'),
path('leads/<int:lead_id>/delete/', views.delete_lead, name='delete_lead'),

    path(
        "leads/generate/",
        views.generate_leads,
        name="generate_leads"
    ),

    path(
        "automations/",
        views.automations,
        name="automations"
    ),

    path(
        "automations/create/",
        views.create_automation,
        name="create_automation"
    ),

    path("analytics/", views.analytics, name="analytics"),

    path("projects/", views.projects, name="projects"),
    path("chatboard/", views.chatboard, name="chatboard"),

    path(
        "settings/",
        views.settings_page,
        name="settings"
    ),
]

