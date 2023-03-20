# from django.db import models
#
#
# # Create your models here.
#
#
# # Document models
# class Document(models.Model):
#     brief = models.CharField(max_length=50)
#     content = models.TextField()
#     author_created_date = models.CharField(max_length=20)
#     docs_id = models.IntegerField()
#
#     # category_id = models.ForeignKey()
#
#     def __init__(self, *args):
#         return self.brief, self.docs_id, self.author_created_date, self.content
