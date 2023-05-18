from test_models import Author, Qoutes


author = Author(fullname='Grigoriy Skovoroda',
                born_date='December 2 1722',
                born_location='v. Chornuhi',
                description='novelist, poet')

qoutes = Qoutes(tags=['novelist', 'poet'],
                author='Grigoriy Skovoroda',
                quote='What can be sweeter than when a good soul loves and longs for you?')


