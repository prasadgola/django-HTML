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
    address = models.CharField(max_length=200,null = True)
    city = models.CharField(max_length=100,null = True)
    course = models.CharField(max_length=100,null = True)
    pincode = models.CharField(max_length=20,null = True)
    image = models.ImageField(upload_to='profile_image',null = True, blank = True)


class onetoone(models.Model):
    onetooneid = models.AutoField(primary_key = True, null = False, blank = True) # auto increment and primary key
    user = models.ForeignKey(users, on_delete=models.CASCADE, null = True, blank = True) # foreign key
    onemet = models.CharField(max_length=20,null = True)
    # partner = models.CharField(max_length=20,null = True)
    onetopic = models.CharField(max_length=100)
    # oneduration = models.PositiveIntegerField(null=True, blank=True)
    onelocation = models.CharField(max_length=20,null = True)
    onedate = models.DateField(null = True)


    # def __str__(self):
    #     return "%s" (self.onetoneid)

class weeklypresentation(models.Model):
    weeklypresentationid = models.AutoField(primary_key = True, null = False, blank = True) # auto increment later and primary key
    user = models.ForeignKey(users, on_delete=models.CASCADE, null = True, blank = True) # foreign key
    weektopic = models.CharField(max_length=100)
    weekduration = models.PositiveIntegerField(null=True, blank=True)
    weekdate = models.DateField(null = True)

    # def __str__(self): return "%s" (self.weeklypresentationid)


class dailypresentation(models.Model):
    dailypresentationid = models.AutoField(primary_key = True, null = False, blank = True) # auto increment later and primary key
    user = models.ForeignKey(users, on_delete=models.CASCADE, null = True, blank = True) # foreign key
    dailytopic = models.CharField(max_length=100)
    dailyduration = models.PositiveIntegerField(null=True, blank=True)
    dailydate = models.DateField(null = True)



class socials(models.Model):
    socialsid = models.AutoField(primary_key = True, null = False, blank = True) # auto increment later and primary key
    user = models.ForeignKey(users, on_delete=models.CASCADE, null = True, blank = True) # foreign key
    # socialsplace = models.CharField(max_length=100,null = True)
    socialstopic = models.CharField(max_length=100)
    socialsduration = models.PositiveIntegerField(null=True, blank=True)
    socialsdate = models.DateField(null = True)



class visitors(models.Model):
    visitorsid = models.AutoField(primary_key = True, null = False, blank = True) # auto increment later and primary key
    user = models.ForeignKey(users, on_delete=models.CASCADE, null = True, blank = True) # foreign key
    # visitorscount = models.PositiveIntegerField(null=True, blank=True)
    visitorstopic = models.CharField(max_length=100)
    visitorsduration = models.PositiveIntegerField(null=True, blank=True)
    visitorsdate = models.DateField(null = True)



class referralsgiven(models.Model):
    referralsgivenid = models.AutoField(primary_key = True, null = False, blank = True) # auto increment later and primary key
    user = models.ForeignKey(users, on_delete=models.CASCADE, null = True, blank = True) # foreign key
    # givencount = models.PositiveIntegerField(null=True, blank=True)
    giventopic = models.CharField(max_length=100)
    givenduration = models.PositiveIntegerField(null=True, blank=True)
    givendate = models.DateField(null = True)



class referralstaken(models.Model):
    referralstakenid = models.AutoField(primary_key = True, null = False, blank = True) # auto increment later and primary key
    user = models.ForeignKey(users, on_delete=models.CASCADE, null = True, blank = True) # foreign key
    # takencount = models.PositiveIntegerField(null=True, blank=True)
    takentopic = models.CharField(max_length=100)
    takenduration = models.PositiveIntegerField(null=True, blank=True)
    takendate = models.DateField(null = True)




