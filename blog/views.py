from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect, get_object_or_404
from datetime import datetime
from blog.models import Article

# Create your views here.

def home(request):
    """ Exemple de page non valide au niveau HTML pour que l'exemple soit concis """
    return HttpResponse("""
        <h1>Bienvenue sur mon blog !</h1>
        <p>Les crêpes bretonnes ça tue des mouettes en plein vol !</p>
    """)

def list_articles(request, year=1900, month=1):
    """ Liste des articles d'un mois précis. """
    return HttpResponse("Vous avez demandé les articles de {0} {1}.".format(month, year))

def list_articles2(request, year=0000, month=0):
    return HttpResponse('Articles de %s/%s' % (year, month))

def date_actuelle(request):
    return render(request, 'blog/date.html', {'date': datetime.now()})


def addition(request, nombre1, nombre2):
    total = nombre1 + nombre2

    # Retourne nombre1, nombre2 et la somme des deux au tpl
    return render(request, 'blog/addition.html', locals())

def accueil(request):
    """ Afficher tous les articles de notre blog """
    articles = Article.objects.all() # Nous sélectionnons tous nos articles
    return render(request, 'blog/accueil.html', {'derniers_articles': articles})

def lire(request, id, slug):

    if int(id) > 100:
        return HttpResponse( "Vous avez demandé l'article n° {0} !".format(id) )
    elif int(id)==99:
        return redirect("https://www.djangoproject.com") # redirection

    else:

        article = get_object_or_404(Article, id=id, slug=slug)

        '''
        try:
            article = Article.objects.get(id=id)
        except Article.DoesNotExist:
            raise Http404

        '''
        return render(request, 'blog/lire.html', {'article':article})