from read import *
from tools import *


feigenbaum = 4.66920160910299


# prints sentences that contain 'invisible' and 'alone'
def invisible_alone():
    global InvisibleMan
    everyInvisible = [s for s in onlyWord(
        InvisibleMan, ' [I,i]nvisible') + onlyWord(InvisibleMan, ' [A,a]?lone') if not hasYou(s) and not isChapter(s) and not hasName(s)]
    InvisibleI = [heToI(s) for s in everyInvisible]
    print(len(InvisibleI))
    return "<br>".join(mix(InvisibleI, len(InvisibleI)//feigenbaum))


# prints senteces that contain I form the Invisible Man
def I_am_solitude():
    global InvisibleMan
    everyI = [s for s in onlyI(InvisibleMan) if not search(
        s, ' [I,i]nvisible') and not hasName(s) and not hasYou(s) and not hasHe(s) and not hasShe(s) and not hasWe(s)]
    return ' '.join(mix(everyI, len(everyI)//(feigenbaum*2)))


def interact():
    global Memoirs, Adventures
    Texts = Memoirs + Adventures
    everySpeak = [strip(s) for s in onlyWord(Texts, ' speak') + onlyWord(Texts, ' spoke') + onlyWord(Texts, ' ask')
                  if not hasName(s) and (hasYou(s) or hasHe(s) or hasShe(s) or hasWe(s))]
    return '<br>'.join(mix(everySpeak, len(everySpeak)//feigenbaum))


def unity():
    global Memoirs, Adventures
    Texts = Memoirs + Adventures
    everyBoth = [strip(s) for s in onlyWord(Texts, ' both') +
                 onlyWord(Texts, ' together') if not hasName(s)]
    return ' '.join(mix(everyBoth, len(everyBoth)//feigenbaum))


def we():
    everyWe = [ItoWe(strip(s)) for s in onlyI(InvisibleMan) if not hasName(s)
               and not hasYou(s) and not hasHe(s) and not hasShe(s)]
    return '<br>'.join(mix(everyWe, len(everyWe)//feigenbaum))


# prints sentences which contain the word 'death' from Frankenstein and Dracula
def death(we=False):
    global Frankenstein, Dracula
    AllDeath = onlyWord(Frankenstein+Dracula, ' ?[D,d]eath')
    everyDeath = [strip(s) for s in AllDeath if not hasName(s)]  # len = 107
    everyIdeath = [sheToI(heToI(weToI(s))) for s in everyDeath]
    if we:
        return '<br>'.join([ItoWe(s) for s in mix(everyDeath, len(everyDeath)//feigenbaum) if not hasShe(s) and not hasHe(s)]+['We died.'])
    else:
        return '<br>'.join(list(mix(everyIdeath, len(everyIdeath)//feigenbaum))+['<b>I died.</b>'])
