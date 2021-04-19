echo "Deleting DB..."
rm -rf data/db

echo "Deleting migrations..."
find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
find . -path "*/migrations/*.pyc"  -delete

echo "Creating web..."
docker-compose up --build -d

echo "Creating migrations..."
docker-compose run web python manage.py makemigrations
docker-compose run web python manage.py migrate

echo "Adding superuser..."
docker-compose run web python manage.py createsuperuser