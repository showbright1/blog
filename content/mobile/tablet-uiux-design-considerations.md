Title: Tablet UI/UX Design Considerations
Date: 2011-05-13
Author: Michael


User Interface / User Experience design is obviously a major aspect of
app design/development and one worthy, in my opinion, of considerable
pontification. I've watched several videos regarding UI / NUI design
and skimmed a few books. This aspect of development is really
interesting to me and I plan on writing about it a lot more.

I really like the video here (click the picture above to play embedded
version). Bill Van Hecke is the lead UI/UX designer for the Omni group
and narrates the entire video. As I madly (digitally) scribbled notes (I
love Evernote)... I thought I'd share.  Full disclosure: Yes, the video
is for iPad... Android is obviously my platform of choice, but I
recognize a good design when I see it. We can learn a lot from the iOS
ecosystem.

Notes:

​1. Brutally Massacre Features - is the app still useful to the average
user without this feature? If not, kill it dead.. at least initially.
Simplify your UI as it helps make it more intuitive. It also helps to
keep the project manageable from a development point of view. As with
most things in life; the KISS principle applies.

​2. The Android tablet is not a giant phone - I'm super guilty of this
as of this writing and I intend on rectifying this post-haste. Don't
simply reuse your main layouts for the large and extra-large resource
layout files. Not only is it super lazy design, its a total waste of
space. Furthermore, you are missing an opportunity to enhance your UX,
thus making your brand and app more desirable.

​3. Adding design "space filler" isn't good practice - Now that you have
more space, adding elements and widgets to fill whitespace isn't good
design. You don't want a NASA Space shuttle cockpit. You need to think
about; control occlusion, accuracy, distractions and context. Hide
buttons/menus behind logically groups menu and button items. Only
display relevant controls for the context of the object in focus.

​4. Progressive disclosure - Universal Principles of Design. If you need
three columns stuffed with controls; you are probably making your user
think way too much, increasing the chance of distraction and not using
the power of contextual menus/buttons. Taps are cheap from a cognitive
load perspective, so make more objects "tap-able" and provide useful
contextual actions based on those taps. The rarer something is, the more
acceptable it is to bury the item deeper in lists.

​5. Taps are especially cheap in the Steering wheel zone - The 90 or so
pixels going down the side of the app are super easy for users to reach
and tap while holding the tablet with two hands. Try to implement the
most actionable / relevant UI elements in this zone. The "middle" of the
app is a great place to display the users content. Be cognizant of
control occlusion.

​6. Think about your user eating a sandwich while using your app - I
think this is pretty self explanatory. Gestures are really neat and fun
when used in the right context. However, if your user constantly has to
maneuver the tablet or reposition themselves to use the app, you are
making them think too much.

​7. Tap, drag/swipe, touch & hold, double tap, pinch / un-pinch, rotate
- These are iOS's gestures. Like it or not my fellow Android-ians... the
Apple Marketing machine has cleverly trained future tablet users while
marketing their wares. They show these "basic" gestures in commercials
and elsewhere and research has shown these to be easily performed with
one hand. Other gestures can be included for "power-users" but don't
make them required.

​8. You have approximately 250ms to show users that a command was
understood before they become confused, angry, anxious or other
emotional state that is undesirable. When a user interacts with the app,
it should respond with "something" be that a glowing, changing of state,
movement, etc. Let your users know that the action they just performed
is valid, even if it wasn't.

​9. Forgiveness - Enable and empower users to explore and exercise
control over the app. Help them feel adventurous. Don't make them afraid
to explore for fear of breaking or ruin something. Playful | fearless, a
big part of the reason why children are better with new technology than
adults. They are AWESOME at failing.

​10. Modality - Lots of basic gestures mean the exact same thing. For
example, the drag can be panning, moving an object, selecting multiple
objects and the list goes on. Setting explicit modes of operations
separates concerns and helps to clearly define how the gesture will
behave in mode. Usability testing becomes very important here. this can
be complicated for the developer and SHOULD make it easier for the user.

​11. Organize the app by meaning, not based on opinion - Your work-flow
may radically differ from your users work-flow. Embrace this, as I
really think this makes designing and implementing the app better for
the user and easier for the developer. DO think about how users will use
the app. DON'T try to predict and code to those assumptions.
