from django.core.management.base import BaseCommand, CommandError
import polars as pl


class Command(BaseCommand):
    help = "Closes the specified poll for voting"

    def handle(self, *args, **options):
        dtypes = {
            "ZIP CODE": pl.Utf8,
        }
        df = pl.read_csv("Business_Licenses_-_Current_Active_20250908.csv", dtypes=dtypes) # pyright: ignore[reportCallIssue]
        print(df.columns)
        self.stdout.write(
            self.style.SUCCESS("print success")
        )
