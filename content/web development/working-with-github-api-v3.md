Title: Working with Github Api v3
Date: 2012-02-08
Author: Michael


I was pleasantly surprised when I needed to use the [Github API][] for a
project. The API is dead simple to use, retrive and iterate data for
almost any repo based stat you can imagine. This is just a quick and
dirty GET example that makes a list of all the repos I follow on Github.


    :::html
    $( document ).ready( function () {
 
    var html = "";
    $.ajax( {
      url : "https://api.github.com/users/MichaelMartinez/watched",
      dataType : "jsonp",
      success : function ( returndata ) {
        $.each( returndata.data, function ( i, item ) {
          html += '<li>' +
            '<h3><a href="' + this.html_url + '">' + this.name + '</a></h3>' +
            '<ul>' +
            '<li>' + 'Description: ' + this.description + '</li>' +
            '<li>' + 'Language: ' + this.language + '</li>' +
            '<li>' + 'Updated: ' + this.updated_at + '</li>' +
            '<li>' + 'Owner: ' + this.owner.login + '</li>' +
            '</ul>' +
            '</li>';
        } );
        $( '#result' ).append( html );
      }
    } );
  } );

  [Github API]: http://develop.github.com/p/general.html

