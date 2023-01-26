from .models import Rating_number

def compute_rating():
    all_rates = Rating_number.objects.all()
