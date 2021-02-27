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

  share_name = models.CharField(max_length=8)
  trading_value = models.DecimalField(max_digits=6,decimal_places=2)
  number_shares = models.IntegerField()
  unit_share_price = models.DecimalField(max_digits=6,decimal_places=2)
  tax = models.DecimalField(max_digits=6,decimal_places=2)
  amount = models.DecimalField(max_digits=6,decimal_places=2)

  operation_type = models.CharField(max_length=2, choices=OPTIONS)
  date = models.DateTimeField(auto_now_add=True)

  investor = models.ForeignKey(Investor, on_delete=models.CASCADE)