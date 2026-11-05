import sqlite3

# Conecta ao arquivo (criado automaticamente se não existir)
conexao = sqlite3.connect("turma.db")
cursor = conexao.cursor()

# Criando uma tabela para armazenar turmas
cursor.execute("""
CREATE TABLE IF NOT EXISTS turmas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    codigo INTEGER,
    sala INTEGER,
    horario REAL
)
""")
# Criando uma tabela para armazenar alunos
cursor.execute("""
CREATE TABLE IF NOT EXISTS alunos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    turma_id INTEGER,
    nome TEXT,
    matricula INTEGER,
    FOREIGN KEY (turma_id) REFERENCES turmas(id)
)
""")
# Criando uma tabela para armazenar professores
cursor.execute("""
CREATE TABLE IF NOT EXISTS professores (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    turma_id INTEGER,
    nome TEXT,
    materia TEXT,
    FOREIGN KEY (turma_id) REFERENCES turmas(id)
)
""")