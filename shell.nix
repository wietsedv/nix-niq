{ pkgs ? import <nixpkgs> {} }:
with pkgs.python38Packages;

buildPythonPackage rec {
  name = "niq";
  src = ./.;
  buildInputs = [
    requests
    brotli
    flake8
    autopep8
  ];
}
