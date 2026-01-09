from django.db import models
from campaigns.models import Campaign
from registrations.models import Registration



class Donation(models.Model):
    class PaymentStatus(models.TextChoices):
        PENDING = 'P', 'Pending'
        SUCCESS = 'S', 'Success'
        FAILED = 'F', 'Failed'

    campaign=models.ForeignKey(Campaign,on_delete=models.PROTECT,related_name='donations')
    registration=models.ForeignKey(Registration,on_delete=models.PROTECT,related_name='donations')
    amount=models.DecimalField(max_digits=12,decimal_places=2)
    payment_status=models.CharField(max_length=1,choices=PaymentStatus.choices, default=PaymentStatus.PENDING)
    payment_provider=models.CharField(max_length=50)
    #Transaction id is only generated once payment is comlpete therefore, it can be blank
    transaction_id=models.CharField(max_length=100,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints=[
            models.UniqueConstraint(
                fields=['transaction_id','payment_provider'],
                name='unique_transaction_id_per_provider'
            )
        ]