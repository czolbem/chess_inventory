<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="readme-top"></a>
<!--
*** Readme based on template from https://github.com/othneildrew/Best-README-Template
-->


<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<h3 align="center">Chess Inventory</h3>

<div>
  <p align="center">
    A simple web app to store and analyse your chess games in one place
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
        <li><a href="#testing">Testing</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#license">License</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

Chess Inventory was created to help keep track of all your chess games from various sources like popular online chess platforms Lichess or Chess.com or traditional Over The Board games. This allows for analysis of games in one convinient place and the creation of statistics across all sources.   

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- GETTING STARTED -->
## Getting Started

To use Chess Inventory, make sure to sort out the prerequisites and follow the installation steps.

### Prerequisites

This project depends on Python 3.11.2. Installation instructions can be found here: https://www.python.org


The project should be OS independent but has only been tested on Windows 10.


### Installation
This installation deploys the app for development purposes. That means it uses Django's built-in web server and a local sqlite3 database. The settings.py configures DEBUG = True, which is insecure. <b>DO NOT USE IN A PRODUCTION ENVIRONMENT.</b> Follow https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/ if you want to do that. 


The following commands are based on Windows cmd.exe.
1. Clone the repo
   ```cmd
   git clone https://github.com/czolbem/chess_inventory.git
   ```
2. (Optional) Create a virtual environment
   ```cmd
   python -m venv c:\path\to\myenv
   ```
3. (Optional) Activate the virtual environment
   ```cmd
   <venv>\Scripts\activate.bat
   ```
4. Install requirements via pip
   ```cmd
   pip install -r requirements.txt
   ```
5. Apply the migrations to the database
   ```cmd
   python manage.py migrate
   ```
### Testing

To run the tests via Django:
   ```cmd
   python manage.py test
   ```
To generate a code coverage report:
1. Run the tests with coverage
   ```cmd
   coverage run --source='.' manage.py test
   ```
2. Generate the report
   ```cmd
   coverage report -m
   ```
   or for a html report
   ```cmd
   coverage html
   ```


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

To run the app in Django's lightweight development web server, use the following command:
```
python manage.py runserver
```

This starts the app at the default url [127.0.0.1:8000]().


To add new games, follow "Add Game" and paste a valid PGN (Portable Game Notation). The [examples](https://github.com/czolbem/chess_inventory/blob/main/examples) folder contains a few PGN files for you to play with.  


You can then find your games in the game list and can navigate to single games through clicking a row. Currently, Chess Inventory shows some details and calculated opening information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

- [ ] Game walk-through
- [ ] Integrating chess engine and allowing game analysis
- [ ] Creating statistics from the games like most popular openings

<p align="right">(<a href="#readme-top">back to top</a>)</p>




<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>




<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/czolbem/chess_inventory.svg?style=for-the-badge
[contributors-url]: https://github.com/czolbem/chess_inventory/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/czolbem/chess_inventory.svg?style=for-the-badge
[forks-url]: https://github.com/czolbem/chess_inventory/network/members
[stars-shield]: https://img.shields.io/github/stars/czolbem/chess_inventory.svg?style=for-the-badge
[stars-url]: https://github.com/czolbem/chess_inventory/stargazers
[issues-shield]: https://img.shields.io/github/issues/czolbem/chess_inventory.svg?style=for-the-badge
[issues-url]: https://github.com/czolbem/chess_inventory/issues
[license-shield]: https://img.shields.io/github/license/czolbem/chess_inventory.svg?style=for-the-badge
[license-url]: https://github.com/czolbem/chess_inventory/blob/main/LICENSE
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/marc-czolbe
[product-screenshot]: images/screenshot.png
[Next.js]: https://img.shields.io/badge/next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white
[Next-url]: https://nextjs.org/
[React.js]: https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB
[React-url]: https://reactjs.org/
[Vue.js]: https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vuedotjs&logoColor=4FC08D
[Vue-url]: https://vuejs.org/
[Angular.io]: https://img.shields.io/badge/Angular-DD0031?style=for-the-badge&logo=angular&logoColor=white
[Angular-url]: https://angular.io/
[Svelte.dev]: https://img.shields.io/badge/Svelte-4A4A55?style=for-the-badge&logo=svelte&logoColor=FF3E00
[Svelte-url]: https://svelte.dev/
[Laravel.com]: https://img.shields.io/badge/Laravel-FF2D20?style=for-the-badge&logo=laravel&logoColor=white
[Laravel-url]: https://laravel.com
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
[JQuery.com]: https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white
[JQuery-url]: https://jquery.com 