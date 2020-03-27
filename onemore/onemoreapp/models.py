from django.db import models


class Person(models.Model):
    first_nam = models.CharField(max_length=5)
    last_nam = models.CharField(max_length=5)

class Gola(models.Model):
    first_nam = models.CharField(max_length=10)
    last_nam = models.CharField(max_length=10)

# class allconnected(models.Model):
#     username = models.CharField(max_length=20)
#     password = models.CharField(max_length=10)

class users(models.Model):
    user_id = models.AutoField(primary_key = True, null = False, blank = True)
    username = models.EmailField()
    password = models.CharField(max_length=20) # encryption required
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    birthday = models.DateField(null=True)
    gender = models.CharField(max_length=10, null = True)
    phonenumber = models.CharField(max_length=20,null = True)
    specialization = models.CharField(max_length=20)
    image = models.FileField(null = True)


class onetoone(models.Model):
    onetooneid = models.AutoField(primary_key = True, null = False, blank = True) # auto increment and primary key
    user = models.ForeignKey(users, on_delete=models.CASCADE, null = True, blank = True) # foreign key
    partner = models.CharField(max_length=20)
    onetopic = models.CharField(max_length=100)
    oneduration = models.PositiveIntegerField(null=True, blank=True)
    onedate = models.DateField(null = True)


    # def __str__(self):
    #     return "%s" (self.onetoneid)

class weeklypresentation(models.Model):
    weeklypresentationid = models.AutoField(primary_key = True, null = False, blank = True) # auto increment later and primary key
    userid = models.ForeignKey(users, on_delete=models.CASCADE, null = True, blank = True) # foreign key
    weektopic = models.CharField(max_length=100)
    weekduration = models.PositiveIntegerField(null=True, blank=True)
    weekdate = models.DateField(null = True)

    # def __str__(self): return "%s" (self.weeklypresentationid)
