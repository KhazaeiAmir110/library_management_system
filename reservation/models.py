from django.db import models
from user.models import User
from documentation.models import Documentation


class ReservationTest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    documentation = models.ForeignKey(Documentation, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    pyment = models.DecimalField(max_digits=10, decimal_places=1, name='pyment')

    def __str__(self):
        return str(self.pyment)
