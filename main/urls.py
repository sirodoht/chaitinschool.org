from django.urls import path

from main import views

urlpatterns = [
    path("", views.index, name="index"),
    path("feedback/", views.FeedbackView.as_view(), name="feedback"),
    path("subscribe/", views.subscribe, name="subscribe"),
    path("code-of-conduct/", views.coc, name="coc"),
    path("events/", views.WorkshopList.as_view(), name="workshop_list"),
    path(
        "workshops/<slug:slug>/",
        views.AttendanceView.as_view(),
        name="workshop",
    ),
    path(
        "workshops/<slug:slug>/ics/",
        views.workshop_ics,
        name="workshop_ics",
    ),
    path(
        "workshops/<slug:slug>/announce/",
        views.AnnounceView.as_view(),
        name="announce",
    ),
    path("blog/", views.BlogView.as_view(), name="blog"),
    path("blog/<slug:slug>/", views.PostView.as_view(), name="post"),
    path(
        "broadcast/",
        views.Broadcast.as_view(),
        name="broadcast",
    ),
    path(
        "unsubscribe/<uuid:key>/",
        views.unsubscribe_key,
        name="unsubscribe_key",
    ),
]
