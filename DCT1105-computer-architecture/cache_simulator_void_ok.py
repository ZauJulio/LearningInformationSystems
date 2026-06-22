#cache simulator
#Desenvolvido em projeto de monitoria por Robson Agripino,
#sob orientação de Luiz Paulo de Assis Barbosa. 
import os
from colorama import init
from colorama import Fore, Back, Style
init(autoreset=True)
import math
from random import randint

cor = {0:Back.BLUE, 1:Back.YELLOW, 2:Back.GREEN, 3:Back.RED}

def embaralhaEnd(num_ord):
    num_aleatorios = []

    for i in num_ord:
        num_aleatorios.append(randint(0, 100))

    for i in range(len(num_ord)):
        for j in range(1, len(num_ord)):
            if(num_aleatorios[i] > num_aleatorios[j]):
                aux = num_ord[i]
                num_ord[i] = num_ord[j] 
                num_ord[j] = aux
    return num_ord

def printMapeamentoCache(nbt, nbi, nbeb):
    msg='| '+str(nbt)+' | '+str(nbi)+' | '+str(nbeb)+' | '
    len(msg)
    print('            +'+'-'*(len(msg)-3)+'+')
    print('Mapeamento: | '+Fore.BLUE+str(nbt)+Fore.RESET+' | '+ Fore.YELLOW+str(nbi)+Fore.RESET+' | '+Fore.GREEN+str(nbeb)+Fore.RESET+' | ')
    print('            +'+'-'*(len(msg)-3)+'+')


def limp():
    os.system('cls' if os.name == 'nt' else 'clear')

def conteudoBloco(addr, map):
    nbeb = map.getNbeb()
    
    minb = "0"*nbeb
    maxb = "1"*nbeb
    i = ''
    t = ''
    if(map.getNbi() != 0):
        i = format(addr.getIndex(), '0'+str(map.getNbi())+'b')
    if(map.getNbt() != 0):
        t = format(addr.getTag(), '0'+str(map.getNbt())+'b')

   
    minb = t+i+minb
    maxb = t+i+maxb

    minb = format(int(minb,2), "0X")
    maxb = format(int(maxb,2), "0X")
    #print(t,i +"   " +minb, maxb)
    if(nbeb == 0):
        return minb
    return minb+"~"+maxb


def initCache(cache, nbc, nbconj):

    ncj = int(nbc/nbconj)
    for i in range(ncj):
        cj = []
        for j in range(nbconj):
            cj.append('')
        cache.append(cj)

def insertCache(cache, enderecos, map):  
    #print(end)
    contHit = 0
    contMiss = 0
    contSub = 0

    ncj = len(cache)
    nbpc = len(cache[0])
    
    for endereco in enderecos:
        endPrint = '['
        for i in enderecos:
            if((i != endereco) or (Back.RESET in endPrint)):  
                endPrint += i.getAddHex() + ", "
            else:
                endPrint += Back.RED + i.getAddHex()+ Back.RESET + ", "

        endPrint = endPrint[0:-2]
        endPrint += "]"

        limp()
        end = endereco.getAddHex()
       
        tag = endereco.getTag()

        ncj = len(cache)

        ind = endereco.getIndex()
        hit = -1
        aux2 = cache[ind][0]
        addr = computeAddrMappingFields(int(end, 16), map)

        addrBin = format(addr.getAdd(), '0'+str(map.getNbe())+'b')

        printMapeamentoCache(map.getNbt(), map.getNbi(), map.getNbeb())

        print(endPrint)

        addrcort = cor[0]+addrBin[0:map.getNbt()] 
        addrcori = cor[1]+addrBin[map.getNbt():map.getNbt()+map.getNbi()] 
        addrcored = cor[2]+ addrBin[map.getNbt()+map.getNbi():]

        addrBin = addrcort+addrcori+addrcored

        print("Endereço:", addr.getAddHex() + "  " + addrBin)
        print("Tag:", addr.getTagHex() + " " + addrcort)
        print("Indice:", addr.getIndHex() + " " + addrcori)
        print("End. de byte:", addr.getAddByteHex() + " " + addrcored)

        cont = 0
        for i in range(len(cache[ind])):
            t = ''
            if(cache[ind][i] != ''):
                #print(cache[ind][i])
                addr = computeAddrMappingFields(int(cache[ind][i], 16), map)
                t = addr.getTag()
            if(t == tag):
                print("HOUVE UM HIT")
                hit = i
                contHit += 1 
                break
            if(t == ''):
                cont = 1

        #fim = nbpc
        fim = len(cache[0])
    
        if(hit != -1):
            fim = hit+1
        elif(cont == 1):
            print("HOUVE UM MISS (Existia blocos vazios)")
            contMiss += 1
        else:
            addr = computeAddrMappingFields(int(cache[ind][nbpc-1], 16), map)
            print("HOUVE UM MISS (Substituiu o end. "+str(cache[ind][nbpc-1])+" por "+str(end)+" no conj."+addr.getIndHex() +" )")
            contSub += 1
            contMiss += 1
        for j in range(1, fim):
            aux1 = cache[ind][j]
            cache[ind][j] = aux2
            aux2 = aux1

          
        cache[ind][0] = end
        #print(cache)
        estast = "| HITS: " + str(contHit) + " | MISS: " + str(contMiss) + " | HIT RATE: " + str(round(contHit/(contHit+contMiss) *100,2))+"% | SUBST: " + str(contSub)+ " |"

        print("     "+"-"*len(estast))
        print("     "+estast)
        print("     "+"-"*len(estast))
        printCache(cache, enderecos, map)
        a = input()


