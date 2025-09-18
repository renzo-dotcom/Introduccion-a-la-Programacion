"""Si quiero mostrar una frase aleatoria entre 3 opciones, como hago?"""

import random

correo1="@gmail.com"
correo2="@outlook.com"
correo3="@yahoo.com"

ale=random.randint(1,3)

if ale==1 :
    print(correo1)
elif ale==2 :
    print(correo2)
elif ale==3 :
    print(correo3)