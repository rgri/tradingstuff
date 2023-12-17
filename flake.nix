{

  inputs.nixpkgs.url = "github:NixOS/nixpkgs/";
  outputs = { self, nixpkgs }:
    let
      system = "x86_64-linux";
      pkgs = (import nixpkgs { inherit system; });
      pyPkgs = ps: with ps; [ scipy matplotlib numpy ];
    in {
      devShells.x86_64-linux.default = pkgs.mkShell {
        packages = [ pkgs.poetry (pkgs.python3.withPackages pyPkgs) ];

        # shellHook = ''
        #   export LD_LIBRARY_PATH="${pkgs.zlib}/lib"
        # '';
      };
    };

}
