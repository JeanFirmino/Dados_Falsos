#!/usr/bin/env python
# coding: utf-8

# # Gerador de dados - Biblioteca Faker
# 
# # Informações retiradas de seu documento oficial

# # Documento oficial ><>  https://faker.readthedocs.io/en/stable/#  <><

# Faker é um pacote Python que gera dados falsos para você.
# Se você precisa inicializar seu banco de dados, 
# criar documentos XML bonitos, preencha sua persistência para 
# fazer um teste de resistência ou anonimize os dados retirados de um
# serviço de produção, o Faker é para você.

# Compatível com python 3.6 e/ou superior.

# ## Instalar pacote na máquina
# 
# pip install Faker 
# 
# ou 
# 
# python -m pip install <package>
# 
# ou 
# 
# # No Jupyter
# import  sys 
# ! { Sys.executable } -m pip install numpy

# ## Iniciando a biblioteca

# In[67]:


from faker import Faker
fake = Faker()


# In[68]:


# Para gerar nomes pessoais
for _ in range(10):
  print(f"{fake.name()}")


# In[69]:


# Para gerar endereços
for _ in range(10):
  print(f"{fake.address()}\n")


# In[70]:


# Para gerar textos
print(f"{fake.text()}")


# ## Provedores

# Cada uma das propriedades do gerador (como name, address, e lorem) são chamados de “falsos”. 
# Um gerador faker tem muitos deles, empacotado em “provedores”.

# In[71]:


from faker.providers import internet

fake = Faker()
fake.add_provider(internet)

print(fake.ipv4_private())


# Todos os tipos de dados gerados podem ser encontrados em: https://faker.readthedocs.io/en/stable/providers.html

# ## Localização (idioma dos seus dados)

# "faker.Faker" pode tomar uma localidade como um argumento, para retornar dados relacionados com aquela localidade. Se nenhum provedor localizado for encontrado, a fábrica volta para o string LCID padrão para inglês dos EUA, ou seja: "en_US". 

# In[72]:


fake = Faker('it_IT')
for _ in range(10):
    print(f"{fake.name()}\n")
# Para dados da Itália    


# In[73]:


# Para vários idiomas
fake = Faker(['it_IT', 'en_US', 'ja_JP','pt_BR','pt_PT','es_ES','ru_RU','fr_FR','ro_RO'])
for _ in range(10):
    print(f"{fake.name()}")


# Caso queira usar uma localidade diferente, 
# use esse link e encontre as informações disponíveis: https://faker.readthedocs.io/en/stable/locales.html

# Caso queira usar grandes grupos de idiomas de uma vez, use isso...

# In[74]:


fake = Faker(['pt','de','en','es','la','th','fr','ru','ja'])
for _ in range(10):
    print(f"{fake.name()}")


# Dessa forma o idioma não será limitado a uma região ou a um local!

# ## Otimizações

# O construtor Faker usa um argumento relacionado ao desempenho chamado "use_weighting". Ele especifica se deve-se tentar ter a frequência de valores correspondem às frequências do mundo real (por exemplo, o nome em inglês Gary ser muito mais frequente do que o nome Lorimer). Se "use_weighting" é "False", então todos os itens têm a mesma chance de serem selecionados, e a seleção o processo é muito mais rápido. O padrão é "True". 

# In[75]:


# Exemplo:
fake = Faker(['pt'])
for _ in range(10):
    print(f"{fake.name()}")


# # Exemplo - Geração de Dados em vários idiomas 

# ## Endereços

# In[76]:


from faker import Faker
fake = Faker(['pt','de','en','es','la','th','fr','ru','ja'])
Faker.seed(0)
# Para endereços
for _ in range(10):
    print(f"Endereço completo:{fake.address()}")
    print(f"Número da residência:{fake.building_number()}")
    print(f"Cidade:{fake.city()}")
    print(f"Sufixo da cidade:{fake.city_suffix()}")
    print(f"País:{fake.country()}")
    print(f"Código do país:{fake.country_code()}")
    print(f"Código postal:{fake.postcode()}")
    print(f"Endereço da rua:{fake.street_address()}")
    print(f"Nome da rua:{fake.street_name()}\n")


