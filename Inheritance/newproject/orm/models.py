from django.db import models
from django.utils import timezone

# Abstract Model

# This is used when you want to create a base model with fields and methods that will 
# be inherited by other models, but you don't 
# want the base model to be created as a table in the database.

class BaseItem(models.Model):
    title = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ['title'] # provides the default ordering for the items

    def __str__(self):
        return self.title

class ItemA(BaseItem):
    content = models.TextField()

    class Meta(BaseItem.Meta):
        ordering = ['-created']

class ItemB(BaseItem):
    file = models.FileField(upload_to='files')

class ItemC(BaseItem):
    file = models.FileField(upload_to='images')

class ItemD(BaseItem):
    slug = models.SlugField(max_length=255, unique=True)

#Multi-table model inheritance
# In this type, both the base model and the child model will have their own tables in the database.
# The child model will have a one-to-one link to the base model (Django handles this automatically),
# and each instance of the child model corresponds to a row in both tables.

class Books(models.Model):
    title = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)

class ISBN(Books):
    books_ptr = models.OneToOneField(
        Books, on_delete=models.CASCADE,
        parent_link=True,
        primary_key=True,
    )
    ISBN = models.TextField()


#Proxy Model
# Proxy models are used to change the behavior of an existing model, 
# such as adding methods or changing the default manager or ordering, 
# without adding any new fields. The proxy model doesn't create a new table;
# it uses the table of the original model.

class NewManager(models.Manager):
    pass

class BookContent(models.Model):
    title = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)

class BookOrders(BookContent):
    class Meta:
        proxy = True
        ordering = ['created']

    def created_on(self):
        return timezone.now() - self.created