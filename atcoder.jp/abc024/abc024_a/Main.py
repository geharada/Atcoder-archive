a,b,c,k = map(int,input().split())
s,t = map(int,input().split())
print(s * a + t * b - (c * (s + t))) if s + t >= k else print(s * a + t * b)