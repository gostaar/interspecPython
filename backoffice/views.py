from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, ListView

from backoffice.models import Adherent, Emprunt


# Create your views here.

def HomePageView(request):
    adherents = Adherent.objects.all()
    template_name = 'home.html'
    dernier_Emprunt_list = Emprunt.objects.all()[:5]
    context = {'adherents': adherents, 'dernier_Emprunt_list': dernier_Emprunt_list}
    return render(request, template_name, context)

class SearchResultsView(ListView):
    model = Adherent
    template_name = 'search_results.html'

    def get_queryset(self):
        query = self.request.GET.get("q")
        object_list = Adherent.objects.filter(Q(nom__icontains=query) | Q(prenom__icontains=query))
        return object_list

def detail(request, emprunt_id):
    emp = get_object_or_404(Emprunt, pk=emprunt_id)
    context = {'emp': emp}
    template_name = "emprunt_detail.html"
    return render(request, template_name, context)