Title: Android and the UI
Date: 2010-11-03
Author: Michael


I just watched the [Google I/O 2010 Android UI Design Patterns video][]
a bit to be sure, but it was very informative and I suggest watching it
when you have the time (1 hour) if you haven't seen it. The video
explained some concepts that I have had trouble grasping for which I'm
very thankful. Hopefully, I'll find more along these lines.

A few of the tutorials I've followed in making apps request the user to
delete the HDPI, MDPI and LDPI folders and simply rename one folder
to Drawable. The talk explains why those folders are not only included
in the initial app structure, but why they are increasingly critical for
cross device penetration. For example, lets say you have app icons that
look great on a medium density pixel per inch screen. If you simply use
the Drawable folder with said icons, when your app encounters a LDPI or
HDPI screen the icons will scale horribly if you haven't accounted for
it in the code.

The talk also spoke to 5 main design paradigms for great Android
applications, which are; Dashboard, Action bar, Search bar, Quick
Actions and Companion widget. I'm not going to get into each one as the
Googlers do a *WAY* better job (with visuals aids) explaining them.  I
found them to a great place to start and perhaps some self introspection
to my own shortcomings when designing just about everything. I think I
should pay way more attention to usability and user expectations.

The QA was really enlightening for me and here is why. I've been
struggling like heck with the Quasi-WYSIWYG & XML based UI editor  in
the Eclipse IDE. I thought I was deficient in my XML coding ability and
I am, BUT I not as bad as I thought. I mean, I had problems making the
simplest things look right in the editor and subsequently the emulator.
Thank goodness I have a real Android device otherwise I would have made
a completely unusable app. Back to the point, A question asked if the
Google Android team was working on a UI editor that either replaced or
updated the "ATROCIOUS" Eclipse implementation. All of the Google
employees on the stage simply looked down and smiled when the question
came in. I think its safe to say that anyone (Including Googlers) who
have worked with the tool thinks of it as a brain-stealing-puppy-killer.

The product manager said they are working on a product to resolve this
very issue but he was not in a position to disclose the details
publicly. Needless to say, I'm eagerly anticipating its release. I hope
they take some strong cues from Microsofts Expression Blend and/or
Design. A tool that would automagically convert PSD/AI files to Android
specific XML files would be so absolutely kick arse. I can't really
think of any adjectives to describe how happy I'd be.

An Aside about tutorials/learning:

Learning from a book is easy when the book has a lot of pictures and
samples/examples. Its not as easy to learn when the book is simply text
and the concept is abstract and non-linear. Perhaps the best method of
learning is the video, at least for me. You can skip ahead in a video,
but its annoying once you realize that you missed something important
and have to rewind. So I generally let it play from start to end. When
I'm nose deep in a book, I have the tendency to jump around and look at
the pictures and read ahead, then back and then I'm lost. This is before
I really understand what I'm looking at which is a of a waste of time
because I have to read it over.

\*Also, don't always blindly accept tutorials as the correct way to do
something simply because it worked. I have learned an important lesson
tonight in regards to this point in the example above.

  [Google I/O 2010 Android UI Design Patterns video]: http://www.youtube.com/watch?v=M1ZBjlCRfz0
    "Google I/O Android UI Design"
