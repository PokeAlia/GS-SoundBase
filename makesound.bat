"./tools/sndarc.exe" gs_sound_data.sarc

"python3 ./tools/make_soundlist.py"

@goto ok

:ok
   @echo =======================
   @echo  Convert is SUCCESS !!!
   @echo =======================
   @goto end

:err
   @pause

:end

