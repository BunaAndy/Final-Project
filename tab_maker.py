import wave
from frequency_array import get_freq_array
from guitar_dictionary import GUITARFREQFRET as freqDict

def make_tab(filepath: str, noteSplit):
    splitList = get_freq_array(filepath, noteSplit)
    raw = wave.open(filepath)
    prevSplit = [-1, -1, -1, -1, -1, -1]
    antepenSplit = [-1, -1, -1, -1, -1, -1]
    tab = []
    for split in splitList:
        splitTab = minimizing_agent(split, prevSplit, antepenSplit)
        tab.append(splitTab)
        antepenSplit = prevSplit
        prevSplit = splitTab
    return string_tab(tab)

def string_tab(tablist):
    tab = ""
    for i in range(5, -1, -1):
        tabstring = "#--"
        for tabline in tablist:
            if (tabline[i] == -1):
                tabstring = tabstring + "----"
            elif tabline[i] < 10:
                tabstring = tabstring + "-" + str(tabline[i]) + "--"
            else:
                tabstring = tabstring + str(tabline[i]) + "--"
        tab = tab + tabstring + "\n"
    return tab


def minimizing_agent(split: list[float], prevSplit, antepenSplit):
    # Start with lowest frequency, and work our way up
    split.sort()
    # looks like a lot of for loops, but length of each of these is 6, so 
    # for every frequency, we need to add it to the tab list
    tablist = [-1, -1, -1, -1, -1, -1]
    for freq in split:
        # find each possible fret and string based on given frequency
        possFrets = []
        for key in freqDict.keys():
            fret = freqDict.get(key).get(freq)
            if not (fret == None):
                possFrets.append((fret, key))
        # now determine which of those has the minimal score, which is determined by the absolute value
        # of the difference between the possible fret and previous fret. A smaller score means smaller distance
        # is more likely to be the best placement for that frequency 
        minscore = 999999
        fret = (-1,-1)
        for possFret in possFrets:
            # First, add the fret num to the score, we want to prefer
            # frets closeer to the head of the guitar
            score = possFret[0]
            # Add score for prev frets
            for prevFret in prevSplit:
                if (prevFret == -1):
                    continue
                score = score + abs(possFret[0] - prevFret)
            # Now add score for antepen frets
            for antFret in antepenSplit:
                if (antFret == -1):
                    continue
                score = score + abs(possFret[0] - antFret)
            # check if it's smaller than current min, and if so update fret and min score
            if score < minscore:
                minscore = score
                fret = possFret
        # Now we have the fret closest to the rest of the tab, we can add it to the tab
        tablist.pop(fret[1])
        tablist.insert(fret[1], fret[0])
    # Finally, return teh completed tablist for this split
    return tablist