def alinha(st, num):
    return " "* (int ((num-len(str(st)) )/2)) + str(st)  + " "* ((int ((num-len(str(st)) )/2))+  (int ((num-len(str(st)) )%2))  )
def printCache(cache, enderecos, map):
    bloco = ''
    #print(cache)
    bar = "| IND "
    barTam = "| IND "
    tamInd = len(bar) - 1
    t = "  TAG  |" 
    d = "        DADOS        |"
    
    bar += "|V|"+t+d+ Back.RESET+ " "
    barTam += "|V|"+t+d+ " "
    
    tamTag = len(t) - 1
    tamDat = len(d) - 1

    print("-"*(len(barTam)-1))
    print(bar[:-1]) 
    print("-"*(len(barTam)-1))


    for i in range(len(cache)):
        linha = ''
        printa = 0
        for j in range(len(cache[i])):
            if(cache[i][j] == ''):

                linha += cor[i%4]+'|'+alinha(format(i, "0X"), tamInd)+'|0|'+alinha("", tamTag)+"|"+alinha("" , tamDat )+ "|"+Back.RESET+"\n"
            else:   

                addr = computeAddrMappingFields(int(cache[i][j], 16), map)
                printa = 1
                linha += cor[i%4]+'|'+alinha(format(i, "0X"), tamInd)+'|1|'+alinha(addr.getTagHex(), tamTag)+"|"+alinha("*("+conteudoBloco(addr, map)+")",tamDat)+ "|"+Back.RESET+"\n"
        if(printa == 1):       
            print(linha[:-1])


class input_data:

    # Class Attribute
   
    # Initializer / Instance Attributes
    def __init__(self, tmp, nbc, nbconj, nppb, nbypb):
        self.tmp = tmp
        self.nbc = nbc
        self.nbconj = nbconj
        self.nppb = nppb
        self.nbypb = nbypb

    def description(self):
        return "{},{},{},{},{}".format(self.tmp, self.nbc, self.nbconj, self.nppb, self.nbypb)

    def getTmp(self):
        return self.tmp

    def getNbc(self):
        return self.nbc

    def getNbconj(self):
        return self.nbconj

    def getNppb(self):
        return self.nppb

    def getNbypb(self):
        return self.nbypb

