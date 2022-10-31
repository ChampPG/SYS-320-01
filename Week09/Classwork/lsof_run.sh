#!/bin/bash
input="./pid.txt"
while IFS= read -r line
do
  sudo -S lsof -p $line | awk {print $9}
done < "$input"