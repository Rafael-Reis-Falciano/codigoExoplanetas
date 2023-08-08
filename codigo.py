from selenium import webdriver 
from selenium.webdriver.common.by import By 
from bs4 import BeautifulSoup 
import time 
import pandas
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

url = "https://exoplanets.nasa.gov/discovery/exoplanet-catalog/"
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get(url)
time.sleep(10)

dados = []
def pegar_dados():
    for i in range(0,25):
        while True:
            informações = BeautifulSoup(driver.page_source,"html.parser")
            for j in informações.find_all("ul",attrs={"class","exoplanet"}):
                guardar = j.find_all("li")
                for indice,li in enumerate(guardar):
                    if indice == 0:
                        dados.append(li.find_all("a")[0].contents[0])
                    else:
                        dados.append(li.contents[0])
cabeçalho = ["nome","anos-luz de distância da Terra","massa","magnitude (brilho)","data de descoberta"]
arquivo = pandas.DataFrame(dados,columns=cabeçalho)
arquivo.to_csv("exoplanetas.csv",index=True,index_label="id")