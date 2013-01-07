Title: Installing iPython Notebook on Mountain Lion
Date: 2013-01-06
Author: Michael Martinez

I've successfully installed iPython Notebook on a few different versions of OSX
in recent months. There are quite a few methods of accomplishing this task and
many of them seem quite elegant. The fact remains that installing iPyNB is not
as strait forward as one might like and hopefully you find this of some utility.

*******

## Dependencies ##


This was built on a Mac running OSX 10.8.2 with the [command line tools](http://developer.apple.com/downloads)
installed. I deleted my version of Xcode because it takes up a lot of space on
my SSD and I am not a mac dev (at the moment). You can sign up for a free ID with
Apple to get the download and there are lots of other goodies in the download area.

My system also has the package manager [Homebrew](http://mxcl.github.com/homebrew/)
installed. You could probably build everything here by hand, but why not
leverage community efforts that lead to less stress, effort and error prone
configuration? Install Homebrew, be happy and get to work orders of magnitude
faster.

*******

## System Configuration ##


The C language ecosystem is a bit perplexing as an outsider with no real experience
with the language and tool-chain. Thanks to the good people at Google, we can enter
the foray with battle paint and Bluetooth keyboards. In all seriousness, I am not
entirely sure why I had to do these steps with OSX Mountain Lion... but I did
and you might want to follow suit.

* [Thoughtbot ML Stuff](http://robots.thoughtbot.com/post/27985816073/the-hitchhikers-guide-to-riding-a-mountain-lion)
* [Get Homebrew and ML to be happy](https://gist.github.com/3182604)

...et cetera, et cetera...

The "fix" I came to realize after lots of head banging was *Critical* as ML ships with llvm-gcc-4.2.
Homebrew and a _lot_ of the software it builds do not like llvm-gcc-4.2. They make
it known when they refuse to install the packages you've requested. Here is what
you do:

    :::bash
    $ sudo ln -s /usr/bin/llvm-gcc-4.2 /usr/bin/gcc-4.2

Yep, not much... but boy was that frustrating to figure out. The other story here
is to download X11 via [Quartz 2.7.2+](http://xquartz.macosforge.org/trac/wiki),
then install and symlink it in:

    :::bash
    $ ln -s /opt/X11 /usr/X11

*******

## iPython Install ##


Now that we have that fun stuff taken care of we can install iPython Notebook
and some science-y tools. To get started you should probably look into some kind of environment manager.
[virtualenv burrito](https://github.com/brainsik/virtualenv-burrito) is a good start to get up and running quickly.
I know there are many ways to skin this cat: pythonbrew, virtualenv, virtualenvwrapper.

Pick one and go for it. I was weary of Pythonbrew until a few weeks ago when it
became active again. I think it is the closest thing to Ruby's RVM and it worked
for me in a VM. However, I wanted to try virtualenv burrito as it nicely packages
virtualenv += wrapper and has performed flawlessly thus far. Seriously pick one
move on.

    :::bash
    $ mkvirtualenv ipy

Now that we have a new virtualenv, lets get installing:

    :::bash
    $ workon ipy
    $ pip install ipython

Once ipython has finished installing we need to install readline

    :::bash
    $ pip install readline

Then we install tornado for iPython Notebook

    :::bash
    $ pip install tornado

The next item is the installation of the ZeroMQ library. Ultimately we want to install
pyzmq. However, its a bit dicey using pip for reasons explained on their repo page
[here](https://github.com/zeromq/pyzmq#mac-osx).

    :::bash
    $ brew install zeromq --universal

Once that is completed we can now install pyzmq with pip:

    :::bash
    $ pip install pyzmq

Next is the install of pygments for syntax highlights:

    :::bash
    $ pip install pygments

After pygments installs we need to install freetype and libpng via
Homebrew. The reason we want ipython is for the super awesome graphics,
right? Well, you need these badboys to get super awesome graphics.

    :::bash
    $ brew install freetype
    $ brew install libpng

Now time to install pyqt. I believe there is some misconception about pyqt and
what is needed to install it correctly. If you followed this [Sympy wiki entry](https://github.com/sympy/sympy/wiki/Installing-the-IPython-qtconsole-in-Mac-OS-X)
you would install the QT stuff prematurely. Before I installed pyqt, I had a gander
at the Homebrew formula. In it, I noticed that pyqt will download and install all the
dependencies to make it work. I am telling you, Homebrew will make you happy!!!

    :::bash
    $ brew install pyqt

YOU HAVE DONE IT!!! You now have a fully functional iPython qtconsole and notebook.
I suggest installing in this order to minimize errors.

*******

## Science Modules ##


Now lets install numpy

    :::bash
    $ pip install numpy

We need some fortran to compile scipy, so before we can install scipy we need:

    :::bash
    $ brew install gfortran

Note: I found that homebrew would hang on the mpfr dependency. I filed a bug and
it was [fixed](https://github.com/mxcl/homebrew/commit/4900ad83b973f0db32f8808193f2ec55ffd4f412)
in less than 8 hours on a Sunday. That is Fucking Awesome. (not much else to say)

Now we can go get scipy:

    :::bash
    $ pip install scipy

Some folks recommend installing matplotlib from git on ML. I took one for the team
and just let it rip with pip and it worked great.

    :::bash
    $ pip install matplotlib

These are probably the bare essentials to get started with some science. You may
want to install Pandas, Sympy, stats models, pymc and others if you are a ninja. I am
in the process of learning the math required to really use these libraries/modules,
so I am definitely not a ninja just yet... but watch this space.

Here are some cool notebooks to play around with:

* [Invisibleroads CrossCompute](https://github.com/invisibleroads/crosscompute-tutorials)
* [What can iPython Notebook do?](https://github.com/ipython/ipython/tree/master/docs/examples/notebooks)
* [Machine Learning with iPython Notebooks](https://github.com/masinoa/machine_learning)
