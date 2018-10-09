n,m = [int(i) for i in input().split()]
prices = [int(i) for i in input().split()]
neg_prices = [x for x in prices if x<0]
neg_prices.sort()
m = min(m, len(neg_prices))
neg_prices = [neg_prices[i] for i in range(m)]
print(-int(sum(neg_prices)))