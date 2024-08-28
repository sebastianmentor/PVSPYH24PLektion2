x = 42

print("---Vår första if-sats i rätt ordning!---")
if x == 42:
    print(x,"är meningen med livet")
elif x > 0:
    print("x är positivt")
elif x < 0:
    print("x är negativt")
else:
    print("x måste vara noll här!")


print("---Vår andra if-sats i annan ordning!---")
if x > 0:
    print("x är meningen med livet")
elif x == 42:
    print("x är positivt")
elif x < 0:
    print("x är negativt")
else:
    print("x måste vara noll här!")


print("---Vår tredje if-sats i annan ordning!---")
if x == 42:
    print("x är meningen med livet!")
    print("x är positivt")
elif x > 0:
    print("x är positivt")
elif x < 0:
    print("x är negativt")
else:
    print("x måste vara noll här!")

print("---Vår fjärde if-sats i annan ordning!---")
if x == 42:
    print("x är meningen med livet!")
if x > 0:
    print("x är positivt")
elif x < 0:
    print("x är negativt")
else:
    print("x måste vara noll här!")


match x:
    case x if x == 42:
        print("x är meningen med livet!")
    case x if x > 0:
        print("x är positivt")
    case x if x < 0:
        print("x är negativt")
    case _:
        print("x måste vara noll här!")