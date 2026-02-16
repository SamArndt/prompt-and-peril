# Prompt & Peril
An AI-driven RPG where ChatGPT is the Dungeon Master and Open5e is the Rulebook.

## How it Works (The Architecture)

*   **The Brain ([ChatGPT API](https://platform.openai.com)):** Acts as the Dungeon Master. It doesn't just chat; it uses a specialized “System Prompt” to define the world setting, generating the story, player choices, and narrative consequences.
*   **The Rulebook ([Open5e API](https://open5e.com)):** Provides the “hard” data. If the AI introduces a “Goblin,” the [Django](https://www.djangoproject.com) app fetches the actual stats (HP, Armor Class) from Open5e so the AI doesn't just make up numbers.
*   **The Memory (Django + Database):** Stores the “State.” It remembers the player's inventory, health, and past decisions to keep the story consistent over time.

## Setup Instructions

1. **Clone the repo**
2. **Create a virtual environment:**  
   `python -m venv venv`
3. **Activate it:**  
   * **Mac/Linux:** `source venv/bin/activate`
   * **Windows:** `venv\Scripts\activate`
4. **Install Django:**  
   `pip install django`
5. **Run Migrations:**  
   `python manage.py migrate`
6. **Start Server:**  
   `python manage.py runserver`

## Project Structure

*   `config/`: Main project settings and URLs.
*   `db.sqlite3`: Local development database.

