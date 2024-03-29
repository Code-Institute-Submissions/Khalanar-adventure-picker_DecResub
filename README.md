# Adventure Picker

![amiresponsive](/assets/images/amiresponsive.png)

Adventure Picker is a CLI lightweight game engine for *Choose your own adventure* type games.

You can play the game [here](https://adventure-picker.herokuapp.com/)!

Players are set in a scenario in which they have to type their desired next action. This takes players to the next event. Currently there are two main types of events, Events and Combat. Some events lead to a direct death, others to combat and most tothe next event. Combat is turn based and player's damage is calculated at random. A GameOver alert appears the player dies in combat, prompting to restart the game or exit. If the enemy dies, the player continues to the next step in the adventure.

The current version includes Chapter 1 of the story. After Chapter 1 the player will acquire a new class, based on his/her ingame choices. Classes will become important in next versions, each with a differentiated story and a signature skill to help in combat and provide additional dialogue options in some shared events.


## User Stories
### UX and Game Design
- First Time Visitor Goals
    - As a First Time Visitor, I want to understand how to play.
    - As a First Time Visitor, I want to help unfold the story with my own choices.
    - As a First Time Visitor, I want to feel invested in the story.

- Returning Visitor Goals
    - As a Returning Visitor, I want to explore other paths in the game.

- Design Compromises
    - At some stage during development I tested using a different kind of input. Players would type A or B to make their selection on how the story should continue.
    - I decided to remove this feature and have players type the option they wanted, as this created in players a stronger sense of connection to their choices.

## Testing
### PEP8 Validation
Testing completed at [PEP8 online](http://pep8online.com/)
- **gamemanager.py** No errors ![gamemanager](/assets/images/gamemanager-pep8.png)
- **events.py** No errors ![events](/assets/images/events-pep8.png)
- **run.py** No errors ![run](/assets/images/run-pep8.png)

### Input Validation and Error-Checking
- *Player input* is capitalised and checked against the capitalised *next available events* list
- If the *Player input* does not match any of the available events, user is prompted to try again

### Known Issues
- There is an issue where sometimes the emulated CLI will not clear between events. It seems to happen at random and is not an issue in the Linux CLI


## Releases
### Next Release Includes
- Chapter 2 for each character class
- Next version features

### Next Version Features
- Main weapon can be changed, with min and max damage output values
- Add a Merchant to buy and sell your main weapon
- Character classes with signature skill
- Event's text will be held in a separate json file for readability

## Technology
### Languages
- [Python](https://www.python.org/)

### Programs
- [Caret](https://chrome.google.com/webstore/detail/caret/fljalecfjciodhpcledpamjachpmelml?hl=en) Text Editor for ChromeOS
- [Terminal](https://chromeos.dev/en/productivity/terminal) Linux Terminal Emulator for ChromeOS

## Credits
- CI interactive web console
- No external code was used

## Deployment

### Fork and Clone Your Repository
1. On GitHub, go to the selected repositories main page
2. In the top-right corner, click the Fork button
3. Go to your fork of the repository
4. Clickthe green download code button
5. Clone the repository using HTTPS, under "Clone with HTTPS", then click .
6. Or, To clone the repository using an SSH key, click Use SSH, then click .
7. Or, To clone a repository using GitHub CLI, click Use GitHub CLI, then click .
8. Open the Terminal
9. Change the current working directory to the location where you want the cloned directory
10. Type git clone
11. Then paste the URL you copied earlier
12. Press Enter
13. You now have a local clone

### Remote Deployment
1. On GitHub, go to your chosen repository
2. Click the green Gitpod button to deploy the repository to your machine

### Local Deployment
1. Go to Gitpod
2. Select the repository to be used and click open
3. Python runs in the terminal so the live deployed version is in a mock terminal created by CodeInstitute that can be accessed through Heroku

### Heroku deployment
1. Using Gitpod, create a list of requirements that the project needs to run (dependencies) - these will go in the requirements.txt file.
2. Type pip3 freeze > requirements.txt into the terminal.
3. Go to [Heroku](https://heroku.com) and login to your account.
4. From the Heroku dashboard, create a new app (tab located in the top right hand corner, below account settings image).
5. Click “Create new app”.
6. Create a name for the website to be deployed (this must be unique).
7. Select the region you are in.
8. Click the “Create app” button
9. Click on the settings tab.
10. Go to the Config Vars section and click add.
11. The **key** is **PORT** and the **value** is **8000**
12. Scroll down to the Buildpacks section and click "Add buildpack".
13. The first one to add is **python**.
14. Click save changes
15. Click “Add buildpack” again.
16. Select **node.js**.
17. Click “Save changes”.
18. Buildpacks need to be in this order (Python on top and node.js underneath).
19. Scroll back to the nav bar and click the “Deploy” tab.
20. Go to deployment method and select GitHub.
21. Search for the repository you want to connect to.
22. Click "search".
23. Once the repository has been located, click “Connect” to link the repository to Heroku.
24. Scroll down to Automatic deploys and click “Enable Automatic Deploys”.
