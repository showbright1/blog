Title: NFLgame - Python for American Football
Date: 2013-03-17
Author: Michael Martinez

NFLgame is a Python package that allows programmatic access to NFL data.
It is a super fun way to get stats about your favorite NFL player or team.
My plan is more sinister as I attempt to leverage this in my quest to win a
fantasy football league.

The Github repo is located [here.](https://github.com/BurntSushi/nflgame)

<a class="btn btn-large" href="/static/ipynb/NFL.ipynb"><i class="icon-download-alt"></i> Download this Notebook</a>

In[1]:

    :::python
    import nflgame


### Lets have a look at some basic stats for the last 3 games of the NFL Regular season ###

First we'll have a look at the top 25 rushers for weeks 15, 16, 17. Awesome that we get
summary stats right out of the box, right?

In[15]:

    :::python
    games = nflgame.games(2012, week=[15, 16, 17])
    players = nflgame.combine(games)
    for p in players.rushing().sort("rushing_yds").limit(25):
        print p, p.rushing_yds



    A.Peterson 497
    A.Morris 378
    M.Lynch 324
    D.Williams 322
    C.Spiller 300
    J.Charles 289
    A.Foster 276
    M.Forte 260
    V.Ballard 252
    K.Moreno 240
    B.Pierce 232
    D.Martin 220
    S.Jackson 206
    C.Johnson 206
    D.McFadden 200
    D.Murray 197
    R.Bush 195
    M.Ingram 182
    S.Ridley 181
    S.Greene 180
    R.Wilson 179
    F.Gore 179
    M.Leshoure 158
    R.Rice 150
    D.Wilson 147


Next, we'll look at the top 25 running backs and the total amount of touchdowns
for weeks 15, 16, 17 using the players variable we created above.

In[16]:

    :::python
    for p in players.touchdowns().sort("rushing_tds").limit(25):
        print p, p.rushing_tds



    A.Morris 6
    M.Tolbert 5
    R.Wilson 4
    C.Wells 3
    M.Forte 2
    R.Grant 2
    M.Turner 2
    M.Ingram 2
    A.Peterson 2
    T.Richardson 2
    K.Moreno 2
    J.Hester 2
    M.Leshoure 2
    D.Williams 2
    M.Lynch 2
    S.Ridley 2
    D.Woodhead 2
    C.Johnson 2
    S.Greene 2
    D.Lewis 1
    A.Dalton 1
    B.Green-Ellis 1
    A.Rodgers 1
    D.Harris 1
    D.Wilson 1


Fumbles are bad in fantasy football, umkay. Lets see the top 25 fumblers for the
same weeks...

In[17]:

    :::python
    for p in players.fumbles().sort("fumbles_tot").limit(25):
        print p, p.fumbles_tot



    P.Rivers 4
    C.Kaepernick 4
    R.Tannehill 3
    M.Sanchez 3
    N.Foles 2
    A.Dalton 2
    J.Cutler 2
    M.Colston 2
    J.Freeman 2
    D.Amendola 2
    C.Ponder 2
    C.Henne 2
    T.Holliday 2
    M.Stafford 2
    R.Fitzpatrick 2
    D.Murray 2
    A.Brown 2
    D.Moore 2
    J.McKnight 2
    T.Yates 2
    C.Harbor 1
    J.Maclin 1
    C.Thornton 1
    A.Green 1
    M.Forte 1

*******

### Now lets have a go with a basic 'player on player' comparison and see if we can dig up any help from the past ###

In my first week of the 2012 Fantasy Football season I had the RB match up
between Marshawn Lynch and Frank Gore. My team started M. "Beast Mode" Lynch and
I came up a bit short... could the outcome have been different with some
analysis? I had other RB's on the bench.

M. Lynch, player ID: 00-0025399

F. Gore, player ID: 00-0023500

The player can be looked up by name or player ID. Iterate through the list of
player in `for` loop and `print p.playerid` or `print p.name` ... or just look
in [players.json](https://github.com/BurntSushi/nflgame/blob/master/nflgame/players.json)
and use `control-f` , then start typing a players name to find
all the available fields for each player.

In[85]:

    :::python
    week1 = nflgame.games(2012, week=1)
    players = nflgame.combine(week1)
    for p in players.rushing().sort("rushing_yds").limit(25):
        if p.playerid == "00-0025399" or p.playerid == "00-0023500":
            print "--------"
            print p.player, p.formatted_stats()

    print "-------"




    --------
    Frank Gore (RB, SF) rushing_lngtd: 23, rushing_tds: 1, rushing_twopta: 0,
    rushing_lng: 23, rushing_yds: 112, rushing_att: 16, rushing_twoptm: 0,
    receiving_tds: 0, receiving_lng: 1, receiving_rec: 1, receiving_twopta: 0,
    receiving_yds: 1, receiving_lngtd: 0, receiving_twoptm: 0
    --------
    Marshawn Lynch (RB, SEA) rushing_lngtd: 0, rushing_tds: 0, rushing_twopta:
    0, rushing_lng: 11, rushing_yds: 85, rushing_att: 21, rushing_twoptm: 0,
    receiving_tds: 0, receiving_lng: 7, receiving_rec: 2, receiving_twopta: 0,
    receiving_yds: 12, receiving_lngtd: 0, receiving_twoptm: 0, fumbles_trcv: 0,
    fumbles_tot: 1, fumbles_rcv: 0, fumbles_yds: 0, fumbles_lost: 0
    -------


Lets have a look at three, first game, match-ups between the 49'ers and the Seahawks.

In[144]:

    :::python
    game12 = nflgame.one(2012, 7, "SF", "SEA")
    print game12.nice_score()
    print '*****'
    print "2012 Away team: %s" % (game12.away)
    # convert the named tuple to dict and iterate with items
    for i, v in game12.stats_away._asdict().items():
        print i, v
    print '-------'
    print "2012 Home team: %s" %game11.home
    # convert the named tuple to dict and iterate with items
    for i, v in game11.stats_home._asdict().items():
        print i, v

    print '-------'




    SF (13) vs. SEA (6)
    *****
    2012 Away team: SEA
    first_downs 13
    total_yds 251
    passing_yds 115
    rushing_yds 136
    penalty_cnt 3
    penalty_yds 20
    turnovers 1
    punt_cnt 4
    punt_yds 194
    punt_avg 31
    pos_time 27:59
    -------
    2012 Home team: SF
    first_downs 12
    total_yds 209
    passing_yds 124
    rushing_yds 85
    penalty_cnt 9
    penalty_yds 102
    turnovers 0
    punt_cnt 5
    punt_yds 298
    punt_avg 54
    pos_time 31:07
    -------


In[145]:

    :::python
    game11 = nflgame.one(2011, 1, "SF", "SEA")
    print game11.nice_score()
    print '*****'
    print "2011 Away team: %s" % (game11.away)
    # convert the named tuple to dict and iterate with items
    for i, v in game11.stats_away._asdict().items():
        print i, v
    print '-------'
    print "2011 Home team: %s" %game11.home
    # convert the named tuple to dict and iterate with items
    for i, v in game11.stats_home._asdict().items():
        print i, v

    print '-------'
    week_11 = nflgame.games(2011, week=1)
    players = nflgame.combine(week_11)
    for p in players.rushing().sort("rushing_yds").limit(25):
        if p.playerid == "00-0025399" or p.playerid == "00-0023500":
            print "--------"
            print p.player, p.formatted_stats()

    print "-------"



    SF (33) vs. SEA (17)
    *****
    2011 Away team: SEA
    first_downs 18
    total_yds 219
    passing_yds 155
    rushing_yds 64
    penalty_cnt 11
    penalty_yds 72
    turnovers 3
    punt_cnt 7
    punt_yds 342
    punt_avg 33
    pos_time 28:53
    -------
    2011 Home team: SF
    first_downs 12
    total_yds 209
    passing_yds 124
    rushing_yds 85
    penalty_cnt 9
    penalty_yds 102
    turnovers 0
    punt_cnt 5
    punt_yds 298
    punt_avg 54
    pos_time 31:07
    -------
    --------
    Frank Gore (RB, SF) rushing_lngtd: 0, rushing_tds: 0, rushing_twopta: 0,
    rushing_lng: 16, rushing_yds: 59, rushing_att: 22, rushing_twoptm: 0,
    receiving_tds: 0, receiving_lng: 12, receiving_rec: 3, receiving_twopta: 0,
    receiving_yds: 19, receiving_lngtd: 0, receiving_twoptm: 0
    -------


In[151]:

    :::python
    game10 = nflgame.one(2010, 1, "SEA", "SF")
    print game10.nice_score()
    print '*****'
    print "2010 Away team: %s" % (game10.away)
    # convert the named tuple to dict and iterate with items
    for i, v in game10.stats_away._asdict().items():
        print i, v
    print '-------'
    print "2010 Home team: %s" %game10.home
    # convert the named tuple to dict and iterate with items
    for i, v in game10.stats_home._asdict().items():
        print i, v

    print '-------'
    week_10 = nflgame.games(2010, week=1)
    players = nflgame.combine(week_10)
    for p in players.rushing().sort("rushing_yds").limit(25):
        if p.playerid == "00-0025399" or p.playerid == "00-0023500":
            print "--------"
            print p.player, p.formatted_stats()

    print "-------"



    SEA (31) vs. SF (6)
    *****
    2010 Away team: SF
    first_downs 14
    total_yds 263
    passing_yds 214
    rushing_yds 49
    penalty_cnt 8
    penalty_yds 60
    turnovers 2
    punt_cnt 6
    punt_yds 249
    punt_avg 35
    pos_time 32:45
    -------
    2010 Home team: SEA
    first_downs 14
    total_yds 242
    passing_yds 165
    rushing_yds 77
    penalty_cnt 5
    penalty_yds 35
    turnovers 1
    punt_cnt 5
    punt_yds 207
    punt_avg 36
    pos_time 27:15
    -------
    -------
*******

So we took a look at the team stats for the last three, first game, match-ups
to see if we could uncover any actionable information. We see that Frank Gore
played in 2011 but not in 2010. Marshawn Lynch did not play in 2011 nor in 2010. Not
much to go on there...

Rushing yards were low in the first two games, which may have suggested that the
third game would have been similar. However, the 2012 match-up had both teams with over 100 yards
rushing which may or may not be an outlier. Now to be thorough, I should compare the
running backs I had on the bench in a similar manner. Then, ultimately, make a reasonable guess.

Not all is lost in this simple analysis, I learned a bit about tuples in the
process. I can also say that I am learning while playing which is 'win-win.' Perhaps the
trophy on my mantle is a bit pre-mature at this point, as I really need to learn statistics
(stay tuned for more on that front).

Here is a neat little tidbit about Named tuples that I learned during this.
The team stats are created in game.py and are delivered as a `namedtuple()`.
The `._asdict()` method on Named Tuples will return an ordered
dict as described [here](http://docs.python.org/release/2.7.4/library/collection
s.html#collections.somenamedtuple._asdict). Once you have a dict, simply use
(chain on) the `.items()` method to iterate over the key and value. If you want
the keys or values by themselves, use the `.keys()` or `.values()` methods
respectively.

I plan on using this extensively next season. In preparation, I have been
learning statistics and the Pandas data analysis python library.

Note: Everything I work on in this space is using iPython Notebook and will
be published for you to run as well...

