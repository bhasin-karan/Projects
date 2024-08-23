### Start scene file
**OpenScene** will load **Alpha_chrctl**
### How to play and what parts of the level to oberserve technology
- **The player spawns in a safe zone, allowing them to get a feel for movement and camera control. The HUD is also displayed here to give additional context to the player, displaying lives, health, and tutorial messages if necessary. Once the player approaches the front of the room, the door reacts to their presence, opening into the first hallway. A sentry patrols back and forth here, and if the player passes in front of the sentry, it will play an alert sound and begin to chase them. This will cause damage to the player, who can escape by running out of its detection radius, breaking line of sight, or passing through the next door. These sentries can be deployed in various configurations or with differing waypoints to increase or decrease threat where appropriate. After passing a second sentry, the player reaches a door with red lights, indicating a lock. A door with green lights to the right demonstrates that something can be done to open the main door, and when the player navigates to the left, they enter the command bay through a malfunctioning door, necessitating either precise entry or persistence. This combination of proximity doors, locked doors, and closed doors forms the basis for the maze that the player will have to navigate. A green cube that releases the key is on top of a structure, but the player cannot access it from here. The player can jump from smaller structures and, with the help of lowered gravity, reach the button. Differing gravity areas and other platforming elements will be part of future development. Once this button is pressed, the key falls to the floor, where the player can pick it up. From here, the player can return to the main hallway and notice that the main door is now lit up by green lights, indicating the key has been collected. Once the player passes through, they reach the bay, at which point the end of the alpha is triggered by proximity.**
### Known problem areas
1. **Camera motion and character movement with using mouse and keyboard inputs at the same time can be a bit difficult around objects in a tight indoor map. This can be improved via further tweaking the motion parameters for camera and character. In addition, the main character can appear to float on objects where the visual renderer and their respective collider have different volumes around edges. This may be improved via more sophisticated raycasting for ground checks, but it needs to be investigated further.**
2. **The varying gravity areas are currently implemented as gravity pads, wherein the jump rate and fall rates are different, this may be desired for better visual feedback but needs to be looked into more.**
3. **Chase transition, but should work at distances; fsm to be investigated for future development**

## Manifest of which files authored by each teammate
### Roshaun - Environment Set Up 
#### Assets
- Sci-Fi Styled Modular Pack 
#### Scripts 
- KeyRelease.cs
- DroneRoomActivator.cs
- GameQuitter.cs
- edited some parameters for ThirdPersonControl.cs 
#### Description and Settings
- When the user climbs up the different gravity areas (battery-packs in the command bay), there is a button on the top that when collided with will release the key for the player to get. 
- The other drones will eventually be stored behind individual rooms that will open once the player connects to a droid and walks in the direction of the glass door. 
- Once the player has reached the bridge and walks towards the “prison”, then the game is complete and a visual is provided with instructions on how to exit the game.
---
### Karan - Environment Set Up 
#### Assets
- Sci-Fi Styled Modular Pack 
#### Scripts
- Corridors -  ‘Corridor_I’ prefab from the asset pack lined up to create the hallways
- Proximity Doors - ‘door_2’ prefab and added a box collider for triggers for open/close
- Proximity Door Script attached: When the asset with the tag ‘Player’ is inside the collider the character_nearby bool (which is a condition in the transitions for the animator) is set to true and the door opens, when the character leaves the collider it closes
- Closed Doors - ‘door_2’ prefab with box collider disabled and no script attached. Default state in animation is closed, so they stay closed and cannot be opened.
- Guarded Rooms - Added a ‘Corridor_T’ with glass on the open ends. Situated behind the closed doors and cannot be entered.
- Opened Door - ‘door_2’ prefab that is already unlocked and opened. For now, I just set the default state to opened in the animator with playerNearby always true, so that the door remains opened.
- Malfunctioning Door - ‘door_2’ prefab where the default state is open in animator, and the transition condition has been deleted so it keeps rotating between the 4 states (open, opened, close, closed)
- Locked Door or KeyLockedDoor - ‘door_2’ prefab that is locked and doesn’t open till the player collects the key. It has a box collider added for the trigger points.
- Key Unlock Door script attached: If the player has the key collector script attached and ‘hasKey’ is true and the player is in the trigger area then the door opens and stays opened once unlocked.
- Player/Main Character - To be replaced by the Main Character, has a basic Player Controller script created for development that can be ignored. The Key Collector script needs to be added to the main character: It is used to change hasKey from false to true once the player has the key.
- Key: Key prefab from ‘Models’ folder. It has Collect Key script attached, once player with Key Collector script touches the key, it disappears and changes hasKey boolean to true.
---
### Alok - Main Character
#### Assets
- Jammo
- Teddy Suit
#### Scripts
- ThirdPersonControl.cs
- CharacterStateController.cs 
#### Description and Settings
- Implemented main character control, including WASD movement, ability to jump based on grounding check and animation controller with animation from Jammo asset store package. 
- Implemented third-person camera control using Unity cinemachine and main character‘s movement for smooth camera target following. Tuned motion parameters for free look camera for FOV, mouse axis control and cinemachine collider. 
- Implemented Character State controller that updates character skin and eye colors based on its health/remaining lives. Main constructs are in place, the update functionality needs to be tied to further gameplay in coming weeks. 
- Implemented manipulation of gravity and jump height for different gravity zones by provisioning checks against user selectable ground masks. 
#### How to play/technical reqs
    "WASD or Arrow keys plus mouse pointer to change the forward-facing direction for Jammo, the Droid. Jump input via space key. Numeric 1, 2 or 3 change Jammo’s suit and eyes color. Camera pans with motion of mouse pointer, up/down (range limited) and left/right (with full wrapping around the Droid to navigate the environment)"
---
### Archit - Enemy Droids
#### Assets
- Sentry Detect/Walk/Idle animations and Sentry Animation Controller
- Sentry Prefab
#### Scripts
- SentryAI Script
#### Description
- Sentry animations and controller; animations made by hand - not currently scaled to sentry speed
- Imported sentry prefab and all associated components (Navmesh, Animator, etc.)
#### Assumptions
- Waypoints as objects in scene, player set in scene, size of sentry/navmesh agent
- Detection/attack radii set with defaults, player script name and function assumed (can be changed) for hits
---
### Xun - Open Scene and HUD
#### Assets
- TeddySuitKid2099
- Spaceship
- Planets of Solar System 3D
- Progress Bar

#### Scripts
- GameStartter.cs
- GameQuitter.cs
- CharacterStateController.cs
- GravityIndicator.cs
- InGameMenu.cs
- LivesCount.cs
- ProgressBar.cs

#### Description
- Implement the eintire open scene, mostly, just combine 2 online assets, twick the location of objects, and added start and quit button. Alok helpped reduce the asset size to help maintain proper git repo size
- Implement the HUD system for main game, which includes a textbox that can be disabled, a lives count syste, a health bar system, and a gravity indicator system.
- 3 lives will be initialized, and whenever a health bar is reduced to 0, the lives count will reduce.
- Test scrips have been added to test health life and gravity HUD system. Press J/K to increase/reduce health. Press I/O/P to check the gravity indicator system

#### How to Play
- In OpenScene, 2 buttons can be clicked
- In Alpha_chrctl, the HUD menu is supposed to a read only dash board. But I've added test keyboard inputs. Press J/K to increase/reduce health. Press I/O/P to check the gravity indicator system
---