print("Hej och välkommen till humörjhjälparen!")
humör = input("Vänligen skriv in ditt humör: ")

emoji = None
text = ''
vet_humör = True

if humör.lower() == 'glad':
    emoji = "😁"
    text = "Du är glad idag! Det gör mig glad!"

elif humör.lower() == 'ledsen':
    emoji = "😭"
    text = "Du är ledsen! Jag är ledsen med dig."

elif humör.lower() == 'arg':
    emoji = "😡"
    text = "Gud förbannat vad allt är bajs💩"

elif humör.lower() == 'kattastrof':
    emoji = "🙀"
    text = "The world is doomed!!!"

else:
    emoji = "🤷‍♀️🤷🤷‍♂️"
    text = "Tyvärr, jag kan inte tyda vilket humör du har! Ber om ursäkt för detta"
    vet_humör = False


if not vet_humör:
    print(text, emoji)
else:
    print("Jag förstår att ditt humör är att vara:", humör)
    print(text)
    print("Här kommer en emoji som reflekterar ditt humör:", emoji)