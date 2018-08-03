rm -rf public
git worktree prune
git worktree add -B master public/ upstream/master

echo "saying something here"

# grab and rebuild the comments directory
python grab_comments.py

hugo
echo "rachitsingh.com" > public/CNAME
cd public && git add --all && git commit -m "." && cd ..
