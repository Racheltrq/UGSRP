from django.db import models

# Create your models here.
key_alphabet = [('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E'), ('F', 'F'), ('G', 'G')]
sharp_flat = [('sharp', '#'), ('flat', 'b')]


class Key(models.Model):
    name = models.CharField(choices = key_alphabet, max_length = 1)
    type = models.CharField(max_length = 3, default = 'maj')
    s_f = models.CharField(choices = sharp_flat, default = '', max_length = 5)
    component_pitches = models.CharField(max_length = 30, default = '')
    component_pitches1 = models.CharField(max_length = 30, blank = True)
    component_pitches2 = models.CharField(max_length = 30, blank = True)
    common = models.BooleanField(default = False)
    def __str__(self):
        return self.name + ' ' + self.s_f + ' ' + self.type
