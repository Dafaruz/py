print("welcome to the tip calculator.\n")
total_bill=float(input("whatis the total bill amount$\n"))
how_many_pepole=int(input("how many pepole are you\n"))
what_percentage=int((int(input("what percentage tip you wold like to give"))/100)+1)

payment_per_person=round((total_bill*what_percentage)/how_many_pepole,2)
print(f"each person shole pay {payment_per_person}")

