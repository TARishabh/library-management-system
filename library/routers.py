from rest_framework.routers import DefaultRouter
from .views import UserViewSet,AuthorViewSet,BookViewSet,IssuedBookViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'author', AuthorViewSet)
router.register(r'book', BookViewSet)
router.register(r'issuedbooks', IssuedBookViewSet)