class address:

    # Class Attribute
   
    # Initializer / Instance Attributes
    def __init__(self, add, add_block, tag, ind, add_byte):
        self.add = add
        self.add_block = add_block
        self.tag = tag
        self.ind = ind
        self.add_byte = add_byte

    def description(self, type='dec'):
        if (type=='dec'):
            return "{},{},{},{},{}".format(self.add, self.add_block, self.tag, self.ind, self.add_byte)
        elif (type=='hex'):
            return "{},{},{},{},{}".format(format(self.add,'X'), format(self.add_block,'X'), format(self.tag,'X'), format(self.ind,'X'), format(self.add_byte,'X'))
    def getAddHex(self):
        return format(self.add, "X")
    def getTagHex(self):
        return format(self.tag,'0X')

    
    def getAdd(self):
        return self.add

    def getAddH(self):
        return self.addh

    def getAddBlock(self):
        return self.add_block

    def getTag(self):
        return self.tag

    def getIndex(self):
        return self.ind
    def getIndHex(self):
        return format(self.ind, "0X")

    def getAddByte(self):
        return self.add_byte

    def getAddByteHex(self):
        return format(self.add_byte, "0X")
    
    def colision(self, address):
        return (self.ind == address.getIndex()) and (self.tag != address.getTag())
    
    def equal(self,address):
        return self.add == address.getAdd()

class map:

    # Class Attribute
   
    # Initializer / Instance Attributes
    def __init__(self, nbe, nbt, nbi, nbeb,map_type=''):
        self.nbe = nbe
        self.nbt = nbt
        self.nbi = nbi
        self.nbeb = nbeb
        self.map_type = map_type

    def description(self):
        return "{},{},{},{}".format(self.nbe, self.nbt, self.nbi, self.nbeb)

    def getNbe(self):
        return self.nbe

    def getNbt(self):
        return self.nbt

    def getNbi(self):
        return self.nbi

    def getNbeb(self):
        return self.nbeb

    def setMapType(self, map_type):
        self.map_type = map_type

    def getMapType(self):
    	return self.map_type    

    def equal(self, map):
        return ((self.nbe == map.getNbe()) and (self.nbt == map.getNbt()) and (self.nbi == map.getNbi()) and (self.nbeb == map.getNbeb()))           

    def __str__(self):
        return str(self.nbe) + ', ' + str(self.nbt) + ', ' + str(self.nbi)  + ', ' + str(self.nbeb)  + ', ' + self.map_type
   

def computeNumBits( num ):
    num_bits = math.ceil(math.log2(num))
    return num_bits

def mapping(inp_data):
    nbe = computeNumBits(inp_data.getTmp()) 
    if(inp_data.getNbconj()==1):
        nbi = computeNumBits(inp_data.getNbc())
    elif(inp_data.getNbconj() > 1 and inp_data.getNbconj() <= inp_data.getNbc()): 
        nbi = computeNumBits(inp_data.getNbc()/inp_data.getNbconj())
    nbeb = computeNumBits(inp_data.getNppb())

    nbt = nbe - nbi - nbeb
    
    msg='| '+str(nbt)+' | '+str(nbi)+' | '+str(nbeb)+' | '
    len(msg)
    print("\nMapeamento:")
    print('+'+'-'*(len(msg)-3)+'+')
    print('| '+Fore.GREEN+str(nbt)+Fore.RESET+' | '+ Fore.YELLOW+str(nbi)+Fore.RESET+' | '+Fore.RED+str(nbeb)+Fore.RESET+' | ')
    print('+'+'-'*(len(msg)-3)+'+')
    m = map(nbe, nbt , nbi, nbeb)
    return m

def computeAddrMappingFields(addr, map):
    endBloco = int(addr/(2**map.getNbeb()))
    indice = endBloco%(2**map.getNbi())
    tag = int(endBloco/(2**map.getNbi()))
    endByte = addr%(2**map.getNbeb())
    new_addr = address(addr, endBloco, tag, indice, endByte)
    return new_addr        

def convertSufix(str):
    tokens = str.split(' ')
    tokensAux = []
    for i in tokens:
        if(i != ''):
            tokensAux.append(i)
    tokens = tokensAux

    num = 0
    if len(tokens)==2:
        tokens[1] = tokens[1].upper()
        if tokens[1]=='KB' or  tokens[1]=='K':
            num = eval(tokens[0])*1024
        elif tokens[1]=='MB' or tokens[1]=='M':
            num = eval(tokens[0])*(1024**2)
        elif tokens[1]=='GB' or tokens[1]=='G':
            num = eval(tokens[0])*(1024**3)
        elif tokens[1]=='PAL' or tokens[1]=="pal" or tokens[1]=="p" or tokens[1]=="P":
            num = eval(tokens[0])*4
    else:
        num = eval(tokens[0])               
    return num    

