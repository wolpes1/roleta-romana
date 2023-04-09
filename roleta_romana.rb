#Número determinante de quantas pessoas existem
puts "Quantas pessoas estarão na fila?"
quantidade_pessoas = gets.chomp.to_i

#Número determinante de quantos passos serão necessários
puts "Quantos passos a morte dará?"
passo = gets.chomp.to_i


#Contador de passos dados
contador = 0

#Array para a fila de pessoas
fila = Array.new

#Loop para angariar cada posição à fila
while quantidade_pessoas != 0
    fila.append(quantidade_pessoas)
    quantidade_pessoas -= 1
end

fila.sort!

tamanho_fila = fila.length


#Loop do programa
while tamanho_fila != 1
    contador += passo
    if contador > tamanho_fila
        contador -= tamanho_fila
    end
    fila.delete_at(contador-1)
    tamanho_fila = fila.length
end

print "O local protegido é o número #{fila}\n"
