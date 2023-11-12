from django.db import models
from django.utils import timezone

# Create your models here.
class Document(models.Model):
    clause_text = models.CharField(max_length=1000)
    domain = models.CharField(max_length=1000, default="")
    pub_date = models.DateTimeField("date published")
    tags = models.CharField(max_length=2000, default="")
    source = models.CharField(max_length=2000, default="")

    def __str__(self):
        return "[{}] {}: {}".format(self.id, self.source, self.clause_text[:20])
    
class DocumentCode(models.Model):
    document = models.ForeignKey(Document, on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)
    artifacts_restricted = models.CharField(max_length=1000)
    uses_restricted = models.CharField(max_length=1000)
    how_restricted = models.CharField(max_length=2000)
