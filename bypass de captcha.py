#!/usr/bin/env python
# coding: utf-8

# In[2]:


get_ipython().system('pip install anticaptchaofficial')


# In[3]:


get_ipython().system('pip install webdriver_manager')


# In[8]:


#serviceLindo
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from anticaptchaofficial.recaptchav2proxyless import *
import time
from chave import chave_api

navegador = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
link = "https://google.com/recaptcha/api2/demo"
navegador.get(link)

chave_captcha = navegador.find_element(By.ID, 'recaptcha-demo').get_attribute('data-sitekey')

solver = recaptchaV2Proxyless()# "instancia"
solver.set_verbose(1)#atualiza o status de espera
solver.set_key(chave_api)#AQUI VAI A CHAVE DA API DO CAPTCHA
solver.set_website_url(link)#LINK DO SITE QUE VOCE QUER RESOLVER
solver.set_website_key(chave_captcha)# ao visualizar o captcha como dev, vai na Div Id- captcha, e lá tera a chave -> datasitkey 

resposta = solver.solve_and_return_solution()

if resposta != 0:#ver erro string
    print(resposta)
    # ao validar com o if...preencher o campo do token do captcha
    # g-recaptcha-response
    navegador.execute_script(f"document.getElementById('g-recaptcha-response').innerHTML = '{resposta}'")
    navegador.find_element(By.ID, 'recaptcha-demo-submit').click()
else:
    print(solver.err_string)

time.sleep(100)


# In[ ]:




