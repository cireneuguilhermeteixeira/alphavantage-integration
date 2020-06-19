sudo -i -u postgres
psql

create database ptl;
create user ponto_tel_user with encrypted password 'pontotel';
grant all privileges on database ptl to ponto_tel_user;
\q
exit


source env/bin/activate



export POSTGRES_USER="ponto_tel_user"
export POSTGRES_PW="pontotel"
export POSTGRES_URL="127.0.0.1:5432"
export POSTGRES_DB="ptl" 



pip3 install -r requirements.txt




flask db init
flask db migrate
flask db upgrade
flask run