def reversed_array():
    N = int(input("Введите кол-во чисел:"))
    numbers = []
    for _ in range(N):
        number = int(input()) #читам число
        numbers.append(number) #добавляю в массив
        reversed_numbers = numbers[::-1] #переворачиваем массив
        print("".join(map(str, reversed_numbers)))

if __name__ == "__main__":
    reversed_array