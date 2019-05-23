# word='akarsh s good boy'
# str=word.split()
# print(str)
#
#
# for x in str:
#     newlist=list(x)
#     test=newlist.append('ay')
#     test.join()
#     print(test)
#     # print(newlist)
#
# nes='worf'
# print(nes[0])
def pig(word):
    st = word.split()
    print(st)
    i=0
    for err in st:
            first_letter = err[0]
            if (first_letter in 'aeiou'):
                pig_word = err +'ay'
                print(pig_word)
            else:
                pig_word = err[1:] + first_letter + 'ay'
                # return pig_word
                print(pig_word)
            i=i+1



# print(pig('hi steve'))

pig('akarsk steve ')
