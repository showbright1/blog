Title: AS3 MadComponents Tutorial Series - Tablet and Phone in One!
Date: 2011-09-12
Author: Michael


This tutorial will demonstrate both tablet and phone layout in one
ActionScript 3 Flash application for mobile. We will utilize the
powerful [MadComponents library][] to quickly and easily add an amazing
spilt screen view for the tablet. Then we will basically recycle the
phone tutorial shown in the previous [separation of concerns
tutorial][].

Tablets such as the iPad and Android variants have quite a bit more
screen real estate to work with. We can literally replicate a desktop
experience with the tablet resolutions we are seeing today. So what
should we do with all of this real estate? The answer to that question
is; It depends. I know that is a bit of a cop-out, but we can not
realistically attempt to cover every situation.

This app will determine the screen resolution and choose the best layout
to initialize. The table will utilize the popular split-view pattern for
the tablet with a list control on the left side and content on the
right. The phone layout consists of list based navigation as shown in
the previous [example.][separation of concerns tutorial]

DISCLAIMER: The colors used are ATROCIOUS. I did this to make absolutely
sure the tutorial-ee can see what colors are used and where. Its a bit
confusing and you'll need to experiment anyway.

The SRC files can be downloaded [HERE][].

Lets get this party started:

    :::as3
    package
    {
        import com.danielfreeman.madcomponents.*;

        import flash.desktop.NativeApplication;
        import flash.display.Sprite;
        import flash.display.StageAlign;
        import flash.display.StageScaleMode;
        import flash.events.Event;
        import flash.events.KeyboardEvent;
        import flash.events.MouseEvent;
        import flash.system.Capabilities;
        import flash.ui.Keyboard;

        public class SplitViewMAD extends Sprite
        {
        //////////////////////////// DATA FOR BOTH APPLICATIONS ////////////////////////////
            protected static const DATA:XML = <data>
    <item label="List Item 1"/>
    <item label="List Item 2"/>
    <item label="List Item 3 (this wrapping text; test test test test)"/>
    <item label="List Item 4"/>
                </data>;
        //////////////////////////// END DATA //////////////////////////////////////////////	

        /////////////////////////// TABLET XML DEFINITION //////////////////////////////////	
            // List can also be masked for a wrapping effect
            protected static const SPLITVIEW:XML = <columns stageColour="#A15D6F" id="myCols" gapH="4" widths="36%, 64%" background="#707449">
    <vertical id="myScroll" background="#E4D1B0"><list id="myList" colour="#c10000" autoLayout="true"><search colour="#D66821" field="label"/>{DATA}<label id="label" alignH="fill"/></list></vertical>
    <pages id="myPages">{Page0.LAYOUT}{Page1.LAYOUT1}{Page2.LAYOUT2}{Page3.LAYOUT3}</pages>
    </columns>;

            protected var _page:UIPages;

        /////////////////////////// END TABLET ///////////////////////////////////////////////

        /////////////////////////// PHONE XML DEFINITIONS ///////////////////////////////////	

            protected static const LIST:XML = <list colour="#999999" background="#DADED4"><search colour="#DADED4" field="label"/>{DATA}</list>;

            // Each additional "Page" needs to have different id's for the components, even when they are separated into separate classes
            protected static const NAVIGATION:XML = <navigation id="nav" colour="#C100000" clickColour="#C100000" title="Phone Nav">
                {LIST}
            {Page0.LAYOUT}
            {Page1.LAYOUT1}
            {Page2.LAYOUT2}
            {Page3.LAYOUT3}
            </navigation>;

            protected var _uiNavigation:UINavigation;
            protected var _list:UIList;
        ////////////////////////////// END PHONE //////////////////////////////////////////////	


        ///////////////////////////// INDEPENDENT CLASS VARS //////////////////////////////////	
            protected var _resY:int = Capabilities.screenResolutionX;
            protected var _resX:int = Capabilities.screenResolutionY;
            protected var _dpi:int = Capabilities.screenDPI;
        ///////////////////////////// END CLASS VARS //////////////////////////////////////////

The comments should visually separate the XML. The order in which you
define this data is absolutely inconsequential.

The DATA constant is used for both layouts. I'm quite sure there are a
myriad of optimizations you could make here, but I wanted to make this
as clear as possible for the uninitiated.

Lets concentrate on the SPLITVIEW constant for a bit. The root node or
tag is **columns**. We can use any numbers we like here. 36% for the
left column and 64% for the right looked good on my Galaxy Tab 10.1
Android tablet.

After columns, you'll see the <vertical> node and it is the container
for the left column. I choose to define the list here. You can get
really creative and add images and/or other components in this column.
The main thing to consider is text wrapping. If you aren't careful or
have long labels, the text will spill onto the next column. In this
case, I set **autoLayout = true** in the list node. Then we define the
actual label node contained in the DATA constant with this tag; \< label
id="label" alignH="fill" /\>. This will make your text wrap nice and
neat.

The right column is defined in the \< pages \> node. This, again, can be
any node you'd like for your particular application but page worked well
for this example. Note that we once again defined our pages outside this
class and call them by their LAYOUT constant, then initialize them in a
later method. You don't need to specify LAYOUT followed by a number, as
LAYOUT or any other name will work just as well. I do that because,
again, my brain works best with everything separated as cleanly as
possible.

The independent class vars grab the screen resolution in the X and Y
axis and also provide the screen DPI. This will enable us to make the
right decision on which layout we like to display.

Lets move onto the constructor:

    :::as3
    //////////////////////////// CONSTRUCTOR /////////////////////////////////////////////	
    public function SplitViewMAD(screen:Sprite = null) {

        if (screen){
            screen.addChild(this);
        }

        trace("Screen Resolution is " + _resX + "x" + _resY + " at " + _dpi + "ppi");

        // support autoOrients
        stage.align = StageAlign.TOP_LEFT;
        stage.scaleMode = StageScaleMode.NO_SCALE;

        // If the screen in the Y-axis is larger than 855px init tablet layout
        if(_resY >= 855){
        initializeTablet();
        } 
        // If the screen in the Y-axis is smaller than 855px init Phone layout
        if(_resY <= 855){
        //Register the back button listener in constructor before UI.create and all is well
        stage.addEventListener(KeyboardEvent.KEY_DOWN, goBackButton);
        initializePhone();
        }
    }


This constructor simply chooses to initialize the phone or tablet based
on the resolution in the Y-axis. The number I decided to use for a break
over is 855px because I'm testing on the OG Droid-1 (480x854) and a
Galaxy 10.1 tablet (800 x 1290). I needed a way to make sure that the
proper layout is initializing (you know, that it actually works). A more
robust switch statement or if/else block is absolutely more appropriate
in a real world scenario based on the devices one is targeting.

The only gotcha here is the physical Android back button in the
initializePhone block. The physical Android back button listener needs
to be called before UI.create, which is in the initializePhone method,
to work properly.

In the interest of keeping all the logic available to copy and paste
here is the phone logic. Note: its not materially different than the
[previous tutorial][separation of concerns tutorial].

    :::as3
    ////////////////////// PHONE ////////////////////////
    private function initializePhone():void
    {
        // Create the main UI or "Landing Page"
        UI.create(this, NAVIGATION);

        // Initialize "views"
        // Initialize "views"
        Page0.initialize();
        Page1.initialize();
        Page2.initialize();
        Page3.initialize();

        // Navigation layout and behaviour 
        _uiNavigation = UINavigation(UI.findViewById("nav"));
        _uiNavigation.autoForward = false;
        _uiNavigation.autoBack = false;
        // Change page handler
        _uiNavigation.addEventListener(UIList.CLICKED, navigationChange);
        _uiNavigation.navigationBar.backButton.addEventListener(MouseEvent.MOUSE_UP, goBack);
        // Nav back button color
        _uiNavigation.navigationBar.backButton.colour = 999999;


    }

    // Handles List item clicks
    public function navigationChange(event:Event):void {

        var navIndex:int = _uiNavigation.index;
        // Check to see if current page is @ 0 to set correct title
        if(_uiNavigation.pages[0]){
            _uiNavigation.title = "Phone Nav";
        }

        // navigation logic 
        if(navIndex == 0){
            _uiNavigation.goToPage(2, UIPages.SLIDE_LEFT);
            _uiNavigation.title = "Page 1";
        } else if (navIndex == 1){
            _uiNavigation.goToPage(3, UIPages.SLIDE_LEFT);
            _uiNavigation.title = "Page 2";
        }else if (navIndex == 2){
            _uiNavigation.goToPage(4, UIPages.SLIDE_LEFT);
            _uiNavigation.title = "Page 3";
        }
    }
    // Nav bar back button
    protected function goBack(event:Event):void {
        var navIndex:int = _uiNavigation.index;
        _uiNavigation.goToPage(0, UIPages.SLIDE_RIGHT);
        _uiNavigation.title = "Phone Nav";
        trace("NavBar Event fired");
    }
    // Device back button handler
    protected function goBackButton(event:KeyboardEvent):void
    {
        // With autoBack set to false, you lose the back button for some reason
        // You can use the Native App library to hard check a back button press
        var navIndex:int = _uiNavigation.index;
        if(event.keyCode == Keyboard.BACK){
            _uiNavigation.goToPage(0, UIPages.SLIDE_RIGHT);
            _uiNavigation.title = "Phone Nav";
            trace("Keyboard event fired");
        }
    }	
    //////////////////////// END PHONE /////////////////////////////

Next we'll look at the tablet specific code:

    :::as3
    /////////////////////// TABLET ////////////////////////////////
    private function initializeTablet():void
    {
        // Create the main UI or "Landing Page"
        UI.create(this, SPLITVIEW);

        // Initialize "views"
        Page0.initialize();
        Page1.initialize();
        Page2.initialize();
        Page3.initialize();  

        // Add the list 
        _list = UIList(UI.findViewById("myList"));
        _list.addEventListener(UIList.CLICKED, changePage);

        // Add the pages component
        _page = UIPages(UI.findViewById("myPages"));

    }

    protected function changePage(event:Event):void
    {
        // TODO: holder page @ index 0 in DATA constant so first page is 1 and second is two. Holder will have a cool logo or something
        var index:int = _list.index;

        // Navigation logic 
        if(index == 0){
            _page.goToPage(1,UIPages.SLIDE_RIGHT);
        } else
        if (index == 1){
            _page.goToPage(2,UIPages.SLIDE_RIGHT);
        } else
        if (index == 2){
            _page.goToPage(3,UIPages.SLIDE_RIGHT);
        }
    }
    ////////////////////// END TABLET ////////////////////////////////
    }
    }

