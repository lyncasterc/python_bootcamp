def make_song(count=99, beverage='soda'):
    
    while count >= 0:
        yield f"{count} bottles of {beverage} on the wall"
        count-=1
        
        if count == 0:
            yield f"No more {beverage}!"
            break

gen = make_song(99,'beer')

for g in gen:
    print(g)
        
    



