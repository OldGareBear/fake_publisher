from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls import patterns, url, include
from django.views.generic import TemplateView

urlpatterns = patterns('',
    (r'^sourdough_popsicles/', TemplateView.as_view(template_name="sourdough_popsicles.html")),
    (r'^mushrooms/', TemplateView.as_view(template_name="mushrooms.html")),
    (r'^veggie_burgers/', TemplateView.as_view(template_name="veggie_burgers.html")),
    (r'^hill/', TemplateView.as_view(template_name="hill.html")),
    (r'winter_fresh_gum_medley', TemplateView.as_view(template_name="winter_fresh_gum_medley.html"))
)