from django import forms
from .models import Article

class ContactForm(forms.Form):
    sujet = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    envoyeur = forms.EmailField(label="Votre adresse e-mail")
    renvoi = forms.BooleanField(help_text="Cochez si vous souhaitez obtenir une copie du mail envoyé.", required=False)


    '''
    def clean_message(self):
        message = self.cleaned_data['message']
        if "pizza" in message:
            raise forms.ValidationError("On ne veut pas entendre parler de pizza !")
            
        return message # Ne pas oublier de renvoyer le contenu du champ traité
    '''

    def clean(self):
        cleaned_data = super(ContactForm, self).clean()
        sujet = cleaned_data.get('sujet')
        message = cleaned_data.get('message')

        if sujet and message:  # Est-ce que sujet et message sont valides ?
            if "pizza" in sujet and "pizza" in message:
                '''raise forms.ValidationError(
                    "Vous parlez de pizzas dans le sujet ET le message ? Non mais ho !"
                )'''
                self.add_error("message",
                               "Vous parlez déjà de pizzas dans le sujet, "
                               "n'en parlez plus dans le message !"
                               )

                '''
                Notons qu’au lieu d’utiliser une chaîne de caractères pour le message d’erreur, 
                vous pouvez également spécifier comme deuxième paramètre de la méthode une instance de 
                forms.ValidationError, comme utilisé précédemment.
                '''

        return cleaned_data  # N'oublions pas de renvoyer les données si tout est OK

class ArticleForm(forms.ModelForm):

    class Meta:
        model = Article
        #fields = '__all__'
        #exclude = ('slug','date')
        fields = ('titre', 'auteur','categorie','contenu')


class NouveauContactForm(forms.Form):
    nom = forms.CharField()
    adresse = forms.CharField(widget=forms.Textarea)
    photo = forms.ImageField()


