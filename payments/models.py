from django.db import models
from users.models import User
from courses.models import StudentCourse


class Payment(models.Model):
    PAYMENT_TYPES = (
        ("card", "Card"),
        ("cash", "Cash"),
        ("click", "Click"),
        ("payme", "Payme"),
        ("coin", "Coin"),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    student_course = models.ForeignKey(StudentCourse, on_delete=models.CASCADE)
    payment_type = models.CharField(max_length=20, choices=PAYMENT_TYPES)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} | {self.amount}"