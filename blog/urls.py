from django.urls import path, re_path
from . import views

urlpatterns = [
    path('accueil', views.home),

    re_path(r'^articles/(?P<year>\d{4})/(?P<month>\d{2})', views.list_articles), # expression réguliere
    path('articles/<int:year>/', views.list_articles), # expression non reguliere
    re_path(r'^articles$', views.list_articles2),

    path('date', views.date_actuelle),
    path('addition/<int:nombre1>+<int:nombre2>/', views.addition),

    path('', views.accueil, name='accueil'),
    path('article/<int:id>-<slug:slug>', views.lire, name='lire'),

    path('contact/', views.contact, name='contact'),
    path('message/', views.message, name='message'),
]

'''
<id_article> # format str par défaut
<int:year>/<int:month> # format int
str  : c’est le format par défaut (celui utilisé pour notre id_article, par exemple). 
Cela permet de récupérer une chaîne de caractères non vide, excepté le caractère "/" ;
slug  : correspond à une chaîne de caractères sans accents ou caractères spéciaux. Un exemple de slug peut être mon-1er-article-de-blog
uuid  : format standardisé de données, souvent utilisé pour avoir des identifiants uniques
path  : similaire à str, mais accepte également le "/". Cela permet de récupérer n’importe quelle URL, quel que soit son nombre de segments.

'''
