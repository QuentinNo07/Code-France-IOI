def ensemble(nb_fois):
   if nb_fois==0:
      return "0"
   else:
      avant=(ensemble(nb_fois-1))
      return "({} + {})".format(avant,avant)


def equation(nb_fois):
   expression=ensemble(nb_fois)
   return "0 = {}".format(expression)

nb_fois=int(input())
print(equation(nb_fois))