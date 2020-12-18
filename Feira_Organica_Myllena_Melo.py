carrinho=list()
dados_usuario=list()
quant=0
total=0

def mostralinha():
    print('-='*20)

    
legumes = [['1-batata doce 500g', '8.41'], ['2-cenoura 500g','8.41'] , ['3-tomate salada 500g','8.71'] , ['4-chuchu 600g','6.14'],['5-beringela 500g','7.11'] , ['6-brocolis comum und','8.01'], ['7-alho 80gramas','8.27'], ['8-tomate 500g','9.20'],['9-pepino 400G','7.50'], ['10-aipim 500g','6.90'], ['11-cebola 500g','7.90']]
frutas=[['12-manga palmer 350g','6.34'],['13-banana prata 800g','7.90'],['14-morango 250g','12.90'],['15-limao tahiti 500g','7.90'],['16-laranja pera 500g','7.90'],['17-melao 800g','9.90'],['18-manga tommy 350g','5.90'],['19-uva vitória 500g','4.90'],['20-bergamota 500g','3.40'],['21-kiwi verde 350g','7.40']]
verduras=[['22-rucula und','4.21'],['23-alface und','4,90'],['24-alface mimosa und','4.90'],['25-alface lisa und','4.90'],['26-alface romana und','4.90'],['27-aipo verde und','3.90'],['28-acelga und','1,40'],['29-couve chinesa und','4.90'],['30-mostarda und','4.90'],['31-taioba und','5.24'],['32-chicoria und','4.90']]
ervasetemperos=[['33-salsa lisa und','4.48'],['34-cheiro verde und','4.48'],['35-cebolinha und','4.48'],['36-erva cidreira und','4.48'],['37-tomilho und','4.48'],['38-oregano und','4.48'],['39-capim limao und','4.48'],['40-alcafrão 100g','2.90'],['41-coentro und','4.48'],['42-manjericao und','5.50']]
mercearia=[['43-açai pote  1L', '13.19'],['44-chia em pó 120g','10.49'],['45-cafe moido 250g','17.49'],['46-farinha 250g','5.53'],['47-farinhasoja 300g','6.55'],['48-ovos 10und','15.90'],['49-açucar  1kg','5.95'],['50-azeite 500ml','29.99'],['51-nectar de caju 1L','11.74'],['52-arroz  1kg','13.90']]

mostralinha()
print('|\t\tLEGUMES\t\t\t|')
mostralinha()
print("#Cod/Item                       R$Preço ")
mostralinha()
for i in legumes:
    print(f'{i[0]} ----------\tR$ {i[1]}')
mostralinha()

mostralinha()
print('|\t\tFRUTAS\t\t\t|')
mostralinha()
print("#Cod/Item                       R$Preço ")
mostralinha()
for i in frutas:
    print(f'{i[0]} ----------\tR$ {i[1]}')
mostralinha()

mostralinha()
print('|\t\tVERDURAS\t\t|')
mostralinha()
print("#Cod/Item                       R$Preço ")
mostralinha()
for i in verduras:
    print(f'{i[0]} ----------\tR$ {i[1]}')
mostralinha()

mostralinha()
print('|\tERVAS E TEMPEROS\t\t|')
mostralinha()
print("#Cod/Item                        R$Preço ")
mostralinha()
for i in ervasetemperos:
    print(f'{i[0]} ----------\tR$ {i[1]}')
mostralinha()

mostralinha()
print('|\t\tMERCEARIA\t\t|')
mostralinha()
print("#Cod/Item                       R$Preço ")
mostralinha()
for i in mercearia:
    print(f'{i[0]} ----------\tR$ {i[1]}')
mostralinha()

