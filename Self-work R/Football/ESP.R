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

