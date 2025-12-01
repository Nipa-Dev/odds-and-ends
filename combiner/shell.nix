{ pkgs ? import <nixpkgs> { system = "x86_64-linux"; } }:

pkgs.mkShell {
  buildInputs = [
    pkgs.python312       # Base Python interpreter
    pkgs.uv              # uv tool to manage Python deps
    pkgs.ruff
  ];

}

