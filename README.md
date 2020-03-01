# anime_recomm_site
A web application that recommends anime for the winter of 2020 based on user preferences.  
2020年冬アニメをユーザの嗜好に合わせて推薦する,Docker上で動くWebアプリケーション  
ユーザ登録，サインイン後，ユーザは視聴済みアニメを検索し登録する．  
視聴済みアニメのリストはDBに保存され，そのデータを元にユーザに対して2020年のオススメ冬アニメを推薦する  

*dockerイメージの構築*  
`docker-compose run --rm web django-admin startproject recommsite .`  

*djangoモデルの準備*  
`docker-compose run --rm web python manage.py makemigrations`  
`docker-compose run --rm web python manage.py migrate`  

*superuserの作成*  
`docker-compose run --rm web python manage.py createsuperuser`  
この後のアニメ登録，推薦はsuperuserでもそうでなくてもできます  

*事前に準備されたアニメリストをDBに挿入*  
`docker-compose run --rm web python manage.py insert_animedata`  

*Webアプリの立ち上げ*  
`docker-compose up`  

*WebアプリのHomeのページにアクセス*  
`http://127.0.0.1:8000/app/home/`  
