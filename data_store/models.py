from django.db import models

# ckeditor'ü kullanmak için.
from ckeditor.fields import RichTextField
# Create your models here.

class DataStore(models.Model):

	author = models.ForeignKey(
		"auth.User",
		models.SET_NULL,
		blank = True,
		null = True,
		verbose_name = "Girişi Yapan Kullanıcı" #Admin panelinde hangi isim ile görüneceği
		)

	title = models.CharField(
		max_length= 100,
		verbose_name = "Veri Adı"
		)

	description = RichTextField(
		verbose_name = "Verinin Tanımı"
		)
	
	created_date = models.DateTimeField(
		auto_now_add=True,
		verbose_name = "Oluşturulma Tarihi"
		)

	data_file = models.FileField(
		blank = True,
		null = True,
		verbose_name = "Veri Dosyasını ekleyin."
	)

	# Bu fonksiyon ile admin panelinde hangi isim ile listeleneceği.
	def __str__(self):
		return(self.title) # Yukarıdaki title değişkeni ile listelenecek.