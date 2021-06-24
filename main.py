list=[{'name': 'mouse', 'price': 200}, {'name': 'table', 'price': 400}, {'name': 'phone', 'price': 4000}]
bought_thing = []
n = 100
while n != 0:
    print("1 - Create notice" )
    print("2 - Show all notices")
    print("3 - To buy something by name of notice")
    print("4 - Show bought thing")
    print("5 - Show general price")
    print("6 - The most expensive thing")
    print("0 - go out")
    n = int(input("Enter number: "))
    if n == 1:
        name = input("Enter name: ")
        price = int(input("Enter price: "))
        list.append({'name': name, 'price': price})
    if n == 2:
        for i in range(len(list)):
            print(i, list[i])
    if n == 3:
        find = input('Enter name ')
        for i in list:
            if i['name'] == find:
                bought_thing.append(i)
    if n == 4:
        for i in range(len(bought_thing)):
            print(bought_thing[i])
    if n == 5:
        sum = 0
        for i in bought_thing:
            sum += i['price']
        print(sum)
    if n == 6:
        expensive = 0
        expensive_thing = []
        for i in bought_thing:
            if i['price'] >= expensive:
                expensive = i['price']
                expensive_thing = i
        print(expensive_thing)


