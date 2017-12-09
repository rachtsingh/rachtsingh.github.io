rm -rf public
git worktree add -B gh-pages public upstream/gh-pages
echo "rachitsingh.com" >> public/CNAME
hugo
cd public && git add --all && git commit -m "Publishing to gh-pages" && cd ..
