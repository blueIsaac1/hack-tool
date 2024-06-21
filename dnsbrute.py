import dns.resolver # type: ignore

res = dns.resolver.Resolver()
arquivo = open(r"C:\\Users\\LAMBISGOIAPC\\Desktop\\i\\solyd\\Subdomain-wordlist.txt", "r")
subdominios = arquivo.read().splitlines()

alvo = "bancocn.com"

for subdominio in subdominios:
	try:
		sub_alvo = subdominio + "." + alvo 
		resultado = res.resolve(sub_alvo, "A")
		for ip in resultado:
			print(sub_alvo, "->", ip)
	except:
		pass
