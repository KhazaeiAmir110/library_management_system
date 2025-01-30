from apps.book.models import Book, City, Genre, Author
from apps.reservation.models import Reservation
from apps.users.models import User

User.objects.create_table()
Author.objects.create_table()
City.objects.create_table()
Genre.objects.create_table()
Book.objects.create_table()
Reservation.objects.create_table()
