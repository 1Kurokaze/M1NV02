def loginUsuario(perfil):
    if perfil.lower() == 'admin':
        print('Bem-vindo, Administrador')
    else:
        print('Bem-vindo, Usuário')

# Chamadas da função com diferentes valores como parâmetro
loginUsuario('Admin')
loginUsuario('admin')
loginUsuario('User')
loginUsuario('usuário')
loginUsuario('ADMIN')
loginUsuario('Administrador')