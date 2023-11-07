from django.db import models


class Language(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

  
class Repository(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=350)
    url = models.URLField(unique=True)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    stars = models.IntegerField()
    issues = models.IntegerField()
    forks = models.IntegerField()
    last_commit = models.DateTimeField()

    def __str__(self):
        return f'''
        Name: {self.name}
        Description: {self.description}
        URL: {self.url}
        Language: {self.language}
        Stars: {self.stars}
        Issues: {self.issues}
        Forks: {self.forks}
        last_commit: {self.last_commit}
        '''
