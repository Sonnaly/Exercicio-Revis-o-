preco_kg_file = [4.9,5.8]
preco_kg_alcatra = [5.9,6.8]
preco_kg_picanha = [6.9,7.8]
preco_kg_escolhido = [0,0]
preco_produto = 0.0
cartao_bool = False
tipos_carne = ["Filé Duplo", "Alcatra","Picanha"]
limite_peso = 5
carne_escolhida =""
qtde_carne = 0.0
formas_pgto = ["Cartão Tabajara","Outros"]
pgto_escolhido= ""
desconto_forma_pgto=0.05
valor_desconto = 0.0
print("Tipos de carne disponíveis:")
print(tipos_carne)
while carne_escolhida not in tipos_carne:
  carne_escolhida = str(input("Qual tipo de carne?"))
while qtde_carne <=0:
  qtde_carne = float(input("Quantidade?"))
print("Formas de Pagamento:")
print(formas_pgto)
while pgto_escolhido not in formas_pgto:
  pgto_escolhido = str(input("Forma de pagamento escolhida"))
#Calcular preço:
if carne_escolhida =="Filé Duplo":
  preco_kg_escolhido = preco_kg_file
if carne_escolhida =="Alcatra":
  preco_kg_escolhido = preco_kg_alcatra
if carne_escolhida =="Picanha":
  preco_kg_escolhido = preco_kg_picanha
if qtde_carne < limite_peso:
  preco_produto = preco_kg_escolhido[1] *qtde_carne
if qtde_carne >= limite_peso:
  preco_produto = preco_kg_escolhido[0] *qtde_carne
preco_produto = round(preco_produto,2)
preco_final = preco_produto
if pgto_escolhido == formas_pgto[0]:
  valor_desconto = round(preco_produto *  desconto_forma_pgto,2)
  preco_final = round(preco_produto - valor_desconto,2)
print ("Cupom fiscal")
print("Carne escolhida: ", carne_escolhida)
print ("Quantidade:", qtde_carne, "kg.")
print("Preço total: R$", preco_produto)
print("Desconto: R$", valor_desconto)
print("Valor a pagar: R$", preco_final)
