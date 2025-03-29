from sys import stdin
def main():
   x1,y1,x2,y2 = map(int,input().split())
   aireAeroport = (y2 - y1) * (x2 - x1)
   nbTerrains = int(input())
   for _,description in zip(range(nbTerrains),stdin):
      x1Terrain,y1Terrain,x2Terrain,y2Terrain = map(int,description.split())
      dx = max(0, min(x2,x2Terrain) - max(x1,x1Terrain))
      dy = max(0, min(y1,y1Terrain) - max(y2,y2Terrain))
      aireAeroport -= dx * dy
   print(aireAeroport)
main()