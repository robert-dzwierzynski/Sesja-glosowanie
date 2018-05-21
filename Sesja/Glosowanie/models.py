

from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
import datetime

class Uchwala(models.Model):
    title = models.CharField(max_length=500, verbose_name="Tytuł uchwały")
    body = models.TextField(verbose_name="Treść uchwały")
    is_visible = models.BooleanField(verbose_name="Widoczna",)
    date_add = models.DateField(("Data dodania"),default=datetime.date.today)

    class Meta:
        verbose_name = "Uchwała"
        verbose_name_plural = "Uchwały"

    def get_absolute_url(self):
        return reverse("glosowanie:detale_uchwaly", kwargs={"id_uchwaly":self.id})

    def __unicode__(self):
        return self

    def __str__(self):
        return self.title


class Glosowanie(models.Model):
    VOTES_CHOICES = [
        (1,'Za'),
        (0,'Przeciw'),
        (2,'Wstrzymuję się')
    ]
    id_uzytkownika = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    id_uchwaly = models.ForeignKey(Uchwala, on_delete=models.CASCADE)
    vote = models.PositiveSmallIntegerField(choices=VOTES_CHOICES, default=None)

    def __unicode__(self):
        return self
    def get_str_vote(self):
        return self.get_vote_display()

    def __str__(self):
        return str(self.id)

