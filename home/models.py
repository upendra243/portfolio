from django.db import models
# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=50)

class MySkills(models.Model):
    # user = models.ForeignKey(User)
    title = models.CharField(max_length=20)
    icon_class = models.CharField(max_length=30)
    description = models.TextField()
    skills = models.CharField(max_length=200)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return "{0}-{1}".format(self.id, self.title)


"""
s = MySkills.object.filter(user__name="Upendra")

SELECT * from myskills s 
JOIn User  u On s.user_id= u.id
WHERE u.name = "Upendra";


MySkills.object.filter(rating__contains='hello')

"""
