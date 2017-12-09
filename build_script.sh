rm -rf public
git worktree prune
git worktree add -B master public/ upstream/master
hugo
echo "rachitsingh.com" > public/CNAME
cd public && git add --all && git commit -m "." && cd ..
