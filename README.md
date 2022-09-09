you can set up a Django environment in Docker using ./build 

To use whitenoise (Production handling of static files and caching as such in code)  /admin with css works with debug but not with debug off the css files are missing

To get the admin css  for the staticfiles/admin you can:

./build 

attach to latest container

cp -pr /usr/local/lib/python3.8/site-packages/django/contrib/admin/static/admin /app/staticfiles/

ow these files can be added to the admin and added to git locally as they are in the repo now



fixes

500 no correct hosts file

500 for form no env file

forms error (wrong version of django - fixed now)


if css does not update then remove staticfiles dir from server republish and restart app