def showAddressDetails(enderecos):
    print("-------------------------------------------")    
    print("Endereços:")    
    print(enderecos)
    print("-------------------------------------------")
    print("[<end. MP>, <end. Bloco>, "+Fore.GREEN+"<tag>"+", "+Fore.YELLOW+"<ind>"+Fore.RESET+", "+Fore.RED+"<end. Byte>"+Fore.RESET+"]")
    for j in enderecos:
        print("em decimal:")
        print("["+j.description()+"]")
        print("em hexa:")
        print("["+j.description('hex')+"]")
        print("-------------------------------------------")

def generateAndShowColisions(num_ends, enderecos, map):
    end_para_colisao = []
    num_colisoes=num_ends
    
    #print("\nColisões geradas:")
    #print("-------------------------------------------")
    #print("[<end. MP>, <end. Bloco>, "+Fore.GREEN+"<tag>"+", "+Fore.YELLOW+"<ind>"+Fore.RESET+", "+Fore.RED+"<end. Byte>"+Fore.RESET+"]")
    for k in range(0,eval(num_colisoes)):   
        idx = randint(0,eval(num_ends)-1)
        escolhido = enderecos[idx]

        if ((escolhido.getTag() >= 0) and (escolhido.getTag() < (2**map.getNbt())-1)):
            new_tag = escolhido.getTag() + 1
        elif (escolhido.getTag() == (2**map.getNbt())-1): 
            new_tag = escolhido.getTag() - 1

        new_endByte = randint(0,2**map.getNbeb() -  1)

        end_col = new_tag*(2**(map.getNbeb()+map.getNbi())) + escolhido.getIndex()*(2**map.getNbeb()) + new_endByte
        
        new_addr = computeAddrMappingFields(end_col, map)
        end_para_colisao.append(new_addr)
        #print("end escolhido:")         
        #print('['+ escolhido.description() +']')

        #print("end gerado:")
        #print('['+ new_addr.description() +']')
        #print("-------------------------------------------")
    #print("Sequência de endereços com colisões:")   
    enderecos = enderecos + end_para_colisao
    
    list_end = []
        
    endPrint = '['
    for i in enderecos:  
        endPrint += "0x"+i.getAddHex() + ", "
        list_end.append(i.getAdd())

    endPrint = endPrint[0:-2]
    endPrint += "]"
    print("\nEndereços em decimal")
    print(list_end)
    print("\nEndereços em hexadecimal")
    print(endPrint)
    print("--------------------------------------------------------------\n")
    return enderecos

