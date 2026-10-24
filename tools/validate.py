"""Dependency-free project checks; not a complete HTML5 conformance validator."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit, unquote
import re
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parent.parent
VOID = set('area base br col embed hr img input link meta param source track wbr'.split())

class Document(HTMLParser):
    def __init__(self, path):
        super().__init__(convert_charrefs=True)
        self.path, self.ids, self.refs, self.stack, self.errors = path, set(), [], [], []
        self.counts, self.aria_refs, self.lang, self.viewport = {}, [], None, False
        self.current, self.doctype = 0, False
        self.feed(path.read_text())
        self.close()
        assert not self.stack, (path.name, 'unclosed tags', self.stack)
        assert not self.errors, (path.name, self.errors)
    def handle_decl(self, decl):
        self.doctype = decl.lower() == 'doctype html'
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        self.counts[tag] = self.counts.get(tag, 0) + 1
        if tag not in VOID:
            self.stack.append(tag)
        if 'id' in a:
            assert a['id'] not in self.ids, (self.path.name, 'duplicate ID', a['id'])
            self.ids.add(a['id'])
        if tag == 'html': self.lang = a.get('lang')
        if tag == 'meta' and a.get('name') == 'viewport': self.viewport = True
        if a.get('aria-current') == 'page': self.current += 1
        self.aria_refs.extend(a.get('aria-labelledby', '').split())
        for key in ('href', 'src'):
            if key in a:
                self.refs.append((tag, key, a[key]))
        if tag == 'img': assert 'alt' in a, (self.path.name, 'missing image alt')
        assert tag not in ('script', 'iframe', 'form', 'base'), (self.path.name, 'unexpected element', tag)
        assert not any(k.startswith('on') for k in a), 'Unexpected inline event handler'
    def handle_endtag(self, tag):
        if not self.stack or self.stack[-1] != tag:
            self.errors.append(('unbalanced close', tag, self.stack[-1:]))
        else:
            self.stack.pop()

def check():
    docs = {p.name: Document(p) for p in ROOT.glob('*.html')}
    assert set(docs) == {'index.html', 'terms.html'}
    for name, d in docs.items():
        assert d.doctype and d.lang == 'en' and d.viewport
        for tag in ('main', 'article', 'h1', 'title'):
            assert d.counts.get(tag) == 1, (name, 'expected one', tag)
        assert d.current == 2, (name, 'current header and footer navigation')
        assert all(x in d.ids for x in d.aria_refs), (name, 'broken accessible label')
        text = d.path.read_text()
        assert 'com.builtbyjasim.jascutstudio' in text and 'zasimkhan3@gmail.com' in text
        assert not re.search(r'\b(TODO|TBD|lorem ipsum|example\.com)\b', text, re.I)
        for tag, attr, ref in d.refs:
            u = urlsplit(ref)
            if u.scheme:
                assert u.scheme in ('https', 'mailto'), (name, 'unsafe scheme', ref)
                assert tag == 'a', (name, 'remote auto-loaded resource', ref)
                continue
            assert not u.netloc and not u.path.startswith('/'), (name, 'nonrelative link', ref)
            target = (d.path.parent / unquote(u.path)).resolve() if u.path else d.path
            assert target.is_relative_to(ROOT) and target.is_file(), (name, 'missing/outside link', ref)
            if u.fragment:
                assert target.name in docs and unquote(u.fragment) in docs[target.name].ids, (name, 'bad fragment', ref)
        print(f'PASS {name}: balanced structure, landmarks, labels, navigation, links and local assets; {len(d.ids)} IDs')
    css = (ROOT/'assets/styles.css').read_text()
    assert css.count('{') == css.count('}')
    assert '@media(max-width:760px)' in css and '@media print' in css and 'prefers-color-scheme:dark' in css
    assert 'url(' not in css and '@import' not in css
    ET.parse(ROOT/'assets/brand-mark.svg')
    assert (ROOT/'.nojekyll').exists() and (ROOT/'README.md').exists()
    print('PASS CSS structure/responsive/dark/print rules, SVG XML and Pages root packaging')
    print('No remote requests, JS, credentials, commits or deployment are performed by this validator.')

if __name__ == '__main__':
    check()
