
import sys
import os


def list(dir):
    filenames = os.listdir(dir)
    for filename in filenames:
        path = os.path.join(dir, filename)
        print(path)
        print(os.path.abspath(path))

def create_dir(todir):
    if not os.path.exists(todir):
        os.mkdir(todir)




def main():
    # list('c:/users/mflores1/pycharmprojects/practicepython')
    create_dir('c:/users/mflores1/pycharmprojects/practicepython/test')
    # args = sys.argv[1:]
    # if not args:
    #     print('Error')
    #     sys.exit(0)
    # else:
    #     List(sys.argv[1])

if __name__ == '__main__':
    main()