from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=128)  # Hashed password
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255, blank=True)
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=20, choices=(('librarian', 'Librarian'), ('user', 'User')), default='user')

    def __str__(self):
        return self.username

class Author(models.Model):
    name = models.CharField(max_length=255)
    biography = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    ISBN = models.CharField(max_length=13, unique=True)
    genre = models.CharField(max_length=13,blank=True, null=True,choices=(('Fiction', 'Fiction'), ('AutoBioGraphy', 'AutoBioGraphy')))
    publication_date = models.DateField()
    quantity = models.PositiveIntegerField()
    description = models.TextField(blank=True)
    cover_image = models.URLField(blank=True)

    def __str__(self):
        return self.title

class IssuedBook(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    issue_date = models.DateField(auto_now_add=True)
    due_date = models.DateField()
    return_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"{self.book.title} issued to {self.user.username}"
