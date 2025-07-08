from django.db import models

class Kopi(models.Model):
    nama = models.CharField(max_length=100)
    asal = models.CharField(max_length=100)
    deskripsi = models.TextField()
    harga = models.DecimalField(max_digits=8, decimal_places=2)

    gambar = models.ImageField(upload_to='gambar_kopi/', blank=True, null=True)  # Tambahan

    def __str__(self):
        return self.nama

