Title: PhoneGap/Callback 1.3.0 - USE IT!
Date: 2011-12-17
Author: Michael


PhoneGap 1.2.0 broke apps when used on devices with Ice Cream Sandwich /
Android 4.0.\* The <meta> tag was being ignored I.e.

    :::html
    <meta name="viewport" content="width=device-width, initial-scale=1.0, 
    minimum-scale=1.0, user-scalable=no" />

This is not parsed by the browser in PG 1.2.0, or is parsed and parsed
incorrectly which made the viewport appear to be very zoomed out.
Whichever case it may be, this is not good for the apps out there using
the amazing Phonegap. I filed a JIRA ticket on the [Apache JIRA Callback
site.][] I was informed by Brion Vibber that 1.3.0 was fixing the issue
and that it had been tagged in git. Alright!

So what do you do?

Well, I cloned PhoneGap from here: https://github.com/callback/phonegap

You then have two options; Build it using Ant or Build it using Eclipse
or similar IDE

I think using a pure Ant is the easiest and I'll explain it here:

​1. Download latest PhoneGap/Callback from git

​2. Make a local.properties with SDK directory with this snippet:

    :::bash
    sdk.dir=/Developer/Development/android-sdk-mac_x86



​3. Then in terminal, navigate (cd /blah/blah) to the "framework"
directory within the Callback directory

​4. type "ant jar" (Hopefully you get no build.xml errors)

​5. Done

The other way is not significantly more difficult but involves more
steps. If all you need is the PhoneGap Jar and \*.js Use the "pure" ant
method. If you want to have a play with the source then by all means use
the IDE to build the file. I will explain it if there is demand.

  [Apache JIRA Callback site.]: https://issues.apache.org/jira/browse/CB-131
