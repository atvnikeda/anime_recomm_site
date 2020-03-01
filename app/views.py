from django.shortcuts import render
from .models import Animations,User_Fav_Anime
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

def to_season(s):
    seasons = {0:'冬',1:'春',2:'夏',3:'秋'}
    s_list = s.split('_')
    ans = s_list[0] + seasons[int(s_list[1])]
    return ans

# Create your views here.
def home(request):
    """Home画面
    """
    return render(request, 'home.html')

def anime_regis(request):
    """anime_regis
    ユーザが好きなアニメを登録する
    """
    if request.method == 'GET':
        """
        requestがGETのとき
        検索機能
        """
        title = request.GET.get('animetitle')
        anime_list = Animations.objects.filter(title__contains=str(title))
        if len(anime_list) > 0:
            get_animes = []
            for anime in anime_list:
                get_animes.append({'aid':anime.aid,'title':anime.title,'season':to_season(anime.season)})
            return render(request,'anime_regis.html',{'anime_list':get_animes,'search_title':title})

    if request.method == 'POST':
        """
        requestがPOSTのとき
        好きなアニメをDBに登録する
        """
        aid = request.POST.get('anime_id')
        uname = request.POST.get('username')
        degree = request.POST.get('degree')
        ntitle = request.POST.get('nowtitle')
        exist = User_Fav_Anime.objects.filter(user_name=uname,aid=aid)
        if len(exist) > 0:
            message = 'Insert Error'
        else:
            try:
                insert = User_Fav_Anime(user_name=uname,aid=aid,watch_degree=degree)
            except:
                message = 'Insert Error'
            else:
                message = 'Insert Success'
                insert.save()
        return render(request,'anime_regis.html',{'aid':aid,'uname':uname,'degree':degree,'now_title':ntitle,'message':message})
    return render(request,'anime_regis.html')

def anime_recomm(request):
    """anime_recomm
    アニメを推薦する
    requestがPOSTでないときは、推薦を開始するボタンが出てくる
    """
    if request.method == 'POST':
        """
        requestがPOSTのとき
        推薦結果を返す
        """
        uname = request.POST.get('username')
        data = Animations.objects.all().order_by('aid')
        aid_list = []
        animation_2020 = []
        for d in data:
            aid_list.append(d.aid)
            if d.season == "2020_0":
                animation_2020.append((d.aid,d.title))
        ani_vec = np.load("/code/src/review.npy")
        u_data = []
        uf_data = User_Fav_Anime.objects.filter(user_name=uname)
        if len(uf_data) > 0:
            for uf in uf_data:
                u_data.append((uf.aid,uf.watch_degree))
            user_anime_vecs = np.empty([0,300])
            user_weight = []
            for ud in u_data:
                i = aid_list.index(int(ud[0]))
                user_anime_vecs = np.append(user_anime_vecs,[ani_vec[i]],axis=0)
                user_weight.append(int(ud[1]))
            user_vec = np.average(user_anime_vecs,axis=0,weights=user_weight)
            recom_data = []
            for anime in animation_2020:
                j = aid_list.index(int(anime[0]))
                cs = cosine_similarity([user_vec],[ani_vec[j]])
                recom_data.append((int(anime[0]),cs))
            recom_data.sort(key=lambda x:x[1])
            ans = []
            for i in range(len(recom_data)):
                if i >= 5:
                    break
                now_aid = recom_data[len(recom_data) - i - 1][0]
                animedata = Animations.objects.filter(aid=now_aid)
                title = ""
                for am in animedata:
                    title = am.title
                url = 'https://www.anikore.jp/anime/' + str(now_aid) + '/'
                ans.append({'aid':now_aid,'title':title,'rank':i+1,'anime_url':url})
            return render(request,'anime_recomm.html',{'aid_list':ans})
        else:
            message = '好きなアニメが登録されていません。登録してからやり直してください'
            return render(request,'anime_recomm.html',{'message':message})
    return render(request,'anime_recomm.html')
