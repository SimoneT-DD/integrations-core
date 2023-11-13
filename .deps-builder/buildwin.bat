
set omnibus_project=python-dependencies
cd %~p0\omnibus

REM Execute omnibus
bundle install
set PACKAGE_VERSION=0.0.1
bundle exec omnibus build %omnibus_project% --log-level=debug
