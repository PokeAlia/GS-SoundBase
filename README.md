This project aims to make SDAT Editing with NitroComposer / NitroSystem Sound Maker easier for Pokemon HGSS by splitting each of it's sound data files into 4 SARC files.

# Getting Started
For documentation, see the `/docs` folder. For documentation on adding/removing/editing sounds, use the SDK as a reference.

## Installation
In order to install and modify, you will need:
*  A copy of either TWL-System or NTR-System. We cannot provide this ourselves for legal reasons (to compile the `gs_sound_data.sdat` file).
*  A text editor, such as Notepad++ or Visual Studio Code
*  Git
*  Microsoft Windows 7 or above

Open up Command Prompt and navigate to the folder you wish to place the project files in, then run ``git clone https://github.com/PokeAlia/GS-SoundBase``.

Once the command above has finished, run ``explorer .`` to open File Explorer in the Project Folder.

Download the TWL-System or NTR-System, and navigate to the ``tools/bin`` folder, and copy everything to the ``tools`` folder in the root of the project.

Run ``makesound.bat`` to make the sound file by double clicking it in file explorer.
