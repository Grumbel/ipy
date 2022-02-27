{
  description = "A simple interactive Python console";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-21.11";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs = { self, nixpkgs, flake-utils }:
    flake-utils.lib.eachDefaultSystem (system:
      let
        pkgs = nixpkgs.legacyPackages.${system};
      in rec {
        packages = flake-utils.lib.flattenTree {
          ipy = pkgs.python3Packages.buildPythonPackage rec {
            pname = "ipy";
            version = "0.1";
            src = nixpkgs.lib.cleanSource ./.;
           };
        };
        defaultPackage = packages.ipy;
      });
}
