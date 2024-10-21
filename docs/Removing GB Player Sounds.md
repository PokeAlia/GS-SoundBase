In order to remove the GB Player Sound data, you need to open ``gs_sound_data.sarc`` and replace the following line:
```
#include "psg.sarc"
```
with:
```
; #include "psg.sarc"
```

Once you've done this, compile the SDAT file as normal.
