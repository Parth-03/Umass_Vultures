from users.models import Person, FoodComment, FoodPost
from django.contrib.auth.models import User, Group, Permission
from django.contrib.contenttypes.models import ContentType
from faker import Faker
import random

persons = []
posts= []
comments= []
fake = Faker()
        


# Create Persons

for i in range(1, 10):
    a_name = fake.name()
    a_password = fake.name()
   # a_score= fake.random_int(0, 100)
    person = Person.objects.create_user(username= a_name, password=a_password)
    person.save()
    persons.append(person)


# Create Food Posts
for i in range(1,100):
    a_score= fake.random_int(0, 50)
    a_location= fake.address()
    a_date= fake.date()
    a_info= fake.sentence()
    a_user = random.choice(persons)
    post= FoodPost(postScore= a_score, location= a_location, postUser= a_user, postDate= a_date, postInfo=  a_info)
    post.save()
    posts.append(post)


# Create Food Comments

for i in range(1, 1000):
    a_content= fake.sentence()
    a_score= fake.random_int(0, 25)
    a_date= fake.date()
    a_commenter = random.choice(persons)
    a_post = random.choice(posts)
    comment= FoodComment(commenter= a_commenter, commentPost= a_post, commentContent= a_content, commentScore= a_score, commentDateTime= a_date)
    comment.save()
    comments.append(comment)

print("\nUser:")
for a in Person.objects.all():
    print(a)

print("\nFood Post:")
for b in FoodPost.objects.all():
    print(b)

print("\nFood Comment:")
for i in FoodComment.objects.all():
    print(i)


username = "admin1"
password = "admin1"
email = "admin@326.edu"
adminuser = Person.objects.create_user(username=username, password=password)
adminuser.save()
adminuser.is_superuser = True
adminuser.is_staff = True
adminuser.save()
message = f"""
====================================================================
The database has been setup with the following credentials:
  username: {username}
  password: {password}
  email: {email}
You will need to use the username {username} and password {password}
to login to the administrative webapp in Django.
Please visit http://localhost:8080/admin to login to the admin app.
Run the django server with:
  $ python3 manage.py runserver 0.0.0.0:8080
====================================================================
"""
print(message)