# ## Automóvel 

# In[77]:


fake = Faker(['pt','de','en','es','la','th','fr','ru','ja'])
Faker.seed(0)
# Para automóvel
for _ in range(10):
    print(f"Licença:{fake.license_plate()}\n")


# ## Dados bancários

# In[78]:


fake = Faker(['pt','de','en','es','la','th','fr','ru','ja'])
Faker.seed(0)
# Para endereços
for _ in range(10):
    print(f"Número de trânsito de roteamento ABA:{fake.aba()}")
    print(f"Código de país do provedor do banco.:{fake.bank_country()}")
    print(f"Gere um número de conta bancária básico:{fake.bban()}")
    print(f"Gere um número de conta bancária internacional:{fake.iban()}")
    print(f"Swift:{fake.swift()}")
    print(f"Swift11:{fake.swift11()}")
    print(f"Swift8:{fake.swift8()}\n")


# ## continuar em https://faker.readthedocs.io/en/stable/providers/faker.providers.barcode.html

# ## Cores

# In[79]:


for _ in range(10):
    print(f"Cor:{fake.color(hue=(100, 200), color_format='rgb')}")
    print(f"Nome da cor:{fake.color_name()}")
    print(f"Cor hexadecimal:{fake.hex_color()}")
    print(f"Cor para o CSS:{fake.rgb_css_color()}")
    print(f"Cor HEX:{fake.safe_hex_color()}")


# ## Empresa

# In[80]:


for _ in range(10):
    print(f"Nome fantasia:{fake.bs()}")
    print(f"Lema:{fake.catch_phrase()}")
    print(f"Slogam:{fake.catch_phrase_attribute()}")
    print(f"Palavra-chave:{fake.catch_phrase_noun()}")
    #print(f"CNPJ:{fake.cnpj()}")
    print(f"Nome da empresa:{fake.company()}")
    #print(f"ID da empresa:{fake.company_id()}")
    print(f"Sufixo da empresa:{fake.company_suffix()}")


# ## Data

# In[81]:


for _ in range(10):
    print(f"Data:{fake.date()}")
    print(f"Data de aniversário:{fake.date_of_birth()}")
    print(f"Data nesse século:{fake.date_this_century()}")
    print(f"Data nessa década:{fake.date_this_decade()}")
    print(f"Data nesse mês:{fake.date_this_month()}")
    print(f"Data nesse ano:{fake.date_this_year()}")
    print(f"Data com a ISO8601:{fake.iso8601()}")


# In[82]:


## Internet


# In[83]:


for _ in range(10):
    print(f"Email pessoal:{fake.ascii_email()}")
    print(f"Email empresarial:{fake.company_email()}")
    print(f"Gerador de domínio:{fake.dga()}")
    print(f"Email:{fake.email()}")
    print(f"Email livre:{fake.free_email()}")
    print(f"IPV4:{fake.ipv4()}")
    print(f"IPV4 público:{fake.ipv4_public()}")
    print(f"IPV6:{fake.ipv6()}")
    print(f"URI:{fake.uri()}")
    print(f"URL:{fake.url()}")
    print(f"Nome de usuário:{fake.user_name()}")


# ## Emprego

# In[84]:


for _ in range(10):
    print(f"Emprego:{fake.job()}")


# ## Informações pessoais 

# In[85]:


for _ in range(10):
    print(f"Nome Completo:{fake.name()}")
    print(f"Número de telefone:{fake.phone_number()}")
    #print(f"CPF:{fake.cpf()}")
    #print(f"Identidade:{fake.rg()}")
    print(f"SSN:{fake.ssn()}")


# In[ ]:





# In[ ]:





# In[ ]:




