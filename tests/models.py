from django.db import models


class Test(models.Model):
    """Save condition, 4 answers and correct answers for tests"""
    condition = models.TextField(verbose_name='Умова завдання', max_length=512, null=True)

    # Text of answers
    first = models.CharField(verbose_name='а) :', max_length=128, null=True)
    second = models.CharField(verbose_name='б) :', max_length=128, null=True)
    third = models.CharField(verbose_name='в) :', max_length=128, null=True)
    fourth = models.CharField(verbose_name='г) :', max_length=128, null=True)

    # Variants of answer
    variants = (
        (0, "Варіант а)"),
        (1, "Варіант б)"),
        (2, "Варіант в)"),
        (3, "Варіант г)"),
    )

    # Correct answer number (start from 0)
    correctChoice = models.PositiveSmallIntegerField(verbose_name='Правильна відповідь:', choices=variants, null=True)

    # Return first 100 characters of condition
    def __str__(self):
        return self.condition[:100] + '...'
