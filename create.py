from test_models import Author, Qoutes
from connect import connect


author = Author(fullname='Grigoriy Skovoroda',
                born_date='December 2 1722',
                born_location='v. Chornuhi',
                description='novelist, poet')
author.save()

qoutes = Qoutes(tags=['novelist', 'poet'],
                author='Grigoriy Skovoroda',
                quote='What can be sweeter than when a good soul loves and longs for you?')
qoutes.save()


