library(XML)

url17 <- "http://www.livefutbol.com/calendario/esp-primera-division-2016-2017-spieltag_2/38/"
url16 <- "http://www.livefutbol.com/calendario/esp-primera-division-2015-2016-spieltag/38/"  # from here there is a patron, let's automatize this
url15 <- "http://www.livefutbol.com/calendario/esp-primera-division-2014-2015-spieltag/38/"
liga17 <- readHTMLTable(url17, header = TRUE)[[4]]
liga16 <- readHTMLTable(url16, header = TRUE)[[4]]
liga15 <- readHTMLTable(url15, header = TRUE)[[4]]

liga17$Year <- 2017
head(liga17)
liga16$Year <- 2016
liga15$Year <- 2015
head(liga16)
head(liga15)

# cramos un data.frame 'gordote' con una nueva variable que indique el año:

Ligas <- rbind.data.frame(liga17, liga16)
Ligas <- rbind.data.frame(Ligas, liga15)


for (i in 1987:2015){
  url <- paste0("http://www.livefutbol.com/calendario/esp-primera-division-", toString(i), "-", toString(i + 1), "-spieltag/38/")
  datos<- readHTMLTable(url, header = TRUE)[[4]]
  datos$Year <- i
  Ligas <- rbind.data.frame(Ligas, datos)
}


summary(Ligas)
str(Ligas)

# Ahora que sabemos que el data.frame se ha creado correctamente, vamos a darle nombre apropiado a sus culumnas:
head(Ligas)
# -------------------------------------------------------
# v1 : Rank
# v2 : será eliminada, no contiene información
# v3 : Team
# v4 : Matches
# V5 : Victories
# v6 : Defeats
# v7 : Ties 
# v8 : Goals
# v9 : ?, por el momento la dejaré intacta
# v10 : Score
# -------------------------------------------------------

# Elimino primero v2
Ligas$V2 <- NULL
head(Ligas)

# también: names(Ligas)
colnames(Ligas) <- c('Rank', 'Team', 'Matches', 'Victories', 'Defeats', 'Ties', 'Goals', 'V9', 'Score', 'Year')
head(Ligas)

# el cambio de nombres se ha efectuado correctamente, nos resta convertir las varibles al tipo correcto, y 
# quizás, dividir los goles en contra y a favor, creando dos nuevas varibles

#Ligas$Goals[1]
#class(Ligas$Goals[1][1])

#Ligas[, which(names(Ligas) == 'Goals')][1] # 106:41
#class(Ligas[, which(names(Ligas) == 'Goals')][1]) # "factor"
#test <- as.character(Ligas[, which(names(Ligas) == 'Goals')][1])
#class(test)
#as.character(Ligas[, which(names(Ligas) == 'Goals')])
#class(Ligas[, which(names(Ligas) == 'Goals')][1])
Ligas$GPositive <- as.character(Ligas[, which(names(Ligas) == 'Goals')])
class(Ligas$GPositive)
head(Ligas)
Ligas$GNegative <- Ligas$GPositive
head(Ligas)

Ligas$GPositive[1].split(":")

class(strsplit(Ligas$GPositive[1], ':'))
length(strsplit(Ligas$GPositive[1], ':'))
test <- unique(strsplit(Ligas$GPositive[1], ':'))[[1]]
test
length(test)


# Guardo el data.frame una vez creado y arreglado
save(Ligas, file = "LigasESP.RData")
