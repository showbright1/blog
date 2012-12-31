Title: Coffeescript, Jasmine and Katas
Date: 2012-03-10
Author: Michael


Hey-O!

[CoffeeScript][] is nice. It provides syntactic sugar and adds
tremendous functionality to the web developers tool-chest. Those who
appreciate terse, yet readable and well formatted code; CoffeeScript
will seem like a manna from heaven. I find that I am already looking at
my JavaScript and refactoring it in my head to CoffeeScript.

On long road trips I generally have a few hours to kill while the rest
of the family is asleep. I generally take this time to fire up some
podcasts and/or tutorials and to learn as I drive. I actually look
forward to this time as I can almost totally focus on the content.

This trip I decided to load my Galaxy Nexus with a metric ton of
CoffeeScript screen casts (just audio) and podcasts. My intention was to
get the basics out of the way and I accomplished that objective.

Since I've returned home, I have decided to stick with CoffeeScript and
add a few more. I have decided that my code needs to tested more
throughly. CoffeeScript has made testing a complete breeze.

I've also become a believer in dedicated, [deliberate practice][]. One
can constantly reuse the same patterns and never really push themselves
to get better. However, those who deliberately practice techniques and
patterns they are not comfortable with generally begin to excel faster
than those who just put in the hours haphazardly.

I used [this code kata][] with CoffeeScript and Jasmine.

Click the post image to see the passing tests!

Here is my solution:

The Spec's in CoffeeScript

    :::coffee
    describe "StringCalc", ->
        describe "constructor with null", ->
          beforeEach ->
            @mystrCalc = new StrCalc()

          it 'replaces null with 0', ->
            (expect @mystrCalc.firstNum).toEqual 0

        describe "constructor with zero ", ->
          beforeEach ->
            @mystrCalc = new StrCalc('0')

          it 'replaces "0" with 0', ->
            (expect @mystrCalc.firstNum).toEqual 0

        describe "constructor with multiple numbers", ->
          beforeEach ->
            @mystrCalc = new StrCalc('1, 2, 3')

          it 'matches first arg to firstNum', ->
            (expect @mystrCalc.firstNum).toEqual 1

          it 'matches second arg to secondNum', ->
            (expect @mystrCalc.secondNum).toEqual 2

          it 'matches third arg to thirdNum', ->
            (expect @mystrCalc.thirdNum).toEqual 3

        describe "add method", ->
          beforeEach ->
            @mystrCalc = new StrCalc('2, 4, 6')

          it 'adds three arguments of StrCalc', ->
            (expect @mystrCalc.total).toEqual 12

        describe "add method with bigger numbers", ->
          beforeEach ->
            @mystrCalc = new StrCalc('20\n40, 60')

          it 'adds three arguments for big numbers and wacky delimiters', ->
            (expect @mystrCalc.total).toEqual 120

The implementation in CoffeeScript:

    :::coffee
    window.StrCalc = class StrCalc

        constructor: (myStr = 0) ->
          if myStr is '0' or myStr is 0
            @firstNum = 0
          else
            @parseMyNum myStr

        parseMyNum: (myStr) ->
          pattern = /(\d)+.*?(\d*)/gm
          result = myStr.match pattern
          @firstNum = parseInt result[0]
          @secondNum = parseInt result[1]
          @thirdNum = parseInt result[2]
          @add()

        add: ->
          @total = @firstNum + @secondNum + @thirdNum

Paste the CoffeeScript [here][] to see what it looks like in JavaScript.

  [CoffeeScript]: http://coffeescript.org/
  [deliberate practice]: http://www.missiontolearn.com/2010/04/deliberate-practice/
  [this code kata]: http://osherove.com/tdd-kata-1/
  [here]: http://js2coffee.org/
