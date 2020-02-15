from django.contrib import admin
from .models import Categorie, Article
from django.utils.text import Truncator

class ArticleAdmin(admin.ModelAdmin):

# Configuration de la liste d'articles
    list_display   = ('titre', 'auteur', 'date', 'apercu_contenu')
    list_filter    = ('auteur','categorie',)
    date_hierarchy = 'date'
    ordering       = ('-date', )
    search_fields  = ('titre', 'contenu')

    """
    list_display : Liste des champs du modèle à afficher dans le tableau
    list_filter : Liste des champs à partir desquels nous pourrons filtrer les entrées
    date_hierarchy : Permet de filtrer par date de façon intuitive
    ordering : Tri par défaut du tableau
    search_fields : Configuration du champ de recherche
    """


# Configuration du formulaire d'édition
    fieldsets = (
        # Fieldset 1 : meta-info (titre, auteur…)
       ('Général', {
            'classes': ['wide', ],
            'fields': ('titre', 'auteur', 'categorie', 'slug')
        }),
        # Fieldset 2 : contenu de l'article
        ('Contenu de l\'article', {
           'description': 'Le formulaire accepte les balises HTML. Utilisez-les à bon escient !',
           'fields': ('contenu', )
        }),
    )

    """
    Les dictionnaires dans les Fieldset  contiennent trois types de données :

        fields  : liste des champs à afficher dans le fieldset ;
        description  : une description qui sera affichée en haut du fieldset, avant le premier champ ;
        classes  : des classes CSS supplémentaires à appliquer sur le fieldset (par défaut, il en existe trois : wide, extrapretty  et collapse).
    """

    prepopulated_fields = {'slug': ('titre', ), }
    # prepopulated_fields a pour principal usage de remplir les champs de type SlugField  en fonction d’un ou plusieurs autres champs


    def apercu_contenu(self, article):
        """
        Retourne les 40 premiers caractères du contenu de l'article,
        suivi de points de suspension si le texte est plus long.
        """
        return Truncator(article.contenu).chars(40, truncate='...')



admin.site.register(Categorie)
admin.site.register(Article, ArticleAdmin)


