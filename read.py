from test_models import Author, Qoutes
from connect import connect


if __name__ == '__main__':
    authors = Author.objects()
    for author in authors:
        print(author.to_mongo().to_dict())
    # for post in Post.objects(tags='mongodb'):
    #     print(post.title)
    qoutes = Qoutes.objects()
    for qoute in qoutes:
        print(qoute.to_mongo().to_dict())