#compra do usuário 
while True:
    item=str(input('Qual produto deseja colocar no carrinho?'))
    if item == '1':
        print ('Você adicionou batata doce no carrinho ')
        carrinho.append('batata doce')
        quant = float(input('Quantidade (em gramas)?'))
        carrinho.append(quant)
        total += ((quant*8.41)/500)
        carrinho.append(total)
        print('Total do carrinho:', "R$ %.2f" % total)
        continuar = str(input('Deseja continuar?(S/N) ')).upper()
        if continuar != 'S':
            break
    if item == '2':
        print ('Você adicionou cenoura no carrinho ')
        carrinho.append('cenoura')
        quant = float(input('Quantidade (em gramas)?'))
        carrinho.append(quant)
        total += ((quant*8.41)/500)
        carrinho.append(total)
        print('Total do carrinho:', "R$ %.2f" % total)
        continuar = str(input('Deseja continuar?(S/N) ')).upper()
        if continuar != 'S':
            break
    if item == '3':
        print ('Você adicionou tomate salada no carrinho ')
        carrinho.append('tomate salada')
        quant = float(input('Quantidade (em gramas)?'))
        carrinho.append(quant)
        total += ((quant*8.71)/500)
        carrinho.append(total)
        print('Total do carrinho:', "R$ %.2f" % total)
        continuar = str(input('Deseja continuar?(S/N) ')).upper()
        if continuar != 'S':
            break
    if item == '4':
        print ('Você adicionou chuchu no carrinho ')
        carrinho.append('chuchu')
        quant = float(input('Quantidade (em gramas)?'))
        carrinho.append(quant)
        total += ((quant*6.14)/600)
        carrinho.append(total)
        print('Total do carrinho:', "R$ %.2f" % total)
        continuar = str(input('Deseja continuar?(S/N) ')).upper()
        if continuar != 'S':
            break
    if item == '5':
        print ('Você adicionou beringela no carrinho ')
        carrinho.append('beringela')
        quant += float(input('Quantidade (em gramas)?'))
        carrinho.append(quant)
        total += ((quant*7.11)/500)
        carrinho.append(total)
        print('Total do carrinho:', "R$ %.2f" % total)
        continuar = str(input('Deseja continuar?(S/N) ')).upper()
        if continuar != 'S':
            break
    if item == '6':
        print ('Você adicionou brocolis comum no carrinho ')
        carrinho.append('brocolis comum')
        quant = float(input('Quantidade?'))
        carrinho.append(quant)
        total += ((quant*8.01)/1)
        carrinho.append(total)
        print('Total do carrinho:', "R$ %.2f" % total)
        continuar = str(input('Deseja continuar?(S/N) ')).upper()
        if continuar != 'S':
            break
    if item == '7':
        print ('Você adicionou alho comum no carrinho ')
        carrinho.append('alho')
        quant = float(input('Quantidade (em gramas)?'))
        carrinho.append(quant)
        total += ((quant*8.01)/80)
        carrinho.append(total)
        print('Total do carrinho:', "R$ %.2f" % total)
        continuar = str(input('Deseja continuar?(S/N) ')).upper()
        if continuar != 'S':
            break
    if item == '8':
        print ('Você adicionou tomate italiano no carrinho ')
        carrinho.append('tomate italiano')
        quant = float(input('Quantidade (em gramas)?'))
        carrinho.append(quant)
        total += ((quant*9.20)/500)
        carrinho.append(total)
        print('Total do carrinho:', "R$ %.2f" % total)
        continuar = str(input('Deseja continuar?(S/N) ')).upper()
        if continuar != 'S':
            break
    if item == '9':
        print ('Você adicionou pepino japones no carrinho ')
        carrinho.append('pepino japones')
        quant = float(input('Quantidade (em gramas)?'))
        carrinho.append(quant)
        total += ((quant*7.50)/400)
        carrinho.append(total)
        print('Total do carrinho:', "R$ %.2f" % total)
        continuar = str(input('Deseja continuar?(S/N) ')).upper()
        if continuar != 'S':
            break
    if item == '10':
        print ('Você adicionou aipim no carrinho ')
        carrinho.append('aipim')
        quant = float(input('Quantidade (em gramas)?'))
        carrinho.append(quant)
        total += ((quant*6.90)/500)
        carrinho.append(total)
        print('Total do carrinho:', "R$ %.2f" % total)
        continuar = str(input('Deseja continuar?(S/N) ')).upper()
        if continuar != 'S':
            break
    if item == '11':
        print ('Você adicionou cebola no carrinho ')
        carrinho.append('cebola')
        quant = float(input('Quantidade (em gramas)?'))
        carrinho.append(quant)
        total += ((quant*7.90)/500)
        carrinho.append(total)
        print('Total do carrinho:', "R$ %.2f" % total)
        continuar = str(input('Deseja continuar?(S/N) ')).upper()
        if continuar != 'S':
            break
    if item == '12':
        print ('Você adicionou manga palmer no carrinho ')
        carrinho.append('manga palmer')
        quant = float(input('Quantidade (em gramas)?'))
        carrinho.append(quant)
        total += ((quant*6.34)/350)
        carrinho.append(total)
        print('Total do carrinho:', "R$ %.2f" % total)
        continuar = str(input('Deseja continuar?(S/N) ')).upper()
        if continuar != 'S':
            break
    if item == '13':
        print ('Você adicionou banana prata no carrinho ')
        carrinho.append('banana prata')
        quant = float(input('Quantidade (em gramas)?'))
        carrinho.append(quant)
        total += ((quant*7.90)/800)
        carrinho.append(total)
        print('Total do carrinho:', "R$ %.2f" % total)
        continuar = str(input('Deseja continuar?(S/N) ')).upper()
        if continuar != 'S':
            break
    if item == '14':
        print ('Você adicionou morango  no carrinho ')
        carrinho.append('morango')
        quant = float(input('Quantidade (em gramas)?'))
        carrinho.append(quant)
        total += ((quant*12.9)/250)
        carrinho.append(total)
        print('Total do carrinho:', "R$ %.2f" % total)
        continuar = str(input('Deseja continuar?(S/N) ')).upper()
        if continuar != 'S':
            break
    if item == '15':
        print ('Você adicionou limao tahiti no carrinho ')
        carrinho.append('limao tahiti')
        quant = float(input('Quantidade (em gramas)?'))
        carrinho.append(quant)
        total += ((quant*7.90)/500)
        carrinho.append(total)
        print('Total do carrinho:', "R$ %.2f" % total)
        continuar = str(input('Deseja continuar?(S/N) ')).upper()
        if continuar != 'S':
            break
    if item == '16':
        print ('Você adicionou laranja pera no carrinho ')
        carrinho.append('laranja pera')
        quant = float(input('Quantidade (em gramas)?'))
        carrinho.append(quant)
        total += ((quant*7.90)/500)
        carrinho.append(total)
        print('Total do carrinho:', "R$ %.2f" % total)
        continuar = str(input('Deseja continuar?(S/N) ')).upper()
        if continuar != 'S':
            break
    if item == '17':
        print ('Você adicionou melao amarelo no carrinho ')
        carrinho.append('melao amarelo')
        quant = float(input('Quantidade (em gramas)?'))
        carrinho.append(quant)
        total += ((quant*9.90)/800)
        carrinho.append(total)
        print('Total do carrinho:', "R$ %.2f" % total)
        continuar = str(input('Deseja continuar?(S/N) ')).upper()
        if continuar != 'S':
            break
    if item == '18':
        print ('Você adicionou manga tommy no carrinho ')
        carrinho.append('manga tommy')
        quant = float(input('Quantidade (em gramas)?'))
        carrinho.append(quant)
        total += ((quant*5.90)/350)
        carrinho.append(total)
        print('Total do carrinho:', "R$ %.2f" % total)
        continuar = str(input('Deseja continuar?(S/N) ')).upper()
        if continuar != 'S':
            break
    if item == '19':
        print ('Você adicionou uva vitória no carrinho ')
        carrinho.append('uva vitória')
        quant = float(input('Quantidade (em gramas)?'))
        carrinho.append(quant)
        total += ((quant*4.90)/500)
        carrinho.append(total)
        print('Total do carrinho:', "R$ %.2f" % total)
        continuar = str(input('Deseja continuar?(S/N) ')).upper()
        if continuar != 'S':
            break
    if item == '20':
        print ('Você adicionou tangerina bergamota no carrinho ')
        carrinho.append('tangerina bergamota')
        quant = float(input('Quantidade (em gramas)?'))
        carrinho.append(quant)
        total += ((quant*3.40)/500)
        carrinho.append(total)
        print('Total do carrinho:', "R$ %.2f" % total)
        continuar = str(input('Deseja continuar?(S/N) ')).upper()
        if continuar != 'S':
            break
    if item == '21':
        print ('Você adicionou kiwi no carrinho ')
        carrinho.append('kiwi')
        quant = float(input('Quantidade (em gramas)?'))
        carrinho.append(quant)
        total += ((quant*7.40)/350)
        carrinho.append(total)
        print('Total do carrinho:', "R$ %.2f" % total)
        continuar = str(input('Deseja continuar?(S/N) ')).upper()
        if continuar != 'S':
            break
    if item == '22':
        print ('Você adicionou rucula selvatica no carrinho ')
        carrinho.append('rucula selvatica')
        quant = float(input('Quantidade?'))
        carrinho.append(quant)
        total += ((quant*4.21)/1)
        carrinho.append(total)
        print('Total do carrinho:', "R$ %.2f" % total)
        continuar = str(input('Deseja continuar?(S/N) ')).upper()
        if continuar != 'S':
            break
    if item == '23':
        print ('Você adicionou alface americana no carrinho ')
        carrinho.append('alface americana')
        quant = float(input('Quantidade?'))
        carrinho.append(quant)
        total += ((quant*4.90)/1)
        carrinho.append(total)
        print('Total do carrinho:', "R$ %.2f" % total)
        continuar = str(input('Deseja continuar?(S/N) ')).upper()
        if continuar != 'S':
            break
    if item == '24':
        print ('Você adicionou alface mimosa no carrinho ')
        carrinho.append('alface mimosa')
        quant = float(input('Quantidade?'))
        carrinho.append(quant)
        total += ((quant*4.90)/1)
        carrinho.append(total)
        print('Total do carrinho:', "R$ %.2f" % total)
        continuar = str(input('Deseja continuar?(S/N) ')).upper()
        if continuar != 'S':
            break
    if item == '25':
        print ('Você adicionou alface lisa no carrinho ')
        carrinho.append('alface lisa')
        quant = float(input('Quantidade?'))
        carrinho.append(quant)
        total += ((quant*4.90)/1)
        carrinho.append(total)
        print('Total do carrinho:', "R$ %.2f" % total)
        continuar = str(input('Deseja continuar?(S/N) ')).upper()
        if continuar != 'S':
            break
    if item == '26':
        print ('Você adicionou alface romana no carrinho ')
        carrinho.append('alface romana')
        quant = float(input('Quantidade?'))
        carrinho.append(quant)
        total += ((quant*4.90)/1)
        carrinho.append(total)
        print('Total do carrinho:', "R$ %.2f" % total)
        continuar = str(input('Deseja continuar?(S/N) ')).upper()
        if continuar != 'S':
            break
    if item == '27':
        print ('Você adicionou aipo no carrinho ')
        carrinho.append('aipo')
        quant = float(input('Quantidade?'))
        carrinho.append(quant)
        total += ((quant*4.90)/1)
        carrinho.append(total)
        print('Total do carrinho:', "R$ %.2f" % total)
        continuar = str(input('Deseja continuar?(S/N) ')).upper()
        if continuar != 'S':
            break
    if item == '28':
        print ('Você adicionou acelga no carrinho ')
        carrinho.append('acelga')
        quant = float(input('Quantidade?'))
        carrinho.append(quant)
        total += ((quant*1.40)/1)
        carrinho.append(total)
        print('Total do carrinho:', "R$ %.2f" % total)
        continuar = str(input('Deseja continuar?(S/N) ')).upper()
        if continuar != 'S':
            break
    if item == '29':
        print ('Você adicionou couve chinesa no carrinho ')
        carrinho.append('couve chinesa')
        quant = float(input('Quantidade?'))
        carrinho.append(quant)
        total += ((quant*4.90)/1)
        carrinho.append(total)
        print('Total do carrinho:', "R$ %.2f" % total)
        continuar = str(input('Deseja continuar?(S/N) ')).upper()
        if continuar != 'S':
            break
    if item == '30':
        print ('Você adicionou mostarda no carrinho ')
        carrinho.append('mostarda')
        quant = float(input('Quantidade?'))
        carrinho.append(quant)
        total += ((quant*4.90)/1)
        carrinho.append(total)
        print('Total do carrinho:', "R$ %.2f" % total)
        continuar = str(input('Deseja continuar?(S/N) ')).upper()
        if continuar != 'S':
            break
    if item == '31':
        print ('Você adicionou taioba no carrinho ')
        carrinho.append('taioba')
        quant = float(input('Quantidade?'))
        carrinho.append(quant)
        total += ((quant*5.24)/1)
        carrinho.append(total)
        print('Total do carrinho:', "R$ %.2f" % total)
        continuar = str(input('Deseja continuar?(S/N) ')).upper()
        if continuar != 'S':
            break
    if item == '32':
        print ('Você adicionou chicoria frise  no carrinho ')
        carrinho.append('chicoria frise ')
        quant = float(input('Quantidade?'))
        carrinho.append(quant)
        total += ((quant*4.90)/1)
        carrinho.append(total)
        print('Total do carrinho:', "R$ %.2f" % total)
        continuar = str(input('Deseja continuar?(S/N) ')).upper()
        if continuar != 'S':
            break
    if item == '33':
        print ('Você adicionou salsa lisa no carrinho ')
        carrinho.append('salsa lisa')
        quant = float(input('Quantidade?'))
        carrinho.append(quant)
        total += ((quant*4.48)/1)
        carrinho.append(total)
        print('Total do carrinho:', "R$ %.2f" % total)
        continuar = str(input('Deseja continuar?(S/N) ')).upper()
        if continuar != 'S':
            break
    if item == '34':
        print ('Você adicionou cheiro verde no carrinho ')
        carrinho.append('cheiro verde')
        quant = float(input('Quantidade?'))
        carrinho.append(quant)
        total += ((quant*4.48)/1)
        carrinho.append(total)
        print('Total do carrinho:', "R$ %.2f" % total)
        continuar = str(input('Deseja continuar?(S/N) ')).upper()
        if continuar != 'S':
            break
    if item == '35':
        print ('Você adicionou cebolinha no carrinho ')
        carrinho.append('cebolinha')
        quant = float(input('Quantidade?'))
        carrinho.append(quant)
        total += ((quant*4.48)/1)
        carrinho.append(total)
        print('Total do carrinho:', "R$ %.2f" % total)
        continuar = str(input('Deseja continuar?(S/N) ')).upper()
        if continuar != 'S':
            break
    if item == '36':
        print ('Você adicionou erva cidreira no carrinho ')
        carrinho.append('erva cidreira')
        quant = float(input('Quantidade?'))
        carrinho.append(quant)
        total += ((quant*4.48)/1)
        carrinho.append(total)
        print('Total do carrinho:', "R$ %.2f" % total)
        continuar = str(input('Deseja continuar?(S/N) ')).upper()
        if continuar != 'S':
            break
    if item == '37':
        print ('Você adicionou tomilho no carrinho ')
        carrinho.append('tomilho')
        quant = float(input('Quantidade?'))
        carrinho.append(quant)
        total += ((quant*4.48)/1)
        carrinho.append(total)
        print('Total do carrinho:', "R$ %.2f" % total)
        continuar = str(input('Deseja continuar?(S/N) ')).upper()
        if continuar != 'S':
            break
    if item == '38':
        print ('Você adicionou oregano no carrinho ')
        carrinho.append('oregano')
        quant = float(input('Quantidade?'))
        carrinho.append(quant)
        total += ((quant*4.48)/1)
        carrinho.append(total)
        print('Total do carrinho:', "R$ %.2f" % total)
        continuar = str(input('Deseja continuar?(S/N) ')).upper()
        if continuar != 'S':
            break
    if item == '39':
        print ('Você adicionou capim limao no carrinho ')
        carrinho.append('capim limao')
        quant = float(input('Quantidade?'))
        carrinho.append(quant)
        total += ((quant*4.48)/1)
        carrinho.append(total)
        print('Total do carrinho:', "R$ %.2f" % total)
        continuar = str(input('Deseja continuar?(S/N) ')).upper()
        if continuar != 'S':
            break
    if item == '40':
        print ('Você adicionou alcafrão no carrinho ')
        carrinho.append('alcafrão')
        quant = float(input('Quantidade?'))
        carrinho.append(quant)
        total += ((quant*2.90)/1)
        carrinho.append(total)
        print('Total do carrinho:', "R$ %.2f" % total)
        continuar = str(input('Deseja continuar?(S/N) ')).upper()
        if continuar != 'S':
            break
    if item == '41':
        print ('Você adicionou coentro no carrinho ')
        carrinho.append('coentro')
        quant = float(input('Quantidade?'))
        carrinho.append(quant)
        total += ((quant*4.48)/1)
        carrinho.append(total)
        print('Total do carrinho:', "R$ %.2f" % total)
        continuar = str(input('Deseja continuar?(S/N) ')).upper()
        if continuar != 'S':
            break
    if item == '42':
        print ('Você adicionou manjericao no carrinho ')
        carrinho.append('manjericao')
        quant = float(input('Quantidade?'))
        carrinho.append(quant)
        total += ((quant*5.50)/1)
        carrinho.append(total)
        print('Total do carrinho:', "R$ %.2f" % total)
        continuar = str(input('Deseja continuar?(S/N) ')).upper()
        if continuar != 'S':
            break
    if item == '43':
        print ('Você adicionou açai com guarana no carrinho ')
        carrinho.append('açai com guarana')
        quant = float(input('Quantidade?(em litros)'))
        carrinho.append(quant)
        total += ((quant*13.19)/1)
        carrinho.append(total)
        print('Total do carrinho:', "R$ %.2f" % total)
        continuar = str(input('Deseja continuar?(S/N) ')).upper()
        if continuar != 'S':
            break
    if item == '44':
        print ('Você adicionou chia no carrinho ')
        carrinho.append('chia')
        quant = float(input('Quantidade?(em gramas)'))
        carrinho.append(quant)
        total += ((quant*10.49)/120)
        carrinho.append(total)
        print('Total do carrinho:', "R$ %.2f" % total)
        continuar = str(input('Deseja continuar?(S/N) ')).upper()
        if continuar != 'S':
            break
    if item == '45':
        print ('Você adicionou cafe moido no carrinho ')
        carrinho.append('cafe moido')
        quant = float(input('Quantidade?(em gramas)'))
        carrinho.append(quant)
        total += ((quant*17.49)/250)
        carrinho.append(total)
        print('Total do carrinho:', "R$ %.2f" % total)
        continuar = str(input('Deseja continuar?(S/N) ')).upper()
        if continuar != 'S':
            break
    if item == '46':
        print ('Você adicionou farinha de aveia no carrinho ')
        carrinho.append('farinha de aveia')
        quant = float(input('Quantidade?(em gramas)'))
        carrinho.append(quant)
        total += ((quant*5.53)/250)
        carrinho.append(total)
        print('Total do carrinho:', "R$ %.2f" % total)
        continuar = str(input('Deseja continuar?(S/N) ')).upper()
        if continuar != 'S':
            break
    if item == '47':
        print ('Você adicionou farinha de soja no carrinho ')
        carrinho.append('farinha de soja')
        quant = float(input('Quantidade?(em gramas)'))
        carrinho.append(quant)
        total += ((quant*6.55)/300)
        carrinho.append(total)
        print('Total do carrinho:', "R$ %.2f" % total)
        continuar = str(input('Deseja continuar?(S/N) ')).upper()
        if continuar != 'S':
            break
    if item == '48':
        print ('Você adicionou ovos caipira no carrinho ')
        carrinho.append('ovos caipira')
        quant = float(input('Quantidade?'))
        carrinho.append(quant)
        total += ((quant*15.90)/10)
        carrinho.append(total)
        print('Total do carrinho:', "R$ %.2f" % total)
        continuar = str(input('Deseja continuar?(S/N) ')).upper()
        if continuar != 'S':
            break
    if item == '49':
        print ('Você adicionou acucar cristal no carrinho ')
        carrinho.append('acucar cristal')
        quant = float(input('Quantidade?(em kg)'))
        carrinho.append(quant)
        total += ((quant*5.95)/1)
        carrinho.append(total)
        print('Total do carrinho:', "R$ %.2f" % total)
        continuar = str(input('Deseja continuar?(S/N) ')).upper()
        if continuar != 'S':
            break
    if item == '50':
        print ('Você adicionou azeite virgem no carrinho ')
        carrinho.append('azeite virgem')
        quant = float(input('Quantidade?(em ml)'))
        carrinho.append(quant)
        total += ((quant*29.99)/500)
        carrinho.append(total)
        print('Total do carrinho:', "R$ %.2f" % total)
        continuar = str(input('Deseja continuar?(S/N) ')).upper()
        if continuar != 'S':
            break
    if item == '51':
        print ('Você adicionou nectar de caju no carrinho ')
        carrinho.append('nectar de caju')
        quant = float(input('Quantidade?(em litros)'))
        carrinho.append(quant)
        total += ((quant*11.74)/1)
        carrinho.append(total)
        print('Total do carrinho:', "R$ %.2f" % total)
        continuar = str(input('Deseja continuar?(S/N) ')).upper()
        if continuar != 'S':
            break
    if item == '52':
        print ('Você adicionou arroz polido no carrinho ')
        carrinho.append('arroz polido')
        quant = float(input('Quantidade?(em kg)'))
        carrinho.append(quant)
        total += ((quant*13.90)/1)
        carrinho.append(total)
        print('Total do carrinho:', "R$ %.2f" % total)
        continuar = str(input('Deseja continuar?(S/N) ')).upper()
        if continuar != 'S':
            break

