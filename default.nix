{ pkgs ? import <nixpkgs> {} }:

pkgs.python38Packages.buildPythonPackage rec {
  name = "niq";
  src = ./.;
  buildInputs = with pkgs.python38Packages; [
    requests
    brotli
  ];
}
