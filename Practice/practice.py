# def say_hello():
#     print("Hello")

# say_hello()

# def say_hello(name):
#     print(f'Hello {name}')

# say_hello('Jose')

# def add_num(num1,num2):
#     return num1+num2

# result = add_num(10,20)



# def even_check(number):
#     return number % 2 == 0
    

# result = even_check(21)

# print(result)

# Return true if any number is even inside a list

# def even_number_in_list(num_list):


#     #place holder variables
#     even_numbers = []


#     for number in num_list:
#         if number % 2 == 0:
#             even_numbers.append(number)
#         else:
#             pass

#     return even_numbers

# result = even_number_in_list([1,2,3,4,5,6,7,8,9,10])

# print(result)





# Tuple unpacking

# stock_prices = [('APPL', 200),('GOOG',400),('MSFT',100)]

# for item in stock_prices:
#     print(item)

# for ticker,price in stock_prices:
#     print(ticker)

work_hours = [('Abby',100),('Billy',400),('Cassie',800)]

def employee_of_month(work_hours):

    current_max = 0
    employee_of_month = ''

    for employee,hours in work_hours:
        if hours > current_max:
            current_max = hours
            employee_of_month = employee
        else:
            pass

    #Return
    return(employee_of_month,current_max)

# result = employee_of_month(work_hours)
name,hours = employee_of_month(work_hours)

print(name + ' ' + str(hours))