# Mini Ultimatum Game

**Important Notice**: Contributions to this project are restricted until November 10, 2023, for ongoing research and development. During this period, the repository is in a read-only state and will not accept pull requests or issues. We appreciate your interest and look forward to welcoming contributions when the restriction is lifted.

This project is an implementation of a mini ultimatum game using the oTree framework. In this game, three players interact with each other, with one player endowed with Ksh 200, and the others making decisions based on the initial offer.

## Project Overview

### Game Flow

1. **Page 1 - Player 1 (Sender):**
   - Player 1 is endowed with Ksh 200.
   - Player 1 decides how much to send to Player 2 (Receiver).

2. **Page 2 - Player 3 (Punisher):**
   - Player 3 (Punisher) sees the amount Player 1 decided to send to Player 2.
   - Player 3 decides to either Punish or Not Punish Player 1 based on the offer's fairness.

3. **Page 3 - Results Page:**
   - Player 1 and Player 2 are notified of the results.
   - Payouts are calculated based on the decisions made.

### Exit Survey

The game concludes with an exit survey that consists of three questions to gather additional information from the participants.

## Installation

To run this project, follow these steps:

1. **Clone the Repository:**

   Open your command-line terminal and clone this repository to your local machine by running:

   ```bash
   git clone https://github.com/rky-ke/Mini-Ultimatum-Game.git 
   
   ```

2. **Navigate to the Project Folder:**

   Change the directory to the project folder:

   ```bash
   cd Mini-Ultimatum-Game

   ```

3. **Set Up a Virtual Environment:**

   Create a virtual environment and activate it:

   ```bash
   python -m venv otree-env
   source otree-env/bin/activate  #I am Using Ubuntu Operating System

   ```

4. **Install Dependencies:**

   Install the required Python packages listed in the requirements.txt file:

   ```bash
   pip install -r requirements.txt

   ```

5. **Run the oTree Development Server:**

   Start the oTree development server to run the game:
   ```bash
   otree devserver

   ```
   The server will provide a URL where you can access the game in your web browser (usually http://127.0.0.1:8000).

6. **Play The Game:**

   Follow the on-screen instructions to play the game and participate in the exit survey

## Note for first time oTree User 

If you are using oTree for the first time and encounter issues with starting the development server, you may receive a message like "oTree has been updated. Please delete your database (db.sqlite3)." 

To resolve this, follow these steps:

   1. **Delete the Database:**

      Open your terminal and navigate to the project directory. Then, delete the existing `db.sqlite3` database by running:

      ```bash
      rm db.sqlite3