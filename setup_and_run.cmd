@echo off
REM ------------------------------
REM Script de préparation et lancement du backend Inventaire SaaS
REM ------------------------------

REM 1️⃣ Supprimer l'ancien venv s'il existe
IF EXIST venv (
    echo Suppression de l'ancien venv...
    rmdir /S /Q venv
)

REM 2️⃣ Créer un nouveau venv
echo Création du venv...
python -m venv venv

REM 3️⃣ Activer le venv
echo Activation du venv...
call venv\Scripts\activate.bat

REM 4️⃣ Mettre pip à jour
echo Mise à jour de pip...
python -m pip install --upgrade pip

REM 5️⃣ Installer les packages un par un pour éviter les conflits
echo Installation des packages requis...
python -m pip install Flask==2.3.3
python -m pip install Flask-SQLAlchemy==3.0.5
python -m pip install Flask-JWT-Extended==4.6.0
python -m pip install qrcode pandas python-docx waitress

REM 6️⃣ Lancer le serveur avec Waitress
echo Lancement du serveur...
python run_waitress.py

pause
