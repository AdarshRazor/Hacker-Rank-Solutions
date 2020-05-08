if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for i in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores        

    query_name = input()
    new=list(student_marks[query_name])
    l=len(new)
    total=sum(new)
    avg=total/len(new)
    
    print("%.2f"%avg)
