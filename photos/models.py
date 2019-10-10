from django.db import models
import datetime as dt

# Create your models here.
class Location(models.Model):

    """ class to indicate where the image was taken"""

    loc_name = models.CharField(max_length=30)

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

    cat_name = models.CharField(max_length=30)

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

class Images(models.Model):

    """class to hold the photos"""

    photo = models.ImageField(upload_to='Images/')
    name = models.CharField(max_length=30)
    descripton = models.TextField()
    location = models.ForeignKey(Location)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
    time_posted = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        """ initialize class"""
        return self.name


    def save_image(self):

        '''Method to save an image in the database'''

        self.save()


    def update_image(self):

        ''' Method to update a image in the database'''

        self.update()

    def delete_image(self):

        ''' Method to delete an image from the database'''

        self.delete()

    @classmethod
    def get_images(cls):
        '''
        Method that gets all image posts from the database
        Returns:
            gotten_image_posts : list of image post objects from the database
        '''
        gotten_images = Images.objects.all()
        return gotten_images

    @classmethod
    def get_image_by_id(cls, id):
        '''
        Method that loops through the class and pick an anticipated id
        Returns:
            selected_image : desired image
        '''
        selected_image = Images.objects.filter_by(id=id)
        return selected_image

    @classmethod
    def search_by_cat_name(cls, search_term):
        photo = cls.objects.filter(name__icontains=search_term)
        return photo

    @classmethod
    def filter_by_loc_name(cls, filter_term):
        photo = cls.objects.filter(name__icontains=filter_term)
        return photo



        



    