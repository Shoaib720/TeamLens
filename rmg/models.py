from django.db import models

# Create your models here.
class ProfileUpdate(models.Model):
    STATUS_CHOICES = [
        ('CV Shared', 'CV Shared'),
        ('CV Rejected', 'CV Rejected'),
        ('Awaiting L1', 'Awaiting L1'),
        ('L1 Rejected', 'L1 Rejected'),
        ('Awaiting L2', 'Awaiting L2'),
        ('L2 Rejected', 'L2 Rejected'),
        ('Awaiting L3', 'Awaiting L3'),
        ('L3 Rejected', 'L3 Rejected'),
        ('Awaiting Feedback', 'Awaiting Feedback'),
        ('Awaiting Kickstart', 'Awaiting Kickstart'),
        ('Fulfilled', 'Fulfilled'),
        ('Inactivated', 'Inactivated'),
    ]
    cv_name = models.CharField(max_length=100)
    requirement_name = models.CharField(max_length=100)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='CV Shared')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    comments = models.CharField(max_length=300, blank=True)
    marked_deleted = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.cv_name} - {self.requirement_name}"
    
class ProfileUpdateHistory(models.Model):
    resource = models.ForeignKey(ProfileUpdate, on_delete=models.CASCADE, related_name='history')
    cv_name = models.CharField(max_length=100)
    requirement_name = models.CharField(max_length=100)
    status = models.CharField(max_length=50)
    comments = models.TextField(blank=True)
    changed_at = models.DateTimeField(auto_now_add=True)
    change_type = models.CharField(max_length=10, choices=[('create', 'Create'), ('update', 'Update'), ('delete', 'Delete')])

    def __str__(self):
        return f"{self.cv_name} | {self.status} | {self.changed_at}"