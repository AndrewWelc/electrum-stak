#!/bin/bash
# Run this after a new release to update dependencies

venv_dir=~/.electrum-stak-venv
contrib=$(dirname "$0")

which virtualenv > /dev/null 2>&1 || { echo "Please install virtualenv" && exit 1; }

for i in '' '-hw' '-binaries'; do
    rm "$venv_dir" -rf
    virtualenv -p $(which python3) $venv_dir

    source $venv_dir/bin/activate

    echo "Installing $i dependencies"

    python -m pip install -r $contrib/requirements/requirements${i}.txt --upgrade

    echo "OK."

    requirements=$(pip freeze --all)
    restricted=$(echo $requirements | $other_python $contrib/deterministic-build/find_restricted_dependencies.py)
    requirements="$requirements $restricted"

    echo "Generating package hashes..."
    rm $contrib/deterministic-build/requirements${i}.txt
    touch $contrib/deterministic-build/requirements${i}.txt

    for requirement in $requirements; do
        echo -e "\r  Hashing $requirement..."
        $other_python -m hashin -r $contrib/deterministic-build/requirements${i}.txt ${requirement}
    done

    echo "OK."
done

echo "Done. Updated requirements"
