#!/usr/bin/env sh
set -e
action=$1
shift

help () {
  echo "
  Backend Available Commands
    help                     : show this help
    runserver                : start a local development server
    loads_initial_data       : create the initial data of characters and super powers, it is necessary to run it only once but if you run more times the data is not duplicated
    test [args...]           : run pytest args with coverage report if no args run full test suite
  "
}

run_server () {
  exec "uvicorn" "main:app" "--app-dir" "/user/home" "--host" "0.0.0.0" "--port" "8000"
}

case ${action} in
help)
  help
  exit 0
  ;;
runserver)
  run_server
  ;;
loads_initial_data)
  exec "python" "loads_initial_data.py"
  ;;
test)
  exec "pytest" "--cov-report" "html" "--cov-report" "xml" "--cov-report" "term" "--cov=app" "--cov-config=.coveragerc" "${@}"
  ;;
*)
  echo "Unknown action: \"${action}\"."
  help
  ;;
esac

exec "${action}" "$@"
