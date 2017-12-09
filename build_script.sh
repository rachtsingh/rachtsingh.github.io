rm -rf public
git worktree add -B master public upstream/master
echo "rachitsingh.com" >> public/CNAME
hugo
cd public && git add --all && git commit -m "." && cd ..
