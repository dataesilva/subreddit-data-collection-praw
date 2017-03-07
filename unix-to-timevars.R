loit <- read_csv("filename.csv")
View(loit)

loit$est <- as.POSIXct(as.numeric(as.character(loit$created)), origin = "1970-01-01", tz= "EST")
loit$year <- as.POSIXlt(loit$est, tx = "EST")$year
loit$mon <- as.POSIXlt(loit$est, tx = "EST")$mon
loit$mday <- as.POSIXlt(loit$est, tx = "EST")$mday
loit$wday <- as.POSIXlt(loit$est, tx = "EST")$wday
loit$hour <- as.POSIXlt(loit$est, tx = "EST")$hour
loit$iswknd <- as.POSIXlt(loit$est)$wday < 1 | as.POSIXlt(loit$est)$wday > 5
summary(loit2$iswknd)

write.csv(loit, "newfilename.csv", row.names=F)
