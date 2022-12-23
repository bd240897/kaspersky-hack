from django.views.generic import TemplateView


class QuickStartView(TemplateView):

    template_name = "viewer/quick_start.html"