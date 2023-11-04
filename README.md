# oTree Ultimatum Game

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

To run this project, you'll need to have oTree installed. If you haven't installed oTree, you can do so with pip:

```bash
pip install requirements.txt   

