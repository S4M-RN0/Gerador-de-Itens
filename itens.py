import random
import eel

eel.init("web")

# Início da função de consumíveis
def dropConsu(rar):
    com = ['Pergaminho de Identificação', 'Bandagem Simples', 'Pomada Mágica', 'Combustível', 'Pergaminho de Magia Comum', 'Incenso de Foco Simples']
    uncom = ['Bandagem Mediana', 'Pomada Mágica Mediana', 'Mapa Incomum', 'Saco de Moedas', 'Pergaminho de Treinamento', 'Pergaminho de Magia Incomum', 'Incenso de Foco Mediano']
    raro = ['Bandagem Avançada', 'Pomada Mágica Avançada', 'Kit de Costura', 'Mapa Raro', 'Suprimentos', 'Saco Grande de Moedas', 'Resíduo do Infinito', 'Pergaminho de Mágia Rara', 'Incenso de Foco Avançado', 'Pergaminho de Teleporte']
    epic = ['Bandagem Superior', 'Pomada Mágica Superior', 'Mapa Épico', 'Saco Enorme de Moedas', 'Fragmento do Infinito', 'Pergaminho de Magia Épica', 'Incenso de Foco Superior', 'Pergaminho de Ressurreição']
    leg = ['Bandagem Excelente', 'Pomada Mágica Excelente', 'Mapa Lendário', 'Caixa de Suprimentos', 'Mapa do Tesouro', 'Pedaço do Infinito', 'Pergaminho de Magia Lendária', 'Pergaminho de Teleporte em Massa', 'Incenso de Foco Excelente', 'Pergaminho de Ressurreição em Massa']
    
    if rar == 1 :
        eel.printDrop(random.choice(com))
    elif rar == 2 :
        eel.printDrop(random.choice(uncom))
    elif rar == 3 :
        eel.printDrop(random.choice(raro))
    elif rar == 4 :
        eel.printDrop(random.choice(epic))
    else :
        eel.printDrop(random.choice(leg))
    return 0
# Fim da função de consumíveis

# Início da função de poções
def dropPot(rar):
    com = ['Sem pot comum', 'Sem pot comum2']
    uncom = ['Sem pot incomum', 'Sem pot incomum2']
    raro = ['Sem pot rara', 'Sem pot rara2']
    epic = ['Sem pot epica', 'Sem pot epica2']
    leg = ['Sem pot leg', 'Sem pot leg2']
    
    if rar == 1 :
        eel.printDrop(random.choice(com))
    elif rar == 2 :
        eel.printDrop(random.choice(uncom))
    elif rar == 3 :
        eel.printDrop(random.choice(raro))
    elif rar == 4 :
        eel.printDrop(random.choice(epic))
    else :
        eel.printDrop(random.choice(leg))
    return 0
# Fim da função de poções

# Início da função de engenhocas
def dropEng(rar):
    com = ['Sem eng comum', 'Sem eng comum2']
    uncom = ['Sem eng incomum', 'Sem eng incomum2']
    raro = ['Sem eng rara', 'Sem eng rara2']
    epic = ['Prótese Braço-de-Lâmina', 'Prótese Caminhante-da-Tempestade']
    leg = ['Sem eng leg', 'Sem eng leg2']
    
    if rar == 1 :
        eel.printDrop(random.choice(com))
    elif rar == 2 :
        eel.printDrop(random.choice(uncom))
    elif rar == 3 :
        eel.printDrop(random.choice(raro))
    elif rar == 4 :
        eel.printDrop(random.choice(epic))
    else :
        eel.printDrop(random.choice(leg))
    return 0
# Fim da função de engenhocas

# Início da função de armaduras
def dropArmor(rar):
    tipo = ['Escudo:', 'Armadura Leve:', 'Armadura Média:', 'Armadura Pesada:']
    uncom = ['+1', '+2', 'Espaço de Runa(+1)']
    raro = ['+3', 'Espaço de Runa(+2)']
    epic = ['+4', 'Espaço de Runa(+3)']
    leg = ['+5', 'Espaço de Runa(+4)']
    
    if rar == 1 :
        eel.printDrop(random.choice(tipo))
    elif rar == 2 :
        eel.printDrop(random.choice(tipo) + ' ' + random.choice(uncom))
    elif rar == 3 :
        cbnt = random.randint(1, 2)
        if cbnt == 1 :
            eel.printDrop(random.choice(tipo) + ' ' + random.choice(raro))
        else :
            eel.printDrop(random.choice(tipo) + ' ' + random.choice(uncom) + ', ' + random.choice(uncom))
    elif rar == 4 :
        cbnt = random.randint(1, 3)
        if cbnt == 1 :
            eel.printDrop(random.choice(tipo) + ' ' + random.choice(epic))
        elif cbnt == 2 :
            eel.printDrop(random.choice(tipo) + ' ' + random.choice(raro) + ', ' + random.choice(uncom))
        else :
            eel.printDrop(random.choice(tipo) + ' ' + random.choice(uncom) + ', ' + random.choice(uncom) + ', ' + random.choice(uncom))
    else :
        cbnt = random.randint(1, 5)
        if cbnt == 1 :
            eel.printDrop(random.choice(tipo) + ' ' + random.choice(leg))
        elif cbnt == 2 :
            eel.printDrop(random.choice(tipo) + ' ' + random.choice(epic) + ', ' + random.choice(uncom))
        elif cbnt == 3 :
            eel.printDrop(random.choice(tipo) + ' ' + random.choice(raro) + ', ' + random.choice(raro))
        elif cbnt == 4 :
            eel.printDrop(random.choice(tipo) + ' ' + random.choice(raro) + ', ' + random.choice(uncom) + ', ' + random.choice(uncom))
        else :
            eel.printDrop(random.choice(tipo) + ' ' + random.choice(uncom) + ', ' + random.choice(uncom) + ', ' + random.choice(uncom)  + ', ' + random.choice(uncom))
    
    return 0
