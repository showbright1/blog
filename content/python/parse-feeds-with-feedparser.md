Title: Parse Feeds with FeedParser
Date: 2013-05-20
Author: Michael Martinez


I am currently working on a [Flask](http://flask.pocoo.org/) feed reader app.
The plan is to enable a reader app that attaches to static site generator like
[Pelican](http://docs.getpelican.com/en/latest/),
[Nikola](http://nikola.ralsina.com.ar/) and
[Mynt](http://mynt.mirroredwhite.com/) among many [others](http://www.quora.com
/Whats-the-best-available-static-blog-website-generator-in-Python). I have the
basic structure of the app done and I wanted to implement feed parsing. With
quite a bit of effort I probably could have rolled my own bugging feedparser,
but I am a believer in not re-inventing the wheel. So I turned to Google and
found FeedParser for python.

[Feedparser](http://pythonhosted.org/feedparser/index.html) is touted as a
[universal feed parser](https://pypi.python.org/pypi/feedparser/5.1.3) that
handles RSS 0.9x, RSS 1.0, RSS 2.0, CDF, Atom 0.3, and Atom 1.0 feeds. In order
to really understand how this package works, I decided to create this notebook
and share with all of you. Hopefully, it sheds some light on the finer details
of working with feeds and python.

<a class="btn btn-large" href="/static/ipynb/Feedparser.ipynb"><i class="icon-download-alt"></i> Download this Notebook</a>


### Feed Data

There are basically two "groups" of data that come with every feed. The feed
data itself, as in the hackaday, or Planet Python feed(s) and the relevant data
about them. The other group of data are the feed entries, and these can be
thought of as the stream of entities that the feed produces. For this example,
entries are individual blog posts supplied by the feed.

The first task is to import feedparser and get a few feeds to work with.

In[1]:


    :::python
    import feedparser
    planet_python = feedparser.parse('http://planet.python.org/rss20.xml')
    hack = feedparser.parse('http://www.hackaday.com/rss.xml')


So let's get some data about the specific feeds we have just accessed and parsed
with feedparser.


In[2]:


    :::python
    hack.feed.title


Out[2]:


    u'Hack a Day'



If we want to store the title data as a string in a database or something, we
can use the encode to `utf-8` method as demo'ed below. If not, simply calling
`feed.title` will return the raw (parsed) title of the feed.


In[3]:


    :::python
    planet_python.feed.title.encode('utf-8')


Out[3]:


    'Planet Python'



The feed links. Reference the doc's for a full list of feed items that can be accessed.

In[4]:


    :::python
    hack.feed.link


Out[4]:


    u'http://hackaday.com'



In[5]:


    :::python
    planet_python.feed.link


Out[5]:


    u'http://planet.python.org/'



There are two convenience http methods that can potentially save a bunch of
error prone manual date/time checking code. In short, your implementation needs
a way to check if the feed has any updated items. [ETag and last modified
Headers](http://pythonhosted.org/feedparser/http-etag.html) are special http
headers that *may* be sent on subsequent requests to check for updates. Proper
[exception](http://docs.python.org/2/tutorial/errors.html) handling and testing
will need to be done to ensure these operate as expected. I've included them
here we will try them out at the end of the post.

In[6]:


    :::python
    h_tag = hack.etag
    h_tag


Out[6]:


    u'jJkun8gY53hstqhk+8EvcdIIKuA'



In[7]:


    :::python
    h_mod = hack.modified
    h_mod


Out[7]:


    'Mon, 20 May 2013 06:29:38 GMT'



In[8]:


    :::python
    p_tag = planet_python.etag
    p_tag


Out[8]:


    u'"17d8206-c0c4e-4dd1fe032e880"'



In[9]:


    :::python
    p_mod = planet_python.modified
    p_mod


Out[9]:


    'Mon, 20 May 2013 05:48:02 GMT'



### Entries, or the meat and potatoes of Feed parsing

The other half of the equation in this demo is accessing the data that the feed
produces. The following explores the myriad of ways to get and manipulate this
data

Calling entries on our feedparser object returns a FeedParserDict. After
inspecting the source code, FeedParserDict subclasses a UserDict which
subclasses dict but it behaves like a list as well. This is what I love about
Python.

The first item in the entries is called with entries at index 0. This gives us a
clue as to how the data is structured. The doc's are equally clear about what
you can access with `entries[i].<item here>`. Chain `encode('utf-8') to the end
of each call to get a string.

In[10]:


    :::python
    hack.entries[0]


Out[10]:


    {'author': u'Mike Szczys',
     'author_detail': {'name': u'Mike Szczys'},
     'authors': [{}],
     'comments': u'http://hackaday.com/2013/05/19/hackaday-links-sunday-may-19th-2013/#comments',
     'content': [{'base': u'http://feeds2.feedburner.com/hackaday/LgoM',
       'language': None,
       'type': u'text/html',
       'value': u'<p><img alt="hackaday-links-chain" class="aligncenter size-full wp-image-97424"
       height="32" src="http://hackadaycom.files.wordpress.com/2013/04/hackaday-links-chain.png?w=580&#038;h=32" width="580" />
       </p>\n<p>Laser cutter owners may find <a href="http://www.makercase.com/" target="_blank">this online box design tool</a>
       which [Jon] built quite useful. It&#8217;s got a few more joint options than
       <a href="http://hackaday.com/2012/07/26/box-maker-extension-for-inkscape/">the Inkscape box design add-on</a> does.
       </p>\n<p>Apparently the US Navy has the ability to bring down drones in
       <a href="http://www.youtube.com/watch?v=KEUwnqmKlbE" target="_blank">a flaming pile of laser-caused death</a>.
       [Thanks Joshua]</p>\n<p>[Michail] has been working on <a href="http://3.14.by/en/read/BarsFA-4T-full-adder"
       target="_blank">a transistor-based full adder</a>. He&#8217;s posted a Spice simulation if you want to learn about the design.
       </p>\n<p>Turn your crystal clear LED bodies into diffuse ones <a href="http://rurandom.org/justintime/index.php?title=Diffusing_Leds_the_Fast_Way"
       target="_blank">using a wooden dowel, power drill, and sandpaper</a>. The results look better than what we&#8217;ve accomplished by hand.
       [Thanks Vinnie]</p>\n<p>Play your favorite Atari Jaguar games on an FPGA thanks to the work\xa0[Gregory Estrade] did to get it running on a\xa0Stratix-II board.
       You can pick <a href="https://github.com/Torlus/JagNetlists" target="_blank">up the VHDL and support tools</a>
       in his repo. If you&#8217;re just curious you can watch\xa0<a href="http://www.youtube.com/watch?v=l6KWd-LPwKg"
       target="_blank">his demo vid</a>.</p>\n<p>Members of Open Space Aarhus &#8212; a hackerspace in Risskov, Denmark
       &#8212; have been playing around with a bunch of old server fans. <a href="http://www.youtube.com/watch?v=NILCWpM5oCo"
       target="_blank">They made a skirtless hovercraft</a> by taping them together and letting them rip. Too bad it can&#8217;t
       carry its own power supply</p>\n<p>Here&#8217;s another final project from that bountiful Cornell embedded systems class.
       This team of students made a maze game that <a href="http://people.ece.cornell.edu/land/courses/ece5760/FinalProjects/s2013/cwf38_as889_mao65/index.htm"
       target="_blank">forms the maze by capturing walls drawn on a white board</a>.</p>\n<p>And finally, here&#8217;s
       <a href="http://wastecycle.blogspot.com/2013/05/hardware-vs-electronics-wastecycle.html" target="_blank">a unique
       chess board you can build</a> by raiding your parts bin. [Tetris Monkey] made the board from the LCD screen of a
       broken monitor. The playing pieces are salvaged electronics (like big capacitors) against corroded hardware
       (like nuts and bolts). We think it came out just great!</p>\n<br />Filed under:
       <a href="http://hackaday.com/category/hackaday-links/">Hackaday links</a>  <a rel="nofollow" target="_blank">
       <img alt="" border="0" src="http://feeds.wordpress.com/1.0/comments/hackadaycom.wordpress.com/98186/" /></a>
       <img alt="" border="0" height="1" src="http://stats.wordpress.com/b.gif?host=hackaday.com&#038;blog=4779443&#038;
       post=98186&#038;subd=hackadaycom&#038;ref=&#038;feed=1" width="1" /><img height="1"
       src="http://feeds.feedburner.com/~r/hackaday/LgoM/~4/h48k1BgqUaw" width="1" />'}],
     'feedburner_origlink': u'http://hackaday.com/2013/05/19/hackaday-links-sunday-may-19th-2013/',
     'guidislink': False,
     'id': u'http://hackaday.com/?p=98186',
     'link': u'http://feedproxy.google.com/~r/hackaday/LgoM/~3/h48k1BgqUaw/',
     'links': [{'href': u'http://feedproxy.google.com/~r/hackaday/LgoM/~3/h48k1BgqUaw/',
       'rel': u'alternate',
       'type': u'text/html'}],
     'media_content': [{'medium': u'image',
       'url': u'http://1.gravatar.com/avatar/1aac8835fba7c550fea5a53cd1b0dfb8?s=96&d=http%3A%2F%2F1.gravatar.com%2Favatar%2Fad516503a11cd5ca435acc9bb6523536%3Fs%3D96'},
      {'medium': u'image',
       'url': u'http://hackadaycom.files.wordpress.com/2013/04/hackaday-links-chain.png'}],
     'published': u'Sun, 19 May 2013 21:01:28 +0000',
     'published_parsed': time.struct_time(tm_year=2013, tm_mon=5, tm_mday=19, tm_hour=21, tm_min=1, tm_sec=28, tm_wday=6, tm_yday=139, tm_isdst=0),
     'slash_comments': u'16',
     'summary': u'Laser cutter owners may find this online box design tool which [Jon] built quite useful.
     It&#8217;s got a few more joint options than the Inkscape box design add-on does. Apparently the US Navy has the
     ability to bring down drones in a flaming pile of laser-caused death. [Thanks Joshua] [Michail] has been working on
      a [&#8230;]<img alt="" border="0" height="1" src="http://stats.wordpress.com/b.gif?host=hackaday.com&#038;blog=4779443&#038;
      post=98186&#038;subd=hackadaycom&#038;ref=&#038;feed=1" width="1" />',
     'summary_detail': {'base': u'http://feeds2.feedburner.com/hackaday/LgoM',
      'language': None,
      'type': u'text/html',
      'value': u'Laser cutter owners may find this online box design tool which [Jon] built quite useful.
      It&#8217;s got a few more joint options than the Inkscape box design add-on does. Apparently the US Navy has the
      ability to bring down drones in a flaming pile of laser-caused death. [Thanks Joshua] [Michail] has been working
      on a [&#8230;]<img alt="" border="0" height="1" src="http://stats.wordpress.com/b.gif?host=hackaday.com&#038;
      blog=4779443&#038;post=98186&#038;subd=hackadaycom&#038;ref=&#038;feed=1" width="1" />'},
     'tags': [{'label': None, 'scheme': None, 'term': u'Hackaday links'},
      {'label': None, 'scheme': None, 'term': u'chess'},
      {'label': None, 'scheme': None, 'term': u'diffuse'},
      {'label': None, 'scheme': None, 'term': u'fans'},
      {'label': None, 'scheme': None, 'term': u'fpga'},
      {'label': None, 'scheme': None, 'term': u'full adder'},
      {'label': None, 'scheme': None, 'term': u'laser'},
      {'label': None, 'scheme': None, 'term': u'maze'}],
     'title': u'Hackaday Links: Sunday, May 19th, 2013',
     'title_detail': {'base': u'http://feeds2.feedburner.com/hackaday/LgoM',
      'language': None,
      'type': u'text/plain',
      'value': u'Hackaday Links: Sunday, May 19th, 2013'},
     'wfw_commentrss': u'http://hackaday.com/2013/05/19/hackaday-links-sunday-may-19th-2013/feed/'}



In[11]:


    :::python
    hack.entries[2].summary


Out[11]:


    u'Sending data from a microcontroller to a PC usually requires some sort of serial connection, either through fiddly
    on-chip USB, FTDI chips, or expensive radio ICs. [Scott] didn&#8217;t want to deal with this when creating a network
    of wireless temperature sensors, so he hacked up a few cheap 433 MHz radio transmitters and\xa0receivers\xa0to transmit
    data [&#8230;]<img alt="" border="0" height="1" src="http://stats.wordpress.com/b.gif?host=hackaday.com&#038;blog=4779443&#038;
    post=98208&#038;subd=hackadaycom&#038;ref=&#038;feed=1" width="1" />'



In[12]:


    :::python
    hack.entries[2].link


Out[12]:


    u'http://feedproxy.google.com/~r/hackaday/LgoM/~3/HfH-IWvdlN8/'



In[13]:


    :::python
    planet_python.entries[0].link


Out[13]:


    u'http://www.pythondiary.com/blog/May.19,2013/looking-advertising-proposals.html'



Lets try to naively iterate over the `planet_python.entries` list which is
actually called FeedParserDict

In[14]:


    :::python
    for i in planet_python.entries:
        print planet_python.entries[i].link



    ---------------------------------------------------------------------------
    TypeError                                 Traceback (most recent call last)
    <ipython-input-14-f4095ac7e970> in <module>()
          1 for i in planet_python.entries:
    ----> 2     print planet_python.entries[i].link
    
    TypeError: list indices must be integers, not FeedParserDict


Ok, that didn't go so well. FeedParserDict looks more like an integer indexed
list with nested dicts. Lets see what kind of data structure is being returned.
Lets print the index

In[15]:


    :::python
    for index in range(len(hack.entries)):
        print index


    0
    1
    2
    3
    4
    5
    6


Now we'll enumerate the list to access the link data... any of the
`entries[i].<item>` will work here.

In[16]:


    :::python
    for index, item in enumerate(hack.entries):
        print item.link + " ** " + item.title + " ** " + item.published


    http://feedproxy.google.com/~r/hackaday/LgoM/~3/h48k1BgqUaw/ ** Hackaday
    Links: Sunday, May 19th, 2013 ** Sun, 19 May 2013 21:01:28 +0000
    http://feedproxy.google.com/~r/hackaday/LgoM/~3/ucspkFVdN0U/ ** ATX Raspi is
    a smart power source for Raspberry Pi ** Sun, 19 May 2013 19:01:10 +0000
    http://feedproxy.google.com/~r/hackaday/LgoM/~3/HfH-IWvdlN8/ ** Wireless
    microcontroller/PC interface for $3 ** Sun, 19 May 2013 17:00:58 +0000
    http://feedproxy.google.com/~r/hackaday/LgoM/~3/xDIE-HyDI3Y/ ** Controlling
    a terminal with Google Voice ** Sun, 19 May 2013 15:00:23 +0000
    http://feedproxy.google.com/~r/hackaday/LgoM/~3/GY6JT-CI7hU/ ** FPGA plays
    Mario like a champ ** Sun, 19 May 2013 13:01:27 +0000
    http://feedproxy.google.com/~r/hackaday/LgoM/~3/UIbzO7WSI_c/ ** Robot air
    hockey championship as a final project ** Sat, 18 May 2013 21:01:42 +0000
    http://feedproxy.google.com/~r/hackaday/LgoM/~3/s7hF-USiG1c/ ** Just put
    your lips together to turn on a lamp ** Sat, 18 May 2013 19:01:30 +0000


So we know how to get to the data, we can start to build some useful data
structures suitable for storage or further operation. Below we create a list
called links, then we create a variable to we set to the length of the returned
number of entries. This integer can be used to loop and access the data we want.
This method of iteration should shield you from IndexError in that the loop
should be equal to the number of entries and nothing more or less

In[17]:


    :::python
    links = []
    for entry in planet_python.entries:
        links.append(entry.link)
    links


Out[17]:


    ['http://www.pythondiary.com/blog/May.19,2013/looking-advertising-proposals.html',
     'http://codeboje.de/tumblr-with-python/',
     'http://www.pythondiary.com/blog/May.19,2013/dvd-collection-source-code-now-available.html',
     'http://www.pythondiary.com/blog/May.19,2013/python-script-encode-django-templates.html',
     'http://pycon.blogspot.com/2013/05/pycon-2014-begins-call-for-launch-day.html',
     'http://python4kids.wordpress.com/2013/05/19/661/',
     'http://holgerkrekel.net/2013/05/19/pep438-is-live-speed-up-python-package-installs-now/',
     'http://txzone.net/2013/05/kivy-1-7-0-is-out/',
     'http://feedproxy.google.com/~r/TwistedMatrixLaboratories/~3/f1Hs3pETcpc/migration-report.html',
     'http://www.gefira.pl/blog/2013/05/18/zato-1-0-the-next-generation-esb-and-application-server-open-source-in-python/',
     'http://scummos.blogspot.com/2013/05/kdev-python-151-released.html',
     'http://learnpython.wordpress.com/2013/01/19/another-quick-python-deal/',
     'http://nuitka.net/posts/nuitka-release-043.html',
     'http://jugad2.blogspot.com/2013/05/python-inspect-module-is-powerful.html',
     'http://pyrseas.wordpress.com/2013/05/17/pyrseas-contributions-solicited/',
     'http://montrealpython.org/2013/05/pycon-day-sponsors/',
     'http://reinout.vanrees.org/weblog/2013/05/17/priniciple-philosophy.html',
     'http://feedproxy.google.com/~r/PyPyStatusBlog/~3/q2ijxAdBLcQ/pypy-201-bohr-smrrebrd.html',
     'http://reinout.vanrees.org/weblog/2013/05/16/web-of-stuff.html',
     'http://reinout.vanrees.org/weblog/2013/05/16/planting-open-source-seeds.html',
     'http://www.tryton.org/posts/last-maintenance-releases-for-series-18.html',
     'http://reinout.vanrees.org/weblog/2013/05/16/advanced-python-metaclasses.html',
     'http://reinout.vanrees.org/weblog/2013/05/15/thread-profiling-python.html',
     'http://reinout.vanrees.org/weblog/2013/05/15/brandon-rhodes.html',
     'http://reinout.vanrees.org/weblog/2013/05/15/imaginative-programmer.html']



We can also slice the "list" to access whatever data we need, by
creating/copying it into another list.

In[18]:


    :::python
    links_one = []
    for i in planet_python.entries[:5]:
        links_one.append(i.link.encode('utf-8'))
    links_one


Out[18]:


    ['http://www.pythondiary.com/blog/May.19,2013/looking-advertising-proposals.html',
     'http://codeboje.de/tumblr-with-python/',
     'http://www.pythondiary.com/blog/May.19,2013/dvd-collection-source-code-now-available.html',
     'http://www.pythondiary.com/blog/May.19,2013/python-script-encode-django-templates.html',
     'http://pycon.blogspot.com/2013/05/pycon-2014-begins-call-for-launch-day.html']



Now we can use `for i in hack.entries[:]:` without index numbers inclusive or
exclusive to get a copy of the list for iteration. Ie. `for i in
hack.entries[1:6]:` where index position 1 is inclusive and 6 would be
exclusive. Below, we ask for the first two items.

In[19]:


    :::python
    hack_dict = []
    for i in hack.entries[:2]:
        hack_dict.append({'title':i.title.encode('utf-8'), 'url':i.link.encode('utf-8'), 'summary':i.summary.encode('utf-8')})
    hack_dict


Out[19]:


    [{'summary': 'Laser cutter owners may find this online box design tool which [Jon] built quite useful.
    It&#8217;s got a few more joint options than the Inkscape box design add-on does. Apparently the US Navy has the
    ability to bring down drones in a flaming pile of laser-caused death. [Thanks Joshua] [Michail] has been working on
    a [&#8230;]<img alt="" border="0" height="1" src="http://stats.wordpress.com/b.gif?host=hackaday.com&#038;blog=4779443&#038;
    post=98186&#038;subd=hackadaycom&#038;ref=&#038;feed=1" width="1" />',
      'title': 'Hackaday Links: Sunday, May 19th, 2013',
      'url': 'http://feedproxy.google.com/~r/hackaday/LgoM/~3/h48k1BgqUaw/'},
     {'summary': 'One aspect of the Raspberry Pi that has always challenged us is the power supply. It was a great idea
     to power the board from a standard micro-USB\xc2\xa0port because economy of scale makes phone chargers
     (even in the 1A range necessary for stable operation of the RPi) cheap and easy to acquire. The thing we [&#8230;]
     <img alt="" border="0" height="1" src="http://stats.wordpress.com/b.gif?host=hackaday.com&#038;blog=4779443&#038;
     post=98166&#038;subd=hackadaycom&#038;ref=&#038;feed=1" width="1" />',
      'title': 'ATX Raspi is a smart power source for Raspberry Pi',
      'url': 'http://feedproxy.google.com/~r/hackaday/LgoM/~3/ucspkFVdN0U/'}]



### Time / Date

Time and date are imporant factors in feed parsing for a myriad of reasons. One
reason is becuase the relavancy of the item may degrade over time. Luckily the
Feedparser package includes some nice convinenice methods to access time/date
data to use how we please. The published_parsed item is a Python 9-tuple that is
easy to manipulate into any format required for storage into a database datetime
column, for example.

In[20]:


    :::python
    #time
    # Go here to learn about formatting times: http://docs.python.org/2/library/time.html#time.strftime
    from time import strftime
    for i in planet_python.entries[:5]:
        print 'Feed Published Time: ' + i.published + '\n' + 'My Formatted time: ' + strftime("%H:%M:%S %z %Z on %a, %d %b %Y", i.published_parsed)
        print '\n'


    Feed Published Time: Sun, 19 May 2013 23:41:20 +0000
    My Formatted time: 23:41:20 -0700 MST on Sun, 19 May 2013


    Feed Published Time: Sun, 19 May 2013 21:31:05 +0000
    My Formatted time: 21:31:05 -0700 MST on Sun, 19 May 2013


    Feed Published Time: Sun, 19 May 2013 17:41:21 +0000
    My Formatted time: 17:41:21 -0700 MST on Sun, 19 May 2013


    Feed Published Time: Sun, 19 May 2013 17:41:21 +0000
    My Formatted time: 17:41:21 -0700 MST on Sun, 19 May 2013


    Feed Published Time: Sun, 19 May 2013 18:20:42 +0000
    My Formatted time: 18:20:42 -0700 MST on Sun, 19 May 2013




### Revisit Etags / Last-Modified

As I tried to explain above these http methods could be extremely useful as a way
to check the status of the respective feeds. I've looked at several feed
projects implementing feedparser and did not utilize this method to check on the
status of the feed. I am not totally sure what that means as it may prove to be
an ineffective way to check on the feed status. I plan on implementing this and
will report back what I find...

In[21]:


    :::python
    # Lets revisit the modified and etag headers to use this library effectively...
    hack = feedparser.parse('http://www.hackaday.com/rss.xml', etag=h_tag, modified=h_mod)
    planet_python = feedparser.parse('http://planet.python.org/rss20.xml',etag=p_tag,  modified=p_mod)


In[23]:


    :::python
    h_mod = hack.modified
    h_mod



    ---------------------------------------------------------------------------
    AttributeError                            Traceback (most recent call last)
    <ipython-input-23-7e9a4afcf0f8> in <module>()
    ----> 1 h_mod = hack.modified
          2 h_mod

    /Users/michaelmartinez/.virtualenvs/iPynotebook/lib/python2.7/site-packages/feedparser.pyc in __getattr__(self, key)
        414             return self.__getitem__(key)
        415         except KeyError:
    --> 416             raise AttributeError, "object has no attribute '%s'" % key
        417 
        418     def __hash__(self):

    AttributeError: object has no attribute 'modified'

In[24]:


    :::python
    h_tag = hack.etag
    h_tag



    ---------------------------------------------------------------------------
    AttributeError                            Traceback (most recent call last)
    <ipython-input-24-569f4162a64d> in <module>()
    ----> 1 h_tag = hack.etag
          2 h_tag

    /Users/michaelmartinez/.virtualenvs/iPynotebook/lib/python2.7/site-packages/feedparser.pyc in __getattr__(self, key)
        414             return self.__getitem__(key)
        415         except KeyError:
    --> 416             raise AttributeError, "object has no attribute '%s'" % key
        417 
        418     def __hash__(self):

    AttributeError: object has no attribute 'etag'

In[22]:


    :::python
    hack.status


Out[22]:


    301



In[25]:


    :::python
    p_tag = planet_python.etag
    p_tag


Out[25]:


    u'"17d8206-c0c4e-4dd1fe032e880"'



In[26]:


    :::python
    p_mod = planet_python.modified
    p_mod



    ---------------------------------------------------------------------------
    AttributeError                            Traceback (most recent call last)
    <ipython-input-26-71aec7e6b70b> in <module>()
    ----> 1 p_mod = planet_python.modified
          2 p_mod

    /Users/michaelmartinez/.virtualenvs/iPynotebook/lib/python2.7/site-packages/feedparser.pyc in __getattr__(self, key)
        414             return self.__getitem__(key)
        415         except KeyError:
    --> 416             raise AttributeError, "object has no attribute '%s'" % key
        417 
        418     def __hash__(self):

    AttributeError: object has no attribute 'modified'

In[27]:


    :::python
    planet_python.status


Out[27]:


    304



In[28]:


    :::python
    hack.debug_message


Out[28]:


    'The feed has not changed since you last checked, so the server sent no data.  This is a feature, not a bug!'



In[29]:


    :::python
    planet_python.debug_message


Out[29]:


    'The feed has not changed since you last checked, so the server sent no data.  This is a feature, not a bug!'



I really hope this proves useful as I could not find a tutorial or demo using
this package/library. Thanks for reading!

                  
