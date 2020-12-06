from django.test import TestCase
from django.core.exceptions import ValidationError

from .models import Sonda


class SondaTestCase(TestCase):

    def test_coordinate_x_bigger_than_4(self):
        sonda = Sonda(x=5, y=0, face='D')
        with self.assertRaises(ValidationError):
            sonda.clean_fields()

    def test_coordinate_x_less_than_0(self):
        sonda = Sonda(x=-1, y=0, face='C')
        with self.assertRaises(ValidationError):
            sonda.clean_fields()

    def test_coordinate_y_bigger_than_4(self):
        sonda = Sonda(x=2, y=5, face='D')
        with self.assertRaises(ValidationError):
            sonda.clean_fields()

    def test_coordinate_y_less_than_0(self):
        sonda = Sonda(x=1, y=-1, face='E')
        with self.assertRaises(ValidationError):
            sonda.clean_fields()

    def test_coordinate_x_min_value(self):
        sonda = Sonda(x=0, y=2, face='D')
        self.assertIsNone(sonda.clean_fields())

    def test_coordinate_x_max_value(self):
        sonda = Sonda(x=4, y=1, face='E')
        self.assertIsNone(sonda.clean_fields())

    def test_coordinate_y_min_value(self):
        sonda = Sonda(x=1, y=0, face='C')
        self.assertIsNone(sonda.clean_fields())

    def test_coordinate_y_min_value(self):
        sonda = Sonda(x=3, y=4, face='B')
        self.assertIsNone(sonda.clean_fields())

    def test_coordinate_wrong_option_face(self):
        sonda = Sonda(x=3, y=4, face='F')
        with self.assertRaises(ValidationError):
            sonda.clean_fields()
