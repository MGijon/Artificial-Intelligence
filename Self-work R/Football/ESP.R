library(XML)

url17 <- "http://www.livefutbol.com/calendario/esp-primera-division-2016-2017-spieltag_2/38/"
url16 <- "http://www.livefutbol.com/calendario/esp-primera-division-2015-2016-spieltag/38/"  # from here there is a patron, let's automatize this
url15 <- "http://www.livefutbol.com/calendario/esp-primera-division-2014-2015-spieltag/38/"
liga17 <- readHTMLTable(url17, header = TRUE)[[4]]
liga16 <- readHTMLTable(url16, header = TRUE)[[4]]
liga15 <- readHTMLTable(url15, header = TRUE)[[4]]

head(liga15)
liga15[1,] # ganador de la liga

for (i in 1987:2015){
  url <- paste0("http://www.livefutbol.com/calendario/esp-primera-division-", toString(i), "-", toString(i + 1), "-spieltag/38/")
  datos[i - 1987] <- readHTMLTable(url, header = TRUE)[[4]]
}


