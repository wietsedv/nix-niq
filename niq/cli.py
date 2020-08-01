#!/usr/bin/env python

from argparse import ArgumentParser
from pathlib import Path
import sys
import requests
import pickle
from collections import Counter

TMP_PATH = Path('/tmp')
NIX_CHANNEL = 'nixpkgs'
NIX_CHANNEL_URL = 'https://channels.nixos.org/nixpkgs-unstable/packages.json.br'
# https://formulae.brew.sh/api/cask.json


def load_channel(name, url, update=False):
    cache_path = TMP_PATH / f'nix-{name}.cache.pkl'
    if not cache_path.exists() or update:
        print('downloading index')
        data = requests.get(url).json()

        if data['version'] != 2:
            print(f'unsupported channel version {data["version"]} (must be 2)')
            exit(1)

        with open(cache_path, 'wb') as f:
            pickle.dump(data['packages'], f)
        return data['packages']

    with open(cache_path, 'rb') as f:
        return pickle.load(f)


def filter_pkgs(pkgs, query):
    query = [q.lower().strip() for q in query]

    for pkg_name in list(pkgs.keys()):
        n = pkg_name.lower()
        for q in query:
            if q not in n:
                del pkgs[pkg_name]
                break

    print(f'found {len(pkgs):,} packages')


def show_statistics(pkgs):
    print(f'{len(pkgs):,} total packages\n')

    groups = Counter([name.split('.')[0] if '.' in name else '[main]' for name in pkgs])
    for group, count in groups.most_common():
        print(f'{group:>20}\t{count:>3,}')


def show_package_info(attr_name, pkg_info):
    print(f'name:        {attr_name} (v{pkg_info["version"]})')
    if 'description' in pkg_info["meta"]:
        print(f'description: {pkg_info["meta"]["description"]}')
    if 'homepage' in pkg_info["meta"]:
        print(f'homepage:    {pkg_info["meta"]["homepage"]}')
    print(f'source:      https://github.com/NixOS/nixpkgs/tree/master/{pkg_info["meta"]["position"].split(":")[0]}')
    # print(json.dumps(pkg_info, indent=2))


def main():
    parser = ArgumentParser('Fast Nixpkgs Quering')
    parser.add_argument('query', nargs='*')
    parser.add_argument('-u', '--update', action='store_true')
    parser.add_argument('-s', '--statistics', action='store_true')
    args = parser.parse_args()

    if len(args.query) == 0 and not args.update and not args.statistics:
        print('no valid argument given. See --help for more information')
        sys.exit(1)

    pkgs = load_channel(NIX_CHANNEL, NIX_CHANNEL_URL, args.update)
    filter_pkgs(pkgs, args.query)

    if args.statistics:
        return show_statistics(pkgs)

    if len(pkgs) < 100:
        for pkg_name, pkg_info in pkgs.items():
            print('')
            show_package_info(pkg_name, pkg_info)


if __name__ == '__main__':
    main()
