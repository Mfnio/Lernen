from calculatior import square

def main():
    test_square()

def test_square():
    for i in range(400):
        if square(i) != i * i:
            print("Es funktioniert nicht bei i * i")
    else:
        print("Alles funktioniert wie es sein soll ")
       
       
       
       
#        else:
#            print("Es funktioniert wie es sein soll bei 2")
#        if square(4) != 16:
#            print("Es funktioniert nicht bei 4")
#        else:
#            print("Es funktioniert wie es sein soll bei 4")           
#funktioniert

main()