# Fim da função de armaduras

# Início da função de armas
def dropWeap(rar):
    tipo = ['Adaga:', 'Arco:', 'Besta:', 'Escopeta:', 'Espada Reta:', 'Katana:', 'Lança:', 'Machado:', 'Maça:', 'Pistola:', 'Rifle:', 'Sabre:']
    uncom = ['+1', '+2', 'Flamejante', 'Congelante', 'Elétrico', 'Venenoso', 'Bento', 'Maldito', 'Arcano', 'Sangrento', 'Encantado', 'Espaço de Runa(+1)']
    raro = ['+3', 'Infundido', 'Sagrado', 'Profano', 'Vampírico', 'Queima-Mana', 'Prateado', 'Ferro Gelado', 'Bizantino', 'Euclidiano', 'Espaço de Runa(+2)']
    epic = ['+4', 'Crítico', 'Captura-Alma', 'Retornável', 'Ecoante', 'Praguejado', 'Espaço de Runa(+3)']
    leg = ['+5', 'Vorpal', 'Temporal', 'Banidor', 'Dimensional', 'Fúria dos Ventos', 'Espaço de Runa(+4)']
    
    if rar == 1 :
        eel.printDrop(random.choice(tipo))
    elif rar == 2 :
        eel.printDrop(random.choice(tipo) + ' ' + random.choice(uncom))
    elif rar == 3 :
        cbnt = random.randint(1, 2)
        if cbnt == 1 :
            eel.printDrop(random.choice(tipo) + ' ' + random.choice(raro))
        else :
            eel.printDrop(random.choice(tipo) + ' ' + random.choice(uncom) + ', ' + random.choice(uncom))
    elif rar == 4 :
        cbnt = random.randint(1, 3)
        if cbnt == 1 :
            eel.printDrop(random.choice(tipo) + ' ' + random.choice(epic))
        elif cbnt == 2 :
            eel.printDrop(random.choice(tipo) + ' ' + random.choice(raro) + ', ' + random.choice(uncom))
        else :
            eel.printDrop(random.choice(tipo) + ' ' + random.choice(uncom) + ', ' + random.choice(uncom) + ', ' + random.choice(uncom))
    else :
        cbnt = random.randint(1, 5)
        if cbnt == 1 :
            eel.printDrop(random.choice(tipo) + ' ' + random.choice(leg))
        elif cbnt == 2 :
            eel.printDrop(random.choice(tipo) + ' ' + random.choice(epic) + ', ' + random.choice(uncom))
        elif cbnt == 3 :
            eel.printDrop(random.choice(tipo) + ' ' + random.choice(raro) + ', ' + random.choice(raro))
        elif cbnt == 4 :
            eel.printDrop(random.choice(tipo) + ' ' + random.choice(raro) + ', ' + random.choice(uncom) + ', ' + random.choice(uncom))
        else :
            eel.printDrop(random.choice(tipo) + ' ' + random.choice(uncom) + ', ' + random.choice(uncom) + ', ' + random.choice(uncom)  + ', ' + random.choice(uncom))
    
    return 0
# Fim da função de armas

# Início da função de magias
def dropMag(rar):
    com = ['Labareda', 'Míssil Mágico', 'Estaca de Gelo']
    uncom = ['Contra-mágica', 'sem mag incom2']
    raro = ['sem mag rara', 'sem mag rara2']
    epic = ['sem mag epica', 'sem mag epica2']
    leg = ['sem mag leg', 'sem mag leg2']
    
    if rar == 1 :
        eel.printDrop(random.choice(com))
    elif rar == 2 :
        eel.printDrop(random.choice(uncom))
    elif rar == 3 :
        eel.printDrop(random.choice(raro))
    elif rar == 4 :
        eel.printDrop(random.choice(epic))
    else :
        eel.printDrop(random.choice(leg))
    return 0
# Fim da função de magias

