# Pokédex Web

A simple website to search for and view Pokémon (Pokédex-style).

Users search for Pokémon, the PokeAPI returns the information, and it is displayed on the screen using Python and Reflex.  

## Screenshots

### PC:

![screenshot_pc 2026-07-31.png](screenshots/screenshot_pc%202026-07-31.png)

### Mobile:

<img src="screenshots/screenshot_cel%202026-07-31.jpg" width="350" alt="Pokédex screenshot (Mobile)">

## Features

-  Simple website inspired by a Pokédex
-  Search bar
-  Show a Pokémon data (stats, weight, height, abilities, type, etc.)
-  Show a Pokémon image
-  Buttons to view the next and previous Pokémon

## Technologies Used

- Python
- Reflex
- Requests to PokeAPI

---

## Installation

1. Clone the repository:

```bash
git clone https://github.com/L-EdMtz/pokedex-reflex
```

2. Navigate to the project directory:

```bash
cd pokedex_web
```

3. Create and activate a virtual environment:

```bash
python -m venv .venv
```

Windows:
```bash
.venv\Scripts\activate
```

4. Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Running the Application

Start the project:

```bash
reflex init
```

Start the development server:

```bash
reflex run
```

Open your browser and navigate to:

```text
http://localhost:3000
```




