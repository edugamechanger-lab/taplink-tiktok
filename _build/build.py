"""Сборка трех таплинков Марго из одного шаблона.

Меняешь ссылки и состав карточек здесь -> запускаешь -> получаешь
index.html для каждой площадки. Дизайн живет в template.html.
"""
import os, sys

GH = 'https://edugamechanger-lab.github.io'

# ---------- ВСЕ ЛИД-МАГНИТЫ (описание карточки один раз) ----------
# page: ведет на страницу с промптом (+ ?from=площадка, страница сама подставит TG-ссылку)
# tg:   ведет сразу в Telegram (ссылка своя для каждой площадки, см. PLATFORMS)
CARDS = {
  'halloween': dict(page=f'{GH}/halloween-escape-room/', cls='card-halloween',
      tag='Игра на уроке · Квест', title='Halloween Escape Room',
      desc='Квест-комната по вашей теме: 4 готовые комнаты и метапромпт.',
      icon='<path d="M14 6c-1-2 0-4 2-4" stroke="#39816C"/><ellipse cx="9" cy="16" rx="6" ry="8" fill="#ffb26b"/><ellipse cx="19" cy="16" rx="6" ry="8" fill="#ffb26b"/><ellipse cx="14" cy="16" rx="5" ry="9" fill="#ffc48a"/><path d="M10 14l2 2h-3zM18 14l-2 2h3zM10 20c2 2 6 2 8 0"/>'),
  'map': dict(page=f'{GH}/karta-probelov/', cls='card-map',
      tag='Пробелы в знаниях', title='Карта пробелов',
      desc='Найдите, что стоит повторить и разобрать на уроке.',
      icon='<path d="m3 6 7-3 8 3 7-3v19l-7 3-8-3-7 3z" fill="#ffe3a0"/><path d="M10 3v19M18 6v19"/><circle cx="14" cy="13" r="3" fill="#b5a4ff"/><path d="M14 16v3"/>'),
  'homework': dict(page=f'{GH}/domashka_s_ii/', cls='card-homework',
      tag='Домашняя работа', title='Домашка, которую нельзя сделать одним запросом к ИИ',
      desc='Для заданий, в которых нужно думать самому.',
      icon='<path d="M6 3h15v22H6z" fill="#ffdf82"/><path d="M10 9h7M10 14h7M10 19h4"/>'),
  'time': dict(page=f'{GH}/10_minut_do_uroka/', cls='card-time',
      tag='Быстрая подготовка', title='До урока 10 минут. Что делаем?',
      desc='Когда времени мало, а урок уже скоро.',
      icon='<circle cx="14" cy="15" r="10" fill="#e1d8ff"/><path d="M14 9v6l4 2M10 2h8"/>'),
  'book': dict(page=f'{GH}/Stranitsa_uchebnika_v_urok/', cls='card-book',
      tag='Работа с учебником', title='Урок по странице учебника',
      desc='Фото страницы превращается в готовый сценарий урока.',
      icon='<path d="M14 7C10 4 5 4 2 5v18c4-1 8-1 12 2 4-3 8-3 12-2V5c-3-1-8-1-12 2v18" fill="#b8e5d6"/>'),
  'detective': dict(cls='card-detective',
      tag='Игра на уроке · Telegram', title='Детектив',
      desc='Урок как расследование: улики нужно заработать знаниями.',
      icon='<circle cx="11" cy="11" r="7" fill="#bfeee7"/><path d="m16 16 9 9" stroke="#ffb73f" stroke-width="4"/><path d="M8 9c0-2 2-3 4-3"/>'),
  'imaginarium': dict(cls='card-imag',
      tag='Игра на уроке · Telegram', title='Имаджинариум',
      desc='Игра в ассоциации по картинкам на материале урока.',
      icon='<rect x="3" y="6" width="13" height="18" rx="2" fill="#ffd6e7" transform="rotate(-8 9 15)"/><rect x="11" y="4" width="13" height="18" rx="2" fill="#fff" /><path d="M14 17l3-4 2 2 2-3 2 5z" fill="#f2a5c4" stroke="none"/><circle cx="16" cy="9" r="1.6" fill="#F6C760" stroke="none"/><rect x="11" y="4" width="13" height="18" rx="2"/>'),
  'millionaire': dict(cls='card-million',
      tag='Игра на уроке · Telegram', title='Кто хочет стать миллионером',
      desc='Знакомое шоу как повторение темы.',
      icon='<path d="M7 4h14l4 6-11 15L3 10z" fill="#c9d6ff"/><path d="M3 10h22M10 4l4 21 4-21M7 4l3 6M21 4l-3 6"/>'),
  'five': dict(cls='card-five',
      tag='Экономия времени · Telegram', title='5 уроков в 2',
      desc='Подробности в посте в Telegram.',
      icon='<rect x="3" y="5" width="22" height="19" rx="3" fill="#e6f7f1"/><path d="M3 10h22M9 3v4M19 3v4"/><path d="M9 15h3M15 15h4M9 19h3"/>'),
}

# ---------- ИДЕИ ДЛЯ УРОКА: одинаковые на всех площадках ----------
LESSON_CARDS = ['halloween','map','five','imaginarium','millionaire','time','homework','book','detective']

