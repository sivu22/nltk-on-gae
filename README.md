# nltk-on-gae
Google App Engine hosted application that supports <a href="http://www.nltk.org/">NLTK</a> queries.

# Project details
For the purpose of testing NLTK, a given text is presented as input and a dictionary is returned as output. The dictionary has nouns as keys and frequencies of appearing in the text as values. The dictionary could be "sorted" using the <code>sorted()</code> function, so that the nouns appear in a descending order by frequency value.<br>
<br>
The frequency distribution is calculated for all the tags that have the 'NN' prefix, which means that for a given text, all the nouns will be extracted. In order to refine the text analysis, one could use specific tags, like 'NN$' or 'NN-TL'. For more information on lexical analysis and tags, consult the NLTK documentation.<br>
<br>
Another example of refining the result is the use of a blacklist. The current blacklist, when used, gives (almost) only nouns that could be represented graphically, in a drawing or picture.

# Testing it
A running project can be found at nounfreq.appspot.com. Just do a HTTP POST, allowed parameters are:<br>
<br>
<code>text</code> the text that needs to be analyzed, which must obviously be URL-encoded.<br>
<br>
<code>resultsLimit</code> the number of results obtained for each tag. For the number 2, each tag will give back the 2 most frequent nouns found in the tag's category.
