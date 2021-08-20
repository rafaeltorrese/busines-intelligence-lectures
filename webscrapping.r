library(XML)  # Loads the XML library
library(RCurl)

getwd()
setwd("C:/Users/Rafael Torres/Documents/slides/business_intelligence/")

getwd()

url <- "https://github.com/asherif844/PracticalBusinessIntelligence/wiki/AdventureWorks---Weekly-Data-by-Discount"
get_URL <- getURL(url)
str(url)
retriveTable <- readHTMLTable(url, which = 1)
head(retriveTable)
