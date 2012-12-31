Title: Twitter Bootstrap with Html5 Boilerplate's Build
Date: 2012-02-20
Author: Michael


[Twitter bootstrap][] is a great piece of kit. [Html5 boilerplate
(h5bp)][] is also a great piece of kit. Those of you who have used h5bp
know it also comes bundled (or not?) with a great [ant build script][].
This build script automagically builds, minifies, compresses,
concatenates, lints and hints the files you specify. A ton of crap,
really.

You will have to read the [documentation][] as it makes some assumptions
in regards to your project scaffolding and what-have-you. Seriously,
read the documentation. You don't have to trust me when I say its worth
it, but it is.

So now that I found this script, I want to use it on every project. Once
everything is set-up it is just so easy to run. I have forced myself to
use it on trivial tests and what not. My [lab page][] is a total
work-in-progress and made with Twitter bootstrap. I thought I would show
you how I integrated h5bp ant-build-script with it.


As you can see, I mimicked the file structure that h5bp recommends in
the documentation (RTFM, right?)

I then modified the project. properties file to include the changes you
see here:

    :::ant
    # project.properties file defines overrides for default.properties

    # Explanation: This file should be created by each user as and when he or she needs to override particular values.
    # Consequently, it should not be placed under version control.

    # Stylesheets
    #
    # Note: Stylesheets will be concatenated in the order they are listed in the file.stylesheets property (i.e. the last
    # file listed will be at the end of the concatenated file), so it probably makes sense to have the main style.css file
    # as the first entry
    # Example:
    # file.stylesheets  = style.css, lightbox.css, plugin.css
    #
    file.stylesheets  = bootstrap.css, style.css

    # Web Pages
    #
    # These are the pages (files) that will be served to users (.html, .php, .asp, etc). Files in this property will
    # be minified / optimised and have any stylesheet or javascript references updated to the minified examples
    #
    # The paths need to be relative
    #
    # Files can be added in a comma separated form
    file.pages        = toolbox.html, vacapp.html 

    # Excluded files and dirs
    #
    # Add any files or directories you add to the project and do not want to be copied to the publish directory as a
    # comma separated list
    # These files are ignored in addition to the default ones specified in default.properties.
    # Example: file.exclude = badfolder/**
    file.exclude      = js/tests/**, style/less/**, 

    # Bypassed JavaScript files and dirs
    #
    # Add any files or folders within the mylibs directory that you want to be copied to the publish directory as a
    # comma separated list
    # These files will not be concatenated or minimized and will simply be copied over as is.
    # Note: you cannot declare an empty file.bypass property, it would exclude the entire mylibs folder
    # Example:
    # file.js.bypass = widgets.js, gadgets.js, gidgets.js
    file.js.bypass = cafflab.js

    # Directory Structure
    #
    # Override any directory paths specific to this project
    #
    # dir.publish
    # dir.js
    #dir.js.libs = js/bootstrap
    #dir.js.mylibs = js/bootstrap
    dir.css = style/css
    # dir.img

Note: I've only included the actual changes to my file. The actual
project.properties is a bit denser.

I haven't gone all-the-way with the power of the build script thus far.
As you can see, I am not fully concatenating my javascript and css
files. However, they are fully linted, hinted and compressed which is
better than nothing, I suppose. I will keep working and making
refinements to this process, but I've seen the light with an
intermediate build step in deployment. It is so full of win, that I
can't imagine doing it another way.

If you simply use build like I have, you will save a tremendous amount
of time optimizing your pages for production. Once you see this in
action... You will have a hard time turning back as well, I reckon.

Todo: Work out how to force the build script into nested directories for
the manifest. Maybe even get a wild hair and attempt to write a pre
build-build that analyzes the project structure.

  [Twitter bootstrap]: http://twitter.github.com/bootstrap/
  [Html5 boilerplate (h5bp)]: http://html5boilerplate.com/
  [ant build script]: https://github.com/h5bp/ant-build-script
  [documentation]: http://html5boilerplate.com/docs/Build-script/
  [lab page]: http://lab.caffeineindustries.com
  []: http://caffeineindustries.com/wp-content/uploads/2012/02/Screen-shot-2012-02-20-at-4.31.30-PM-225x300.png
    "Screen shot 2012-02-20 at 4.31.30 PM"
  [![][]]: http://caffeineindustries.com/wp-content/uploads/2012/02/Screen-shot-2012-02-20-at-4.31.30-PM.png
