from models import Post, LinkPost, ImagePost, TextPost, User


if __name__ == '__main__':
    post = Post.objects(title='mongodb')
    print(post[0].to_mongo().to_dict())