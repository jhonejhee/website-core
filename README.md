# One-page Website
---
- [DesktopView](#desktop-view)
- [MobileView](#mobile-view)
- [About](#about-this-project)
- [Use the project](#use-this-project)
`Note:` If there are any problems with the installation or instruction. Reach out to me.
---

## Desktop View
![Desktop View](https://github.com/jhonejhee/website-core/assets/91509082/05163969-7833-406a-85e7-c619bfe9e03f)


## Mobile View
![Mobile View](https://github.com/jhonejhee/website-core/assets/91509082/d8180691-e64c-438c-bd0a-487271a70785)

---

## About This Project
> This project is made using Python, Django, and Tailwind CSS. This project uses SQLite3 for its database.
> - Python - Backend
> - Django - Framework
> - Tailwind CSS - Styling

---

## Use this project
Before starting make sure that you have PIP installed.

---

### Clone Repository
> ```bash
> git clone https://github.com/jhonejhee/website-core.git
> ```
> Now open your project on your IDE.

---

### Make Your `local` folder
> Open your IDE's Terminal.
> ```shell
> mkdir -p local
> ```
> ```shell
> cp website/project/settings/templates/settings.dev.py ./local/settings.dev.py
> ```

---

### Install `Poetry`
> In your IDE's Terminal or any terminal or shell do:
> ```shell
> pip install poetry
> ```
> Check installation by running this:
> ```shell
> poetry --version
> ```

---

### Make a new virtual environment
> Open your IDE's Terminal. Make sure that your project is open.
> Name it `venv`
> ```shell
> python -m venv venv
> ```
> After that, a folder named `venv` should appear on your project directory.
> Restart your Terminal.
>
> > `Poetry` should automatically activate your virtual environment `venv`.
> > If not, activate it manually using:
> > ```shell
> > venv/Scripts/Activate.ps1
> > ```
>
> You should now see `(venv) path/to/ptoject-folder>`.
> This means that the `venv` is already activated.
> Installed packages in the virtual environment stays inside that environment and will not be installed in your local system.

---

### Install dependencies
> Run this in your virtual environment:
> ```shell
> poetry update
> ```
> and then
> ```shell
> poetry install
> ```
> This will install all dependencies

---

### Connect Database (SQLite3)
### Update Database Dictionary
> Go to `website/project/settings/base.py`.
> Find your `DATABASE` dictionary and change the `'NAME'` into your `db.sqlite3`'s absolute path.

### Allow host to open your project
> Go to `website/project/settings/base.py`.
> Find `ALLOWED_HOSTS` dictionary and put `['*']`
> This means that all host can open your project.

---

#### Migrate Database
> Run this in your virtual environment:
> ```shell
> make migrations
> ```
>
> After making `migrations` do:
> ```shell
> make migrate
> ```
> Note: To see how these `make` commands were made and how they work, see `Makefile` in your project.

---

### Run your project
> Run this in your virtual environment:
> ```shell
> make run-server
> ```
> Open the output link in your browser.
> The link should look like `https://127.0.0.1:8000/`.
