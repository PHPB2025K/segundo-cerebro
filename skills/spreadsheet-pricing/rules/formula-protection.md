# Protecao de Formulas — Spreadsheet Pricing

> REGRA ABSOLUTA: colunas listadas abaixo NUNCA podem ser escritas pelo skill.
> Se o skill escrever numa celula com formula, a formula e destruida permanentemente.
> NAO existe undo via API — o dano e irreversivel.

---

## Colunas PROIBIDAS por aba

### MELI (16 colunas protegidas)
```
C  STATUS          =IF(A=0,"SEM ESTOQUE",...)
I  FRETE CHEIO     =G*0.28
J  COMISSAO ML     =IF(H="Classico",G*12.5%,IF(H="Premium",G*17.5%,0))
K  CUSTO FIXA      =IF(G<12.5,G*50%,0)
L  IMPOSTO         =G*7%
O  DEVOLUCOES      =G*0.04
Q  ADS             =G*0.06
R  FRETE           =IF(G<79.9,0,IF(OR(H="Classico",...),I*50%,IF(H="Premium",I*70%,0)))
S  COM AFILIADO    =G*0.1
T  MARGEM          =(U*100)/G/100
U  LUCRO LIQ       =G-F-J-K-L-M-P-R-Q-O
V  MARGEM AFIL     =(W*100)/G/100
W  LUCRO AFIL      =G-F-J-K-L-M-P-R-Q-S-O
Y  NCM             =VLOOKUP(EAN,ESTOQUE,...)
Z  PESO            =VLOOKUP(EAN,ESTOQUE,...)
AA MARCA           =VLOOKUP(EAN,ESTOQUE,...)
```

### SHOPEE (11 colunas protegidas + 4 especiais)
```
B  ICONE           Formula de icone
C  STATUS          =IF(A=0,"SEM ESTOQUE",...)
H  COMISSAO        =G*IF(G<=79.99,20%,14%)
J  TAXA FIXA       =IF(G<=79.99,4,IF(G<=99.99,16,...))
K  IMPOSTO         =G*0.07
M  DEVOLUCOES      =G*0.04
N  ADS             =G*0.05
R  COM AFILIADO    =G*0.1
X  NCM             =VLOOKUP(EAN,ESTOQUE,...)
Y  PESO            =VLOOKUP(EAN,ESTOQUE,...)
Z  MARCA           =VLOOKUP(EAN,ESTOQUE,...)

ESPECIAIS (copiar formula da row anterior ao inserir nova linha):
S  MARGEM          Formula varia por row
T  LUCRO LIQ       Formula varia por row
U  MARGEM AFIL     Formula varia por row
V  LUCRO AFIL      Formula varia por row
```

### AMAZON (10 colunas protegidas)
```
C  STATUS          =IF(A=0,"SEM ESTOQUE",...)
H  COMISSAO AMZ    =G*0.12
J  IMPOSTO         =G*7%
N  ADS             =G*0.089
O  DEVOLUCOES      =G*0.04
Q  MARGEM          =(R*100)/G/100
R  LUCRO LIQ       =G-F-H-I-J-L-M-O-P-N-K
T  NCM             =VLOOKUP(SKU,ESTOQUE,...)
U  PESO            =VLOOKUP(SKU,ESTOQUE,...)
V  MARCA           =VLOOKUP(SKU,ESTOQUE,...)
```

### ESTOQUE (3 colunas protegidas)
```
D  STATUS          =IF(A=0,"SEM ESTOQUE",...)
J  VALOR ESTOQUE   =A*F
K  CALC AUXILIAR   =IF(L="","",L*F)
```

---

## Checklist antes de escrever

Antes de executar `gog sheets update` em qualquer celula:
1. Identificar a aba e coluna
2. Verificar nesta lista se e PROIBIDA
3. Se for PROIBIDA: NAO escrever, sob nenhuma circunstancia
4. Se for INPUT: escrever com formato correto (ver format-rules.md)
5. Se for ESPECIAL (S/T/U/V Shopee): copiar formula da row anterior
