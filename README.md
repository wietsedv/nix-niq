# niq

`niq` is a simple cli tool for quering the nix-unstable channel (currently hardcoded). It is currently a pragmatic minimal implementation that does what I need it to do.

The current package is not intended for use by others, but feel free to try it. The tool is readonly, so it is completely safe to use.

## Installation


~~~shell
$ nix-env \
  -f https://github.com/wietsedv/personal-nixpkgs/archive/master.tar.gz \
  -iA niq
~~~


## Usage

 - `niq -u`
   - downloads and caches the package list
 - `niq calibre`
    ```
    found 1 packages

    name:        calibre (v4.19.0)
    description: Comprehensive e-book software
    homepage:    https://calibre-ebook.com
    source:      https://github.com/NixOS/nixpkgs/tree/master/pkgs/applications/misc/calibre/default.nix
    ```

 - `niq python38 tqdm`
    ```
    found 1 packages

    name:        python38Packages.tqdm (v4.47.0)
    description: A Fast, Extensible Progress Meter
    homepage:    https://github.com/tqdm/tqdm
    source:      https://github.com/NixOS/nixpkgs/tree/master/pkgs/development/python-modules/tqdm/default.nix
    ```

## Motivation
Both `nix-env -qa` and the [online browser](https://nixos.org/nixos/packages.html?channel=nixpkgs-unstable) are slow and are missing information (mainly the link the derivation source). `niq` solves these problems by caching the package list and by showing the information that I find relevant.