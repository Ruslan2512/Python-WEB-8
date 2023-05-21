from test_models import Author, Qoutes
from connect import connect


def find(command):
    authors = Author.objects()
    quotes = Qoutes.objects()
    while command != "exit":
        if command == "fullname":
            for author in authors:
                print(author.fullname)
        elif "tag" in command:
            print(*[qt.quote for qt in quotes if command[4:] in qt.tags])
        elif "tags" in command:
            tags_list = command[5:].split(",")
            for tg in tags_list:
                print(*[qt.quote for qt in tg if command[5:] in qt.tags])
        elif "name" in command:
            print(*[qt.quote for qt in quotes if command[6:] == qt.author])
        elif command == "exit":
            break
        else:
            print("Unknown command")


if __name__ == '__main__':
    find(input("command: "))

