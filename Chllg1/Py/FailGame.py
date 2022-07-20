def main():
    instances = []
    while True:
        try:
            numStud = int(input('Instance {}\nStudent amount(EOF for Exit): '.format(len(instances))))
        except EOFError:
            result(instances)

        instances.append([])
        for x in range(numStud):
            instances[len(instances)-1].append(input('Enter {} Student Name Followed By Grade: '.format(x+1)))


def result(inst):
    for num, instance in enumerate(inst):
        instance = sorted(instance)
        grade = 'Start 10'
        same = []
        for student in instance:
            if int(student.split()[-1]) <= int(grade.split()[-1]):
                grade = student
        
        grade = grade.split()[0:-1]
        failed = ''
        for word in grade:
            failed+= word+' '
        print('Instance {}\n{}\n'.format(num, failed))
    exit()

if __name__ == '__main__':
    main()