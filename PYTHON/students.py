class Student():
    def __init__(self, firstname, secondname, birthdate, avgball):
        self.firstname = firstname
        self.secondname = secondname
        self.birthdate = birthdate
        self.avgball = avgball

fields = ['firstname', 'secondname', 'birthdate', 'avgball']

def get_students():
    students = []

    while 1:
        isBreak = False
        student = {}

        try:
            for f in fields:
                curr = input(f + ": ")
                student[f] = curr

                if curr == '':
                    raise ValueError("Empty field!")

                if curr == '.stop': 
                    isBreak = True
                    break
        except Exception as error:
            print(error)
        else:
            if isBreak:
                break
            st = Student(**student)
            students.append(st)
            if input("stop?(yes, ye, .stop) ") in ['.stop', 'yes', 'ye']:
                break

    return students

def log_and_write(students):
    if len(students) == 0: return
    print('\nStudents:\n')
    with open("Group.txt", 'w') as wf:
        for st in students:
            for f in fields:
                s = "%s: %s\n" % (f, getattr(st, f))
                wf.write(s)
                print("   ", s, end='')
            print()
            wf.write("\n")

def main():
    sts = get_students()
    log_and_write(sts)

if __name__ == "__main__":
    print("To stop write \".stop\"\n")
    main()

