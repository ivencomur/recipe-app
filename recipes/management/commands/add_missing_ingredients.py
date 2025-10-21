from django.core.management.base import BaseCommand
from django.core.management import call_command
from recipes.models import Ingredient

class Command(BaseCommand):
    help = "Create missing base Ingredients (Salt, Pepper, Parsley) and relink recipes."

    def handle(self, *args, **kwargs):
        names = ["Salt", "Pepper", "Parsley"]
        created_any = False
        for n in names:
            obj, created = Ingredient.objects.get_or_create(name=n)
            status = "created" if created else "exists"
            self.stdout.write(self.style.SUCCESS(f"Ingredient {n}: {status}"))
            created_any = created_any or created

        # Now (re)run the auto-linker so recipes pick these up
        self.stdout.write(self.style.WARNING("Running auto_link_ingredients..."))
        call_command("auto_link_ingredients")
        self.stdout.write(self.style.SUCCESS("Done."))
