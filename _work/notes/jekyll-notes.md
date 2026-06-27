- Why does docs.redwitch.ca have "This site is open source. Improve this page." footers and docs.pancakes.ca does not?
- It looks like all the markdown files remain but html copies are created next to them. Markdown tables are broken in https://docs.redwitch.ca/product/Red-Witch-Master-Document-List.html
- Soft linebreaks not rendering (as expected but not desired) https://docs.redwitch.ca/product/Red-Witch-Privacy.html
- broken links in Red-Witch-Post-Market-Surveillance.md
- check: pancakes/docs/index.md may not be necessary, gh-pages might use README.md instead
- https://docs.pancakes.ca/playlist/pancakes-playlist.html has link to https://docs.pancakes.ca/playlist/pancakes-playlist-demands.md why isnt this linked to the html which was also created?

---

## Likely causes

**1. Red Witch footer vs Pancakes no footer**

`docs.redwitch.ca` is using a Jekyll theme/layout that includes the GitHub repository footer. The rendered Red Witch pages explicitly show `This site is open source. Improve this page.` ([redwitch][1]) Pancakes does not show that footer on the checked playlist page. ([pancakes][2])

Check both repos for:

```bash
cat docs/_config.yml
find docs -maxdepth 3 -type f \( -name '*.html' -o -name '*.md' \) | grep -E '_layouts|_includes|config'
```

Look for `theme`, `remote_theme`, `github`, `repository`, `_layouts/default.html`, or `_includes/footer.html`.

**2. Markdown files remaining beside generated HTML**

That usually means the Pages output is not pure Jekyll output, or source files are being copied into the published artifact. Vanilla Jekyll renders Markdown into static HTML; Jekyll’s own description is that it renders Markdown/Liquid and outputs a static site. ([GitHub][3])

Check the Pages workflow. If you have an Action doing something like `cp -r docs public` and then also generating HTML, that explains `.md` and `.html` side by side.

**3. Broken markdown tables**

The Red Witch table is not being parsed as a table; it is rendered inline as text. ([redwitch][1]) Same issue appears in Pancakes playlist: the table header and rows are collapsed into plain lines. ([pancakes][2])

Likely causes:

```md
# Bad
| Col | Col |
|————|————|
```

Use ASCII hyphens and blank lines:

```md
| Col | Col |
| --- | --- |
| A | B |
```

Also avoid Word/AI smart dash characters in Markdown table separators.

**4. Soft linebreaks**

That is expected Markdown behavior. The Privacy page confirms single-line source breaks are collapsed into paragraphs. ([redwitch][4])

Best fixes, in order:

```md
Separate paragraphs with blank lines.
```

or:

```md
Use <br> only where you truly want a hard visual break.
```

I would not globally enable hard-wrap unless these docs are mostly migrated Word content.

**5. `pancakes/docs/index.md` may be unnecessary**

Yes, likely. GitHub Pages/Jekyll normally serves `README.md` as the directory index if no `index.md`/`index.html` is present, but an explicit `index.md` is clearer and lets you control front matter/title/layout. Keep it if you want docs landing-page control.

**6. Why `.md` links are not rewritten to `.html`**

Jekyll does not automatically rewrite ordinary Markdown links like:

```md
[pancakes-playlist-demands.md](pancakes-playlist-demands.md)
```

to:

```md
[pancakes-playlist-demands.html](pancakes-playlist-demands.html)
```

Use `.html` links manually, or use Jekyll link tags consistently.

## Recommended fix order

1. Normalize all Markdown tables: ASCII `---`, blank line before table.
2. Change internal doc links from `.md` to `.html` for published pages.
3. Inspect Pages build workflow for raw `.md` copy behavior.
4. Decide whether Red Witch and Pancakes should use the same theme/layout.
5. Keep `docs/index.md` if you want intentional landing-page control.

[1]: https://docs.redwitch.ca/product/Red-Witch-Master-Document-List.html " Red Witch – QMS Project Document Index | redwitch"
[2]: https://docs.pancakes.ca/playlist/pancakes-playlist.html "Pancakes Playlist | pancakes"
[3]: https://github.com/jekyll/jekyll?utm_source=chatgpt.com "Jekyll is a blog-aware static site generator in Ruby"
[4]: https://docs.redwitch.ca/product/Red-Witch-Privacy.html " Red Witch – External Design Input: Cambridge Menstrual Tracking App Report | redwitch"


---

Yes. For these repos, a small shared Jekyll theme is the right move.

I would make it:

**`fley-jekyll-theme`** or **`fley-docs-theme`**

Use it for:

```text
docs.redwitch.ca
docs.pancakes.ca
future docs.* sites
```

Core features:

```text
- consistent header/footer
- no unwanted “Improve this page” unless explicitly enabled
- readable markdown tables
- soft-linebreak policy decision
- project logo/title/nav
- canonical docs layout
- consistent CSS for QMS/product docs
- link styling for generated .html pages
```

Repo shape:

```text
fley-docs-theme/
  _layouts/
    default.html
    page.html
  _includes/
    header.html
    footer.html
    nav.html
  assets/
    css/
      main.scss
  _sass/
    fley/
      _base.scss
      _tables.scss
      _docs.scss
  README.md
  fley-docs-theme.gemspec
```

Then each docs repo gets a tiny config:

```yaml
remote_theme: mlehotay/fley-docs-theme

title: Red Witch Docs
project_name: Red Witch
show_improve_page_link: false
```

For now, I would **not** start with a gem-published theme. Start as a GitHub `remote_theme`, use it in both sites, then package later if needed.
