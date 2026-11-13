from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="books.index"),
    path('list_books/', views.list_books, name="books.list_books"),
    path('one_book/<int:bookId>/', views.viewbook, name="books.one_book"),
    path('aboutus/', views.aboutus, name="books.aboutus"),


    path('html5/links/', views.links_view, name='books.html5_links'),
    path('html5/text/formatting/', views.text_formatting_view, name='books.html5_formatting'),
    path('html5/listing/', views.listing_view, name='books.html5_listing'),
    path('html5/tables/', views.tables_view, name='books.html5_tables'),

    path('search/', views.search_view, name='books.search'),
    # Lab 7 Paths
    path('simple/query', views.simple_query, name='simple_query'),      # Task 3
    path('complex/query', views.complex_query, name='complex_query'),  # Task 4
    # Lab 8 Paths
    path('lab8/task1', views.lab8_task1, name='lab8_task1'),
    path('lab8/task2', views.lab8_task2, name='lab8_task2'),
    path('lab8/task3', views.lab8_task3, name='lab8_task3'),
    path('lab8/task4', views.lab8_task4, name='lab8_task4'),
    path('lab8/task5', views.lab8_task5, name='lab8_task5'),
    #path('lab8/task7', views.student_city_count, name='student_city_count'),
    # Lab 9 Paths
    path('lab9/task1', views.lab9_task1, name='lab9_task1'),
    path('lab9/task2', views.lab9_task2, name='lab9_task2'),
    path('lab9/task3', views.lab9_task3, name='lab9_task3'),
    path('lab9/task4', views.lab9_task4, name='lab9_task4'),
    path('lab9/task5', views.lab9_task5, name='lab9_task5'),
    path('lab9/task6', views.lab9_task6, name='lab9_task6'),

    # Lab 10 - Part 1
    path('lab10_part1/listbooks', views.lab10_part1_list_books, name='lab10_part1_list'),
    path('lab10_part1/add', views.lab10_part1_add_book, name='lab10_part1_add'),
    path('lab10_part1/edit/<int:book_id>', views.lab10_part1_edit_book, name='lab10_part1_edit'),
    path('lab10_part1/delete/<int:book_id>', views.lab10_part1_delete_book, name='lab10_part1_delete'),

    # Lab 10 - Part 2
    path('lab10_part2/listbooks', views.lab10_part2_list_books, name='lab10_part2_list'),
    path('lab10_part2/add', views.lab10_part2_add_book, name='lab10_part2_add'),
    path('lab10_part2/edit/<int:book_id>', views.lab10_part2_edit_book, name='lab10_part2_edit'),
    path('lab10_part2/delete/<int:book_id>', views.lab10_part2_delete_book, name='lab10_part2_delete'),

# Lab 11 - Task 1 (One-to-Many Student)
    path('students/list', views.student_list, name='student_list'),
    path('students/add', views.student_add, name='student_add'),
    path('students/edit/<int:student_id>', views.student_edit, name='student_edit'),
    path('students/delete/<int:student_id>', views.student_delete, name='student_delete'),

    # Lab 11 - Task 2 (Many-to-Many Student2)
    path('students2/list', views.student2_list, name='student2_list'),
    path('students2/add', views.student2_add, name='student2_add'),
    path('students2/edit/<int:student_id>', views.student2_edit, name='student2_edit'),
    path('students2/delete/<int:student_id>', views.student2_delete, name='student2_delete'),

    # Lab 11 - Task 3 (Image Handling - BookPhoto)
    path('photos/list', views.photo_list, name='photo_list'),
    path('photos/add', views.photo_add, name='photo_add'),
    path('photos/edit/<int:photo_id>', views.photo_edit, name='photo_edit'),
    path('photos/delete/<int:photo_id>', views.photo_delete, name='photo_delete'),

]