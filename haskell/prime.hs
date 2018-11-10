prime = sieve [20^1000000..]
sieve (p:ps) = p : sieve [x | x <- ps, mod x p /= 0]
