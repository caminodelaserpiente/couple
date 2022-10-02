import random 


def data():
    data_elements = [
        'person_1',
        'person_2',
        'person_3',
        'person_4'
        ]
    return data_elements

def couples():
    elements = data()
    couples = []
    try:
        # Show elements in list
        n_elements = len(elements)
        i = 1
        for element in elements:
            print(i,element)
            i += 1
        print("Total elements: ", n_elements, "\n")

        if n_elements & 1 == 0:
            # Create couples
            while True:
                element_1 = random.choice(elements)
                element_2 = random.choice(elements)

                if element_1 != element_2:
                    elements.pop(elements.index(element_1))
                    couples.append(element_1)
                    elements.pop(elements.index(element_2))
                    couples.append(element_2)
                elif element_1 == element_2:
                    pass

                if n_elements == len(couples):
                    break
                
            # # Show pairs created
            print("########## Couples ##########")
            lugar_0 = 0
            lugar_1 = 1
            n_couples = int(len(couples) / 2)
            for i in range(n_couples):
                print(couples[lugar_0], ' & ', couples[lugar_1])
                lugar_0 += 2
                lugar_1 += 2
        else:
            print("*The list is odd, it needs to be even") 
    except:
        print("error")
    
if __name__ == '__main__':
    couples()
