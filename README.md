This project aims to make SDAT Editing with NitroComposer / NitroSystem Sound Maker easier for Pokemon HGSS by splitting each of it's sound data files into 4 SARC files.

# Getting Started
For documentation, see the `/docs` folder. For documentation on how the HGSS Sound Engine works, however please use the SDK Documentation in ``docs/NitroComposer`` as a reference for editing the SARC Files.

## Installation
In order to install and modify, you will need:
*  A copy of either TWL-System or NTR-System. We cannot provide this ourselves for legal reasons (to compile the `gs_sound_data.sdat` file).
*  A text editor, such as Notepad++ or Visual Studio Code
*  Git
*  Microsoft Windows 7 or above
*  Python 3 (to compile the ``/docs/sound_list.html`` sub tables).

Open up Command Prompt and navigate to the folder you wish to place the project files in, then run ``git clone https://github.com/PokeAlia/GS-SoundBase``.

Once the command above has finished, run ``explorer .`` to open File Explorer in the Project Folder.

Download the TWL-System or NTR-System, and navigate to the ``tools/bin`` folder, and copy everything to the ``tools`` folder in the root of the project.

Once you've done this, grab a HeartGold or SoulSiver ROM and extract the Sound Data from ``/data/data/sound/gs_sound_data.sdat``, open it up in Nitro Studio 2 and extract the files to somewhere outside the project file.

Once Nitro Studio 2 has unfrozen, the files have extracted. Open the location you extracted the files into, and copy the ``Banks``, ``Sequences`` and ``WaveArchives`` folder into the project folder. ''DO NOT COPY THE ``gs_sound_data.sarc`` FILE AS IT WILL OVERWRITE THE TEMPLATE''.

Run ``makesound.bat`` to make the sound file by double clicking it in file explorer.
