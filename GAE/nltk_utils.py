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

import nltk
import re


blacklist = ["everybody", "anybody", "anyone", "everyone", "nobody", "noone", "do", "dont",
                "he", "she", "her", "him", "yesterday", "today", "tomorrow", "anytime", "anywhere",
                "something", "anything", "everything", "nothing", "i", "you", "a", "thank", "thanks",
                "good", "bad", "once", "twice", "time", "week", "month", "year", "this", "that",
                "then", "now", "don", "don't", "t"]


def findTags(tagPrefix,taggedText,tagResults,useBlacklist = True):
    if useBlacklist:
        cfd = nltk.ConditionalFreqDist((tag, word) for (word, tag) in taggedText
                                        if tag.startswith(tagPrefix) and not (word.lower() in blacklist))
    else:
        cfd = nltk.ConditionalFreqDist((tag, word) for (word, tag) in taggedText
                                        if tag.startswith(tagPrefix))

    if tagResults < 1:
        return dict((tag, cfd[tag].keys()[:len(cfd[tag].keys())]) for tag in cfd.conditions())

    return dict((tag, cfd[tag].keys()[:tagResults]) for tag in cfd.conditions())


def getTagsAndFreqDist(inputText):
    # Take out some punctuation to avoid cases like: grandmother - grandmother's
    # or door - cottage-door
    inputText = re.sub("[.\-'']", " ", inputText)

    tokenizedText = nltk.word_tokenize(inputText)
    tags = nltk.pos_tag(tokenizedText)
    freqDist = nltk.FreqDist(tokenizedText)

    return (tags, freqDist)
