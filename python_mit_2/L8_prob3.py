def FancyDivide(list_of_numbers, index):
   denom = list_of_numbers[index]
   return [SimpleDivide(item, denom)
               for item in list_of_numbers]


def SimpleDivide(item, denom):
   try:
       return item / denom
   except ZeroDivisionError:
       return 0

def main():
    print(FancyDivide([0, 2, 4], 0))

if __name__ == '__main__':
    main()
