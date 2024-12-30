    VENV_NAME="elastiq_venv"

    echo "Creating virtual environment..."
    python3 -m venv $VENV_NAME

    echo "Activating virtual environment..."
    source $VENV_NAME/bin/activate


    echo "Upgrading pip and installing dependencies..."
    pip install --upgrade pip
    pip install -r requirements.txt

    echo "Installed versions:"
    pip show selenium | grep Version
    pip show pytest | grep Version