def main():
    type_map = ''
    par = 'init'
    while(par != ''):
        print("< Ex: 4 GB, 2 K, 1, 4 >")
        print("< Ex: 4 GB, 2 K, 1, 1 PAL >")
        par = input("Informe: <tamMP>, <#SlotsCache>, <#SlotsPorConj>, <#BytesPorSlot> ")
        if(par==''):
            break

        tokens = par.split(', ', 4)

        tmp = convertSufix(tokens[0])
        nbc = convertSufix(tokens[1])
        nbconj = convertSufix(tokens[2])
        nppb = convertSufix(tokens[3]) 
        nbypb = convertSufix(tokens[3])  #convertSufix já trata a multiplicação por 4 devido oao sufixo PAL

        inp_data = input_data(tmp, nbc, nbconj, nppb, nbypb)

        if(not((inp_data.getTmp() != 0) and (inp_data.getTmp() & (inp_data.getTmp()-1) == 0))):
            print(Fore.YELLOW+'<tamMP> não é uma potência de 2!')
            continue
        elif(not((inp_data.getNbc() != 0) and (inp_data.getNbc() & (inp_data.getNbc()-1) == 0))):    
            print(Fore.YELLOW+'<#SlotsCache> não é uma potência de 2!')
            continue
        elif(not((inp_data.getNbconj() != 0) and (inp_data.getNbconj() & (inp_data.getNbconj()-1) == 0))):    
            print(Fore.YELLOW+'<#SlotsPorConj> não é uma potência de 2!')
            continue
        elif(inp_data.getNbc() < inp_data.getNbconj()):
            print(Fore.YELLOW + 'Parâmetros de entrada incorretos!')
            print(Fore.YELLOW + 'Número de blocos por conjuntos maior que o número de blocos da cache!')            
            continue
        elif(inp_data.getTmp() < (inp_data.getNbc()*inp_data.getNppb())):
            print(Fore.YELLOW + 'Parâmetros de entrada incorretos!')
            print(Fore.YELLOW + 'Cache é maior que a MP!')            
            continue

        #map = mapping(tmp,nbc,nbconj,nbypb)
        map = mapping(inp_data)
        
        if(map.getNbe() < map.getNbi() + map.getNbeb()):
            print(Fore.YELLOW + 'Parâmetros de entrada incorretos!')
            continue
        elif(map.getNbi()==0):
            if(map.getNbeb()  == map.getNbt() + map.getNbeb()):
                map.setMapType('ta')
                print(Fore.YELLOW + 'Mapeamento Totalmente Associativo!')                
                print(Fore.YELLOW + 'No limite!')
                print(Fore.YELLOW + 'Tamanho da cache é igual ao da MP!') 
                print(Fore.YELLOW + 'Não existe possibilidade de colisão!')
                #continue
            else:
                map.setMapType('ta')
                print(Fore.YELLOW + 'Mapeamento Totalmente Associativo!')
                #print(Fore.YELLOW + 'Não existe possibilidade de colisão!')
                #continue
        elif(nbconj==1):
            if(map.getNbe()  == map.getNbi() + map.getNbeb()):
                map.setMapType('dir')
                print(Fore.YELLOW + 'Mapeamento Direto!')                
                print(Fore.YELLOW + 'No limite!')
                print(Fore.YELLOW + 'Tamanho da cache é igual ao da MP!') 
                print(Fore.YELLOW + 'Não existe possibilidade de colisão!')
                continue
            else:
                map.setMapType('dir')
                print(Fore.YELLOW + 'Mapeamento Direto!')
        elif(nbconj > 1 and nbconj <= nbc):
            if(map.getNbeb()  == map.getNbi() + map.getNbeb()):
                map.setMapType('ac')
                print(Fore.YELLOW + 'Mapeamento Associativo por Conjuntos!')                
                print(Fore.YELLOW + 'No limite!')
                print(Fore.YELLOW + 'Tamanho da cache é igual ao da MP!')                
                print(Fore.YELLOW + 'Não existe possibilidade de colisão!')
                continue
            else:
                map.setMapType('ac')                  
                print(Fore.YELLOW + 'Mapeamento Associativo por Conjuntos!')
        
        num_ends = input("Informe o #endereços desejado:")
        # código para gerar automaticamente uma sequência de endereços para exemplificação
        if(num_ends==''):
            break

        enderecos = []
        for i in range(0, eval(num_ends)):
            cand = randint(0,2**map.getNbe() - 1)
            new_addr = computeAddrMappingFields(cand, map)
            enderecos.append(new_addr)

        #showAddressDetails(enderecos)

        address_list = generateAndShowColisions(num_ends, enderecos, map)
        
        # pega lista de endereços e mostra os detalhes 
        inp = input("Informe uma lista de endereços:")
        inp = inp[1:-1]
        tokens = inp.split(', ')

        if(num_ends==''):
            break

        enderecos = []
        for i in tokens:
            if(i[0:2]=='0x'):
                i = int(i[2:],16)
            else:
                i = int(i)
            new_addr = computeAddrMappingFields(i, map)
            enderecos.append(new_addr)    
            #enderecos.append(i)
    
        #showAddressDetails(enderecos)
        #cacheHitAndMiss()
        
        cache = []

        initCache(cache, nbc, nbconj)
        # print(cache)
        # input()
        
        #enderecos = embaralhaEnd(enderecos)
        # print(map)
        # if map.getMapType()=='ac':
        #     print('ok, bateu!')
        # input()
        insertCache(cache, enderecos, map)
        # print(cache)
        # input()

    #TODO
    #Fazer código pra determinarr hit or miss na cache para os endereços determinados pelo usuário
main()
