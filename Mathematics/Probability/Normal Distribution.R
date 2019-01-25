options(digits = 3)
m <- 30;
s <- 4;
p1 <- pnorm(40, m, s)
p2 <- 1 - pnorm(21, m, s)
p3 <- pnorm(35, m, s) - pnorm(30, m, s)
result <- c(p1, p2, p3)
cat(result, sep = "\n")
