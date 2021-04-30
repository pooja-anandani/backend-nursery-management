# backend-nursery-management

1) The whole backend is built on python 3.8 and postgres database. Please run requirments file to avoid version conflicts on libraries.

2) Create super user and create 2 roles 1) nursery 2) customer. 

3) Nursery should have following permissions: 
   core | user | can view user
   nursery|plant|can view plant 
   nursery|plant|can add plant
   nursery|plant|can change plant
   nursery|plant|can delete plant 
   orders | orders | can view orders
   


4) Customer should have following permissions: 
  nursery|plant|can view plant 
  orders|cart| can add cart 
  orders|cart| can change cart 
  orders|cart| can delete cart 
  orders|cart| can view cart 
  


