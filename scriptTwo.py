import pyperclip
# step One get the stuff that is on the clipBoard right now

clipBoardData = pyperclip.paste()
#step 2 add Numbers infront of these
listFormed = clipBoardData.split('\n')
number = 1
for i in range(len(listFormed)):
    listFormed[i] = f'{number}. {listFormed[i]}'
    number += 1
stringtoCopy = '\n'.join(listFormed)

pyperclip.copy(stringtoCopy)
# print(listFormed)

# 1. The cat slept peacefully on the windowsill
# 2. Rain tapped softly against the glass
# 3. She walked through the garden, admiring the flowers
# 4. A distant bell rang through the quiet town