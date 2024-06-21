import dns.resolver

res = dns.resolver.Resolver()

with open(r"C:\\Users\\LAMBISGOIAPC\\Desktop\\i\\solyd\\resolvers.txt", "r") as arquivo:
    resolvers = arquivo.read().splitlines()

alvo = "bancocn.com"

for resolv in resolvers:
    try:
        sub_alvo = resolv + "." + alvo 
        resultado = res.resolve(sub_alvo, "A")
        for ip in resultado:
            print(f"{sub_alvo} -> {ip}")
    except dns.resolver.NoAnswer:
        print(f"Nenhum resultado encontrado para {sub_alvo}")
    except dns.resolver.NXDOMAIN:
        print(f"O domínio {sub_alvo} não existe")
    except dns.resolver.Timeout:
        print(f"Timeout ao consultar {sub_alvo}")
    except dns.resolver.NoNameservers:
        print(f"Sem servidores DNS para {sub_alvo}")
    except Exception as e:
        print(f"Erro ao resolver {sub_alvo}: {e}")

