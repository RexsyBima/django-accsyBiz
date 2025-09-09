from django.core.management.base import BaseCommand
from a_features.models import Feature

FEATURES = [
    ("wheelchair_entrance","Wheelchair-accessible entrance"),
    ("wheelchair_restroom","Accessible restroom"),
    ("step_free_path","Step-free path"),
    ("spacious_layout","Spacious layout"),
    ("braille_menu","Braille menu"),
    ("large_print_menu","Large-print menu"),
    ("digital_menu_qr","Digital/QR menu"),
    ("hearing_loop","Hearing loop"),
    ("captioned_tvs","Captioned TVs"),
    ("text_comm","Text-based communication"),
    ("quiet_hours","Quiet/Sensory-friendly hours"),
    ("low_noise_area","Low-noise area"),
    ("service_animals","Service animals welcome"),
    ("gender_neutral_restroom","Gender-neutral restroom"),
    ("accessible_parking","Accessible parking"),
]

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        for code, label in FEATURES:
            Feature.objects.get_or_create(code=code, defaults={"label": label})
        self.stdout.write(self.style.SUCCESS("Seeded features"))
