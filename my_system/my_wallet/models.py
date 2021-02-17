from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Investor(models.Model):
  # constant values
  CONSERVATIVE = 'CS'
  MODERATE = 'MT'
  DASHING = 'DG'
  RISK_PROFILE = [
    (CONSERVATIVE, 'conservative'),
    (MODERATE, 'moderate'),
    (DASHING, 'dashing'),
  ]

  user = models.OneToOneField(User, blank=False, on_delete=models.CASCADE)

  name = models.CharField(max_length=80)
  risk_profile = models.CharField(
    max_length=2,
    choices=RISK_PROFILE,
    null=False
  )

class Operation(models.Model):
  # Constant values
  PURCHASE = 'PS'
  SALE = 'SL'
  OPTIONS = [
    (PURCHASE, 'purchase'),
    (SALE, 'sale'),
  ]

  number_shares = models.IntegerField()
  unit_share_price = models.FloatField()
  tax = models.FloatField()
  operation_type = models.CharField(max_length=2, choices=OPTIONS)
  date = models.DateTimeField(auto_now_add=True)