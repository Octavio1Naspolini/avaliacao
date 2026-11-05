#Classe Turma
class Turma:
    def __init__(self, codigo, sala, horario):
        self.id = None
        self.codigo = codigo
        self.sala = sala
        self.horario = horario
    #Método para salvar as turmas no banco de dados
    def salvar(self, conn):
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO turmas (codigo, sala, horario)
            VALUES (?, ?, ?)
        """, (self.codigo, self.sala, self.horario))
        self.id = cursor.lastrowid
        conn.commit()
        return self.id
    #Método para listar as turmas no banco de dados
    @staticmethod
    def listar(conn):
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM turmas")
        return cursor.fetchall()
#Classe Aluno
class Aluno:
    def __init__(self, nome, matricula, turma_id):
        self.nome = nome
        self.matricula = matricula
        self.turma_id = turma_id
    #Método para salvar os alunos no banco de dados
    def salvar(self, conn):
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO alunos (turma_id, nome, matricula)
            VALUES (?, ?, ?)
        """, (self.turma_id, self.nome, self.matricula))
        conn.commit()
    #Método para listar os alunos no banco de dados
    @staticmethod
    def listar(conn):
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM alunos")
        return cursor.fetchall()
    #Método para listar os alunos da turma no banco de dados
    @staticmethod
    def listar_com_turma(conn):
        cursor = conn.cursor()
        cursor.execute("""
            SELECT a.nome, a.matricula, t.codigo, t.sala
            FROM alunos a
            JOIN turmas t ON a.turma_id = t.id
        """)
        return cursor.fetchall()
#Classe Professor
class Professor:
    def __init__(self, nome, materia, turma_id):
        self.nome = nome
        self.materia = materia
        self.turma_id = turma_id
    #Método para salvar os professores no banco de dados
    def salvar(self, conn):
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO professores (turma_id, nome, materia)
            VALUES (?, ?, ?)
        """, (self.turma_id, self.nome, self.materia))
        conn.commit()
    #Método para listar os professores no banco de dados
    @staticmethod
    def listar(conn):
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM professores")
        return cursor.fetchall()
    #Método para listar os professores da turma no banco de dados
    @staticmethod
    def listar_com_turma(conn):
        cursor = conn.cursor()
        cursor.execute("""
            SELECT p.nome, p.materia, t.codigo
            FROM professores p
            JOIN turmas t ON p.turma_id = t.id
        """)
        return cursor.fetchall()