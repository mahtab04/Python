# squares = [1, 4, 9, 16]
# sum = 0
# for num in squares:
#     sum += num

# print(sum)  # 30

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        print(name)
        scores = list(map(float, line))
        student_marks[name] = scores
        print(student_marks)
    query_name = input()
    if query_name == name:
        
