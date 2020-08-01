{ pkgs ? import <nixpkgs> {} }:

pkgs.mkShell rec {
  name = "niq";
  src = ./.;
  buildInputs = with pkgs.python38Packages; [
    requests
    brotli
    flake8
    autopep8
  ];
}
