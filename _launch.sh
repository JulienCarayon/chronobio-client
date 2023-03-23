FILE=aigrisculteurs/chronobio 

if [ -f "$FILE" ]; then
    rm -rf aigrisculteurs/chronobio 
fi
ln -s ../../../chronobio aigrisculteurs/chronobio #Create a symlink to prevent useless folder redundency.

python3 aigrisculteurs/aigrisculteurs_client.py -a 127.0.0.1 -p $1 -u aigrisculteurs