from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=60)
    email = models.EmailField(blank=True,null=True)

    def __str__(self):
        return self.name

class Contact(models.Model):
    date = models.DateField()
    notes = models.TextField(blank=True)
    people = models.ManyToManyField(Person)
    finished = models.NullBooleanField()
    next_contact = models.DateField(blank=True, null=True)

    def list_of_people(self):
        list_of_people = ""
        for person in self.people.all():
            list_of_people += person.__str__()
            list_of_people += ", "
        return list_of_people

    def __str__(self):
        string = (self.list_of_people() + str(self.date))
        return string

class Solution(models.Model):
    date = models.DateField()
    notes = models.TextField(blank=True)
    contact = models.ManyToManyField(Contact)

    def __str__(self):
        return str(self.date)
        
