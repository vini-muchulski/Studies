import wikipedia

wikipedia.set_lang("pt")
#setando a linguagem para português

busca = wikipedia.search("nasa")
print(busca)
# search retorna uma lista com os resultados da busca


pagina = wikipedia.page(busca[0])
# page retorna um objeto com as informações da página
#print(pagina)

#conteudo = pagina.content
#print("Conteudo: ", conteudo)

resumo = pagina.summary
print("Resumo:", resumo)