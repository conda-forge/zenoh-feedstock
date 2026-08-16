python "${RECIPE_DIR}/check_rust_compiler_version.py" "${SRC_DIR}/rust-toolchain.toml"
cargo-bundle-licenses --format yaml --output ${SRC_DIR}/THIRDPARTY.yml
