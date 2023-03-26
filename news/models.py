from django.db import models

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def summary(self):
        return self.content[:100] + '...'
    
    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')
    
    def __str__(self):
        return self.title