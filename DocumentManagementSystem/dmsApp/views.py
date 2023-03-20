from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
# request --> response

def say_hello(request):
    # Pull data from db
    # transform
    # send email
    return HttpResponse('Hello World, This is my first Request')


def home_page(request):
    return HttpResponse('Home Page')


# 1. Create CRUD for Document, User
# 2. Filter Document by Category, username
# 3. Able to upload document with media file
# 4. Unit testing
# --> using postman for API calling.


# ############################### CRUD for Document

# Empty List of Docs
original_list_docs = []


# Create document & add document to empty list


def add_docs_to_list(request):
    # Dummy data
    new_document = {
        'docs_id': 2,
        'brief': 'Personal Docs',
        'content': 'FirstName: Johnny, LastName: Stiffer',
        'author_created_date': 3 / 20 / 2023
    }
    original_list_docs.append(new_document)

    return HttpResponse(original_list_docs)

# Retrieve document


def get_documents(request):
    # Dummy data

    my_document = {
        'docs_id': 1,
        'brief': 'Personal Docs',
        'content': 'FirstName: Long, LastName: Nguyen',
        'author_created_date': 3 / 20 / 2023
    }

    return HttpResponse(my_document.items())

# Delete Document from a list
doc1 = {
    'docs_id': 1,
    'brief': 'Personal Docs',
    'content': 'FirstName: Johnny, LastName: Stiffer',
    'author_created_date': 3 / 20 / 2023
}
doc2 = {
    'docs_id': 2,
    'brief': 'Personal Docs',
    'content': 'FirstName: Long, LastName: Nguyen',
    'author_created_date': 3 / 17 / 2023
}
doc3 = {
    'docs_id': 3,
    'brief': 'Personal Docs',
    'content': 'FirstName: Derek, LastName: King',
    'author_created_date': 3 / 12 / 2023
}

# A list contain 3 docs
list_docs = [doc1, doc2, doc3]


def remove_docs(request):

    # remove() specific item from a list
    # docs at index 2 was removed
    list_docs.remove(list_docs[2])

    return HttpResponse(list_docs)


# Update Documents

def update_single_doc(request):
    new_doc = doc1.update({'content': 'Position: Software Engineer, Age: 25'})

    return HttpResponse(list_docs)
