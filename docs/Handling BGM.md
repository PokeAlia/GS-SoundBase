BGM and the Sound Engine in Pokemon HeartGold/SoulSilver is very finnicky, in that it requires quite a few rules you need to set yourself.

# Bank Allocation
## Opening/Ending & System Themes
These tracks generally use ``BANK_BGM_OPEND``, however you can use any BANK file.

## Field & Dungeon Themes
If you change tracks by means of walking from one map to another, then the engine will break slightly by continuing to use the previous track's BANK. A way to bypass this is to have the tracks share the same BANK.

If you warp, then it should work.

## Battle Themes
You can handle these in any way you wish to do so.

## Other Music (Event/Demo/Encounter/ME)
You must use BANK_BASIC at all times.
