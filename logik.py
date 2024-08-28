väder = 'sol'
lokalisering = 'inne'
har_paraply = True

if väder == 'regn' and (lokalisering == 'ute' or har_paraply):
    print('Öppna paraplyet!')
else:
    print('Inget paraply behövs!')

if input('namn:') == 'Kalle' and int(input('ålder:')) == 20:
    print('Hej kalle, du är 20 år gammal!')
else:
    print('Oj hoppsan!')
