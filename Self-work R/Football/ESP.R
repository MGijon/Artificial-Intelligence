library(XML)

url17ESP <- "http://www.livefutbol.com/calendario/esp-primera-division-2016-2017-spieltag_2/38/"
url16ESP <- "http://www.livefutbol.com/calendario/esp-primera-division-2015-2016-spieltag/38/"
liga17ESP <- readHTMLTable(url17ESP, header = TRUE)[[4]]
liga16ESP <- readHTMLTable(url16ESP, header = TRUE)[[4]]
liga17ESP