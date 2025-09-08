import mysql.connector
 
# 1. Conexão com o banco de dados hospital
conexao = mysql.connector.connect(
host="localhost",  # Servidor do MySQL
user="root", # Usuário padrão do XAMPP
 password="", # Senha (vazia no XAMPP por padrão)
 database="bliblioteca"  # Nome do banco criado no phpMyAdmin
)
 
# 2. Criar cursor
cursor = conexao.cursor()
 
# 3. Receber entrada do usuário
nomeAutor = input("Digite o nome do autor que deseja cadastrar: ")
 
# 4. Comando SQL para inserir médico
sql = "INSERT INTO autores (nomeAutor) VALUES (%s)"
sql2 = "SELECT autores FROM (nomeAutor)"
valores = (nomeAutor,)
 
cursor.execute(sql, valores)
 
# 5. Confirmar no banco (commit é obrigatório para INSERT/UPDATE/DELETE)
conexao.commit()
 
print(f"Autor '{nomeAutor}' cadastrado com sucesso!")
print(sql2)
 
# 6. Fechar cursor e conexão
cursor.close()
conexao.close()