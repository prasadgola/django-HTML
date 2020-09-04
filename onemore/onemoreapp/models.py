from django.db import models


# class allconnected(models.Model):
#     username = models.CharField(max_length=20)
#     password = models.CharField(max_length=10)

class users(models.Model):
    user_id = models.AutoField(primary_key = True, null = False, blank = True)
    username = models.EmailField()
    password = models.CharField(max_length=20) # encryption required
    fullname = models.CharField(max_length=20)
    birthday = models.DateField(null=True)
    phonenumber = models.CharField(max_length=20,null = True)


class onetoone(models.Model):
    onetooneid = models.AutoField(primary_key = True, null = False, blank = True) # auto increment and primary key
    user = models.ForeignKey(users, on_delete=models.CASCADE, null = True, blank = True) # foreign key
    onemet = models.CharField(max_length=20,null = True)
    oneinvited = models.CharField(max_length=20,null = True)
    oneratings = models.CharField(max_length=20,null = True)
    onetopic = models.CharField(max_length=100)
    onedate = models.DateField(null = True)


    # def __str__(self):
    #     return "%s" (self.onetoneid)

class weeklypresentation(models.Model):
    weeklypresentationid = models.AutoField(primary_key = True, null = False, blank = True) # auto increment later and primary key
    user = models.ForeignKey(users, on_delete=models.CASCADE, null = True, blank = True) # foreign key
    weektopic = models.CharField(max_length=100)
    weekduration = models.PositiveIntegerField(null=True, blank=True)
    weekdate = models.DateField(null = True)
    weekbestby = models.CharField(max_length=100)

    # def __str__(self): return "%s" (self.weeklypresentationid)


class dailypresentation(models.Model):
    dailypresentationid = models.AutoField(primary_key = True, null = False, blank = True) # auto increment later and primary key
    user = models.ForeignKey(users, on_delete=models.CASCADE, null = True, blank = True) # foreign key
    dailytopic = models.CharField(max_length=100)
    dailyduration = models.CharField(max_length=100)
    dailydate = models.DateField(null = True)
    dailybestby = models.CharField(max_length=100)



class socials(models.Model):
    socialsid = models.AutoField(primary_key = True, null = False, blank = True) # auto increment later and primary key
    user = models.ForeignKey(users, on_delete=models.CASCADE, null = True, blank = True) # foreign key
    socialsplace = models.CharField(max_length=100,null = True)
    socialstopic = models.CharField(max_length=100)
    # socialsduration = models.PositiveIntegerField(null=True, blank=True)
    socialsdate = models.DateField(null = True)
    socialspic = models.ImageField(upload_to='profile_image',null = True, blank = True)



class visitors(models.Model):
    visitorsid = models.AutoField(primary_key = True, null = False, blank = True) # auto increment later and primary key
    user = models.ForeignKey(users, on_delete=models.CASCADE, null = True, blank = True) # foreign key
    # visitorscount = models.PositiveIntegerField(null=True, blank=True)
    visitorstopic = models.CharField(max_length=100)
    visitorsnumbers = models.PositiveIntegerField(null=True, blank=True)
    visitorsdate = models.DateField(null = True)
    visitorspic = models.ImageField(upload_to='profile_image',null = True, blank = True)


class referralsgiven(models.Model):
    referralsgivenid = models.AutoField(primary_key = True, null = False, blank = True) # auto increment later and primary key
    user = models.ForeignKey(users, on_delete=models.CASCADE, null = True, blank = True) # foreign key
    # givencount = models.PositiveIntegerField(null=True, blank=True)
    givenby = models.CharField(max_length=100)
    giventype = models.CharField(max_length=100)
    givenaddress = models.CharField(max_length=100)
    givenphonenumber = models.CharField(max_length=100)



