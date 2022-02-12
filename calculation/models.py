from django.db import models

# Create your models here.


class BaseModel(models.Model):
    created_by = models.CharField(
        max_length=50, null=True, blank=True, help_text="username"
    )
    updated_by = models.CharField(
        max_length=25, null=True, blank=True, help_text="username"
    )
    created_at = models.DateTimeField(null=True, blank=True, auto_now_add=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    is_deleted = models.BooleanField(default=False, help_text="Used for Soft Delete")

    class Meta:
        abstract = True


class InterestData(BaseModel):
    loan_date = models.DateField()
    release_date = models.DateField()
    principal = models.IntegerField(max_length=1000, help_text="Principal")
    total = models.FloatField()
    rate = models.IntegerField()

    def __str__(self):
        return str(self.total)