# ---------- ПЛОЩАДКИ ----------
# cards: порядок карточек; tg: ссылки для карточек, ведущих сразу в Telegram
# hidden: карточки, которые пока выключены (появятся, когда уберешь из списка)
PLATFORMS = {
  'tiktok': dict(repo='taplink-tiktok',
      monster='https://t.me/EdhackMargo_bot?start=dl-1792672868157bf8b026c1',
      channel='https://t.me/+o4L5wq8P-pNlMWZi',
      neuroom=True,
      cards=LESSON_CARDS,
      hidden=[],
      tg={'detective':'https://t.me/+4XKcWlmjE700ZjU6',
          'five':'https://t.me/+Kjfa4eD-g3lhNGYy',
          'millionaire':'https://t.me/+39jDPG0P2fg1YmMy',
          'imaginarium':'https://t.me/+GPFJBLITlRo2NjUy'}),
  'insta': dict(repo='taplink-instagram',
      monster='https://t.me/EdhackMargo_bot?start=dl-1792932694453',
      channel='https://t.me/+7sPl4z8dBiw2YTVi',
      neuroom=False,
      cards=LESSON_CARDS,
      hidden=[],
      tg={'five':'https://t.me/+b4uRO8E9KEBkODky',
          'imaginarium':'https://t.me/+GFF_1wtA4MVjYzgy',
          'millionaire':'https://t.me/+1Nvd-bykiX4wMzky',
          'detective':'https://t.me/+eUrjpwzRdyRlZTMy'}),
  'youtube': dict(repo='taplink-youtube',
      monster='https://t.me/EdhackMargo_bot?start=dl-1793236235442',
      channel='https://t.me/+hYBj5MtyjL0zMjMy',
      neuroom=False,
      cards=LESSON_CARDS,
      hidden=[],
      tg={'imaginarium':'https://t.me/+yrpe1eRi3tw4NjIy',
          'five':'https://t.me/+82FbQioWJJQ0NjUy',
          'millionaire':'https://t.me/+qPRs5BzBELkyYmZi',
          'detective':'https://t.me/+-5Xo3smHAx44OWJi'}),
}

EXTRA_CSS = '''
.card-imag .icon{background:#ffeef5;color:#c2557f}
.card-imag .tag{color:#c2557f}
.card-million .icon{background:#e9efff;color:#5e78c3}
.card-million .tag{color:#5e78c3}
.card-five .icon{background:#e6f7f1;color:#368b7b}
.card-five .tag{color:#368b7b}
.card-halloween .icon{background:#fff0e3;color:#c0611f}
.card-halloween .tag{color:#c0611f}
'''

def card_html(key, src, tg):
    c = CARDS[key]
    href = c['page'] + '?from=' + src if 'page' in c else tg.get(key) or PLATFORMS['insta']['tg'][key]
    return f'''<!-- {c['title']} -->
        <a class="card {c['cls']}" href="{href}" target="_blank" rel="noopener noreferrer">
          <span class="icon" aria-hidden="true"><svg viewBox="0 0 28 28">{c['icon']}</svg></span>
          <div class="copy">
            <div class="tag">{c['tag']}</div>
            <div class="title">{c['title']}</div>
            <div class="desc">{c['desc']}</div>
          </div>
          <span class="arrow" aria-hidden="true">↗</span>
        </a>'''

def build(src, out_dir):
    here = os.path.dirname(os.path.abspath(__file__))
    t = open(os.path.join(here, 'template.html'), encoding='utf-8').read()
    neu = open(os.path.join(here, 'neuroom.html'), encoding='utf-8').read()
    P = PLATFORMS[src]
    shown, hidden = [], []
    for k in P['cards']:
        if 'page' not in CARDS[k] and k not in P['tg']:
            if k not in PLATFORMS['insta']['tg']:
                sys.exit(f'{src}: нет TG-ссылки для карточки {k}')
            print(f'  ! {src}: для «{CARDS[k]["title"]}» нет своей ссылки, временно стоит ссылка Instagram')
        h = card_html(k, src, P['tg'])
        if k in P['hidden']:
            hidden.append('        <!-- ВЫКЛЮЧЕНО:\n        ' + h.replace('<!--', '').replace('-->', '') + '\n        -->')
        else:
            shown.append('        ' + h)
    nav = ('<nav class="links" aria-label="Материалы для учителя">\n\n'
           + '\n\n'.join(shown) + ('\n\n' + '\n'.join(hidden) if hidden else '')
           + '\n\n      </nav>')
    html = (t.replace('{{CARDS}}', nav)
             .replace('{{MONSTER}}', P['monster'])
             .replace('{{CHANNEL}}', P['channel'])
             .replace('{{NEUROOM}}', neu if P['neuroom'] else '')
             .replace('/* ---------- TELEGRAM ---------- */', EXTRA_CSS.strip() + '\n\n/* ---------- TELEGRAM ---------- */', 1))
    assert '{{' not in html
    os.makedirs(out_dir, exist_ok=True)
    open(os.path.join(out_dir, 'index.html'), 'w', encoding='utf-8').write(html)
    return len(shown)

if __name__ == '__main__':
    root = sys.argv[1] if len(sys.argv) > 1 else '/home/claude'
    for src, P in PLATFORMS.items():
        n = build(src, os.path.join(root, P['repo']))
        print(f'{src}: {n} карточек -> {P["repo"]}/index.html')
