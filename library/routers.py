from rest_framework.routers import DefaultRouter
from .views import UserViewSet,AuthorViewSet,BookViewSet,IssuedBookViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet,basename='user')
router.register(r'author', AuthorViewSet,basename='author')
router.register(r'book', BookViewSet,basename='book')
router.register(r'issuedbooks', IssuedBookViewSet,basename='issuedbooks')