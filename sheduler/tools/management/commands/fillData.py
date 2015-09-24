# django
from django.contrib.auth.models import User
from django.core.management.base import BaseCommand, CommandError

# project
from doctor.models import Doctor
from appointment.models import Appointment

import random
from datetime import datetime, timedelta

NAMES_LIST = [
    u'Александр',
    u'Сергей',
    u'Дмитрий',
    u'Андрей',
    u'Алексей',
    u'Максим',
    u'Евгений',
    u'Владимир',
    u'Иван',
    u'Михаил',
    u'Елена',
    u'Ольга',
    u'Наталья',
    u'Екатерина',
    u'Анна',
    u'Татьяна',
    u'Юлия',
    u'Анастасия',
    u'Ирина',
    u'Мария',
]

SURNAMES_LIST = [
    u'Смирнов',
    u'Иванов',
    u'Кузнецов',
    u'Соколов',
    u'Попов',
    u'Лебедев',
    u'Козлов',
    u'Новиков',
    u'Морозов',
    u'Петров',
    u'Волков',
    u'Соловьёв',
    u'Васильев',
    u'Зайцев',
    u'Павлов',
    u'Семёнов',
    u'Голубев',
    u'Виноградов',
    u'Богданов',
    u'Воробьёв',
    u'Фёдоров',
    u'Михайлов',
    u'Беляев',
    u'Тарасов',
    u'Белов',
    u'Комаров',
    u'Орлов',
    u'Киселёв',
    u'Макаров',
    u'Андреев',
]


# time deltas

def random_date():
    t = datetime.today()
    app_datetime = datetime(t.year, t.month, t.day) + timedelta(days=random.randint(0, 15), hours=random.randint(9, 18))
    return app_datetime


class Command(BaseCommand):
    args = 'no'
    help = '''
        Resets all data and users. Then fills DB with new sample data.
        Super user for admin becomes: login: , pass: 
    '''
    def handle(self, *args, **options):
        """ """

        admin = User.objects.get_or_create(username='admin', is_staff=True, is_active=True, is_superuser=True)
        if admin[1]:
            admin[0].set_password('1')
            admin[0].save()

        # doctors
        doctors = []
        for i in range(5):
            doctor = Doctor.objects.create(name=random.choice(SURNAMES_LIST))
            doctors.append(doctor)
        print('doctors added')

        # appointments
        for i in range(100):
            app = Appointment.objects.create(
                name=random.choice(NAMES_LIST),
                surname=random.choice(SURNAMES_LIST),
                patronymic=random.choice(SURNAMES_LIST),
                datetime=random_date(),
                doctor=random.choice(doctors),
            )
        print('appointments added')






























