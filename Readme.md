# command platter

-> ./.venv/bin/python.exe

git init
git add .
git commit -m ""
git remote add origin https://github.com/maung-htay/DJAPIUSER.git
git push -u -f origin flaskapijwt
git checkout flaskapijwt
git checkout -b flaskapijwt

# DB Creation

## first time

flask db init

flask db migrate

flask db upgrade
