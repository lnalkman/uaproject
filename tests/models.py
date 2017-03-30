from django.db import models


class Test(models.Model):
    # Умова завдання
    condition = models.TextField(verbose_name='Умова завдання', max_length=512, null=True)

    # Варіанти відповідей
    first = models.CharField(verbose_name='а) :', max_length=128, null=True)
    second = models.CharField(verbose_name='б) :', max_length=128, null=True)
    third = models.CharField(verbose_name='в) :', max_length=128, null=True)
    fourth = models.CharField(verbose_name='г) :', max_length=128, null=True)

    # Вибір правильного варіанту
    variants = (
        (0, "Варіант а)"),
        (1, "Варіант б)"),
        (2, "Варіант в)"),
        (3, "Варіант г)"),
    )
    correctChoice = models.PositiveSmallIntegerField(verbose_name='Правильна відповідь:', choices=variants, null=True)

    # Вивід лише правильного варіанту
    def __str__(self):
        answers = [self.first, self.second, self.third, self.fourth]
        choices = ['а)', 'б)', 'в)', 'г)']
        result = 'NULL'
        choice = 'NULL'
        try:
            result = answers[int(self.correctChoice)]
            choice = choices[int(self.correctChoice)]
        except IndexError:
            pass

        return choice + ' ' + result
