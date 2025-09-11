from django.core.management.base import BaseCommand, CommandError
from a_places.models import Place
import polars as pl



class Command(BaseCommand):
    help = "Closes the specified poll for voting"

    def handle(self, *args, **options):
        dtypes = {
            "ZIP CODE": pl.Utf8,
        }
        df = pl.read_csv("Business_Licenses_-_Current_Active_20250908.csv", dtypes=dtypes) # pyright: ignore[reportCallIssue]
        print(df.columns)
        for i, row in enumerate(df.iter_rows(named=True)):
            if i > 1000:
                break
            if row["LATITUDE"] == "" or row["LONGITUDE"] == "" or row["BUSINESS ACTIVITY"] == "" or row["LATITUDE"] is None or row["BUSINESS ACTIVITY"] is None or row["LONGITUDE"] is None:
                continue
            place, created = Place.objects.get_or_create(
                name=row["DOING BUSINESS AS NAME"],
                business_category = row["BUSINESS ACTIVITY"],
                legal_name=row["LEGAL NAME"],
                address=row["ADDRESS"],
                city=row["CITY"] or "Chicago",
                state=row["STATE"] or "IL",
                zip_code=row["ZIP CODE"] or "",
                neighborhood=row["NEIGHBORHOOD"] or "",
                community_area_name=row["COMMUNITY AREA NAME"] or "",
                category=row["LICENSE DESCRIPTION"] or "",
                license_status=row["LICENSE STATUS"] or "",
                latitude=row["LATITUDE"] if row["LATITUDE"] != "" else None,
                longitude=row["LONGITUDE"] if row["LONGITUDE"] != "" else None,
            )
             # Print the created Place object for verification
            if created:
                print("created new place:")
                print(place)
        self.stdout.write(
            self.style.SUCCESS("print success")
        )
