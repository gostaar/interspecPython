import datetime

from django.test import TestCase
from django.utils import timezone

from backoffice.models import Emprunt


# Create your tests here.
class LivreModelTests(TestCase):

    def test_emprunte_recemment_avec_ancienne_date(self):
        future_time = timezone.now() + datetime.timedelta(days=30)
        e = Emprunt(date_emprunt=future_time)
        self.assertIs(e.emprunte_recemment(), False)

    def test_emprunte_recemment_dans_un_jour(self):
        hier = timezone.now() - datetime.timedelta(days=1)
        e = Emprunt(date_emprunt=hier)
        self.assertIs(e.emprunte_recemment(), True)

    def test_en_retard_avec_date_passee(self):
        passed_time = timezone.now() - datetime.timedelta(days=30)
        e = Emprunt(date_retour=passed_time)
        self.assertIs(e.en_retard(), True)

    def test_en_retard_avec_date_future(self):
        future_time = timezone.now() + datetime.timedelta(days=30)
        e = Emprunt(date_retour=future_time)
        self.assertIs(e.en_retard(), False)

