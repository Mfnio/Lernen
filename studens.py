class Student:
    def __init__(self, name, house):
        self.name = name
        if not name:
            raise ValueError("Name cannot be empty")
        self.house = house


def main():
    student = get_student()
    print(f"{student.name} from {student.house}")

def get_student():
    n = input("Name: ").rstrip().title()
    h = input("House: ").rstrip().title()
    return  Student(n, h)




if __name__ == "__main__":
    main()

