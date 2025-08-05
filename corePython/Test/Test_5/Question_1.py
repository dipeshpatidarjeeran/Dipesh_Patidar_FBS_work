# A list contains the denominations as follows :
# D = [2000, 500, 200, 100 , 50, 20, 10, 5]
# Accept an amount from user and calculate how many
# minimum number of notes will be needed for that
# amount.
D = [2000, 500, 200, 100 , 50, 20, 10, 5]

amount = int(input("enter the amount:-"))
for note in D:
    if amount >= note:
        notes = amount // note
        amount = amount % note
        print(f"{note} x {notes}")