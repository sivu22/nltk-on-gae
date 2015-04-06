#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Copyright 2014 Cristian Sava
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import webapp2
import json
import nltk_utils


class MainHandler(webapp2.RequestHandler):
    def renderJSON(self, dictionary):
        dataJSON = json.dumps(dictionary)

        self.response.headers["Content-Type"] = "application/json; charset=UTF-8"
        self.response.write(dataJSON)

    def get(self):
        self.response.write('NLTK demo project')

    def post(self):
        inputText = self.request.get("text")
        resultsLimit = self.request.get("resultsLimit")

        dictionary = {}
        if inputText and not inputText.isspace():
            numberOfResults = 0
            if resultsLimit:
                numberOfResults = int(resultsLimit)

            (tags, freqDist) = nltk_utils.getTagsAndFreqDist(inputText)
            tagDict = nltk_utils.findTags('NN', tags, numberOfResults)
            for tag in tagDict:
                for word in tagDict[tag]:
                    if word in dictionary:
                        dictionary[word] += freqDist[word]
                    else:
                        dictionary[word] = freqDist[word]

        self.renderJSON(dictionary)


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
