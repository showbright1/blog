Title: Playing with Tweepy
Date: 2013-04-20
Author: Michael Martinez

Tweepy in iPython Notebook. I've wanted to have a play with the Twitter API
for a few months. There is a lot of complexity in this API, so I looked for
a library that abstracted as much as possible. Tweepy was the first to grab
my attention.

Another library that I plan on trying is [Python Twitter Tools]( http://mike.verdone.ca/twitter/).
In hindsight, I probably should have gone with PTT to start as Tweepy returns
inconsistent data when accessing various API endpoints. Not to say Tweepy is bad,
because it worked well for these basic examples.

<a class="btn btn-large" href="/static/ipynb/Tweepy.ipynb"><i class="icon-download-alt"></i> Download this Notebook</a>

This is to set-up tweepy and oauth to play with the Twitter API

- google group is [here:](https://groups.google.com/forum/?fromgroups=#!forum/tweepy)
- docs [here:](http://packages.python.org/tweepy/html/index.html)
- github repo [here:](https://github.com/tweepy/tweepy)

 In[1]:


     :::python
     import tweepy

     # The consumer keys can be found on your application's Details
     # page located at https://dev.twitter.com/apps (under "OAuth settings")
     consumer_key="<key here>"
     consumer_secret="<secret here>"

     # The access tokens can be found on your applications's Details
     # page located at https://dev.twitter.com/apps (located
     # under "Your access token")
     access_token="<access token here>"
     access_token_secret="<access ssecret here>"

     auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
     auth.set_access_token(access_token, access_token_secret)

     myapi = tweepy.API(auth)

     # If the authentication was successful, you should
     # see the name of the account print out
     print myapi.me().name


     Michael Martinez


 If the request was successful, you will see your name print out in the response

 In[2]:


     :::python
     myapi.update_status('Rocking #iPythonNotebook and tweepy')

 Out[2]:


     <tweepy.models.Status at 0x107ca3550>

*******

## The user object ##

 Showing a method to access some variables returned by twitter

 In[3]:


     :::python
     print myapi.me().screen_name


     MonkMartinez


 In[4]:


     :::python
     print myapi.me().description


     Father. Firefighter. Mobile Crafter. Web Crafter. Garage-Business-Dude.


 In[5]:


     :::python
     me = myapi.me()


 In[6]:


     :::python
     print me.followers_count


     116


 In[7]:


     :::python
     me.status.text

 Out[7]:


     u'Rocking #iPythonNotebook and tweepy'



 In[8]:


     :::python
     me.statuses_count

 Out[8]:


     1570



 In[9]:


     :::python
     from IPython.core.display import Image
     mepic = me.profile_image_url
     Image(url=mepic)


 Out[9]:


![my mascot](static/images/myMascot_normal.png)

*******

### Rate limits ###

 For items that return a dict, you can simply iterate through the list

 In[10]:


     :::python
     type(myapi.rate_limit_status())

     #lets work through a returned dict

     rl = myapi.rate_limit_status()

     for k, v in rl.iteritems():
         print '%s : %s' %(k, v)


     photos : {u'daily_limit': 100, u'reset_time': u'Sun Apr 21 17:21:43 +0000
     2013', u'remaining_hits': 100, u'reset_time_in_seconds': 1366564903}
     remaining_hits : 346
     reset_time_in_seconds : 1366482078
     hourly_limit : 350
     reset_time : Sat Apr 20 18:21:18 +0000 2013


 Another way to access variables within the api...

 In[11]:


     :::python
     myapi.rate_limit_status()['remaining_hits']

 Out[11]:


     350



 In[12]:


     :::python
     import datetime
     # get the reset time from twitter call
     twitime = myapi.rate_limit_status()['reset_time_in_seconds']

     #convert the time
     timere = datetime.datetime.fromtimestamp(int(twitime)).strftime('%Y-%m-%d %H:%M:%S')
     print('Twitter will reset at:', timere)


     ('Twitter will reset at:', '2013-04-20 11:21:18')


 In[13]:


     :::python
     for i in myapi.user_timeline():
         print(i.text)


     Rocking #iPythonNotebook and tweepy
     Have you heard ‘Sisi - Stay - Funk Ferret Edit’ by FunkFerret on
     #SoundCloud? https://t.co/lrdhjdOmDa
     Have you heard ‘Rufus Thomas - Itch &amp; Scratch - Funk Ferret Edit’ by
     FunkFerret on #SoundCloud? https://t.co/JW2sKvlvvV
     Can you get paid to evaluate OSS python packages?
     Rocking #iPythonNotebook and tweepy
     @UnlearningEcon Outcomes are NEVER certain. More thinking and less emotion
     would make the world a better place.
     @kennethlove Right on, can't wait!!!
     @kennethlove Really AWESOME #GSWD tut(s)... Muchas Gracias! More coming soon
     I hope?
     I am working on data analysis with #pandas and #iPython for a GIS project
     that may help #firefighters be more efficient.
     Back on the horse after a one month non-programming hiatus. Feels good...
     and my fingers still remember #emacs. #python #iPython
     The damage has already been done. The #bankrun will proceed as if the tax
     levy had passed. #Cyprus
     @charlesfrith short on math eh???
     Enough politics, back to programming and awesomeness in general.
     #hispanics are not dumb people that simply recognize latino names and think,
     "bueno, yo vota para el."
     Not only that, the #republican party thinks that trotting people with
     hispanic last names will to help "win" the hispanic vote. #notworking
     The #republican party is so out of touch with my generation I really don't
     know where to begin.
     @cjno pic or it didn't happen :-)


 In[14]:


     :::python
     for i in myapi.search("#watertown"):
         print'name:', i.from_user,'\n', ':: twit:', i.text, '\n', 'geo:', i.geo


     name: Sirajulrox98
     :: twit: RT @Jessewelle: ish is getting real in Boston. Be safe people. Stay
     in your house #Watertown.
     geo: None
     name: ConradddJay
     :: twit: RT @YourAnonNews: Bomber's uncle: It's about being losers. Not
     Chechnya. Not Islam. They deserve to die. http://t.co/SH1yhnBUFQ #Watertown
     #BostonBombing
     geo: None
     name: Jesicakhua
     :: twit: This goes to show that law enforcement in the US is better that
     most other countries' military. #watertown #boston
     geo: None
     name: SaraGCeli
     :: twit: RT @mackissler: Little boy goes up to police officers and says
     "thank you!" Near the #Watertown home where the suspect was caught.
     http://t.co/xoGlNqx2Lt
     geo: None
     name: Gina_Gillespie
     :: twit: RT @AJELive: Dead #Boston bombings suspect was interviewed by FBI
     http://t.co/hLSqKYKZUz #Watertown
     geo: None
     name: bumpinuglies55
     :: twit: RT @MentalityMag: #Watertown Police Chief claims Tamerlan Tsarnaev
     was cuffed and alive on the ground when Dzhokhar ran him over with stolen SUV,
     killing him.
     geo: None
     name: watertowntab
     :: twit: RT @ThatGuyBoston We are #watertown. We are boston. We are the
     United States of America. Proud to be a family of Boston Firefighters
     geo: None
     name: DMillsTheGod
     :: twit: RT @AJELive: Dead #Boston bombings suspect was interviewed by FBI
     http://t.co/hLSqKYKZUz #Watertown
     geo: None
     name: watertowntab
     :: twit: RT @GarrettQuinn resident Taryn Sullivan, 28, says she was nervous
     but "put my faith in the #Watertown, State Police" http://t.co/39Lf9HB32t
     geo: None
     name: infolibri
     :: twit: RT @AJELive: Dead #Boston bombings suspect was interviewed by FBI
     http://t.co/hLSqKYKZUz #Watertown
     geo: None
     name: fabian70813
     :: twit: RT @YourAnonNews: Cop to NBC reporter:"if you knew what was going
     on, you wouldn't be standing here right now."#watertown #manhunt #Boston via
    @CiaPressOffice
     geo: None
     name: PatrakaarPopat
     :: twit: RT @AJELive: Dead #Boston bombings suspect was interviewed by FBI
     http://t.co/hLSqKYKZUz #Watertown
     geo: None
     name: HaaziqUvais
     :: twit: RT @lisawilliams: Police searched my house while I was away. Attic
     door open items on floor. No complaints: doing their job. #watertown
     http://t.co/A4lw0ZBxoJ
     geo: None
     name: Slainte2505
     :: twit: RT @OpocAnOn: #Dzhokhar #Tsarnaev in this wider picture running
     from second bombing in #bostonbombing #manhunt #Watertown http://t.co/LXWlVR9RkQ
     geo: None


 In[15]:


     :::python
     for i in myapi.lists_subscriptions():
         print i.name



     pythonistas
     python
     Rails
     rails guys
     Rails
     tech pundits
     peoplewhomakestuff
     Microsoft
     MSExpSLTeam
     Rad Designers
     The Pixel Horde
     Designer
     Cool Infographics People
     visual-effects-peeps
     Design/Animation
     design
     design
     Design, UI, Arts & co
     Graphics Software
     UX - IxD


 In[16]:


     :::python
     myapi.update_status('Someone looking for a part-time #pythondev?')

 Out[16]:


     <tweepy.models.Status at 0x108228d10>



 In[19]:


     :::python
     import numpy as np
     import matplotlib.pyplot as plt

     tweet_length = []
     for status in tweepy.Cursor(myapi.user_timeline).items(50):
          tweet_length.append(len(status.text))

     # Convert tweet_length to numpy array
     b = np.array(tweet_length)

     #now calc mean
     vf = np.mean(b)

     #now plot it
     figure(1)
     plt.plot(b, 'gd')

     #Horizontal line
     axhline(y=92, linewidth=1, color='r')

     xlabel('Number of Tweets')
     ylabel('Number of Characters')
     title('Mean length of last 50 tweets: %f characters' %vf)

     grid(True)

![plot](/static/images/tweepy-ipynb.png)
