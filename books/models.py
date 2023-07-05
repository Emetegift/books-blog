from django.db import models

# Create your models here.

class Collection(models.Model):
    collection_name = models.CharField(max_length=100)
    # description = models.CharField(max_length=200)
    coll_cover = models.CharField(max_length=1000)
    coll_buy = models.CharField(max_length=5000)

    def __str__(self):
        return self.collection_name ## This will help return the actual name as wanted


class Piece(models.Model):
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE) #This will link this table to the collection table
    title = models.CharField(max_length=200)
    type = models.CharField(max_length=50)
    author = models.CharField(max_length=200)
    year = models.IntegerField()
    piececover = models.CharField(max_length=1000)
    # coll_buy = models.CharField(max_length=2000)

    def __str__(self):
        return self.title




# from django.db import models

# class Collection(models.Model):
#     collection_name = models.CharField(max_length=100)
#     description = models.CharField(max_length=200)
#     coll_cover = models.ImageField(upload_to='collection_covers/')  # Updated to ImageField
#     # coll_buy = models.CharField(max_length=5000)

#     def __str__(self):
#         return self.collection_name


# class Piece(models.Model):
#     collection = models.ForeignKey(Collection, on_delete=models.CASCADE)
#     title = models.CharField(max_length=200)
#     type = models.CharField(max_length=50)
#     author = models.CharField(max_length=200)
#     year = models.IntegerField()
#     piececover = models.ImageField(upload_to='piece_covers/')  # Updated to ImageField

#     def __str__(self):
#         return self.title
