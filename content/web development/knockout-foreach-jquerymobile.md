Title: Using Knockoutjs's foreach on nested jQuery Mobile lists
Date: 2012-02-22
Author: Michael


I just want to drop a quick note to anyone who may search google for a
problem I ran into.A nested jQuery mobile list can be populated with one
knockoutjs observable array. The only caveat I've seen thus far is that
you need to use the foreach data-binding twice. Once on the outer list
and again for the inner "list" or page.

Example:

    :::html
    <ul data-role="listview"  data-bind="foreach: watched">
            <li data-role="list-divider"> Repo: <h3 data-bind="text: name"></h3>
                <ul data-role="listview" data-bind="foreach: watched">
                    <li><h4>Description:</h4>
                        <p data-bind="text: description"></p>
                <span class="ui-li-count">Forks: <span data-bind="text: forks"></span> - Issues: <span
                        data-bind="text: open_issues"></span>
                                          - Watchers: <span data-bind="text: watchers"></span></span>
                        <p> <h4>Language: </h4>
                        <p data-bind="text: language"></p></p>
                        <p> <h4>Owner:</h4>
                        <p data-bind="text: owner"></p></p>
                        <p> <h4>URL:</h4>
                        <p data-bind="text: url"></p>
                    </li>
                </ul>
            </li>
        </ul>
