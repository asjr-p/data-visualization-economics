#Referência bibliográfica
#Adam Smith - A Riqueza das Nações
#Tradução de Norberto de Paula Lima
#Coleção 'Clássicos de Ouro', 2017, livros I-V

#Abre o arquivo .txt com texto referente ao intervalo de págs. indicado acima
with open ('smith.txt', 'r') as meuarquivo:
    texto = meuarquivo.read()

#Utilize essa linha para testar se o arquivo foi aberto corretamente
#print(texto)

""" 
Execute o código abaixo para exibir a interface gráfica do NLTK
& Baixe os seguintes pacotes (seção All Packages):

- averaged_perceptron_tagger
- floresta
- mac_morpho
- machado
- punkt
- stopwords
- wordnet
- words

Sim, alguns deles são desnecessários para a execução deste código específico;
Ainda assim, caso queira trabalhar com o NLTK posteriormente é útil baixá-los de uma vez.

import nltk
nltk.download() """

from nltk.tokenize import word_tokenize

#Quebra todo o conteúdo da variável texto em palavras separadas em letras minúsculas
palavras = word_tokenize(texto.lower()) 

#Utilize essa linha para testar se as frases foram transformadas e quebradas corretamente
#print(palavras)

from nltk.corpus import stopwords
from string import punctuation

#Cria um conjunto contendo palavras 'sem significado', p. ex.: para, a, o, etc., e pontuações
stopwords = set(stopwords.words('portuguese') + list(punctuation))

#Armazena na variável palavras_sem_stopwords tudo aquilo que não se encaixar no conjunto descrito acima
palavras_sem_stopwords = [palavra for palavra in palavras if palavra not in stopwords]

#Utilize essa linha para testar se as stopwords foram retiradas com sucesso
#print(palavras_sem_stopwords)

from nltk.probability import FreqDist

#Cria o dicionário frequencia onde as keys são cada palavra única e os values são a frequência com que aparecem
frequencia = FreqDist(palavras_sem_stopwords)

#Utilize essa linha para exibir o dicionário mencionado acima
print(frequencia.most_common(1000))

#Retirei as seguintes entradas do dicionário frequencia, pois julguei que pouco contribuiam em termos de informação transmitida
del frequencia['”']
del frequencia['“']
del frequencia['–']
del frequencia['ser']
del frequencia['qualquer']
del frequencia['pode']
del frequencia['sobre']
del frequencia['parte']
del frequencia['todos']
del frequencia['todo']
del frequencia['todas']

import matplotlib.pyplot as plt

#Não deixe de instalar a biblioteca wordcloud, caso necessário busque detalhes no Google
from wordcloud import WordCloud

#Gera a nuvem de palavras a partir do dicionário frequencia
wc = WordCloud(
    background_color='white', width=1000, height=800, max_words=1000, relative_scaling=0.5, colormap='viridis', normalize_plurals=False
    ).generate_from_frequencies(frequencia)

#Plota o gráfico c/ título, subtítulo e nota de rodapé
plt.imshow(wc)
plt.axis('off')
plt.suptitle('A Riqueza das Nações em 1000 palavras', horizontalalignment='center', weight='bold')
plt.title('Gráfico construído a partir da obra: A Riqueza das Nações | Autor: Adam Smith', size='xx-small')
plt.figtext(0.5, 0.05, 'Fonte: vide código-fonte em bitly.com/wordcloud-smith\nElaboração: Paulo André Silveira Jr. (Twitter: @asjr_p) | Terraço Econômico (Twitter: @terracoecon)', size='x-small', horizontalalignment='center')
plt.show()
