class Student():
    def __init__(self):
        self.first_name = "Harshad"
        self.last_name = "chavan"

    def __str__(self):
        return "{} {}".format(self.first_name,self.last_name)


if __name__ == "__main__":
    s1 = Student()
    print(s1)