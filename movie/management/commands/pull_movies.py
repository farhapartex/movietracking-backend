import requests
from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = 'Pull images from server'

    def handle(self, *args, **options):
        url = "https://movie-database-alternative.p.rapidapi.com/"

        querystring = {"r": "json", "y": "2018"}

        headers = {
            "X-RapidAPI-Key": "0eb672c825msh64ad6a7de8533b3p1fa5b7jsn2ee6184a6924",
            "X-RapidAPI-Host": "movie-database-alternative.p.rapidapi.com"
        }

        response = requests.request("GET", url, headers=headers, params=querystring)

        print(response.text)
        print(response.status_code)
        print(response.json())