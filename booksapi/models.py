from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField('Nomi',max_length=50)
    author = models.CharField(verbose_name='Muallif',max_length=50)
    snippet = models.CharField(verbose_name='Qisqacha',max_length=512)
    description = models.TextField(verbose_name='Malumot')
    images = models.ImageField(verbose_name='Rasm', upload_to='images/')
    language = models.CharField(max_length=50, verbose_name='Til', null=True, blank=True)
    shirft = models.CharField(max_length=20, verbose_name='Yozuv', null=True, blank=True)
    category = models.ManyToManyField(Category, related_name='book', verbose_name='Toifa')

    def __str__(self):
        return self.title

class Comment(models.Model):
    book = models.ForeignKey(Book,on_delete=models.CASCADE,related_name='comment',verbose_name='Kitob')
    name = models.CharField('Ism',max_length=50)
    text = models.TextField(verbose_name='Fikr')
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return f"{self.name}, {self.book}"

class BookSource(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='source')
    name = models.CharField(max_length=100, verbose_name='Dokon Nomi/Brendi')
    url = models.URLField(verbose_name='URL Manzil')
    cost = models.DecimalField(max_digits=9, decimal_places=2, verbose_name="Narxi (So'mda)")


class BookReview(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='review')
    name = models.CharField(max_length=100, verbose_name='Ism')
    job = models.CharField(max_length=250, verbose_name='Kasbi/Ishi qisqacha')
    retext = models.TextField(verbose_name='Matn')

