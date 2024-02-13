import os
import re
from functools import reduce

class task8:
    def __init__(self):
        pass

    def ex1(self, path):
        return os.path.exists(path)

    def ex2(self, path="UsersName.txt"):
        if self.ex1(path):
            with open(path, 'r') as f:
                for l in f:
                    yield l
        else:
            with open(path, 'w'):
                pass

    def ex3(self,path):
        arr = list(self.ex2(path))
        num=int(len(arr) *0.1)
        return arr[num:]

    def ex4(self):
        arr = self.ex2()
        return [line for i, line in enumerate(arr)if i%2==0]

    def ex5(self):
        emails=self.ex2("UsersEmail.txt")
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        for e in emails:
            if not re.match(pattern, e):
                print(e)
                return False
        return True

    def ex6(self):
        result=[]
        emails=self.ex2("UsersEmail.txt")
        pattern = r'^[a-zA-Z0-9._%+-]+@gmail.com'
        for e in emails:
            if re.match(pattern, e):
               result.append(e)
        return result

    def ex7(self):
        result={}
        emails=self.ex2("UsersEmail.txt")
        users=self.ex2()
        for e,u in zip(emails, users):
            print(u)
            print(e)
            if e.find(u)!=-1:
                result[u]=e
        return result

    def ex8(self,name):
        name+='\n'
        allNames=self.ex2()
        print(name in allNames)
        print([ord(char) for char in name])
        print(name.count('A'))
    def ex9(self):
        listi=list(self.ex2())
        return all(l[0].isupper() for l in listi)

    def ex10(self):
        listi = list(self.ex2())
        return len(listi)/8*200+len(listi)%8*50