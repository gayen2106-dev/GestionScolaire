# School Manager — projet Django (ISEP-AT)

État final des cours : Tutoriel 1 (premier projet), Tutoriel 2 (templates + CSS),
TP 3 (base de données, applications `pages` / `students` / `teachers`),
TP 4 (formulaires, validation, CRUD, messages).

## Démarrage (Windows PowerShell)

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser      # compte pour /admin/
python manage.py seed_demo            # (facultatif) données fictives
python manage.py runserver
```

Sous Linux / macOS : `source venv/bin/activate` à la place de `Activate.ps1`.

## Pages

| Adresse                    | Rôle                                   |
|----------------------------|----------------------------------------|
| `/`                        | Accueil + chiffres réels               |
| `/about/`                  | À propos                               |
| `/students/`               | Liste + recherche `?q=`                |
| `/students/new/`           | Inscrire un étudiant                   |
| `/students/<id>/`          | Fiche                                  |
| `/students/<id>/edit/`     | Modifier                               |
| `/students/<id>/delete/`   | Supprimer (confirmation, POST)         |
| `/students/classe/<L1>/`   | Étudiants d'une classe                 |
| `/teachers/`               | Liste des enseignants                  |
| `/teachers/new/`           | Ajouter un enseignant                  |
| `/admin/`                  | Administration (onglet dans le menu)   |

## CSS

Un seul fichier : `students/static/students/style.css` (chargé par `templates/base.html`,
donc appliqué à toutes les pages). Palette et variables en tête de fichier (`:root`).
Après modification : Ctrl + F5 dans le navigateur.

## Règle métier

Téléphone : 9 chiffres, espaces tolérés (`77 123 45 67` → `771234567`), champ facultatif.
