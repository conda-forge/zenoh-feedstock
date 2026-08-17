python "%RECIPE_DIR%\check_rust_compiler_version.py" "%SRC_DIR%\rust-toolchain.toml"
if %errorlevel% NEQ 0 exit /b %errorlevel%

cargo-bundle-licenses --format yaml --output %SRC_DIR%\THIRDPARTY.yml
if %errorlevel% NEQ 0 exit /b %errorlevel%
