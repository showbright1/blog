
$(document).ready(function(){
Chirp({
    user: 'monkmartinez',		//Twitter username
    max: 2,			//Maximum number of tweets to show
    count: 10,			//Total tweets to retrieve
    retweets: true,			//Show/Don't show retweets
    replies: false,			//Show/Don't show replies
    cacheExpire: 1000 * 60 * 2,	//Number of milliseconds to cache tweets
    templates: {
                                      base:'<ul class="chirp">{{tweets}}</ul>',
                                      tweet: '<li><a href="http://twitter.com/{{user.screen_name}}" title="{{user.name}} — {{user.description}}"><img src="{{user.profile_image_url}}"></a> {{html}}<span class="meta"><time><a href="http://twitter.com/{{user.screen_name}}/statuses/{{id_str}}">  {{time_ago}}</a></time></li>'
                      },
                target: 'tweets'
        });




    $('.p2col .span6:even').addClass('no-margin-left');

    //Menu
    jQuery('#menu > ul').superfish({
        delay:       1000,
        animation:   {opacity:'show', height:'show'},
        speed:       'fast',
        autoArrows:  true

    });
    $('.sf-sub-indicator').remove();
    (function() {
                var $menu = $('#menu ul'),
                        optionsList = '<option value="" selected>Menu...</option>';

                $menu.find('li').each(function() {
                        var $this   = $(this),
                                $anchor = $this.children('a'),
                                depth   = $this.parents('ul').length - 1,
                                indent  = '';

                        if( depth ) {
                                while( depth > 0 ) {
                                        indent += ' - ';
                                        depth--;
                                }
                        }
                        optionsList += '<option value="' + $anchor.attr('href') + '">' + indent + ' ' + $anchor.text() + '</option>';
                }).end()
                  .after('<select class="res-menu">' + optionsList + '</select>');

                $('.res-menu').on('change', function() {
                        window.location = $(this).val();
                });

        })();

    $(".our-blog article").hover(function () {
        $(this).find("img").stop(true, true).animate({ opacity: 0.7 }, 300);
    }, function() {
        $(this).find("img").stop(true, true).animate({ opacity: 1 }, 300);
    });


        //Portfolio
        var $portfolioClone = $(".filtrable").clone();
        $("#filtrable a").live('click', function(e){

                $("#filtrable li").removeClass("current");

                var $filterClass = $(this).parent().attr("class");
        var $filteredPortfolio = $portfolioClone.find("article");

                if ( $filterClass == "all" ) {
                        $filteredPortfolio = $portfolioClone.find("article");
                } else {
                        $filteredPortfolio = $portfolioClone.find("article[data-type~=" + $filterClass + "]");
                }

                $(".filtrable").quicksand( $filteredPortfolio, {
                        duration: 800,
                        easing: 'easeOutQuint'
                }, function(){

            $('.da-thumbs > li, .da-thumbs > article, .da-thumbs > div').hoverdir();

            $("a[rel^='prettyPhoto']").prettyPhoto();

                });

                $(this).parent().addClass("current");

                e.preventDefault();
        });

    // To Top Button
    $(function(){
        $().UItoTop({ easingType: 'easeOutQuart' });
    });

});


$(window).load(function() {

    $(function () {
        $(".lightbox-image").append("<span></span>");
        $(".lightbox-image").hover(function () {
            $(this).find("img").stop().animate({opacity:0.5}, "normal")
        }, function () {
            $(this).find("img").stop().animate({opacity:1}, "normal")
        })
    });

    $('#top-menu .top-line .btn').click(function(){
        $('#top-menu .top-line .block').html('');

    });

});
