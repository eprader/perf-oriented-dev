{
  description = "Apache Beam applications to be run with Apache Flink";

  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs";
  };

  outputs = { nixpkgs, ... }:
    let
      system = "x86_64-linux";
      pkgs = import nixpkgs { inherit system; };

    in
    {
      devShells.${system} = {
        default = pkgs.mkShell {
          buildInputs = with pkgs; [
            cmake
            ninja
            bc
            hwloc
            valgrind
            massif-visualizer
            linuxPackages_latest.perf
          ];

          shellHook = ''
            export PS1="(nix-shell) $PS1" # NOTE: To communicate that a nix shell is active
          '';
        };
      };
    };
}
