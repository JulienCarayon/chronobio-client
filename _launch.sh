# echo 'DEBUT LAUNCH AIGRISCULTEURS'
# git submodule init
# git submodule update --init --recursive

# FILE=aigrisculteurs/chronobio
# echo $FILE
# if [ -e "$FILE" ]; then
#     echo "chronobio symlink exists, deleting"
#     rm -rf $FILE
# fi
# ln -s -r dependencies/chronobio/chronobio aigrisculteurs/chronobio #Create a symlink to prevent useless folder redundency.


# cd aigrisculteurs
# python3 -m src.aigrisculteurs_client -a 127.0.0.1 -p $1 -u aigrisculteurs
# echo 'FIN LAUNCH AIGRISCULTEURS'
git submodule init
git submodule update --init --recursive


# TROLLED_FILE=./TROLLED
# if test -f "$TROLLED_FILE"; then
#     # echo "Already trolled"
#     TROLLED=1
# else
#     TROLLED=0
# fi
# echo "TROLL STATE: ${TROLLED}"


# FILE=aigrisculteurs/chronobio
# echo $FILE
# if [ -e "$FILE" ]; then
#     echo "chronobio symlink exists, deleting"
#     rm -rf $FILE
# fi

# ln -s -r dependencies/chronobio/chronobio aigrisculteurs/chronobio #Create a symlink to prevent useless folder redundency.
# if [ "$TROLLED" -eq 0 ]; then
#     cat > ./TROLLED
#     echo 'DEBUT DU TROLLING DU PROF'
#     GAME_PATH=$PWD
#     echo ''
#     echo $(ls)
#     echo $GAME_PATH
#     cd $PWD

#     echo 'PWD : '$PWD
#     echo LS : $(ls)
#     cd ../..
#     echo 'PWD : '$PWD
#     echo LS : $(ls)

#     echo $(cp teams/chronobio-client/images/*.png chronobio/viewer/images/)
#     echo $''
#     sh competition.sh
#     echo 'FIN DU TROLLING DU PROF'
#     # cd $GAME_PATH
#     # echo LS : $(ls)

# else
    # rm TROLLED
cd aigrisculteurs
python3 -m src.aigrisculteurs_client -a 127.0.0.1 -p $1 -u aigrisculteurs
# fi
