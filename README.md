# LCCV - Projeto

## Como executar
Para executar a ferramenta, siga os seguintes passos:

1 - Crie um ambiente virtual e instale as dependências mencionadas no requirements.txt. Considere utilizar o comando **pip install -r requirements.txt**.

2 - Depois de ativar o ambiente virtual clone o repositório e no arquivo **tweets/api_twitter/src/initialize_api.py** preencha os campos de tokens e chaves da API do twitter. Você conseguirá essas chaves se cadastrando como desenvolvedor no Twitter.

2 - Abra um terminal/prompt de comando na pasta principal onde se encontra o arquivo manage.py e rode o comando: **python3 manage.py runserver**

3 - Abra um outro terminal na pasta web. Antes de tudo é necessário rodar o comando **npm update** pra atualizar a dependências do node, que não foram incluidas no repositório. Em seguida rode o comando **ng serve --open**.

## Como utilizar a ferramenta
Para iniciar, na aba home, informe um tópico de seu interesse e a quantidade de tweets que deseja analisar. Para fins práticos recomendo que informe um tópico conhecido, como Game of Thrones, Avengers, endgame, Donald Trump, etc e uma quantidade de tweets acima de 100.

Uma outra aba contém os trending topics mundiais. Lá está uma lista com os 10 trending topics do momento em que foi realizada a pesquisa. Você também poderá usar um trending topic para fazer a pesquisa na home.

Por fim a aba dos resultados contém as informações obtidas após a solicitação da API. Sâo 3 gráficos, o primeiro em formato de rosquinha, que representa a análise de sentimentos classificada em grupos. O segundo e terceiro são gráficos de palavras que expressam sentimentos bons e ruins exibindo a ocorrência das palavras. 
Obs: Algumas vezes o gráfico de palavras poderá retornar vazio. Isso significa que poucos tweets foram analisados sobre o tema.

Por fim, há uma lista com os 5 melhores e os 5 piores tweets obtidos na classificação de sentimentos.

## Proposta da Ferramenta

A proposta da ferramenta é extrair resultados estatísticos sobre produtos ou tópicos de interesse. A ferramenta faz operações de data cleaning e data mining. Seus resultados são apresentados para que empresas/indivíduos possam tomar decisões de marketing inteligentes observando quais produtos ou tópicos valem a pena investir.

## WorkFlow da ferramenta

Para o tema pesquisado os tweets são requisitados da API do twitter. Ela retorna informaçes diversas para cada tweet, como o usuário, localização, o tweet em si, etc. Recebido o tweet, ele passará por uma análise de sentimentos utilizando a biblioteca TextBlob, que o classificará com uma pontuação entre -1 e 1. Agora começam as limpezas de dados utilizando regex e NLTK. A primeira limpeza remove emojis, links e tudo aquilo que for desnecessário para a análise. Depois disso, ocorre uma tokenização dos tweets. Depois de gerados os tokens, uma nova limpeza é feita, para retirar stop words. Por fim, ocorre uma contagem de ocorrências baseadas numa base de palavras em inglês que representam sentimentos bons e ruins. Os gráficos são plotados pela matplotlib e enviados para a página web.

Os trending topics são obtidos através da API do twitter que apenas nos retorna os tópicos em alta, uma lista com aproximadamente 50 tópicos. Para fins de apresentação, são exibidos apenas os 10 primeiros.
