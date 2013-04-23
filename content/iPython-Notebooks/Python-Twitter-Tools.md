Title: Python Twitter Tools
Date: 2013-04-22
Author: Michael Martinez

In the first episode of playing with twitter, I demo'ed
[Tweepy](https://github.com/tweepy/tweepy). In this episode, I will use the
[twitter library](https://github.com/sixohsix/twitter) from [Mike
Verdone](http://mike.verdone.ca/twitter/).

- install the library: `pip install twitter`

In the README and other sources of documentation, the config for the user/app
credentials are accessed via `os.path` utilizing a `read_file_token` method.
This method of credential retrieval has perplexed me in the past because I was
unable to find a sort of "canonical" way of repeating this in other projects. So
before started evaluating the code base, I set out to see if I could find a more
'pythonic' way of storing and retrieving credentials. Lo and behold, we have a
ConfigParser module built right into the standard library. Further, Doug Hellmann
has graciously covered the ConfigParser module in great detail
[here](http://pymotw.com/2/ConfigParser/).

To get started with this config option:

- create a twitter.ini file in the same directory as this file (its a simple text file)
- type [twitter] to delineate a section (read about sections in the ConfigParser tut)
- `parser.get` in this case looks in the twitter section and retrieves the value of the argument as a string.

sample twitter.ini file

    :::bash
    [twitter]
    CONSUMER_KEY = iowef03434ijskdmjlfasd2039sdkon
    CONSUMER_SECRET = akldsjfsal3fadijfaosasdk34
    oauth_token = kasdljnbfglkajdsnfq34908
    oauth_secret = dalkfewoiejaosdkmcadfaslkjdfsdfalasdf

note: these values are bogus

<a class="btn btn-large" href="/static/ipynb/Twitter.ipynb"><i class="icon-download-alt"></i> Download this Notebook</a>

In[1]:


    :::python
    from twitter import *
    from ConfigParser import SafeConfigParser
    
    parser = SafeConfigParser()
    parser.read('twitter.ini')
    
    consumer_key = parser.get('twitter', 'CONSUMER_KEY')
    consumer_secret = parser.get('twitter', 'CONSUMER_SECRET')
    oauth_access_token = parser.get('twitter', 'oauth_token')
    oauth_access_secret = parser.get('twitter', 'oauth_secret')
    
    twitter = Twitter(auth=OAuth(
        oauth_access_token, oauth_access_secret, consumer_key, consumer_secret))
    
    # Update your status
    twitter.statuses.update(
        status="Control the things that are in your control")

Out[1]:

    :::python
    {u'contributors': None,
     u'coordinates': None,
     u'created_at': u'Tue Apr 23 05:15:56 +0000 2013',
     u'entities': {u'hashtags': [], u'urls': [], u'user_mentions': []},
     u'favorited': False,
     u'geo': None,
     u'id': 326565076066766848,
     u'id_str': u'326565076066766848',
     u'in_reply_to_screen_name': None,
     u'in_reply_to_status_id': None,
     u'in_reply_to_status_id_str': None,
     u'in_reply_to_user_id': None,
     u'in_reply_to_user_id_str': None,
     u'place': None,
     u'retweet_count': 0,
     u'retweeted': False,
     u'source': u'<a href="http://michaelmartinez.in" rel="nofollow">ipython-local</a>',
     u'text': u'Control the things that are in your control',
     u'truncated': False,
     u'user': {u'contributors_enabled': False,
      u'created_at': u'Sun Oct 31 17:44:06 +0000 2010',
      u'default_profile': False,
      u'default_profile_image': False,
      u'description': u'Father. Firefighter. Mobile Crafter. Web Crafter. Garage-Business-Dude. ',
      u'entities': {u'description': {u'urls': []},
       u'url': {u'urls': [{u'display_url': u'michaelmartinez.in',
          u'expanded_url': u'http://michaelmartinez.in',
          u'indices': [0, 22],
          u'url': u'http://t.co/MTXlg5n87M'}]}},
      u'favourites_count': 1,
      u'follow_request_sent': False,
      u'followers_count': 118,
      u'following': False,
      u'friends_count': 441,
      u'geo_enabled': False,
      u'id': 210539658,
      u'id_str': u'210539658',
      u'is_translator': False,
      u'lang': u'en',
      u'listed_count': 3,
      u'location': u'Arizona',
      u'name': u'Michael Martinez',
      u'notifications': False,
      u'profile_background_color': u'706B5C',
      u'profile_background_image_url': u'http://a0.twimg.com/profile_background_images/543977615/tankdude1-Twit.jpg',
      u'profile_background_image_url_https': u'https://si0.twimg.com/profile_background_images/543977615/tankdude1-Twit.jpg',
      u'profile_background_tile': False,
      u'profile_image_url': u'http://a0.twimg.com/profile_images/1496212678/myMascot_normal.png',
      u'profile_image_url_https': u'https://si0.twimg.com/profile_images/1496212678/myMascot_normal.png',
      u'profile_link_color': u'009999',
      u'profile_sidebar_border_color': u'EEEEEE',
      u'profile_sidebar_fill_color': u'EFEFEF',
      u'profile_text_color': u'333333',
      u'profile_use_background_image': True,
      u'protected': False,
      u'screen_name': u'MonkMartinez',
      u'statuses_count': 1582,
      u'time_zone': u'Arizona',
      u'url': u'http://t.co/MTXlg5n87M',
      u'utc_offset': -25200,
      u'verified': False}}



The nice thing about PTT is that you can inspect the returned fields of the
Twitter API requested as you work. This may save time in that you don't need to
look at the API docs as much. It may also aid in the access of data, as nested
dict's and tuples are not easy to iterate if you don't know how many layers of
nesting to uncover. For example:

In[2]:


    :::python
    home_timeline = twitter.statuses.home_timeline() # returns sweet, parseable decoded json
    home_timeline[0] # the most recent tweet in my timeline

Out[2]:


    {u'contributors': None,
     u'coordinates': None,
     u'created_at': u'Tue Apr 23 05:16:38 +0000 2013',
     u'entities': {u'hashtags': [],
      u'symbols': [],
      u'urls': [{u'display_url': u'oreilly.com/openbook/',
        u'expanded_url': u'http://oreilly.com/openbook/',
        u'indices': [20, 42],
        u'url': u'http://t.co/vtk5YWe44y'}],
      u'user_mentions': []},
     u'favorite_count': 0,
     u'favorited': False,
     u'geo': None,
     u'id': 326565255465558017,
     u'id_str': u'326565255465558017',
     u'in_reply_to_screen_name': None,
     u'in_reply_to_status_id': None,
     u'in_reply_to_status_id_str': None,
     u'in_reply_to_user_id': None,
     u'in_reply_to_user_id_str': None,
     u'lang': u'en',
     u'place': None,
     u'possibly_sensitive': False,
     u'retweet_count': 0,
     u'retweeted': False,
     u'source': u'<a href="http://www.tweetdeck.com" rel="nofollow">TweetDeck</a>',
     u'text': u"Free O'Reilly books http://t.co/vtk5YWe44y",
     u'truncated': False,
     u'user': {u'contributors_enabled': False,
      u'created_at': u'Tue Mar 13 20:12:40 +0000 2007',
      u'default_profile': False,
      u'default_profile_image': False,
      u'description': u'Now putting podcasts in the cloud at http://t.co/kuIpq9dj. Previously Google, Osmosoft. #HTML5 #Rails #UX #DevExp michael@mahemoff.com',
      u'entities': {u'description': {u'urls': [{u'display_url': u'player.fm',
          u'expanded_url': u'http://player.fm',
          u'indices': [37, 57],
          u'url': u'http://t.co/kuIpq9dj'}]},
       u'url': {u'urls': [{u'expanded_url': None,
          u'indices': [0, 19],
          u'url': u'http://mahemoff.com'}]}},
      u'favourites_count': 1747,
      u'follow_request_sent': None,
      u'followers_count': 5715,
      u'following': True,
      u'friends_count': 1138,
      u'geo_enabled': False,
      u'id': 1112431,
      u'id_str': u'1112431',
      u'is_translator': False,
      u'lang': u'en',
      u'listed_count': 486,
      u'location': u'London + Melbourne',
      u'name': u'Michael Mahemoff',
      u'notifications': None,
      u'profile_background_color': u'022330',
      u'profile_background_image_url': u'http://a0.twimg.com/profile_background_images/97774687/twilk_background_4bddb8dda6006.jpg',
      u'profile_background_image_url_https': u'https://si0.twimg.com/profile_background_images/97774687/twilk_background_4bddb8dda6006.jpg',
      u'profile_background_tile': False,
      u'profile_image_url': u'http://a0.twimg.com/profile_images/1150432577/speakhdr_normal.jpg',
      u'profile_image_url_https': u'https://si0.twimg.com/profile_images/1150432577/speakhdr_normal.jpg',
      u'profile_link_color': u'717273',
      u'profile_sidebar_border_color': u'000000',
      u'profile_sidebar_fill_color': u'99CC33',
      u'profile_text_color': u'3E4415',
      u'profile_use_background_image': True,
      u'protected': False,
      u'screen_name': u'mahemoff',
      u'statuses_count': 12996,
      u'time_zone': u'London',
      u'url': u'http://mahemoff.com',
      u'utc_offset': 0,
      u'verified': False}}



In[3]:


    :::python
    home_timeline[0]['text']

Out[3]:


    u"Free O'Reilly books http://t.co/vtk5YWe44y"



urls is a nested dict inside a dict of from the tweet above. Lets see how we
would access that data if we needed it...

In[4]:


    :::python
    def double_nest():
        for i in home_timeline[0]['entities']['urls']:
            print i
            return i
    double_nest()

Out[4]:
    {u'url': u'http://t.co/vtk5YWe44y', u'indices': [20, 42], u'expanded_url':
u'http://oreilly.com/openbook/', u'display_url': u'oreilly.com/openbook/'}




    {u'display_url': u'oreilly.com/openbook/',
     u'expanded_url': u'http://oreilly.com/openbook/',
     u'indices': [20, 42],
     u'url': u'http://t.co/vtk5YWe44y'}



So now that we have the basics down, lets poke around some of the more
interesting API endpoints. I'm going to investigate trends and this requires a
[WOEID](http://developer.yahoo.com/geo/geoplanet/guide/concepts.html) and
because I am a bit lazy, this WOEID look up should suffice. [WOEID Look
up](http://woeid.rosselliot.co.nz/).

In[5]:


    :::python
    trends_available = twitter.trends.available() # returns a long list of places where trends currently "exist" 
    trends_available

Out[5]:


    [{u'country': u'',
      u'countryCode': None,
      u'name': u'Worldwide',
      u'parentid': 0,
      u'placeType': {u'code': 19, u'name': u'Supername'},
      u'url': u'http://where.yahooapis.com/v1/place/1',
      u'woeid': 1},
     {u'country': u'Brazil',
      u'countryCode': u'BR',
      u'name': u'Manaus',
      u'parentid': 23424768,
      u'placeType': {u'code': 7, u'name': u'Town'},
      u'url': u'http://where.yahooapis.com/v1/place/455833',
      u'woeid': 455833},
      u'placeType': {u'code': 7, u'name': u'Town'},
      u'url': u'http://where.yahooapis.com/v1/place/455867',
      u'woeid': 455867},
     {u'country': u'Argentina',
      u'countryCode': u'AR',
      u'name': u'C\xf3rdoba',
      u'parentid': 23424747,
      u'placeType': {u'code': 7, u'name': u'Town'},
      u'url': u'http://where.yahooapis.com/v1/place/466861',
      u'woeid': 466861},
     {u'country': u'Argentina',
      u'countryCode': u'AR',
      u'name': u'Rosario',
      u'parentid': 23424747,
      u'placeType': {u'code': 7, u'name': u'Town'},
      u'url': u'http://where.yahooapis.com/v1/place/466862',
      u'woeid': 466862},
     ... cut to save space

Tucson, Arizona USA = 2508428. Note for passing parameters into requests, the
magic underscore is nessesary as seen in `_id="2508428`

In[6]:


    :::python
    trends_tucson = twitter.trends.place(_id="2508428")


In[7]:


    :::python
    for i in trends_tucson:
        for b in i['trends']:
            print b['name']


    #5PainfulThings
    #IntialsOfSomeoneYouCareAbout
    #MediaQuestionsForDzhokhar
    #encorepaso
    #ThereGoesMyPants
    Tony Allen
    Eric Bledsoe
    Matt Barnes
    Brandon Belt
    Lamar Odom


Nothing really happening in Tucson as these closely match the global trends...
but San Diego is mentioned, what about San Diego? WOEID = 2487889

In[8]:


    :::python
    trends_SD = twitter.trends.place(_id="2487889")
    for i in trends_SD:
        for b in i['trends']:
            print b['name']


    #middleschoolmemories
    #IntialsOfSomeoneYouCareAbout
    #LHHATL
    #ItsTooEarlyTo
    #earthday
    Tony Allen
    Z Bo
    Jason's Lyric
    Matt Barnes
    Rudy Gay


Cool, some of these look interesting but I'll leave the investigation to you ...
Boston had some major incidents this past week. Are Bostonians still talking
about it? Boston WOEID = 2367105

In[9]:


    :::python
    trends_Bos = twitter.trends.place(_id="2367105")
    for i in trends_Bos:
        for b in i['trends']:
            print b['name']


    #IntialsOfSomeoneYouCareAbout
    #ItsTooEarlyTo
    #LHHATL
    #RAW
    Happy Earth Day
    Stevie J
    #dragrace
    Jason's Lyric
    Tony Allen
    Eric Bledsoe


Hmmm... TV shows and big topics... One would assume (you know about assumptions) that perhaps we could find
something about the recent events in Boston trending.

Lets see what a geo search for Tucson yields. There are a million of cool and novel ways to use this data,
this little demo simply shows you how to access the data.

In[10]:


    :::python
    geo_tweets = twitter.geo.search(query="tucson")
    geo_tweets['result']

Out[10]:


    {u'places': [{u'attributes': {},
       u'bounding_box': {u'coordinates': [[[-111.059406, 32.033883],
          [-110.708206, 32.033883],
          [-110.708206, 32.32095],
          [-111.059406, 32.32095]]],
        u'type': u'Polygon'},
       u'contained_within': [{u'attributes': {},
         u'bounding_box': {u'coordinates': [[[-114.816591, 31.332177],
            [-109.045223, 31.332177],
            [-109.045223, 37.00426],
            [-114.816591, 37.00426]]],
          u'type': u'Polygon'},
         u'country': u'United States',
         u'country_code': u'US',
         u'full_name': u'Arizona, US',
         u'id': u'a612c69b44b2e5da',
         u'name': u'Arizona',
         u'place_type': u'admin',
         u'url': u'https://api.twitter.com/1.1/geo/id/a612c69b44b2e5da.json'}],
       u'country': u'United States',
       u'country_code': u'US',
       u'full_name': u'Tucson, AZ',
       u'id': u'e6a7d49161470b37',
       u'name': u'Tucson',
       u'place_type': u'city',
       u'url': u'https://api.twitter.com/1.1/geo/id/e6a7d49161470b37.json'},
      {u'attributes': {},
       u'bounding_box': {u'coordinates': [[[-110.977543, 32.185824],
          [-110.960795, 32.185824],
          [-110.960795, 32.203223],
          [-110.977543, 32.203223]]],
        u'type': u'Polygon'},
       u'contained_within': [{u'attributes': {},
         u'bounding_box': {u'coordinates': [[[-114.816591, 31.332177],
            [-109.045223, 31.332177],
            [-109.045223, 37.00426],
            [-114.816591, 37.00426]]],
          u'type': u'Polygon'},
         u'country': u'United States',
         u'country_code': u'US',
         u'full_name': u'Arizona, US',
         u'id': u'a612c69b44b2e5da',
         u'name': u'Arizona',
         u'place_type': u'admin',
         u'url': u'https://api.twitter.com/1.1/geo/id/a612c69b44b2e5da.json'}],
       u'country': u'United States',
       u'country_code': u'US',
       u'full_name': u'South Tucson, AZ',
       u'id': u'9ba0ab30258b7362',
       u'name': u'South Tucson',
       u'place_type': u'city',
       u'url': u'https://api.twitter.com/1.1/geo/id/9ba0ab30258b7362.json'},
      {u'attributes': {},
       u'bounding_box': {u'coordinates': [[[-111.218168, 32.154521],
          [-111.044793, 32.154521],
          [-111.044793, 32.248227],
          [-111.218168, 32.248227]]],
        u'type': u'Polygon'},
       u'contained_within': [{u'attributes': {},
         u'bounding_box': {u'coordinates': [[[-114.816591, 31.332177],
            [-109.045223, 31.332177],
            [-109.045223, 37.00426],
            [-114.816591, 37.00426]]],
          u'type': u'Polygon'},
         u'country': u'United States',
         u'country_code': u'US',
         u'full_name': u'Arizona, US',
         u'id': u'a612c69b44b2e5da',
         u'name': u'Arizona',
         u'place_type': u'admin',
         u'url': u'https://api.twitter.com/1.1/geo/id/a612c69b44b2e5da.json'}],
       u'country': u'United States',
       u'country_code': u'US',
       u'full_name': u'Tucson Estates, AZ',
       u'id': u'2df92895f5362a8a',
       u'name': u'Tucson Estates',
       u'place_type': u'city',
       u'url': u'https://api.twitter.com/1.1/geo/id/2df92895f5362a8a.json'},
      {u'attributes': {},
       u'bounding_box': {u'coordinates': [[[-110.789464, 31.932823],
          [-110.755804, 31.932823],
          [-110.755804, 31.963138],
          [-110.789464, 31.963138]]],
        u'type': u'Polygon'},
       u'contained_within': [{u'attributes': {},
         u'bounding_box': {u'coordinates': [[[-114.816591, 31.332177],
            [-109.045223, 31.332177],
            [-109.045223, 37.00426],
            [-114.816591, 37.00426]]],
          u'type': u'Polygon'},
         u'country': u'United States',
         u'country_code': u'US',
         u'full_name': u'Arizona, US',
         u'id': u'a612c69b44b2e5da',
         u'name': u'Arizona',
         u'place_type': u'admin',
         u'url': u'https://api.twitter.com/1.1/geo/id/a612c69b44b2e5da.json'}],
       u'country': u'United States',
       u'country_code': u'US',
       u'full_name': u'Corona de Tucson, AZ',
       u'id': u'4d35b22f6680264a',
       u'name': u'Corona de Tucson',
       u'place_type': u'city',
       u'url': u'https://api.twitter.com/1.1/geo/id/4d35b22f6680264a.json'}]}



Cool, Now we'll perform a query for tweets containing `python job` and iterate
the results:

In[11]:


    :::python
    fun_search = twitter.search.tweets(q="python job",result_type='recent', count=20)
    #fun_search # uncomment to see the returned data for fields that look interesting...


In[12]:


    :::python
    for b in fun_search['statuses']:
        for c in b['entities']['urls']:
            print b['text'], b['created_at'], c['url']


    Lead Software Engineer (Server side, Python) * http://t.co/qObCXSv46P
    * Empresa: F-Secure * Lugar: Helsinki #empleo #trabajo #finlandia Tue Apr 23
    05:22:07 +0000 2013 http://t.co/qObCXSv46P
    #Python Install and configure reddit clone script on amazon web services by
    gorrrra: Configure existing r... http://t.co/VgYuI3te4T #Job Tue Apr 23 05:14:09
    +0000 2013 http://t.co/VgYuI3te4T
    New Job Alert: Senior Software Engineers (Ruby on Rails, Python and/or Java)
    at Rafte... http://t.co/Ef7ZsAGdAe #python #jobs Tue Apr 23 05:07:38 +0000 2013
    http://t.co/Ef7ZsAGdAe
    Site Reliability Engineer http://t.co/J784yxGA3w #java #python #jobs #hiring
    #careers Tue Apr 23 05:00:47 +0000 2013 http://t.co/J784yxGA3w
    #uitgeverij #Belgie Python Developer gevraagd voor interne functie te
    Antwerpen: Comput... http://t.co/NstoYH6KIh http://t.co/6R25reAyu2 Tue Apr 23
    04:47:51 +0000 2013 http://t.co/NstoYH6KIh
    #uitgeverij #Belgie Python Developer gevraagd voor interne functie te
    Antwerpen: Comput... http://t.co/NstoYH6KIh http://t.co/6R25reAyu2 Tue Apr 23
    04:47:51 +0000 2013 http://t.co/6R25reAyu2
    [Full-time] Seeking Passionate Python developers at Soshio
    http://t.co/YVWCEEBBhA Tue Apr 23 04:36:33 +0000 2013 http://t.co/YVWCEEBBhA
    RT @zs_frontline: ［Web求人情報］
     Python，Ruby，Perl，PHP，Javaなどを用いたWebアプリの開発やフロントエンド、デザイン案件まで多数あります！...
    http://t.co/t8WBRghjFF Tue Apr 23 04:03:26 +0000 2013 http://t.co/t8WBRghjFF
    ［Web求人情報］
     Python，Ruby，Perl，PHP，Javaなどを用いたWebアプリの開発やフロントエンド、デザイン案件まで多数あります！...
    http://t.co/t8WBRghjFF Tue Apr 23 04:00:06 +0000 2013 http://t.co/t8WBRghjFF
    #job http://t.co/ew5ADWt8oE
     - Senior Python / MongoDB Developer, Array Tue Apr 23 03:55:12 +0000 2013
    http://t.co/ew5ADWt8oE
    #job http://t.co/4WMtLjTtJ0
     - Разработчик Python, Array Tue Apr 23 03:54:08 +0000 2013
    http://t.co/4WMtLjTtJ0
    Python Flask Data Collection http://t.co/cLcyyLaqri Tue Apr 23 03:53:40
    +0000 2013 http://t.co/cLcyyLaqri
    RT @findmjob: Site Reliability Engineer http://t.co/J784yxGA3w #php #git
    #java #rest #unix #ruby #mysql #redis #python #hadoop... http://t.… Tue Apr 23
    03:46:13 +0000 2013 http://t.co/J784yxGA3w
    Site Reliability Engineer http://t.co/J784yxGA3w #php #git #java #rest #unix
    #ruby #mysql #redis #python #hadoop... http://t.co/6xrPUo9zRr Tue Apr 23
    03:42:08 +0000 2013 http://t.co/J784yxGA3w
    Site Reliability Engineer http://t.co/J784yxGA3w #php #git #java #rest #unix
    #ruby #mysql #redis #python #hadoop... http://t.co/6xrPUo9zRr Tue Apr 23
    03:42:08 +0000 2013 http://t.co/6xrPUo9zRr
    Programador Python: Porto Alegre - RS -  Anúncio nº: 919784 Programador(a)
    PythonAnúncio p... http://t.co/fYoyZ35xLT #vagas #programador Tue Apr 23
    03:29:42 +0000 2013 http://t.co/fYoyZ35xLT
    New Job Alert: Software Engineer - Python at Jawbone (San Francisco, CA):
    technical design speci... http://t.co/02proruK5j #python #jobs Tue Apr 23
    03:09:55 +0000 2013 http://t.co/02proruK5j
    #job #python Write up 3 algorithm base on an interface and abstraction in
    OCaml by kennguy13: Sorry... http://t.co/PGb3klkXbV #freelance Tue Apr 23
    03:06:00 +0000 2013 http://t.co/PGb3klkXbV
    #C Write up 3 algorithm base on an interface and abstraction in OCaml by
    kennguy13: Sorry the project has... http://t.co/eV5enpwGcD #JOB Tue Apr 23
    03:02:37 +0000 2013 http://t.co/eV5enpwGcD
    #C Write up 3 algorithm base on an interface and abstraction in OCaml by
    kennguy13: Sorry the pro... http://t.co/V5cPAOv7PX #Programming Tue Apr 23
    03:02:36 +0000 2013 http://t.co/V5cPAOv7PX
    #Python Write up 3 algorithm base on an interface and abstraction in OCaml
    by kennguy13: Sorry the projec... http://t.co/57Kw3abxVV #Job Tue Apr 23
    02:18:35 +0000 2013 http://t.co/57Kw3abxVV


If the traditional method of accessing Twitter bores you or you want finer
control over your use of the Twitter services, I think Python Twitter Tools is a
viable option. It reliably hits and maps to the Twitter API and comes packed
with an IRCBOT and commandline utilities. PTT is actively maintained as of this
writing and looks well constructed in my opinion.
