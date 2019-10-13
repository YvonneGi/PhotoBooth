from django.test import TestCase
from .models import Location,Category,Images

# Tests for Location model.
class LocationTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.kigali= Location(loc_name = 'Kigali')
    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.kigali,Location))
    # Testing Save Method
    def test_save_method(self):
        self.kigali.save_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations) > 0)
    # Testing update Method   
    def test_update(self):
        self.kigali.save_location()
        location = Location.objects.filter(loc_name = "Kigali").first()
        update = Location.objects.filter (id=location.id).update(loc_name = "Gisenyi")
        updated = Location.objects.filter(loc_name = "Gisenyi").first()
        self.assertTrue(Location.loc_name,updated.loc_name)
    # Testing delete Method
    def test_delete(self):
        self.kigali.save_location()
        location = Location.objects.filter(loc_name="Kigali").first()
        delete = Location.objects.filter(id=location.id).delete()
        locations = Location.objects.all()
        self.assertTrue(len(locations) ==0 )

# Tests for Category model.
class CategoryTestClass(TestCase):
    # Set up method
    def setUp(self):
        self.car= Category(cat_name = 'Car')
    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.car,Category))
    # Testing Save Method
    def test_save_method(self):
        self.car.save_category()
        categories = Category.objects.all()
        self.assertTrue(len(categories) > 0)
    # Testing update Method   
    def test_update(self):
        self.car.save_category()
        category = Category.objects.filter(cat_name = "Car").first()
        update = Category.objects.filter (id=category.id).update(cat_name = "House")
        updated = Category.objects.filter(cat_name = "House").first()
        self.assertTrue(Category.cat_name,updated.cat_name)
    #Testing delete Method
    def test_delete_category(self):
       self.car.save_category()
       car = Category.objects.filter(cat_name='Car').first()
       cars = Category.objects.filter(id =car.id).delete()
       cars =Category.objects.all()
       self.assertTrue(len(cars) ==0 )

# Tests for Images model.
class ImagesTestClass(TestCase):
    # Set up method
    def setUp(self):
        self.wall= Images(id=1,photo = '/static/images/wall.jpg',name = 'Wall',
        descripton = 'Generic image')
        self.car = Category(cat_name='Car')
        self.car.save_category()
        self.kigali = Location(loc_name = 'Kigali')
        self.kigali.save_location()
    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.wall,Images))
    # Testing Save Method
    def test_save_method(self):
        self.wall.save_image()
        image = Images.objects.all()
        self.assertTrue(len(image) == 1)
    # Testing update Method   
    def test_update(self):
        self.wall.save_image()
        image = Images.objects.filter(name = "Wall").first()
        update = Images.objects.filter (id=image.id).update(name = "Heaven")
        updated = Images.objects.filter(name = "Heaven").first()
        self.assertTrue(Images.name,updated.name)
    # Testing delete Method
    def test_delete(self):
        self.wall.save_image()
        image = Images.objects.filter(name="Wall").first()
        delete = Images.objects.filter(id=image.id).delete()
        image = Images.objects.all()
        self.assertTrue(len(image) ==0 )
     # Testing get all images Method
    def test_get_images(self):
        images = Images.objects.all()
        self.assertTrue(Images.name)
    # Testing get images by category Method
    def test_search_by_category(self):
        self.wall.save_image()
        fetch_specific = Category.objects.get(cat_name='Car')
        self.assertTrue(fetch_specific.cat_name=='Car')
    # Testing get images by id Method
    # def test_get_image_by_id(self):
    #     self.wall.save_image()
    #     fetched_image = Images.get_image_by_id(1)
    #     self.assertEqual(fetched_image.id,1)

    # Testing filter by by location Method
    # def test_filter_by_location(self):
    #     self.wall.save_image()
    #     fetch_specific = Images.filter_location('kigali')
    #     self.assertEqual(fetch_specific.get(id=1),self.wall)

   

 
