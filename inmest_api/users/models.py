from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.

class IMUser():
    """Custom user model with additional fields."""
    first_name = models.CharField(max_length=100)
    last_name  = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    user_type = models.CharField(max_length=20, 
        choices={
            'EIT': 'Entrepreneur in Training',
            'TEACHING_FELLOW': 'Teaching Fellow',
            'ADMIN_STAFF':'Administrative Staff',
            'ADMIN': 'Administrator',
        },
    
    default = 'EIT'
    
    )
    date_created = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Cohort(models.Model):
    """Represents a group of users within a program or course."""

    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    year = models.IntegerField()
    start_date = models.DateField()
    end_date = models.DateField()
    is_active = models.BooleanField(default=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(IMUser, on_delete=models.CASCADE, related_name='authored_cohorts')

    def __str__(self):
        return f"{self.name}"
    
class CohortMember(models.Model):
    """Links users to their associated cohorts."""

    cohort = models.ForeignKey(Cohort, on_delete=models.CASCADE, related_name='members')
    member = models.ForeignKey(IMUser, on_delete=models.CASCADE, related_name='cohorts')
    is_active = models.BooleanField(default=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(IMUser, on_delete=models.CASCADE, related_name='added_cohort_members')

    def __str__(self):
        return f"{self.member}, {self.cohort}"