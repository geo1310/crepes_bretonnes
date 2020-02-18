from django.db import models
from django.utils import timezone

class Categorie(models.Model):
    nom = models.CharField(max_length=30, default="1")

    def __str__(self):
        return self.nom


class Article(models.Model):
    titre = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    auteur = models.CharField(max_length=42)
    contenu = models.TextField(null=True)
    date = models.DateTimeField(default=timezone.now,
                                verbose_name="Date de parution")
    categorie = models.ForeignKey('Categorie', on_delete=models.CASCADE)

    class Meta:
        verbose_name = "article"
        ordering = ['date']

    def __str__(self):
        return self.titre
        '''
        Cette méthode que nous définirons dans tous les modèles
        nous permettra de reconnaître facilement les différents objets que
        nous traiterons plus tard dans l'administration
        """
        
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


class Contact(models.Model):
    nom = models.CharField(max_length=255)
    adresse = models.TextField()
    photo = models.ImageField(upload_to="photos/")

    def __str__(self):
        return self.nom
