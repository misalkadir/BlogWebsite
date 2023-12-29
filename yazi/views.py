from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from .models import Yazi, Yorum
from .forms import yaziEkleForm

# Create your views here.

def yazi_view(request, slug):
    yazimiz = Yazi.objects.get(slug=slug)
    yorumlar = Yorum.objects.filter(yazi=yazimiz)

    benzerYazilar = Yazi.objects.filter(kategori=yazimiz.kategori)[0:3]

    yazimiz.goruntulenmeSayisi += 1
    yazimiz.save()

    return render(request, "yazi/yaziDetay.html", {"yazi": yazimiz,
                                                   "yorumlar": yorumlar, "benzerYazilar": benzerYazilar})

def yaziEkle_view(request):
    form = yaziEkleForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()

        yazimiz = Yazi.objects.latest("id")

        return HttpResponseRedirect("/yazi/" + yazimiz.slug)

    return render(request, "yazi/yaziEkle.html", {"form": form})

def yorumEkle_view(request):
    metin = request.GET.get("yorumMetin")
    yaziId = request.GET.get("yaziId")

    if metin and yaziId:
        yazimiz = get_object_or_404(Yazi, id=yaziId)
        Yorum.objects.create(metin=metin, yazi=yazimiz)

        return HttpResponseRedirect("/yazi/" + yazimiz.slug)

def begen_view(request, id):
    yazimiz = Yazi.objects.get(id=id)
    yazimiz.begeniSayisi += 1
    yazimiz.save()

    return HttpResponseRedirect("/yazi/" + yazimiz.slug)