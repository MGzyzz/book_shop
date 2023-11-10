# book_shop

Общая настройка для всех операционных систем:

git clone [git@github.com:MGzyzz/book_shop.git](https://github.com/MGzyzz/book_shop.git)

Для запуска проекта, следуете по указаным пунктам 

Windows:

python -m venv venv

. venv/bin/activate

pip3 install -r reqs.txt

python manage.py migrate

python runserver

MacOs:

python3 -m venv venv

. venv/bin/activate

pip3 install -r reqs.txt

python3 manage.py migrate

python3 manage.py runserver
