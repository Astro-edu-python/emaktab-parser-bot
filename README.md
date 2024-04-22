# Emaktab parser bot
Parser bot for emaktab which can parse school info and schedule


## Requirements
* `python 3.11 =<`
* `aiogram 2 <= 2.25`
* `redis`

## Installation and run
1. Clone repository
    ```shell
    git clone https://github.com/Astro-edu-python/emaktab-parser-bot.git
    ```
2. Enter to project directory(`emaktab-parser-bot`)
3. Install requirements
   ```shell
   # linux
   python3.11 -m venv venv && source venv/bin/activate

   # windows
   python -m venv venv
   venv\Scripts\activate
   
   pip install -r requirements.txt
   ```
4. Copy file `example.env` with name `.env` and set all values
5. Run celery
   ```shell
   celery -A emaktab_bot.services.emaktab_tasks.celery worker -l INFO
   ```
6. Run bot in another terminal
   ```shell
   python run.py
   ```
