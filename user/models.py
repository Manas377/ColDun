from django.db import models
from django.contrib.auth.models import AbstractUser, User, BaseUserManager
from django.db.models.expressions import Value

# Create your models here.


class UserManager(BaseUserManager):
    use_in_migration = True

    def _create_user(self, email, password, *args, **kwargs):
        """ This Method creates and saves user through email and password. """
        if not email:
            raise ValueError("Email is required")
        email = self.normalize_email(email)
        user = self.model(email=email, *args, **kwargs)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_user(self, email, password=None, *args, **kwargs):
        kwargs.setdefault('is_staff', False)
        kwargs.setdefault('is_superuser', False)
        return self._create_user(email, password, *args, **kwargs)

    def create_superuser(self, email, password=None, *args, **kwargs):
        kwargs.setdefault('is_staff', True)
        kwargs.setdefault('is_superuser', True)

        if kwargs.get('is_staff') is not True:
            raise ValueError("SUper User Must be Staff, and have 'is_staff'=True.")
        if kwargs.get('is_superuser') is not True:
            raise ValueError("Super User must have 'is_superuser'=True")
        return self._create_user(email, password, *args, **kwargs)

USER_GENDER_CHOICES = [
('Male', 'Male'),
('Female', 'Female'),
('Prefer Not To Disclose', 'Prefer Not To Disclose'),
]

class User(AbstractUser):
    username = None
    email = models.EmailField('Email Address', unique=True)
    date_of_birth = models.DateField(blank=True, null=True)
    first_name = models.CharField(max_length=150, null=True, blank=True)
    contact_number = models.CharField(max_length=12)
    email_verified = models.BooleanField(default=False)
    gender = models.CharField(choices=USER_GENDER_CHOICES, default = 'Prefer Not To Disclose', max_length=50)
    joined_on = models.DateTimeField(auto_now_add=True)
    manage_staff_type = (
        ('SA', 'Admin'),
        ('BDM', 'BDM'),
        ('C', 'Counsellor')
    )
    designation = models.CharField(max_length=10, choices=manage_staff_type)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def total_leads_attempted(self):
        leads = LeadRemark.objects.filter(counsellor = self)
        return leads.count()
    
    def total_follow_ups(self):
        leads = LeadRemark.objects.filter(counsellor=self, followup=True)
    
    class Meta:
        verbose_name_plural = "Users"
        
    
     
