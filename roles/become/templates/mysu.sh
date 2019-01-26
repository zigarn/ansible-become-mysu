#!/bin/sh

# mysu "user" -c "cmd"

if [ $# -lt 3 ]; then
  echo 'Not enough arguments: mysu <user> -c <cmd>' >&2
  exit 1
fi

if [ x"-c" != x"$2" ]; then
  echo 'Wrong 2nd arg: mysu <user> -c <cmd>' >&2
  exit 1
fi

{% if ansible_generic_user %}
sudo su - {{ ansible_generic_user }} <<EOF
{% endif %}
printf 'su %s --command "%s"\n' "$1" "$3" | sudo su - root
{% if ansible_generic_user %}
EOF
{% endif %}
