# Document-Management-System
 
 Create a Document Management System using Django with RestAPI  
 
 ## Desc: 4 tables 
  - Document(docs_id, category_id, brief, content, media_file, author, created_date)
  - category(category_id, category_name), User(username, password, full_name, role_id)
  - Role(role_id, role_name)  
  
  ## Acceptance criteria:  
  
  ### for task 2
  - Create ERD Create API for CRUD task(for all) 
  - Filter Document by Categor
  - Username Able to upload document with media file 
  - Unit testing 
  - Using Postman for API calling
  
  ### for task 3
  - Integrate to Django
  - Web app can connect to mySQL
  - CRUD data on mySQL
  
  ### for task 4
  - Login/Register
  - Admin can grant role for others
  - User can CRUD document but can not Delete/update document of others user
  - User can view all document of system
  - Admin can delete document, category, user(with role user)
