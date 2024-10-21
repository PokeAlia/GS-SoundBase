"./tools/sndarc.exe" gs_sound_data.sarc

@goto ok

:ok
   @echo =======================
   @echo  Convert is SUCCESS !!!
   @echo =======================
   @goto end

:err
   @pause

:end

