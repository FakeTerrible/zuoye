import random

def func(employees, n):
    for i in range(n):
        t = random.randrange(0, len(employees))
        print(employees[t])
        employees.remove(employees[t])


if __name__ == '__main__':
    employees = [i for i in range(300)]
    print("三等获奖奖名单：")
    func(employees, 30)
    print("二等获奖奖名单：")
    func(employees, 6)
    print("一等奖获奖名单：")
    func(employees, 3)
    