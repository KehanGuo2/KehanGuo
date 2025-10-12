from scholarly import scholarly
import json
from datetime import datetime
import os


def extract_publications(author_dict):
    pubs = []
    for p in author_dict.get('publications', []):
        filled = scholarly.fill(p)
        title = filled.get('bib', {}).get('title', '')
        authors_str = filled.get('bib', {}).get('author', '')
        authors = [a.strip() for a in authors_str.split(' and ')] if authors_str else []
        venue = filled.get('bib', {}).get('venue', '')
        year = filled.get('bib', {}).get('pub_year', '')
        url = (
            filled.get('eprint_url')
            or filled.get('pub_url')
            or filled.get('eprint')
            or filled.get('citedby_url')
            or ''
        )

        pubs.append({
            'title': title,
            'authors': authors,
            'venue': venue,
            'year': year,
            'url': url,
        })
    return pubs


def main():
    scholar_id = os.environ.get('GOOGLE_SCHOLAR_ID')
    if not scholar_id:
        raise RuntimeError('GOOGLE_SCHOLAR_ID env var not set')

    author = scholarly.search_author_id(scholar_id)
    scholarly.fill(author, sections=['basics', 'indices', 'counts', 'publications'])

    pubs = extract_publications(author)

    os.makedirs('results', exist_ok=True)
    with open('results/gs_data.json', 'w') as f:
        json.dump({
            'name': author.get('name'),
            'updated': str(datetime.now()),
            'citedby': author.get('citedby'),
            'publications': pubs,
        }, f, ensure_ascii=False)

    # also write site data file for Jekyll
    os.makedirs('../_data', exist_ok=True)
    with open('../_data/publications.yml', 'w') as f:
        # minimal YAML writing
        f.write('\n'.join([
            '- title: "{}"\n  authors: [{}]\n  venue: "{}"\n  year: {}{}{}'.format(
                p['title'].replace('"', '\\"'),
                ', '.join(['"{}"'.format(a.replace('"', '\\"')) for a in p['authors']]),
                p['venue'].replace('"', '\\"'),
                p['year'] if p['year'] else '""',
                '\n  url: "' if p.get('url') else '',
                (p.get('url') or '').replace('"', '\\"') + '"' if p.get('url') else ''
            ) for p in pubs
        ]))


if __name__ == '__main__':
    main()
