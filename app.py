from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Informações de padroes pré configuradas
emailUsuario = 'email do usuario'
senhaUsuario = 'senha do usuario'
nomeCliente = 'Cliente a ser acessado'
numeroPedido = 'Código do contrato'
categoriaContrato = 'Categoria do contrato'
valorContrato = 'valor do contrato'
dataIncial = 'vigência inicial'
dataFinal = 'vigência final'
unidadeContrato = 'Unidade do contrato'
fornecedorContrato = 'CNPJ do fornecedor'

# Entrar no site https://accounts-qa.atlasfacilities.com.br/Account/Login via edge
driver = webdriver.Edge()
driver.get('https://accounts-qa.atlasfacilities.com.br/Account/Login')

# Digitar email 'Username' e senha 'password'
campoEmail = driver.find_element(By.XPATH, "//input[@id='Username']")
campoEmail.send_keys(emailUsuario)

campoSenha = driver.find_element(By.XPATH, "//input[@id='Password']")
campoSenha.send_keys(senhaUsuario)

sleep(3)

#Verificacao caso ja esteja logado no cliente 'S', caso nao 'N'
verificacaoLoggin = input("Está logado no cliente? S / N: ").upper()
if (verificacaoLoggin == 'S'):
    sleep(3)
    pass
else:
    campoPesquisaCliente = driver.find_element(By.XPATH, "//input[@id='inputCompanyName']")
    campoPesquisaCliente.send_keys(nomeCliente)

    buttonVisualizacao = driver.find_element(By.XPATH, "//button[@id='buttonChangeView_0']")
    buttonVisualizacao.click()
    sleep(5)


#Acessando a tela de setup de contrato
driver.get('https://gestao-qa.atlasfacilities.com.br/contracts/new')

sleep(5)

#Preenchendo numero de pedido
campoNumeroPedido = driver.find_element(By.XPATH, "//input[@placeholder='Número do pedido']")
campoNumeroPedido.send_keys(numeroPedido)

#Escolhendo SLA 'Padrao'
dropdownSLA = driver.find_element(By.XPATH, "//p-dropdown[@optionvalue='id' and @placeholder='Selecione o SLA']")
wait = WebDriverWait(driver, 10)
wait.until(EC.visibility_of(dropdownSLA))

sleep(1)
dropdownSLA.click()

opcoesSLA = driver.find_element(By.XPATH, "//li[@aria-label='Padrão']")
sleep(1)
opcoesSLA.click()

#Escolhendo categoria 'Brigada de incendio'
dropdownCategoria = driver.find_element(By.XPATH, "//p-dropdown[@optionvalue='id' and @placeholder='Nome da Categoria']")
wait = WebDriverWait(driver, 10)
wait.until(EC.visibility_of(dropdownCategoria))

sleep(1)
dropdownCategoria.click()

wait = WebDriverWait(driver, 15)
campoPesquisaCategoria = driver.find_element(By.XPATH, "//input[@class='p-dropdown-filter p-inputtext p-component ng-tns-c136-6']")
campoPesquisaCategoria.send_keys(categoriaContrato)
opcoesCategoria = driver.find_element(By.XPATH, "//li[@aria-label='Brigada de incêndio']")
opcoesCategoria.click()

#Escolhendo Modelo de Contratacao 'Continuo'
dropdownModeloContratacao = driver.find_element(By.XPATH, "//p-dropdown[@optionvalue='id' and @placeholder='Modelo da Contratação']")
wait = WebDriverWait(driver, 10)
wait.until(EC.visibility_of(dropdownModeloContratacao))

sleep(1)
dropdownModeloContratacao.click()

opcoesModeloContratacao = driver.find_element(By.XPATH,"//li[@aria-label='Contínuo']")
opcoesModeloContratacao.click()
dropdownModeloContratacao = driver.find_element(By.XPATH, "//p-dropdown[@optionvalue='id' and @placeholder='Modelo da Contratação']")

#Escolhendo Modelo de Contrato 'Sem controle de horario e salario'
dropdownModeloContrato = driver.find_element(By.XPATH, "//p-dropdown[@optionvalue='id' and @placeholder='Modelo do Contrato']")
wait = WebDriverWait(driver, 10)
wait.until(EC.visibility_of(dropdownModeloContrato))

sleep(1)
dropdownModeloContrato.click()

opcoesModeloContrato = driver.find_element(By.XPATH, "//li[@aria-label='Sem controle de horário e salário']")
opcoesModeloContrato.click()

#Passando valor de contrato
campoValorContrato = driver.find_element(By.XPATH, "//input[@placeholder='Valor do contrato']")
campoValorContrato.send_keys(valorContrato)

#Passando data inicial do contrato
campoDataInicial = driver.find_element(By.XPATH, "//input[@placeholder='dd/mm/aaaa' and @class='ng-tns-c92-3 p-inputtext p-component ng-star-inserted']")
campoDataInicial.send_keys(dataIncial)
campoDataInicial.send_keys(Keys.ESCAPE)

#Passando data final do contrato
campoDataFinal = driver.find_element(By.XPATH, "//input[@placeholder='dd/mm/aaaa' and @class='ng-tns-c92-4 p-inputtext p-component ng-star-inserted']")
campoDataFinal.send_keys(dataFinal)
campoDataFinal.send_keys(Keys.ESCAPE)

#Selecionando a unidade do contrato
dropdownUnidade = driver.find_element(By.XPATH, "//p-dropdown[@optionvalue='id' and @placeholder='Selecione a unidade']")
wait = WebDriverWait(driver, 10)
sleep(2)
wait.until(EC.visibility_of(dropdownUnidade))
dropdownUnidade.click()

campoPesquisaUnidade = driver.find_element(By.XPATH, "//input[@class='p-dropdown-filter p-inputtext p-component ng-tns-c136-7']")
campoPesquisaUnidade.send_keys(unidadeContrato)
opcoesUnidade = driver.find_element(By.XPATH, "//li[@aria-label='Unidade Carapicuiba']")
opcoesUnidade.click()
campoDataFinal.send_keys(Keys.ESCAPE)
sleep(2)

#Selecionando o fornecedor
dropdownFornecedor = driver.find_element(By.XPATH, "//p-dropdown[@optionvalue='id' and @placeholder='CNPJ do fornecedor']")
wait = WebDriverWait(driver, 10) 
sleep(2)
wait.until(EC.visibility_of(dropdownFornecedor))
dropdownFornecedor.click()

campoPesquisaFornecedor = driver.find_element(By.XPATH, "//input[@class='p-dropdown-filter p-inputtext p-component ng-tns-c136-5']")
campoPesquisaFornecedor.send_keys(fornecedorContrato)
opcoesFornecedor = driver.find_element(By.XPATH, "//li[@aria-label='50.840.129/0001-86']")
opcoesFornecedor.click()
campoDataFinal.send_keys(Keys.ESCAPE)
sleep(2)

#Salvando contrato
wait = WebDriverWait(driver, 10)
botaoSalvar = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@class='afm-btn-default afm-btn-secondary border-t px-3']")))
campoDataFinal.send_keys(Keys.ESCAPE)
sleep(1)
botaoSalvar.click()

#Acessando a listagem de contratos
driver.get('https://gestao-qa.atlasfacilities.com.br/contracts/list')
driver.refresh()

# Exibir uma caixa de mensagem de sucesso
driver.execute_script(f"alert('Contrato {numeroPedido} salvo com sucesso!')")

# Esperar um momento para que a mensagem seja exibida
driver.implicitly_wait(5)

digite = input("digite algo: ")
driver.quit()
