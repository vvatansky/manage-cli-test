from sys import argv


class Help:
    def run(self, args):
        print(f'-- Run task [help] with arguments: {args}')


class Plus:
    def run(self, args):
        print(f'-- Run task [plus] with arguments: {args}')


class Manager:
    def __init__(self):
        self.tasks = {
            'help': Help(),
            'plus': Plus()
        }

    def parse_args(self, *args):

        result = {'list': []}
        is_wait, anchor = False, None
        for x in args:
            if is_wait:
                result[anchor] = x
                is_wait = False
            else:
                if x[0] == '-':
                    anchor = x
                    is_wait = True
                else:
                    result['list'].append(x)
        return result


    def run(self, task, *args):
        obj = self.tasks.get(task, None)
        if obj:
            obj.run(self.parse_args(*args))


def main():
    if len(argv) < 2: exit()
    _, task, *args = argv
    Manager().run(task, *args)


if __name__ == '__main__':
    main()