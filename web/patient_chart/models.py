from django.db import models
from django.utils import timezone


class PatientChart(models.Model):
    MALE = [
        ('1', 'мужской'),
        ('2', 'женский'),
    ]
    card_number = models.CharField(max_length=255, blank=True, null=True, verbose_name='№ карты')
    fullname = models.CharField(max_length=255, blank=True, null=True, verbose_name='ФИО')
    male = models.CharField(max_length=12, choices=MALE, verbose_name='Пол', blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True, verbose_name='Дата рождения')
    created_at = models.DateField(auto_now_add=True, verbose_name='Дата создания')

    class Meta:
        verbose_name_plural = 'Карта пациента'

    def __str__(self):
        return self.fullname or ''


class Snapshot(models.Model):
    patient = models.ForeignKey(PatientChart, on_delete=models.CASCADE, verbose_name='Пациент', related_name='snapshots')
    description = models.CharField(max_length=255, verbose_name='Описание', blank=True, null=True)
    created_at = models.DateField(default=timezone.now, blank=True, null=True)
    image = models.ImageField(blank=True, null=True, verbose_name='Снимок', upload_to='snapshot')

    class Meta:
        verbose_name_plural = 'Снимки'


class CashWarrant(models.Model):
    patient = models.ForeignKey(PatientChart, on_delete=models.CASCADE, verbose_name='Пациент', related_name='cashwarrants')
    cash = models.IntegerField(blank=True, null=True, verbose_name='Цена')
    description = models.CharField(max_length=255, verbose_name='Описание', blank=True, null=True)
    created_at = models.DateField(default=timezone.now, blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Кассовый ордер'



