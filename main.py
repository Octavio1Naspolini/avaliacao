from model import Turma, Aluno, Professor
import sqlite3

conn = sqlite3.connect('turma.db')

if __name__ == "__main__":
    # Criar turmas
    turma = Turma(202601, 10, 18.30)
    # Salvar turma e obter o ID gerado
    turma_id = turma.salvar(conn)

    # Lista de alunos
    alunos = [
        ("ADRIANO MARGHETI RINALDI", 20261400001),
        ("ANDRE LUIZ CORDEIRO GOMES", 20261400002),
        ("CAMILA GALDINO PACHECO", 20261400036),
        ("CRISTHIANE TRESSI", 20261400246),
        ("DANILO CARGNIN RODRIGUES", 20261400003),
        ("EDUARDO DA SILVA MACHADO", 20261400019),
        ("EVERSON GUIMARAES", 20261400004),
        ("GABRIEL RIBEIRO CANELA DE SOUZA", 20261400006),
        ("HERICA SERAFIM VARGAS", 20261400007),
        ("JOSELLE GIACOMUZZI PIRES", 20261400251),
        ("JULIA LUIZ CARDOSO", 20261400020),
        ("KLEBER PATRICIO DE OLIVEIRA", 20261400010),
        ("MARCELO DE CARVALHO MIGUEL", 20261400012),
        ("OCTAVIO NASPOLINI NETO", 20261400013),
        ("RAFAEL DA SILVA DE MELLO", 20261400014),
        ("RODRIGO NETTO", 20261400015),
        ("VICTOR LUIZ ANGELO DE OLIVEIRA", 20261400017),
        ("VITORIA RAUPP ADAO", 20261400018),
        ("YUKI KOGA PRISCO", 20261400022)
    ]

    # Inserir alunos e criar alunos
    for nome, matricula in alunos:
        aluno = Aluno(nome, matricula, turma_id)
        # Salvar alunos
        aluno.salvar(conn)

    # Criar professor
    professor1 = Professor("Edjanir Correa Costa", "Linguagens de Programação", turma_id)
    professor2 = Professor("Alexssandro Cardoso Antunes", "Segurança da Informação", turma_id)
    # Salvar professores
    professor1.salvar(conn)
    professor2.salvar(conn)
    
    conn.close()