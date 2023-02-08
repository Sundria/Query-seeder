for c in range(1, 101):
    print(f'insert into users (username, password) values ("user" {c}, "saw")')
    if c == 100:
        for d in range(1, 101):
            print(f'insert into accounts (id, balance) values ({d}, 200)')
            if d == 100:
                for e in range(1, 101):
                    print(f'uptade set users set "accountId" = {e} where id = {e}')
user = input('Pressione "Enter" para sair.')

#pyinstaller "nome do arquivo" --onefile



