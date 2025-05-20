# rubberducky
AI-powered rubber duck to help you debug your code.
[blog post](https://n3rdium.dev/blog/posts/4.html)

## Demo video
Coming soon!

## Usage
Install the [Nix](https://nixos.org/) Package Manager:
```bash
$ sh <(curl --proto '=https' --tlsv1.2 -L https://nixos.org/nix/install) --daemon
```

Clone this repo and `cd` into it:
```bash
git clone https://n3rdium/rubberducky.git
cd rubberducky
```

Enter nix shell:
```bash
nix-shell
```

Enter the python virtual environment:
```bash
source ./venv/bin/activate
```

Install deps:
```bash
python -m pip install -r requirements.txt
```

To start rubberducky, run:
```bash
python src/main.py
```

## Contributing
Coming soon!

