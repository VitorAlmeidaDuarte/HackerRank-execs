

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    student = student_marks[query_name]

    media_mark = 0
    for mark in student:
        media_mark += mark
  
    finaly_media = media_mark / 3
    print('%0.2f' % finaly_media)        

