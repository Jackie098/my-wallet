from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class investor(models.Model):
  # constant values
  CONSERVATIVE = 'CS'
  MODERATE = 'MT'
  AGGRESSIVE = 'AG'
  RISK_PROFILE = [
    (CONSERVATIVE, 'conservative'),
    (MODERATE, 'moderate'),
    (AGGRESSIVE, 'aggressive'),
  ]

  user = models.OneToOneField(User, null=False, blank=False, on_delete=models.CASCADE)

  name = models.CharField(max_length=80)
  risk_profile = models.CharField(
    max_length=20,
    choices=RISK_PROFILE
    null=False
  )