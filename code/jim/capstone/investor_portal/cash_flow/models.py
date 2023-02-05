from django.db import models

from personalized_index.models import CustomUser


class CashFlowPlan(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    plan_name = models.CharField(max_length=200, default='my_plan')

    def __str__(self):
        return self.index_name
