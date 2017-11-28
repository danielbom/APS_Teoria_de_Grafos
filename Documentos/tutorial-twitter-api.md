# Tutorial - Twitter API em Python

## Introdução
O Twitter disponibiliza um serviço *web* através de uma API (*Application Programming Interface*) para que usuários possam consumir seus dados e a biblioteca utilizada, **python-twitter**, tem como objetivo facilitar o uso deste serviço para programadores Python.

A documentação do **python-twitter** está disponível em https://python-twitter.readthedocs.io/ e para obter mais informações sobre o serviço fornecido pelo Twitter, a documentação completa está disponível em https://developer.twitter.com/en/docs.


## Instalação
Para instalar a biblioteca é necessário utilizar o gerenciador de pacotes do Python, *PIP*, utilizando o comando `pip install python-twitter`.


## Utilização

### Obtendo *tokens*
O primeiro passo é obter *tokens* autenticados pelo Twitter para que se possa fazer chamadas à API por meio da biblioteca utilizada. Há quatro chaves necessárias para isto, sendo elas: *Consumer Key*, *Consumer Secret*, *Access Token* e *Access Token Secret*.

Para obtê-las é necessário criar um aplicativo na plataforma do Twitter (ver https://apps.twitter.com/app/new). Uma vez que o aplicativo foi criado você será direcionado para uma página que exibe algumas informações sobre ele e então poderá obter os *tokens* na aba `Keys and Access Tokens`. Para finalizar é exigido que a aplicação tenha acesso à sua conta do Twitter, para isso, clique no botão `Create my access token`.

### Utilização da lib **python-twitter**
Os tokens são necessários para executar os métodos presentes na biblioteca utilizada, tais como métodos para obter a lista de amigos, lista de seguidores, *tweets*, postar novos *tweets*, etc.

Primeiramente, instancia-se um objeto autorizado para fazer as chamadas à API:
```
import twitter

api = twitter.Api(
	consumer_key=[consumer key],
	consumer_secret=[consumer secret],
	access_token_key=[access token],
	access_token_secret=[access token secret]
)
```

Obtendo 10 amigos do Neymar:
```
api.GetFriends(screen_name="neymarjr", total_count=10)

# Resposta da API
[
	User(ID=928299714000322560, ScreenName=PSGLeMag),
 	User(ID=69562833, ScreenName=MDALGLISHAPPEAL),
 	User(ID=2182274466, ScreenName=PSGbrasil),
 	User(ID=38164846, ScreenName=PSG_inside),
 	User(ID=775365587941920768, ScreenName=Ligue1_POR),
	User(ID=3282859598, ScreenName=TwitterVideo),
 	User(ID=26053643, ScreenName=jimmykimmel),
	User(ID=65625467, ScreenName=UltrafarmaEVoce),
 	User(ID=538257477, ScreenName=Diegopdamas),
 	User(ID=26264871, ScreenName=LaureusSport)
]
```

Obtendo a lista de 10 seguidores do Google:
```
# Caso deseje obter a lista completa, remova o parâmetro total_count
api.GetFollowers(screen_name="google", total_count=10)

# Resposta da API
[
	User(ID=771813384203272192, ScreenName=capitalgtweets),
	User(ID=2669636582, ScreenName=admob),
	User(ID=762692626403373060, ScreenName=GoogleTCProgram),
	User(ID=3307941657, ScreenName=googlepartners),
	User(ID=734854525375287298, ScreenName=GoogleMyBiz),
	User(ID=294561527, ScreenName=GoogleThailand),
	User(ID=149134959, ScreenName=Google_Sverige),
	User(ID=53002114, ScreenName=GoogleRussia),
	User(ID=58303955, ScreenName=GoogleNL),
	User(ID=384536513, ScreenName=GoogleMsia)
]
```


Uma limitação da API está na quantidade de requisição, sendo possível fazer apenas 15 requisições a cada 15 minutos.