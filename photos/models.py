from django.db import models
import datetime as dt

# Create your models here.
class Location(models.Model):
    """ class to indicate where the image was taken"""
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    def save_location(self):
        '''Method to save a location in the database'''
        self.save()

    def update_location(self):
        ''' Method to update a location in the database'''
        self.update()

    def delete_location(self):
        ''' Method to delete a location from the database'''
        self.delete()

class Category(models.Model):
    """ class to indicate the category of the image"""
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    def save_category(self):
        '''Method to save a category in the database'''
        self.save()

    def update_category(self):
        ''' Method to update a category in the database'''
        self.update()

    def delete_category(self):
        ''' Method to delete a category from the database'''
        self.delete()