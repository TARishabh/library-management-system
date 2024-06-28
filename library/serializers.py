from rest_framework import serializers
from .models import User, Author, Book, IssuedBook
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from django.contrib.auth.hashers import make_password

email_regex = RegexValidator(
    regex=r'^[a-zA-Z0-9.!#$%&\'*+/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$',
    message='Invalid email format. Please enter a valid email address.'
)

class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(validators=[email_regex])

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'role')
        read_only_fields = ('id',)  # Making ID read-only for security
    
    def validate_username(self, value):
        if ' ' in value:
            raise serializers.ValidationError('Username cannot contain spaces.')
        # Check if the username already exists
        if self.instance and self.instance.username == value:
            return value  # Allow the same username during update
        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError('User with this username already exists.')
        return value

    def validate_email(self, value):
        # Check if the email already exists
        if self.instance and self.instance.email == value:
            return value  # Allow the same email during update
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError('User with this email already exists.')
        return value
    
    def create(self, validated_data):
        # Encrypt the password before saving the user
        validated_data['password'] = make_password(validated_data.get('password'))
        return super().create(validated_data)

    def update(self, instance, validated_data):
        # Encrypt the password if it's being updated
        if 'password' in validated_data:
            validated_data['password'] = make_password(validated_data.get('password'))
        return super().update(instance, validated_data)


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('id', 'name', 'biography')
        read_only_fields = ('id',)


class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)  # Nested serializer for author

    class Meta:
        model = Book
        fields = ('id', 'title', 'author', 'ISBN', 'genre', 'publication_date', 'quantity', 'description', 'cover_image')
        read_only_fields = ('id',)

class IssuedBookSerializer(serializers.ModelSerializer):
    book = BookSerializer(read_only=True)  # Nested serializer for book
    user = UserSerializer(read_only=True)  # Nested serializer for user

    class Meta:
        model = IssuedBook
        fields = ('id', 'book', 'user', 'issue_date', 'due_date', 'return_date')
        read_only_fields = ('id',)
