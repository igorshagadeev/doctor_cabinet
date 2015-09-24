Igor Shagadeev

hospital doctors sheduler

Django 1.8, python 3.4, jquery, fullCalendar


how it works - look at service_example.png


hot-start: simple sqlite db included
    1) clone
    2) cd sheduler
    2) $ python manage.py runserver

if no db:

    $ python manage.py makemigrations
    $ python manage.py migrate

make some fixtures to db before run<br/>
that also sets superuser <br/>
login: admin<br/>
passw: 1<br/>

    $ python manage.py fillData