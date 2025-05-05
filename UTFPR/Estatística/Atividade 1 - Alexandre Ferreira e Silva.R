# --------------------------------------------------------------------------------------
# UTFPR - PÓS GRADUAÇÃO EM INTELIGÊNCIA ARTIFICIAL
# Disciplina: Estatística Aplicada
# Prof.: Cléber Gimenez Corrêa
# Aluno: Alexandre Ferreira e Silva
# Atividade Aula 01
# Fonte: ChatGPT, Desmos Grphic Calculator
# --------------------------------------------------------------------------------------

# Carregar o dataset
data("USArrests")
dados <- USArrests

# ------------------------------------------------------------------------
# Ordena os dados para pegar os MAIORES
# ------------------------------------------------------------------------
n <- nrow(dados)
for (i in 1:(n - 1)) {
  for (j in 1:(n - i)) {
    if (dados$UrbanPop[j] < dados$UrbanPop[j + 1]) {
      # Trocar linhas j e j+1
      temp <- dados[j, ]
      dados[j, ] <- dados[j + 1, ]
      dados[j + 1, ] <- temp
    }
  }
}
maiores <- dados[1:5, ]
head(maiores)

# ------------------------------------------------------------------------
# Ordena os dados para pegar os MENORES
# ------------------------------------------------------------------------
n <- nrow(dados)
for (i in 1:(n - 1)) {
  for (j in 1:(n - i)) {
    if (dados$UrbanPop[j] > dados$UrbanPop[j + 1]) {
      # Trocar linhas j e j+1
      temp <- dados[j, ]
      dados[j, ] <- dados[j + 1, ]
      dados[j + 1, ] <- temp
    }
  }
}
menores <- dados[1:5, ]
head(menores)

resultados <- matrix(1:6, nrow = 2, ncol = 3)
rownames(resultados) <- c("Maiores", "Menores")
colnames(resultados) <- c("Média Assassinato", "Média Assalto", "Média Estupro")
# ------------------------------------------------------------------------
# Laço para calcular as médias das MAIORES
# ------------------------------------------------------------------------
media_assassinato <- 0
media_assalto <- 0
media_estrupro <- 0

for (i in 1:5) {
  media_assassinato <- media_assassinato + maiores$Murder[i]
  media_assalto <- media_assalto + maiores$Assault[i]
  media_estrupro <- media_estrupro+ maiores$Rape[i]
}

resultados[1,1] <- media_assassinato/5
resultados[1,2] <- media_assalto/5
resultados[1,3] <- media_estrupro/5

# ------------------------------------------------------------------------
# Laço para calcular as médias das MENORES
# ------------------------------------------------------------------------
media_assassinato <- 0
media_assalto <- 0
media_estrupro <- 0

for (i in 1:5) {
  media_assassinato <- media_assassinato + menores$Murder[i]
  media_assalto <- media_assalto + menores$Assault[i]
  media_estrupro <- media_estrupro + menores$Rape[i]
}

resultados[2,1] <- media_assassinato/5
resultados[2,2] <- media_assalto/5
resultados[2,3] <- media_estrupro/5

# ------------------------------------------------------------------------
# RESULTADOS
# ------------------------------------------------------------------------
resultados