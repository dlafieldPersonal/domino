d=$(date)
git config --global user.name "dlafieldPersonal" &&
git config --global user.email "dlafield@gmail.com" &&
git commit -m "committing ${d}"
git push
echo done
