from django.db import models

class Commission(models.Model):

    # Client details
    name = models.CharField(max_length=100)
    email = models.EmailField()
    whatsapp = models.CharField(max_length=20, blank=True)

    STYLE_CHOICES = [
        ('realism', 'Realism'),
        ('hyperrealism', 'Hyperrealism'),
        ('linework', 'Linework'),
        ('cartoon', 'Cartoon'),
        ('surrealism', 'Surrealism'),
    ]

    SIZE_CHOICES = [
        ('A5', 'A5'),
        ('A4', 'A4'),
        ('A3', 'A3'),
    ]

    PRIORITY_CHOICES = [
        ('CA', 'Common Art'),
        ('IA', 'Important Art'),
        ('VIA', 'Very Important Art'),
    ]

    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ]

    style = models.CharField(max_length=20, choices=STYLE_CHOICES)
    size = models.CharField(max_length=5, choices=SIZE_CHOICES)
    subjects = models.IntegerField(default=1)
    description = models.TextField()
    extra = models.TextField(blank=True)
    deadline = models.DateField(null=True, blank=True)
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='CA')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    deposit_paid = models.BooleanField(default=False)
    balance_paid = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} - {self.style} ({self.status})"

    class Meta:
        ordering = ['-created_at']


class Artwork(models.Model):

    CATEGORY_CHOICES = [
        ('realism', 'Realism'),
        ('hyperrealism', 'Hyperrealism'),
        ('linework', 'Linework'),
        ('cartoon', 'Cartoon'),
        ('surrealism', 'Surrealism'),
    ]

    SIZE_CHOICES = [
        ('A5', 'A5'),
        ('A4', 'A4'),
        ('A3', 'A3'),
    ]

    STATUS_CHOICES = [
        ('available', 'Currently Available'),
        ('sold', 'Sold Out'),
        ('NFS', 'Not For Sale'),
        ('notavail', 'Currently Not Available'),
    ]

    title = models.CharField(max_length=100)
    category = models.CharField(max_length=25, choices=CATEGORY_CHOICES)
    size = models.CharField(max_length=5, choices=SIZE_CHOICES)
    image = models.CharField(max_length=255)
    description = models.TextField(blank=True, default="")
    status = models.CharField(max_length=50, default='available', choices=STATUS_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} - {self.category} ({self.status})"

    class Meta:
        ordering = ['-created_at']


class Price(models.Model):

    CURRENCY_CHOICES = [
        ('NGN', 'Nigerian Naira'),
        ('USD', 'US Dollar'),
        ('GBP', 'British Pound'),
        ('EUR', 'Euro'),
    ]

    artwork = models.ForeignKey(Artwork, on_delete=models.CASCADE, related_name='prices')
    currency = models.CharField(max_length=5, choices=CURRENCY_CHOICES)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.currency} {self.amount} - {self.artwork.title}"

    class Meta:
        unique_together = ['artwork', 'currency']