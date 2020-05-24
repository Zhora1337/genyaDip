# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from recognize import recognize
from django.db import models

class Number(models.Model):
    photo = models.ImageField(upload_to='images/')
    code = models.CharField(max_length=6, null=False)

    def get_numbers(self):
        self.code = recognize(self.photo.path)
        
