from django.db import models

class etender(models.Model):

    Biddername = models.CharField(max_length=200,default = 0)
    Tender_ID = models.CharField(max_length=200,default = 0)
    Tender_Type = models.CharField(max_length=200,default = 0)
    Tender_Category = models.CharField(max_length=200,default = 0)
    Total_Projects_Worked = models.IntegerField(default=0)
    Total_Success_Projects = models.IntegerField(default=0)
    Organization_size = models.IntegerField()
    Organization_established_Year = models.IntegerField()
    Value_of_Last_Project = models.IntegerField()
    Proposed_Cost_of_Project = models.IntegerField()

