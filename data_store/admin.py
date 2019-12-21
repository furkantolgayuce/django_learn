from django.contrib import admin

from .models import DataStore
# Register your models here.

# DataStore uygulamamızın admin panelinde görünmesi ve içerisinde
# Çeşitli özelleştirmelerin yapılabilmesi için bu sayfayı kullanacağız.

@admin.register(DataStore)

class DataStoreAdmin(admin.ModelAdmin):

	# Admin panelinde uygulamamdaki sütunlarda hangi bilgilerin gösterileceği.
	list_display = ["title", "created_date"]

	# Admin panelinde uygulama içerisinde hangi bilgilere göre arama yapılabileceği.
	search_fields=["title"]

	# Admin panelinde uygulama içerisinde hangi bilgilere göre filtreleme yapılabileceği.
	list_filter=["created_date","author"]	

	# Yukarıdaki DataStore'u burada bu class ile bağladık.
	class Meta:
		model = DataStore
