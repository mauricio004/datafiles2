import string


class NewsStory(object):
    def __init__(self, guidx, titlex, subjectx, summaryx, linkx):
        """Creates a News Story"""
        self.guidx = guidx
        self.titlex = titlex
        self.subjectx = subjectx
        self.summaryx = summaryx
        self.linkx = linkx

    def getGuid(self):
        """Returns self's guid (globally unique identifier)"""
        return self.guidx

    def getTitle(self):
        """Returns self's title"""
        return self.titlex

    def getSubject(self):
        """"Returns self's subject"""
        return self.subjectx

    def getSummary(self):
        """Returns self's summary"""
        return self.summaryx

    def getLink(self):
        """Returns self's link (to more content)"""
        return self.linkx

    def __str__(self):
        return 'title:' + self.getTitle()


class Trigger(object):
    def evaluate(self, story):
        """
        Returns True if an alert should be generated
        for the given news item, or False otherwise.
        """
        raise NotImplementedError


class WordTrigger(Trigger):
    def __init__(self, word):
        self.word = word

    def isWordIn(self, text):
        text_copy = text
        for c in text:
            if c in string.punctuation:
                text_copy = text_copy.replace(c, ' ')
        text_copy_list = text_copy.split(" ")
        isWord = False
        for w in text_copy_list:
            if self.word.lower() == w.lower():
                isWord = True
        return isWord


class TitleTrigger(WordTrigger):
    def evaluate(self, story):
        return self.isWordIn(story.getTitle())


class SubjectTrigger(WordTrigger):
    def evaluate(self, story):
        return self.isWordIn(story.getSubject())


class SummaryTrigger(WordTrigger):
    def evaluate(self, story):
        return self.isWordIn(story.getSummary())


class NotTrigger(Trigger):
    def __init__(self, trigger):
        self.trigger = trigger

    def evaluate(self, story):
        return not self.trigger.evaluate(story)


class AndTrigger(Trigger):
    def __init__(self, trigger, trigger2):
        self.trigger = trigger
        self.trigger2 = trigger2

    def evaluate(self, story):
        return self.trigger.evaluate(story) and self.trigger2.evaluate(story)


class OrTrigger(Trigger):
    def __init__(self, trigger, trigger2):
        self.trigger = trigger
        self.trigger2 = trigger2

    def evaluate(self, story):
        return self.trigger.evaluate(story) or self.trigger2.evaluate(story)


class PhraseTrigger(Trigger):
    def __init__(self, phrase):
        self.phrase = phrase

    def evaluate(self, story):
        test = self.phrase in story.getTitle() or self.phrase in story.getSubject() or self.phrase in story.getSummary()
        return test


def filterStories(stories, triggerlist):
    """
    Takes in a list of NewsStory instances.

    Returns: a list of only the stories for which a trigger in triggerlist fires.
    """
    # This is a placeholder (we're just returning all the stories, with no filtering)
    list_stories = []
    for t in triggerlist:
        for s in stories:
            if t.evaluate(s) and s not in list_stories:
                list_stories.append(s)
    return list_stories


def makeTrigger(triggerMap, triggerType, params, name):
    """
    Takes in a map of names to trigger instance, the type of trigger to make,
    and the list of parameters to the constructor, and adds a new trigger
    to the trigger map dictionary.

    triggerMap: dictionary with names as keys (strings) and triggers as values
    triggerType: string indicating the type of trigger to make (ex: "TITLE")
    params: list of strings with the inputs to the trigger constructor (ex: ["world"])
    name: a string representing the name of the new trigger (ex: "t1")

    Modifies triggerMap, adding a new key-value pair for this trigger.

    Returns a new instance of a trigger (ex: TitleTrigger, AndTrigger).
    """
    # TODO: Problem 11


def readTriggerConfig(filename):
    """
    Returns a list of trigger objects
    that correspond to the rules set
    in the file filename
    """

    # Here's some code that we give you
    # to read in the file and eliminate
    # blank lines and comments
    triggerfile = open(filename, "r")
    all = [line.rstrip() for line in triggerfile.readlines()]
    lines = []
    for line in all:
        if len(line) == 0 or line[0] == '#':
            continue
        lines.append(line)

    triggers = []
    triggerMap = {}

    # Be sure you understand this code - we've written it for you,
    # but it's code you should be able to write yourself
    for line in lines:

        linesplit = line.split(" ")

        # Making a new trigger
        if linesplit[0] != "ADD":
            trigger = makeTrigger(triggerMap, linesplit[1],
                                  linesplit[2:], linesplit[0])

        # Add the triggers to the list
        else:
            for name in linesplit[1:]:
                triggers.append(triggerMap[name])

    return triggers



if __name__ == '__main__':
    filename = "c:/Users/mflores1/datafiles/python_mit_2/triggers.txt"
    readTriggerConfig(filename)