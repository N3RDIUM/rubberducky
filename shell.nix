let pkgs = import <nixpkgs> { };
in pkgs.mkShell {
    packages = [
        (pkgs.python3.withPackages (python-pkgs: [
            python-pkgs.torch
            python-pkgs.numpy
            python-pkgs.ollama
            python-pkgs.faster-whisper
            python-pkgs.speechrecognition
            python-pkgs.pydub
            python-pkgs.pyaudio
        ]))
        pkgs.basedpyright
        pkgs.virtualenv
        pkgs.ollama
    ];
    buildInputs = [ pkgs.libz ];
}
