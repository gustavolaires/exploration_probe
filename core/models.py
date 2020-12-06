from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Sonda(models.Model):
    FACE_CHOICES = [
        ('C', 'C'),
        ('D', 'D'),
        ('B', 'B'),
        ('E', 'E'),
    ]

    x = models.IntegerField(
        default=0,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(4),
        ]
    )

    y = models.IntegerField(
        default=0,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(4),
        ]
    )

    face = models.CharField(
        default='D',
        choices=FACE_CHOICES,
        max_length=1
    )

    def rotate(self, sense=''):
        """
            Altera a direcao da sonda.

            GE - Gira 90 graus a esquerda.
            GD - Gira 90 graus a direita.
        """

        faces_size = len(self.FACE_CHOICES)
        current_face = self.FACE_CHOICES.index((self.face, self.face))

        if sense == 'left':
            current_face = (current_face + faces_size - 1) % faces_size
        elif sense == 'right':
            current_face = (current_face + 1) % faces_size

        self.face = self.FACE_CHOICES[current_face][0]

    def move(self):
        """ Move a sonda na direcao em que esta orientada """

        if self.face == 'C':
            self.y += 1

        elif self.face == 'B':
            self.y -= 1

        elif self.face == 'D':
            self.x += 1

        elif self.face == 'E':
            self.x -= 1

    def return_to_inicial_coordinates(self):
        """ Define as coordenadas da sonda como os valores iniciais (0, 0, 'D') """

        self.x = 0
        self.y = 0
        self.face = 'D'
