class Estudante:
    escola = "DIO"
    
    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula
        
    def __str__(self):
        return f'Nome: {self.nome:<10} | Matrícula: {self.matricula:<10} | Escola: {self.escola:<10}'

def print_alunos(*alunos):
    print('#'*40)
    for aluno in alunos:
        print(aluno)
    print('#'*40+'\n')
    
aluno1 = Estudante("Kelven", 1)
aluno2 = Estudante("Kakau", 2)

print_alunos(aluno1,aluno2)

aluno1.escola = "FSA"
print_alunos(aluno1,aluno2)

Estudante.escola = "USP"
aluno3 = Estudante("Kamilly", 3)
print_alunos(aluno1,aluno2,aluno3)