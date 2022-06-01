from django.test import TestCase
from .forms import SensorForm


def test_city_name_is_required(self):
    """ Test name field is required """
    form = SensorForm({'city_name': ''})
    self.assertIn('city_name', form.errors.keys())
    self.assertEqual(
        form.errors['city_name'][0],
        'This field is required.'
    )

def test_country_name_is_required(self):
    """ Test country field is required """
    form = SensorForm({'country': ''})
    self.assertFalse(form.is_valid())
    self.assertIn('country', form.errors.keys())
    self.assertEqual(
        form.errors['country'][0],
        'This field is required.'
    )