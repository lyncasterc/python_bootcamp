l = [12,3,4,5,6]

def rem(l, num):
  i = 0
  diff = None
  removed_cards = []

  if len(l) > num or len(l) == num:
    while i < num:
      a = l.pop()
      removed_cards.append(a)
      i+=1
  if len(l) < num:
    diff = num - len(l)
    num-=diff
    while i < num:
      a = l.pop()
      removed_cards.append(a)
      i+=1

  if len(removed_cards) == 1:
    for card in removed_cards:
      return card
  else:
    return [card for card in removed_cards]
    

rem(l,7)

print(l)