We call UI.create and pass in the SPLITVIEW constant. This is the
MadComponents standard, so if don't get it... I suggest you to have a go
with the other tutorials on [Daniels][MadComponents library] site or
mine. Next, we initialize all the pages that reside outside of this
class, but are defined in the pages node.

We need a way to capture the clicks for the list on the left. So we
instantiate a UIList variable to hold the list data. We then assign a
click listener to the list variable. We also need a mechanism to
navigate the pages once we've determined which list item has been
clicked. So, again we assign a UIPages variable to hold and act on that
data. This is all handled in the changePage event handler which is
relatively self explanatory. I'm still working on the Android back
button for this block. I will update it once I get it handled.

I hope this helps you visualize what is possible with tablets and the
ActionScript3 MadComponent Library. Expect more tutorials to follow!

**This is a screen shot of the tablet running this app:**

![Tablet Split View][]

**This is a screen shot of the phone running this app:**

![Phone Split View][]

  [MadComponents library]: http://madskool.wordpress.com/
  [separation of concerns tutorial]: http://caffeineindustries.com/?p=234
  [HERE]: http://www.mediafire.com/file/d4sbql4o0x44uhd/src.zip
  [Tablet Split View]: http://caffeineindustries.com/wp-content/uploads/2011/09/splitviewtablet800.png
  [Phone Split View]: http://caffeineindustries.com/wp-content/uploads/2011/09/device-2011-09-12-134809.png
