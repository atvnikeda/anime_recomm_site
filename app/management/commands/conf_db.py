from django.core.management.base import BaseCommand
from app.models import Animations,User_Fav_Anime

class Command(BaseCommand):
    """Command
    docker commandで実行される部分
    """
    def handle(self, *args, **options):
        data = Animations.objects.all()
        print(len(data))

        data2 = User_Fav_Anime.objects.all().order_by('aid')
        for d in data2:
            print(d.user_name,d.aid,d.watch_degree)
        print(len(data2))
