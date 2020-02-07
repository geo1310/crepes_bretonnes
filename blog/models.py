from django.db import models
from django.utils import timezone


class Article(models.Model):
    titre = models.CharField(max_length=100)
    auteur = models.CharField(max_length=42)
    contenu = models.TextField(null=True)
    date = models.DateTimeField(default=timezone.now,
                                verbose_name="Date de parution")

    class Meta:
        verbose_name = "article"
        ordering = ['date']

    def __str__(self):

        '''
        Cette méthode que nous définirons dans tous les modèles
        nous permettra de reconnaître facilement les différents objets que
        nous traiterons plus tard dans l'administration
        """
        return self.titre
        '''

    '''
    Créer la table SQL correspondante :
    python manage.py makemigrations 
    python manage.py migrate
    
    Jouer avec une base sqlite :
    
    $ python manage.py shell
    >>> from blog.models import Article # Commençons par importer le modèle que nous avons justement créé
    >>> article = Article(titre="Bonjour", auteur="Maxime")
    >>> article.contenu = "Les crêpes bretonnes sont trop bonnes !"
    >>> article.auteur -> maxime 
    >>> article.save()
    >>> article.titre = "Salut !"
    >>> article.auteur = "Mathieu"
    >>> article.save()
    >>> article.delete()
    
    
    
    
    
    '''