class referralstaken(models.Model):
    referralstakenid = models.AutoField(primary_key = True, null = False, blank = True) # auto increment later and primary key
    user = models.ForeignKey(users, on_delete=models.CASCADE, null = True, blank = True) # foreign key
    # takencount = models.PositiveIntegerField(null=True, blank=True)
    takentopic = models.CharField(max_length=100)
    takenduration = models.PositiveIntegerField(null=True, blank=True)
    takendate = models.DateField(null = True)

class jvtthankyou(models.Model):
    jvtthankyouid = models.AutoField(primary_key = True, null = False, blank = True) # auto increment later and primary key
    user = models.ForeignKey(users, on_delete=models.CASCADE, null = True, blank = True) # foreign key
    youto = models.CharField(max_length=100)
    youamount = models.CharField(max_length=100)
    youbtype = models.CharField(max_length=100)
    yourtype = models.CharField(max_length=100)

class job(models.Model):
    jobid = models.AutoField(primary_key = True, null = False, blank = True) # auto increment later and primary key
    user = models.ForeignKey(users, on_delete=models.CASCADE, null = True, blank = True) # foreign key
    recname = models.CharField(max_length=100)
    recexp = models.CharField(max_length=100)
    recctc = models.CharField(max_length=100)
    recdate = models.DateField(null = True)
    reccomname = models.CharField(max_length=100)

class sphere(models.Model):
    sphereid = models.AutoField(primary_key = True, null = False, blank = True) # auto increment later and primary key
    user = models.ForeignKey(users, on_delete=models.CASCADE, null = True, blank = True) # foreign key
    spherename = models.CharField(max_length=100)
    spherenumber = models.CharField(max_length=100)
    spheremail = models.EmailField()

class trainings(models.Model):
    trainingid = models.AutoField(primary_key = True, null = False, blank = True) # auto increment later and primary key
    user = models.ForeignKey(users, on_delete=models.CASCADE, null = True, blank = True) # foreign key
    startdate = models.DateField(null = True)
    enddate = models.DateField(null = True)
    subject = models.CharField(max_length=100)
    rating = models.PositiveIntegerField(null=True, blank=True)

class interview(models.Model):
    interviewid = models.AutoField(primary_key = True, null = False, blank = True) # auto increment later and primary key
    user = models.ForeignKey(users, on_delete=models.CASCADE, null = True, blank = True) # foreign key
    metwith = models.CharField(max_length=100)
    inviteby = models.CharField(max_length=100)
    rating = models.PositiveIntegerField(null=True, blank=True)
    topic = models.CharField(max_length=100)
    Date = models.DateField(null = True)

class invited(models.Model):
    invitedid = models.AutoField(primary_key = True, null = False, blank = True) # auto increment later and primary key
    user = models.ForeignKey(users, on_delete=models.CASCADE, null = True, blank = True) # foreign key
    title = models.CharField(max_length=100)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    vcompanyname = models.CharField(max_length=100)
    email = models.EmailField()
    companyname = models.CharField(max_length=100)

class need(models.Model):
    trainingid = models.AutoField(primary_key = True, null = False, blank = True) # auto increment later and primary key
    user = models.ForeignKey(users, on_delete=models.CASCADE, null = True, blank = True) # foreign key
    name = models.CharField(max_length=100)
    email = models.EmailField()
    contact = models.CharField(max_length=100)

class edittable(models.Model):
    edittableid = models.AutoField(primary_key = True, null = False, blank = True) # auto increment later and primary key
    user = models.ForeignKey(users, on_delete=models.CASCADE, null = True, blank = True) # foreign key
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phonenumber = models.CharField(max_length=100)
    dob = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    englishlevel = models.CharField(max_length=100)
    Location = models.CharField(max_length=100)
    Address = models.CharField(max_length=100)
    Profession = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    joindate = models.CharField(max_length=100)
    Experience = models.CharField(max_length=100)
    skills = models.CharField(max_length=100)
    projects = models.CharField(max_length=100)
    course = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)
    year = models.CharField(max_length=100)
    college = models.CharField(max_length=100)
    resume = models.FileField()
    image = models.ImageField(upload_to='profile_image',null = True, blank = True)






