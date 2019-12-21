# Django Rehberi

## Projeyi Çalıştırmak İçin

```terminal
git clone https://github.com/furkantolgayuce/django_learn.git && cd django_learn && python3 manage.py runserver
```

## Kurulum ve İlk Adımlar

### Django projemizi oluşturmak için.

```terminal
django-admin startproject proje_adi
```

### Projemizi Başlatmak için.

```terminal
python3 manage.py runserver
```

### SQL değişikliklerini yapmak

SQL değişikliklerini uygulamak için

```terminal
python3 manage.py migrate
```

### Models.py dosyasındaki değişiklikler için

models.py dosyasında değişiklik yaptığımızda öncelikle,

```terminal
python3 manage.py makemigrations
```

ardından 

```terminal
python3 manage.py migrate
```

komutunu vererek değişiklikleri sql içerisine yazdırmalıyız.

### Admin kullanıcısını oluşturmak

```terminal
python3 manage.py createsuperuser
```

### Uygulama Oluşturma

Uygulama oluşturma için ilk önce, 

```terminal
python3 manage.py startapp uygulama_adi
```

komutu verilmeli ardından. settings.py dosyasının içerisinde `INSTALLED_APPS = []` içerisine ekleyelim.

### Templates Klasörü

settings.py dosyasındaki `TEMPLATES=[ ]` değişkeni içerisindeki `'DIRS': []`  satırını `'DIRS': ["templates"]` olarak değiştiriyoruz.

### Statik Dosyaları Kullanma

#### Önce ayar

Statik dosyaları kullanmak için en üst klasörde bir `static` dosyası oluşturacağız. Sonrasında settings.py dosyası içerisine `STATIC_URL = '/static/'` altına

```settings.py
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
    '/var/www/static/',
]
```

komutunu yazacağız.

#### Sonra kullanım

Kullanmak istediğimiz yerde dosya içerisinde yukarıda `{% load static %}` komutuyla static dosyaları yükleyeceğiz ve kullanmak istediğimiz yerde örneğin style.css dosyasını kullanacaksak `{% static 'style.css' %}` şeklinde kullanacağız.

## settings.py Dosyası Değişiklikleri

### Dil Değişimi

Django'nun dilini değiştirmek için, settings.py dosyası içerisindeki

`LANGUAGE_CODE = 'en-us'` satırını `LANGUAGE_CODE = 'tr-TR'` ile değiştirmeliyiz.

### Zaman Dilimi Değişikliği

Zaman dilimini değiştirmek için, settings.py dosyası içerisindeki `TIME_ZONE = 'UTC'` satırını `TIME_ZONE = 'Europe/Istanbul'` ile değiştirmeliyiz.

