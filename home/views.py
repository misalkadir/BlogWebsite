from django.shortcuts import render
from yazi.models import Yazi
from kategori.models import kategori
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

# Create your views here.


def home_view(request):
    yazilarListe = Yazi.objects.all()
    kategoriler = kategori.objects.all()

    paginator = Paginator(yazilarListe, 3)
    page = request.GET.get('sayfa')
    yazilar = paginator.get_page(page)

    return render(request, "index.html", {"yazilar": yazilar, "kategoriler": kategoriler})

def search_view(request):
    query = request.GET.get("query")
    yazilar = Yazi.objects.filter(başlık__contains=query)

    return render(request, "search.html", {"yazilar": yazilar})