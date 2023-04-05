git submodule init
git submodule update --init --recursive

FILE=aigrisculteurs/chronobio
echo $FILE
if [ -e "$FILE" ]; then
    echo "chronobio symlink exists, deleting"
    rm -rf $FILE
fi
ln -s -r dependencies/chronobio/chronobio aigrisculteurs/chronobio #Create a symlink to prevent useless folder redundency.


cd aigrisculteurs
python3 -m src.aigrisculteurs_client -a 127.0.0.1 -p $1 -u aigrisculteurs
