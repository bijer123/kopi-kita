from django.shortcuts import render, redirect, get_object_or_404
from .models import Kopi
from .forms import KopiForm
from django.contrib.auth.decorators import login_required

def tambah_data_kopi_awal():
    if Kopi.objects.count() == 0:
        Kopi.objects.create(
            nama="Kopi Arabika",
            asal="Toraja",
            harga=25000,
            deskripsi="Kopi arabika khas Toraja dengan aroma floral dan rasa asam yang halus."
        )
        Kopi.objects.create(
            nama="Kopi Robusta",
            asal="Lampung",
            harga=18000,
            deskripsi="Kopi robusta dengan rasa pahit kuat dan kandungan kafein tinggi."
        )
        Kopi.objects.create(
            nama="Kopi Gayo",
            asal="Aceh",
            harga=30000,
            deskripsi="Kopi organik dengan karakter kompleks dan aroma rempah dari dataran tinggi Gayo."
        )
        Kopi.objects.create(
            nama="Espresso",
            asal="Italia",
            harga=22000,
            deskripsi="Kopi pekat dan intens yang diseduh dengan tekanan tinggi."
        )
        Kopi.objects.create(
            nama="Kopi Tubruk",
            asal="Jawa",
            harga=12000,
            deskripsi="Kopi tradisional Indonesia tanpa saringan dengan ampas di bawah cangkir."
        )

def index(request):
    tambah_data_kopi_awal()
    daftar_kopi = Kopi.objects.all()
    return render(request, 'katalog/index.html', {'daftar_kopi': daftar_kopi})

def detail_kopi(request, pk):
    kopi = get_object_or_404(Kopi, pk=pk)
    return render(request, 'katalog/detail_kopi.html', {'kopi': kopi})

@login_required
def tambah_kopi(request):
    form = KopiForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'katalog/tambah_kopi.html', {'form': form})

@login_required
def edit_kopi(request, pk):
    kopi = get_object_or_404(Kopi, pk=pk)
    form = KopiForm(request.POST or None, request.FILES or None, instance=kopi)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'katalog/edit_kopi.html', {'form': form})

@login_required
def hapus_kopi(request, pk):
    kopi = get_object_or_404(Kopi, pk=pk)
    kopi.delete()
    return redirect('/')