from datetime import datetime, timedelta
from random import randint

from django.contrib.auth import get_user_model
from django.core.management import BaseCommand

from restaurants.models import Restaurant, CHOICES_RESTAURANT_TYPE, CHOICES_PRICE, CHOICES_TIME, ReservationInfo, \
    Comment, STAR_RATING, ImageForRestaurant, MenuImages

User = get_user_model()
user = User.objects.first()


class Command(BaseCommand):
    def handle(self, *args, **options):
        if Restaurant.objects.all().count() < 100:
            # Create Restaurant
            for i in range(11):
                Restaurant.objects.create(
                    name='Dummy Restaurant' + str(i),
                    address='패스트캠퍼스',
                    district='강남구',
                    geolocation='37.5499689,127.0234623',
                    contact_number='0200000000',
                    description='Dummy Restaurant description',
                    restaurant_type=CHOICES_RESTAURANT_TYPE[randint(0, len(CHOICES_RESTAURANT_TYPE) - 1)][0],
                    average_price=CHOICES_PRICE[randint(0, len(CHOICES_PRICE) - 1)][0],
                    business_hours='Dummy Business hour',
                    maximum_party=randint(1, 100),
                    owner=user,
                )
            first_restaurant = Restaurant.objects.first()
            # Create Comment
            for i in range(1, 7):
                Comment.objects.create(
                    author=user,
                    restaurant=first_restaurant,
                    star_rate=STAR_RATING[randint(1, len(STAR_RATING) - 1)][0],
                    comment=f'Test Comment {i}'
                )
            # Create ReservationInfo
            for i in range(14):
                for j in range(13):
                    if not ReservationInfo.objects.filter(restaurant=first_restaurant, time=CHOICES_TIME[j][0],
                                                          date=datetime.today() + timedelta(days=i)).count():
                        ReservationInfo.objects.create(
                            restaurant=first_restaurant,
                            time=CHOICES_TIME[j][0],
                            date=datetime.today() + timedelta(days=i)
                        )
            # Create ImageForRestaurant
            for i in range(3):
                ImageForRestaurant.objects.create(
                    restaurant=first_restaurant,
                )
            # Create MenuImages
            for i in range(3):
                MenuImages.objects.create(
                    restaurant=first_restaurant,
                )
            print("Successfully create dummy restaurants")
        else:
            print("Dummy Restaurant is over than 100")
