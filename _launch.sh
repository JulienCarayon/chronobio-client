FILE=aigrisculteurs/chronobio 

if [ -d "$FILE" ]; then
    rm -rf $FILE
fi
ln -s dependencies/chronobio/chronobio aigrisculteurs/chronobio #Create a symlink to prevent useless folder redundency.

git submodule init
git submodule update --init --recursive

python3 aigrisculteurs/aigrisculteurs_client.py -a 127.0.0.1 -p $1 -u aigrisculteurs