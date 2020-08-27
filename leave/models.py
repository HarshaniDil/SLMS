from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class designation(models.Model):
    name = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name

class department(models.Model):
    name = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name

class leave(models.Model):
    name = models.CharField(max_length=200, null=True)
    Number_of_Leaves = models.IntegerField(null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name

class head(models.Model):
    user = models.OneToOneField(User,null=True, on_delete=models.CASCADE)
    department = models.ForeignKey(department, null=True, on_delete=models.SET_NULL)
    phoneno = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return str(self.user)

class employee(models.Model):
    user = models.OneToOneField(User,null=True,blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    designation = models.ForeignKey(designation, null=True, on_delete=models.SET_NULL)
    department = models.ForeignKey(department, null=True, on_delete=models.SET_NULL)
    phoneno = models.CharField(max_length=200, null=True)
    leave = models.ManyToManyField(leave)
    profile_pic = models.ImageField(null=True,blank=True, default="profile.png")
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return str(self.name)

class apply(models.Model):
    STATUS = (
        ('Pending', 'Pending'),
        ('Approved','Approved'),
        ('Rejected','Rejected'),
    )

    employee = models.ForeignKey(employee, null=True, on_delete=models.SET_NULL)
    leave = models.ForeignKey(leave, null=True, on_delete=models.SET_NULL)
    date = models.DateField(null=True,blank=True)
    from_date = models.DateField(null=True,blank=True)
    to_date = models.DateField(null=True,blank=True)
    from_time = models.TimeField(null=True, blank=True)
    to_time = models.TimeField(null=True, blank=True)
    reason = models.TextField(max_length=600, null=True)
    status = models.CharField(max_length=200, choices=STATUS , default='Pending')
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return str(self.employee)


class comment(models.Model):
    name = models.CharField(max_length=200, null=True)
    email = models.EmailField(max_length=200, null=True)
    comment = models.TextField(max_length=600, null=True)

    def __str__(self):
        return self.name
   