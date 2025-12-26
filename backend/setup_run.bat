@echo off
echo ========================================
echo Projet Inventaire SaaS - Setup complet
echo ========================================

REM Supprime l'ancien venv s'il existe
if exist venv (
    echo Suppression de l'ancien venv...
    rmdir /s /q venv
)

REM Création du nouveau venv
echo Création du venv...
python -m venv venv

REM Activation du venv
echo Activation du venv...
call venv\Scripts\activate.bat

REM Mise à jour de pip
echo Mise à jour de pip...
python -m pip install --upgrade pip

REM Installation des dépendances
echo Installation des packages...
python -m pip install Flask==2.3.3 Flask-SQLAlchemy==3.0.5 Flask-JWT-Extended==4.6.0 qrcode==7.3 pandas==2.1.1 python-docx==0.8.11 waitress==3.0.2

REM Vérification des installations
echo Vérification des modules installés...
python -m pip show flask
python -m pip show flask_sqlalchemy
python -m pip show flask_jwt_extended
python -m pip show qrcode
python -m pip show pandas
python -m pip show python-docx
python -m pip show waitress

REM Lancement du serveur
echo Lancement du serveur avec Waitress...
python run_waitress.py

pause
