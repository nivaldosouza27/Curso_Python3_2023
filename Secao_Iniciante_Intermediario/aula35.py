### Criar mensagem nomes automaticos ###

cursos = ['ENGENHARIA', 'ADMINISTRACAO', 'DIREITO', 'SISTEMAS DE INFORMACAO',
          'PEDAGOGIA', 'ENFERMAGEM', 'FISIOTERAPIA']
alunos = ['ANA', 'LUIZ', 'JOAO', 'PEDRO', 'HENRIQUE', 'LUCAS', 'GABRIEL']

texto_mensagem = ['Bom dia', 'Boa Tarde', 'Boa noite']

def criar_mensagem(mensagem):
    def add_aluno (alunos):
        def add_curso(curso):
            return f'{mensagem}Seu nome é: {alunos} \
                Voce pode se matricular nos cursos de: {curso}'
        return add_curso
    return add_aluno


for mensagem in texto_mensagem:
    escrever_mensagem = criar_mensagem(mensagem)
    print(escrever_mensagem)