#dados cliente
nomeCliente = str(input('Insira o nome do cliente: '))
endereco = str(input('Insira o endereço de entrega: '))
pagamento = str(input('''Insira a forma de pagamento:
                            1-Cartão de crédito
                            2-Cartão de débito
                            3-Dinheiro
                            >_'''))
if pagamento == '1':
    pagamento = ('Cartão de crédito')
if pagamento == '2':
    pagamento = ('Cartão de débito')
if pagamento == '3':
    pagamento = ('Dinheiro')
else:
    pagamento = ('Outra forma de pagamento.')
    
#print em tela
print (nomeCliente)
print(endereco)
print(pagamento)
print(carrinho)
print('=>O total gasto na feira orgânica foi:', "R$ %.2f" % total)

with open ('nota.txt','w', encoding='utf8') as arquivo:
    arquivo.write(str('Cliente:') + ' ')
with open ('nota.txt','a', encoding='utf8') as arquivo:    
    arquivo.write(str(nomeCliente) + '\n')
with open ('nota.txt','a', encoding='utf8') as arquivo:
    arquivo.write(str('Endereço:') + ' ')
with open ('nota.txt','a', encoding='utf8') as arquivo:
    arquivo.write(str(endereco) + '\n')
with open ('nota.txt','a', encoding='utf8') as arquivo:
    arquivo.write(str('Forma de pagamento:') + ' ')
with open ('nota.txt','a', encoding='utf8') as arquivo:
    arquivo.write(str(pagamento) + '\n')
with open ('nota.txt','a', encoding='utf8') as arquivo:
    arquivo.write(str('Itens comprados:') + ' ')
with open ('nota.txt','a', encoding='utf8') as arquivo:
    for nota in carrinho:
        arquivo.write(str(nota) + ',')
with open ('nota.txt','a', encoding='utf8') as arquivo:
    arquivo.write(str('\nTotal:') + '')
with open ('nota.txt','a', encoding='utf8') as arquivo:
    arquivo.write(str( "R$ %.2f" % total) + '\n')
