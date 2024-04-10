def color_code(color):
    cor = cores()
    resistencia = cor[color]

    return resistencia


def cores():
  cores = { "black": 0,
    "brown": 1,
    "red": 2,
    "orange": 3,
    "yellow": 4,
    "green": 5,
    "blue": 6,
    "violet": 7,
    "grey": 8,
    "white": 9,
  }

  return cores



def colors():
   lista_cores = [
    "black",
    "brown",
    "red",
    "orange",
    "yellow",
    "green",
    "blue",
    "violet",
    "grey",
    "white",
]
   return lista_cores
   



print(color_code("orange"))