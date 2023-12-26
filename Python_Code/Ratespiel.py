print('Willkommen bei "Frag Python"')
answer=input('Bist du bereit für das Quiz? (ja/nein) :')
score=0
total_questions=3
 
if answer.lower()=='ja':
    answer=input('Frage 1: Was ist deine Lieblings Programiersprache? ')
    if answer.lower()=='python':
        score += 1
        print('richtig')
    else:
        print('Falsche Antwort :(')
 
 
    answer=input('Frage 2: Folgst du einem Autor bei "askpython"? ')
    if answer.lower()=='yes':
        score += 1
        print('richtig')
    else:
        print('Falsche Antwort :(')
 
    answer=input('Frage 3: WIe lautet der Name deiner Lieblingswebseite um Python zu lernen? ')
    if answer.lower()=='askpython':
        score += 1
        print('richtig')
    else:
        print('Falsche Antwort :(')
 
print('Danke, dass du bei dem Quiz mitgemacht hast, du hast ',score," Fragen richtig beantwortet!")
mark=(score/total_questions)*100
print('Punktzahl erhalten:',mark)
print('Auf wiedersehen!')