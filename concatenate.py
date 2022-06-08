

class Concatenate:
    def __init__(self, files=[]):
        self.__files = files
        self.__filelist = []
        self.__file_list()
        self.__product = []
        self.__concatenate()

    def __newlineRemover(self, s):
        if s.endswith('\n'):
            return s[0: s.find('\n')]
        else:
            return s

    def __file_list(self):
        for file in self.__files:
            with open(file, 'r') as f1:
                self.__filelist.append(f1.readlines())

    def __concatenate(self):
        for line in range(len(max(self.__filelist))):
            for file in self.__filelist:
                try:
                    if file[line] == '\n':
                        self.__product.append('')
                    else:
                        self.__product.append(
                            self.__newlineRemover(file[line]))
                except IndexError:
                    self.__product.append('')

    def create_file(self):
        counter = 0
        with open('result.txt', 'w') as f:
            for line in self.__product:
                f.write(line)
                counter += 1
                if counter == len(self.__files):
                    f.write('\n')
                    counter = 0

    def print_product(self):
        counter = 0
        for line in self.__product:
            print(line, end='')
            counter += 1
            if counter == len(self.__files):
                print()
                counter = 0

    def __str__(self):
        self.create_file()
        with open("result.txt", 'r') as f:
            return f.read()

    def result(self, destination='result.txt'):
        with open(destination, 'r') as f:
            return f.read()

    def getProduct(self):
        return self.__product


def main():
    concatenate = Concatenate()
    # concatenate.print_product()
    # print(concatenate)
    concatenate.create_file()


if __name__ == '__main__':
    main()
