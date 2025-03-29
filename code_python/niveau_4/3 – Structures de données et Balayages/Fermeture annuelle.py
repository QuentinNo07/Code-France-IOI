def longest_inactive_period(periode, festivals):
    max_inactive = 0
    last_end = 0
    for start, end in festivals :
        if last_end < start:
            max_inactive = max(max_inactive, start - last_end)
        last_end = max(last_end, end)
    max_inactive = max(max_inactive, periode - last_end + festivals [0][0])
    return max_inactive


def main():
   
   periode, nb_festival = map(int, input().split())
   festivals = [tuple(map(int, input().split())) for _ in range(nb_festival)] 
   for D, F in festivals:
      if D > F:  
         festivals .append((D, periode))  
         festivals .append((0, F))          
   festivals .sort()

   print(longest_inactive_period(periode, festivals))
   
main()