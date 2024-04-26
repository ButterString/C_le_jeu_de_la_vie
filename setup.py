# coding: utf-8

# commande à taper en ligne de commande après la sauvegarde de ce fichier:
# python setup.py build
from cx_Freeze import setup, Executable
  
executables = [
        Executable(script = "LifeGame.py",icon = "lifeGame.ico", base = "Win32GUI" )
]
# ne pas mettre "base = ..." si le programme n'est pas en mode graphique, comme c'est le cas pour chiffrement.py.
  
buildOptions = dict( 
        includes = ["grille", "grilleCanvas"],
        include_files = ["lifeGame.ico"]
)
  
setup(
    name = "LifeGame",
    version = "1.0",
    description = "Simulation du jeu de la vie",
    author = "Ohabille",
    options = dict(build_exe = buildOptions),
    executables = executables
)