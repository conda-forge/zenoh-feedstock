cargo-bundle-licenses --format yaml --output ${SRC_DIR}/THIRDPARTY.yml
cargo install --locked --bins --root ${PREFIX} --path ./zenohd
