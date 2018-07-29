rm -rf public
git worktree prune
git worktree add -B master public/ upstream/master

# grab and rebuild the comments directory
python grab_comments.py

hugo
echo "rachitsingh.com" > public/CNAME
cd public && git add --all && git commit -m "." && cd ..
