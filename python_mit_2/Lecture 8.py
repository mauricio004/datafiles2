def FancyDivide(list_of_numbers, index):
    try:
        try:
            raise Exception("0")
        finally:
            denom = list_of_numbers[index]
            for i in range(len(list_of_numbers)):
                list_of_numbers[i] /= denom
    except Exception as err:
        print(err)



def main():
    FancyDivide([0, 2, 4], 0)

if __name__ == '__main__':
    main()
