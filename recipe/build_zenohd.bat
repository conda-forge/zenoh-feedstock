cargo-bundle-licenses --format yaml --output %SRC_DIR%\THIRDPARTY.yml
if %errorlevel% NEQ 0 exit /b %errorlevel%

cargo install --locked --bins --root %LIBRARY_PREFIX% --path .\zenohd
if %errorlevel% NEQ 0 exit /b %errorlevel%
