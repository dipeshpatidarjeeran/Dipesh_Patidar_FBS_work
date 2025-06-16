"""
    Write a program to accept an integer amount from user and tell minimum
    number of notes needed for representing that amount.
"""
notes = int(input("enter the notes:-"))

if(notes > 0):
    rup_2000 = notes // 2000
    note = notes % 2000

    rup_500 = note // 500
    note = note % 500

    rup_200 = note // 200
    note = note % 200

    rup_100 = note // 100
    note = note % 100

    rup_50 = note // 50
    note = note % 50

    rup_20 = note // 20
    note = note % 20

    rup_10 = note // 10
    print(f"Minimum Notes: 2000={rup_2000}, 500={rup_500}, 200={rup_200},\
        100={rup_100}, 50={rup_50}, 20={rup_20}, 10={rup_10}")
else:
    print("Invalid Notes")