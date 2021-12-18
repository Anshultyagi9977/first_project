from django.db import models

# Create your models here.

class StudentData(models.Model):
    name = models.CharField(max_length=100)
    std = models.CharField(max_length=10)
    roll_no = models.IntegerField()

    def __str__(self):
        return self.name


class UserData(models.Model):
    email=models.EmailField()
    name=models.CharField(max_length=100)
    address=models.TextField()
    address2=models.TextField()
    city=models.CharField(max_length=100)
    zip=models.CharField(max_length=6)

    def __str__(self):
        return self.email

class BookDetails(models.Model):
    book_name=models.CharField(max_length=100)
    book_id=models.IntegerField()
    book_author=models.CharField(max_length=100)
    assigned=models.CharField(max_length=100)
    due_date=models.DateField()

    def __str__(self):
        return self.book_name

class ConsumerDetails(models.Model):
    name = models.CharField(max_length=100)
    mobile_No = models.CharField(max_length=100)
    location = models.CharField(max_length=100, default="abc")
    active = models.BooleanField(default=False)
    started_date = models.DateField()

    def __str__(self):
        return self.name

class ItemInventory(models.Model):
    Item_Name = models.CharField(max_length=100)
    Piece_Created = models.IntegerField()
    Piece_Sold = models.IntegerField()
    Out_Of_Stock = models.BooleanField(default=False)
    In_Stock = models.BooleanField(default=False)

    def __str__(self):
        return self.Item_Name

class StudentStatus(models.Model):
    name = models.CharField(max_length=100)
    required_attendence = models.IntegerField()
    present = models.IntegerField()
    total_days = models.IntegerField()
    allowed = models.BooleanField(default=False)
    detained = models.BooleanField(default=False)

    def __str__(self):
        return self.name
class BankDetails(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    expired = models.BooleanField(default=False)
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.name