from django.urls import path

from .views import TaskList, TaskCreate, TaskDetail, TaskEdit, TaskDelete, HomePageView, AppGalleryView

urlpatterns = [
    path('', HomePageView.as_view(), name='index'),
    path('gallery/', AppGalleryView.as_view(), name='app-gallery'),
    path('tasks/', TaskList.as_view(), name='tasks'),
    path('create-task/', TaskCreate.as_view(), name='create-task'),
    path('detail-task/<int:pk>', TaskDetail.as_view(), name='detail-task'),
    path('edit-task/<int:pk>', TaskEdit.as_view(), name='edit-task'),
    path('delete-task/<int:pk>', TaskDelete.as_view(), name='delete-task'),
]
