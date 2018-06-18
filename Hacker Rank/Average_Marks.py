if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for i in range(0,n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    #student_marks[query_name] = print(round((sum(scores)/3),2))
    #print(scores)
    #print(round((sum(student_marks[query_name])/len(student_marks[query_name])),2))
    avg_mark = sum(student_marks[query_name])/len(student_marks[query_name])
    print("%.2f"%round(avg_mark,2))
    # print(student_marks)
    # print(name)
    # print(len(scores))
    # print(" adfakljdf ")