# Início da função de runas
def dropRuna(rar):
    com = ['Runa de um Plebeu Comum', 'Runa de Armas', 'Runa de Feitiços', 'Runa do Foco', 'Runa da Vida', 'Runa da Velocidade', 'Runa da Chance', 'Runa do Crítico', 'Runa de Proteção Física', 'Runa de Proteção Mágica', 'Runa da Alquimia', 'Runa de Carga']
    uncom = ['Runa de um Estudioso Esforçado', 'Runa de um Soldado Sem Nome']
    raro = ['Runa de um Professor Erudito', 'Runa de um Cavaleiro Orgulhoso', 'Fuga Ardilosa']
    epic = ['Runa de um Bravo Guerreiro', 'Sem runa epica2']
    leg = ['Runa de um Grande Herói', 'Sem runa leg2']
    
    if rar == 1 :
        eel.printDrop(random.choice(com))
    elif rar == 2 :
        eel.printDrop(random.choice(uncom))
    elif rar == 3 :
        eel.printDrop(random.choice(raro))
    elif rar == 4 :
        eel.printDrop(random.choice(epic))
    else :
        eel.printDrop(random.choice(leg))
    return 0
# Fim da função de runas

# Início da função de tipo
def dropTipo(mob, rar) :
    if mob == 1 :
    #Drop de criaturas normais
        result = random.randint(1, 20)
        if (result >= 1) and (result <= 4) :         # Consumíveis
            dropConsu(rar)
        elif (result >= 5) and (result <= 8) :       # Poções
            dropPot(rar)
        elif (result >= 9) and (result <= 12) :      # Engenhocas
            dropEng(rar)
        elif (result >= 13) and (result <= 15) :     # Armaduras
            dropArmor(rar)
        elif (result == 16) or (result == 17) :      # Armas
            dropWeap(rar)
        elif (result == 18) or (result == 19) :      # Magias
            dropMag(rar)
        else :                                       # Runas
            dropRuna(rar)
            
    elif mob == 2 :
    #Drop de boss
        result = random.randint(1, 20)
        if (result >= 1) and (result <= 5) :     # Armaduras
            if (rar >= 1) and (rar <= 5) : dropArmor(rar)
            else : eel.printDrop('Armadura Única')
        elif (result >= 6) and (result <= 10) :      # Armas
            if (rar >= 1) and (rar <= 5) : dropWeap(rar)
            else : eel.printDrop('Arma Única')
        elif (result >= 11) and (result <= 15) :      # Magias
            if (rar >= 1) and (rar <= 5) : dropMag(rar)
            else : eel.printDrop('Magia Única')
        else :                                       # Runas
            if (rar >= 1) and (rar <= 5) : dropRuna(rar)
            else : eel.printDrop('Runa Única')
    
    else :
    #Drop de mapa
        result = random.randint(1, 20)
        if (result >= 1) and (result <= 6) :     # Armaduras
            dropArmor(rar)
        elif (result >= 7) and (result <= 11) :      # Armas
            dropWeap(rar)
        elif (result >= 12) and (result <= 16) :      # Magias
            dropMag(rar)
        else :                                       # Runas
            dropRuna(rar)
            
    return 0
# Fim da função de tipo

# Início da função de raridade
def dropRar(mob, qtd) :
    while qtd !=0 :
        if mob == 1 :
        #Drop de criaturas normais
            result = random.randint(1, 20)
            if (result >= 1) and (result <= 7) :      # Comum
                dropTipo(1, 1)
            elif (result >= 8) and (result <= 12) :   # Incomum
                dropTipo(1, 2)
            elif (result >= 13) and (result <= 16) :  # Raro
                dropTipo(1, 3)
            elif (result >= 17) and (result <= 19) :  # Épico
                dropTipo(1, 4)
            else :                                    # Lendário
                dropTipo(1, 5)
            
        else :
        # Drop de boss
            result = random.randint(1, 20)
            if (result >= 1) and (result <= 12) :     # Raro
                dropTipo(2, 3)
            elif (result >= 13) and (result <= 17) :  # Épico
                dropTipo(2, 4)
            elif (result >= 18) and (result <= 19) :  # Lendário
                dropTipo(2, 5)
            else :                                    # Único
                dropTipo(2, 6)
                
        qtd-= 1
# Fim da função de raridade

# Início da função de quantidade
def dropQtd(mob) :
    if mob == 1 :
        result = random.randint(1, 20)
        if (result >= 1) and (result <= 5) :          # 0
            eel.printDrop('Nenhum drop')
        elif (result >= 6) and (result <= 14) :       # 1
            dropRar(mob, 1)
        elif (result >= 15) and (result <= 18) :      # 2
            dropRar(mob, 2)
        else :                                        # 3
            dropRar(mob, 3)
            
    else :
        result = random.randint(1, 20)
        if (result >= 1) and (result <= 10) :         # 1
            dropRar(mob, 1)
        elif (result >= 11) and (result <= 16) :      # 2
            dropRar(mob, 2)
        else :                                        # 3
            dropRar(mob, 3)
# Fim da função de quantidade

# Início do menu 
@eel.expose
def dropMenu(btn, rar) :
    if btn == 1 :
        dropQtd(1)
    elif btn == 2 :
        dropQtd(2)
    elif btn == 3 :
        dropTipo(3, rar)
    elif btn == 4 :
        dropMag(rar)
# Fim do menu
            
# Start the index.html file
eel.start('index.html', size=(500, 500))