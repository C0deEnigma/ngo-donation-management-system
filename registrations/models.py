from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from campaigns.models import Campaign



class Registration(models.Model):
    name=models.CharField(max_length=255,blank=True)
    email=models.EmailField()
    phone=PhoneNumberField(blank=True,region="IN")
    registration_time=models.DateTimeField(auto_now_add=True)
    campaign=models.ForeignKey(Campaign, on_delete=models.PROTECT)
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["email", "campaign"],
                name="unique_email_per_campaign"
            )
        ]