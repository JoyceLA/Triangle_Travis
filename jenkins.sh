pip install -r requirements.txt
autopep8 -ir .
flake8 --max-complexity=16 --exclude=*.txt,*.md,.gitignore --max-line-length=200 .
cd Structured
lettuce AceptanceTest
cd UnitTest
python Test_Triangle.py
coverage run --branch Test_Triangle.py
coverage report -m
coverage html --title="Coverage Triangulo Estructurado - HTML"
cd ../../Traditional
lettuce AceptanceTest
cd UnitTest
python Test_Triangle.py
coverage run --branch Test_Triangle.py
coverage report -m
coverage html --title="Coverage Triangulo Tradicional - HTML"
