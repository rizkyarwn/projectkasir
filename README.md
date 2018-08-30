# Projectkasir Tutorial Installing and Issues ( root-tetew# )

Install projectkasir

1. Download the project on Github rizkyarwn
2. Create a new folder (ex: MyFile)
3. Install virtual enviroment
   >$ virtualenv -python=/usr/bin/python2.7 env-yournamefile (ex: env-kasir)
   
   >$ cd bin
   
   >$ source activate
4. Extract the Project downloaded of github rizkyarwn (https://github.com/rizkyarwn/projectkasir/)
   in the folder "env-kasir"
   >$ cd projectkasir-master
5. Install requirements
   >$ pip install -r requirements.txt
   OR
   >$ pip install django==1.11.6
6. Migrations database
   >$ ./manage.py makemigrations
   
   >$ ./manage.py migrate
7. Running server
   >$ ./manage.py runserver
   
 # Issues Projectkasir
Change some source-code :
   
1. `statistik_tags.py`
When `Statistik` error you can change code

    https://pastebin.com/6Pwk07uv
  
2. `views.py`
When `profile warung` error you can change code

    https://pastebin.com/wyCLzrCt
    
Thank you^^
