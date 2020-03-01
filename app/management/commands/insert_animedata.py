from django.core.management.base import BaseCommand
import pandas as pd
from app.models import Animations

class Command(BaseCommand):
    """Command
    docker commandで実行される部分
    """
    def handle(self, *args, **options):
        df = pd.read_csv('./src/anime_list.csv')
        inserts = []
        for i in range(len(df)):
            insert = Animations(aid=int(df['aid'][i]),title=str(df['title'][i]),season=str(df['season'][i]))
            inserts.append(insert)
        Animations.objects.bulk_create(inserts)
