"""Generuje statyczne strony Synergionu (index, kontakt, projekty/*).
Uruchom: python build.py  — pliki HTML trafiają obok, gotowe pod GitHub Pages."""
from pathlib import Path

ROOT = Path(__file__).parent

PHONE = "+48 601 261 994"
PHONE_HREF = "+48601261994"
MAIL = "michal.kociankowski@synergion.pl"

# --- ikony -----------------------------------------------------------------
ARROW = '<svg viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M4.5 11.5l7-7M5.5 4.5h6v6"/></svg>'
STAR = '<svg viewBox="0 0 20 20" fill="currentColor"><path d="M10 1.5l2.6 5.5 6 .7-4.4 4.1 1.2 5.9L10 14.8l-5.4 2.9 1.2-5.9L1.4 7.7l6-.7z"/></svg>'
CHECK_O = '<svg viewBox="0 0 20 20"><circle cx="10" cy="10" r="10" fill="#ff7a0d"/><path d="M6 10.3l2.6 2.6L14 7.5" fill="none" stroke="#fff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>'
CHECK = '<svg viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M2.5 8.5l3.5 3.5 7.5-8"/></svg>'
MAIL_I = '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M3 5h18a1 1 0 011 1v12a1 1 0 01-1 1H3a1 1 0 01-1-1V6a1 1 0 011-1zm1 2.2V17h16V7.2l-8 5.3-8-5.3zM5.3 7l6.7 4.4L18.7 7H5.3z"/></svg>'
PHONE_I = '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M6.6 10.8a15.1 15.1 0 006.6 6.6l2.2-2.2a1 1 0 011-.25 11.4 11.4 0 003.6.57 1 1 0 011 1V20a1 1 0 01-1 1A17 17 0 013 4a1 1 0 011-1h3.5a1 1 0 011 1c0 1.25.2 2.45.57 3.57a1 1 0 01-.25 1z"/></svg>'
PIN_I = '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M12 2a7 7 0 017 7c0 5.2-7 13-7 13S5 14.2 5 9a7 7 0 017-7zm0 4.5A2.5 2.5 0 1012 11.5 2.5 2.5 0 0012 6.5z"/></svg>'
DOC_I = '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M6 2h8l6 6v13a1 1 0 01-1 1H6a1 1 0 01-1-1V3a1 1 0 011-1zm7 1.5V9h5.5L13 3.5zM8 13h8v1.6H8V13zm0 3.5h8v1.6H8v-1.6z"/></svg>'
SPARK = '<svg viewBox="0 0 16 16" fill="currentColor"><path d="M8 0l1.6 5.2L15 7l-5.4 1.8L8 14l-1.6-5.2L1 7l5.4-1.8z"/></svg>'
TAGI = {
    "uslugi": '<svg viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.6"><circle cx="8" cy="8" r="6"/><circle cx="8" cy="8" r="2.2" fill="currentColor"/></svg>',
    "why": SPARK,
    "story": '<svg viewBox="0 0 16 16" fill="currentColor"><path d="M2 3h12v8H6l-4 3V3z"/></svg>',
    "plans": '<svg viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.6"><rect x="2" y="3" width="12" height="10" rx="2"/><path d="M2 6.5h12"/></svg>',
    "proc": '<svg viewBox="0 0 16 16" fill="currentColor"><circle cx="8" cy="3" r="2"/><circle cx="3" cy="12" r="2"/><circle cx="13" cy="12" r="2"/><path d="M8 5v3M8 8l-4 3M8 8l4 3" stroke="currentColor" stroke-width="1.3"/></svg>',
    "cases": '<svg viewBox="0 0 16 16" fill="currentColor"><path d="M2 13l3-4 3 2 5-7v11H2z"/></svg>',
    "reviews": '<svg viewBox="0 0 16 16" fill="currentColor"><path d="M8 14s-6-3.6-6-8a3.3 3.3 0 016-1.9A3.3 3.3 0 0114 6c0 4.4-6 8-6 8z"/></svg>',
    "team": '<svg viewBox="0 0 16 16" fill="currentColor"><circle cx="5.5" cy="5" r="2.5"/><circle cx="11" cy="5.5" r="2"/><path d="M1 13c0-2.5 2-4 4.5-4S10 10.5 10 13H1zm10-3.5c2 0 4 1.2 4 3.5h-4"/></svg>',
    "faq": '<svg viewBox="0 0 16 16" fill="currentColor"><path d="M1 2h10v7H4l-3 2.5V2zm4 8.5h6l3 2.5V5h-2v5.5H5z"/></svg>',
    "kontakt": MAIL_I,
}
WHY_IC = {
    "metoda": '<svg viewBox="0 0 48 48" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="22" cy="22" r="13"/><path d="M31.5 31.5L42 42"/><path d="M15 25l4-5 4 3 5-7"/></svg>',
    "ludzie": '<svg viewBox="0 0 48 48" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="17" cy="15" r="6"/><circle cx="33" cy="17" r="5"/><path d="M5 40c0-7 5.4-12 12-12s12 5 12 12M29 29c7 0 13 4 13 11"/><path d="M38 4l1.2 3L42 8.2 39.2 9.4 38 12l-1.2-2.6L34 8.2l2.8-1.2z" fill="currentColor"/></svg>',
    "ai": '<svg viewBox="0 0 48 48" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="12" y="12" width="24" height="24" rx="5"/><path d="M19 12V6M29 12V6M19 42v-6M29 42v-6M12 19H6M12 29H6M42 19h-6M42 29h-6"/><path d="M19 29l3.5-10h3L29 29M20.5 25.5h7"/></svg>',
    "decyzja": '<svg viewBox="0 0 48 48" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M6 40h36"/><rect x="9" y="26" width="6" height="10" rx="1"/><rect x="21" y="18" width="6" height="18" rx="1"/><rect x="33" y="9" width="6" height="27" rx="1"/><path d="M8 17l9-7 7 4 12-9"/><path d="M31 5h5v5"/></svg>',
}


def logo_svg():
    return ('<svg viewBox="0 0 32 32" aria-hidden="true"><circle cx="12" cy="16" r="9" fill="none" stroke="#fff" stroke-width="2.4"/>'
            '<circle cx="20" cy="16" r="9" fill="none" stroke="#ff7a0d" stroke-width="2.4"/>'
            '<path d="M16 8.3a9 9 0 010 15.4 9 9 0 010-15.4z" fill="#ff7a0d"/></svg>')


def btn(label, href, style="light", extra=""):
    return f'<a class="btn btn-{style}" href="{href}"{extra}>{label}<span class="ico">{ARROW}</span></a>'


def head(title, desc, p=""):
    return f'''<!doctype html>
<html lang="pl">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex, nofollow">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="assets/img/hero-sm.webp">
<meta name="theme-color" content="#121212">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E%3Crect width='32' height='32' rx='8' fill='%23121212'/%3E%3Ccircle cx='13' cy='16' r='7' fill='none' stroke='%23fff' stroke-width='2.2'/%3E%3Ccircle cx='19' cy='16' r='7' fill='none' stroke='%23ff7a0d' stroke-width='2.2'/%3E%3C/svg%3E">
<link rel="preload" href="{p}assets/fonts/manrope-latin.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="{p}style.css">
<script>document.documentElement.classList.add("js")</script>
</head>
<body>
<div class="demo-bar">Wersja pokazowa strony — treści przykładowe, synergion.pl pozostaje bez zmian</div>
'''


def nav(p="", solid=False, home=True):
    h = "" if home else f"{p}index.html"
    cls = "nav solid" if solid else "nav"
    return f'''<header class="{cls}">
  <div class="wrap">
    <a class="logo" href="{p}index.html" aria-label="Synergion — strona główna">{logo_svg()}Synergion</a>
    <button class="burger" aria-label="Menu" aria-expanded="false"><span></span><span></span><span></span></button>
    <nav class="nav-links">
      <a href="{h}#uslugi">Usługi</a>
      <a href="{h}#jak-pracujemy">Jak pracujemy</a>
      <a href="{h}#projekty">Projekty</a>
      <a href="{h}#zespol">Zespół</a>
      <a href="{h}#faq">FAQ</a>
      <a class="btn btn-pill" href="{p}kontakt.html">Umów rozmowę</a>
    </nav>
  </div>
</header>
'''


def footer(p="", home=True):
    h = "" if home else f"{p}index.html"
    return f'''<footer class="footer">
  <div class="wrap">
    <div class="footer-top">
      <div class="footer-brand">
        <a class="logo" href="{p}index.html">{logo_svg()}Synergion</a>
        <p>Pracownia badań i strategii. Od 2010 roku pomagamy firmom zamieniać rozmowy z klientami w dobre decyzje.</p>
        {btn("Umów rozmowę", p + "kontakt.html", "light")}
      </div>
      <div class="footer-cols">
        <div>
          <h4>Nawigacja</h4>
          <a href="{h}#uslugi">Usługi</a>
          <a href="{h}#jak-pracujemy">Jak pracujemy</a>
          <a href="{h}#projekty">Projekty</a>
          <a href="{h}#zespol">Zespół</a>
          <a href="{p}kontakt.html">Kontakt</a>
        </div>
        <div>
          <h4>Obserwuj nas</h4>
          <a href="#" onclick="return false">LinkedIn</a>
          <a href="#" onclick="return false">Facebook</a>
          <a href="#" onclick="return false">YouTube</a>
        </div>
        <div>
          <h4>Kontakt</h4>
          <a href="tel:{PHONE_HREF}">{PHONE}</a>
          <a href="mailto:{MAIL}">E-mail</a>
          <a href="{p}kontakt.html">Blizne Jasińskiego</a>
        </div>
      </div>
    </div>
    <div class="footer-bottom">
      <span>© 2026 Synergion Michał Kociankowski sp.k. · KRS 0000394354 · ul. Kościuszki 23, Blizne Jasińskiego</span>
      <span>Polityka prywatności · Wersja pokazowa</span>
    </div>
  </div>
</footer>
<script src="{p}main.js" defer></script>
</body>
</html>
'''


def tag(key, text):
    return f'<span class="tag">{TAGI[key]}{text}</span>'


# --- dane ------------------------------------------------------------------
CASES = [
    {
        "slug": "siec-drogerii",
        "img": "case-1",
        "title": "Sieć drogerii odzyskała lojalne klientki dzięki badaniu, które słuchało dłużej niż ankieta.",
        "short": "Sieć drogerii odzyskała 12% lojalnych klientek w rok.",
        "lead": "Klientki odchodziły po cichu, a dane sprzedażowe pokazywały tylko skutek. Przeprowadziliśmy 48 wywiadów pogłębionych, a analizę 90 godzin rozmów przyspieszyło AI. Po sześciu tygodniach sieć wiedziała, co zmienić w programie lojalnościowym.",
        "tags": ["Badania jakościowe", "Segmentacja"],
        "checks": ["+12% powracających klientek", "48 wywiadów pogłębionych", "Raport w 6 tygodni zamiast 10"],
        "meta": [("Klient", "Sieć drogerii (dane poufne)"), ("Branża", "Handel detaliczny"), ("Usługa", "IDI + segmentacja"), ("Czas", "6 tygodni")],
        "challenge": ["Program lojalnościowy sieci tracił najcenniejsze klientki, czyli kobiety 35+, które robią zakupy co tydzień. Ankiety satysfakcji wychodziły dobrze, a mimo to klientki przestawały wracać.",
                      "Zarząd potrzebował odpowiedzi na jedno pytanie: dlaczego zadowolone klientki odchodzą?"],
        "approach": ["Zamiast kolejnej ankiety zaprosiliśmy klientki do rozmowy. Przeprowadziliśmy 48 wywiadów pogłębionych, także z osobami, które już odeszły.",
                     "Nagrania trafiły do naszego środowiska analitycznego: automatyczna transkrypcja, kodowanie wątków i mapa powtarzających się motywów. Badaczki weryfikowały każdy kod i dopisywały interpretację.",
                     "Na warsztacie z zarządem przełożyliśmy wnioski na trzy zmiany w programie lojalnościowym."],
        "results": [("+12%", "więcej powracających klientek po roku"), ("90 h", "rozmów przeanalizowanych w 9 dni"), ("3", "zmiany wdrożone w programie")],
        "quote": ("Po raz pierwszy usłyszeliśmy klientki, a nie tylko policzyliśmy. Warsztat skończył się listą decyzji, nie listą pytań.", "Dyrektorka ds. lojalności, sieć drogerii"),
    },
    {
        "slug": "marka-fmcg",
        "img": "case-2",
        "title": "Marka FMCG przetestowała nową komunikację w 10 dni — od briefu do decyzji.",
        "short": "Marka FMCG sprawdziła trzy warianty kampanii w 10 dni.",
        "lead": "Trzy koncepcje kampanii, 1 200 respondentów i bardzo krótki termin. Połączyliśmy badanie ilościowe z wywiadami online, a wyniki klient oglądał na żywo w panelu, a nie w PDF-ie.",
        "tags": ["Test komunikacji", "Badanie ilościowe"],
        "checks": ["1 200 respondentów w 4 dni", "3 warianty kampanii", "10 dni od briefu do decyzji"],
        "meta": [("Klient", "Marka FMCG (dane poufne)"), ("Branża", "Spożywcza"), ("Usługa", "Pre-test komunikacji"), ("Czas", "10 dni")],
        "challenge": ["Marka miała trzy koncepcje kampanii i dwa tygodnie do zamknięcia planu mediowego. Zespół marketingu był podzielony, a agencja broniła swojego faworyta.",
                      "Potrzebne były twarde dane i zrozumienie, dlaczego jeden wariant działa lepiej."],
        "approach": ["Kwestionariusz przeszedł pre-test na próbie pilotażowej, a AI wyłapało niejasne pytania, zanim ruszyło pole.",
                     "Badanie ilościowe na 1 200 osobach uzupełniliśmy o 16 krótkich wywiadów online. Odpowiedzi otwarte kodowały się na bieżąco, więc klient widział pierwsze wyniki po 48 godzinach.",
                     "Końcową rekomendację omówiliśmy na spotkaniu, które skończyło się decyzją o wyborze wariantu i dwóch poprawkach w spocie."],
        "results": [("10 dni", "od briefu do decyzji"), ("+18 pkt", "przewagi zwycięskiego wariantu w zapamiętywaniu"), ("48 h", "do pierwszych wyników w panelu")],
        "quote": ("Spór w zespole skończył się po jednym spotkaniu. Mieliśmy liczby i słowa konsumentów, a nie opinie.", "Brand manager, marka FMCG"),
    },
    {
        "slug": "bank-tracking",
        "img": "case-3",
        "title": "Bank regionalny dostaje raport z każdej fali badania satysfakcji dzień po zamknięciu pola.",
        "short": "Bank regionalny ma raport z fali dzień po zamknięciu pola.",
        "lead": "Kwartalny tracking satysfakcji klientów trwał dotąd trzy tygodnie od zamknięcia pola do raportu. Zautomatyzowaliśmy powtarzalną część pracy, a badacze skupiają się na tym, co w danych nowe.",
        "tags": ["Program falowy", "Dashboard"],
        "checks": ["Raport 24 h po zamknięciu pola", "4 fale rocznie", "−60% czasu analizy"],
        "meta": [("Klient", "Bank regionalny (dane poufne)"), ("Branża", "Finanse"), ("Usługa", "Tracking satysfakcji"), ("Czas", "Współpraca stała")],
        "challenge": ["Bank co kwartał badał satysfakcję klientów w 40 oddziałach. Raport przychodził po trzech tygodniach, gdy dane były już nieaktualne dla menedżerów oddziałów.",
                      "Celem było skrócenie drogi od danych do działania, bez utraty jakości analizy."],
        "approach": ["Zbudowaliśmy stały szablon analizy: nowe dane z fali same aktualizują wykresy, porównania między falami i alerty o zmianach istotnych statystycznie.",
                     "Badacz dostaje gotowy szkic raportu, który weryfikuje i uzupełnia o interpretację. Menedżerowie oddziałów widzą swoje wyniki w panelu.",
                     "Raz na pół roku prowadzimy z zarządem warsztat, na którym wyniki zamieniamy w priorytety."],
        "results": [("24 h", "od zamknięcia pola do raportu"), ("−60%", "czasu pracy analitycznej na falę"), ("40", "oddziałów z własnym panelem wyników")],
        "quote": ("Menedżerowie reagują teraz w tym samym miesiącu, w którym klient coś zgłosił. Wcześniej to było niemożliwe.", "Dyrektor ds. jakości obsługi, bank regionalny"),
    },
]

SERVICES = [
    ("uslugi-jakosciowe", "Badania jakościowe", "Wywiady pogłębione, grupy fokusowe i etnografia. Rozmawiamy z ludźmi tak długo, aż zrozumiemy, co stoi za ich decyzjami. AI transkrybuje i porządkuje materiał, badacz go interpretuje.", ["Wywiady IDI", "Grupy fokusowe", "Etnografia", "Społeczności online"], ""),
    ("uslugi-ilosciowe", "Badania ilościowe i fale", "Ankiety, testy komunikacji i badania trackingowe. Kwestionariusze sprawdzamy na próbie pilotażowej, a wyniki kolejnych fal widzisz w panelu dzień po zamknięciu pola.", ["CAWI / CATI", "Tracking marki", "Testy konceptów", "Panel wyników"], ""),
    ("uslugi-strategia", "Strategia i warsztaty", "Wnioski z badań zamieniamy w pozycjonowanie, architekturę marki i plan działań. Prowadzimy warsztaty, na których zespół dochodzi do wspólnych decyzji zamiast kolejnego spotkania.", ["Strategia marki", "Pozycjonowanie", "Warsztaty decyzyjne", "Insighty konsumenckie"], "wide"),
]

WHY = [
    ("metoda", "Metodologia przede wszystkim", "Dobieramy metodę do pytania biznesowego, a nie odwrotnie. Rzetelność badania jest dla nas punktem wyjścia."),
    ("ludzie", "Doświadczeni badacze", "Za każdym projektem stoją ludzie z wieloletnim doświadczeniem w badaniach, psychologii i strategii marki."),
    ("ai", "AI, które przyspiesza analizę", "Transkrypcja, kodowanie i raporty falowe dzieją się szybciej. Oszczędzony czas oddajemy na myślenie."),
    ("decyzja", "Wnioski gotowe do działania", "Każdy raport kończy się rekomendacją, a spotkanie podsumowujące — listą decyzji i ich właścicieli."),
]

CHIPS1 = ["Insighty konsumenckie", "Badania falowe", "Segmentacja rynku", "Testy komunikacji", "Pozycjonowanie marki", "Wywiady pogłębione", "Grupy fokusowe"]
CHIPS2 = ["Analiza wspierana AI", "Warsztaty strategiczne", "Testy konceptów", "Ścieżka klienta", "Badania pracownicze", "Architektura marki", "Panel wyników"]

STEPS = [
    ("Brief i pytanie badawcze", "Zaczynamy od rozmowy o decyzji, którą chcesz podjąć. Dopiero potem wybieramy metodę.", ["Warsztat otwierający z zespołem klienta", "Przegląd wiedzy z wcześniejszych projektów", "Plan badania i harmonogram w tydzień"], "Pamięć projektów"),
    ("Projekt i pole badawcze", "Projektujemy kwestionariusz albo scenariusz wywiadu i rekrutujemy właściwych respondentów.", ["Pre-test kwestionariusza na próbie pilotażowej", "Kontrola jakości danych w trakcie pola", "Nagrania i transkrypcje dostępne od razu"], "Automatyczna transkrypcja"),
    ("Analiza wspierana AI", "AI koduje wypowiedzi, liczy tabele i wyłapuje anomalie. Badacz sprawdza każdy wniosek i nadaje mu znaczenie.", ["Kodowanie odpowiedzi otwartych z weryfikacją", "Porównania między falami i alerty zmian", "Szkic raportu w stylu Synergionu"], "Analiza + weryfikacja badacza"),
    ("Rekomendacje i decyzja", "Wyniki omawiamy na spotkaniu, które kończy się decyzjami, a nie tylko prezentacją.", ["Raport z rekomendacjami i panel wyników", "Warsztat decyzyjny z zarządem", "Wsparcie przy wdrożeniu wniosków"], "Panel wyników"),
]

REVIEWS = [
    ("Anna Wiśniewska", "Dyrektorka marketingu, sieć handlowa", "AW", "#c2410c", "Synergion pokazał nam, dlaczego klienci odchodzą, zanim zobaczyliśmy to w sprzedaży. Rekomendacje były konkretne i od razu dało się je wdrożyć.", "5.0"),
    ("Tomasz Zieliński", "Head of Insight, marka FMCG", "TZ", "#3b3930", "Najlepszy partner badawczy, z jakim pracowałem. Szybkość raportów falowych zmieniła nasz sposób pracy z danymi.", "5.0"),
    ("Katarzyna Nowak", "Prezeska, fundacja edukacyjna", "KN", "#6f8fb5", "Badanie wśród rodziców i nauczycieli przeprowadzone z ogromną wrażliwością. Wiemy, od czego zacząć nowy program.", "4.9"),
    ("Piotr Lewandowski", "Dyrektor ds. klienta, bank regionalny", "PL", "#eb9854", "Raport dzień po zamknięciu pola to nie slogan. Menedżerowie oddziałów w końcu reagują na bieżąco.", "5.0"),
    ("Joanna Mazur", "Strategy Director, agencja reklamowa", "JM", "#19191c", "Michał i jego zespół zadają pytania, których nikt inny nie zadaje. Dzięki temu nasza strategia ma solidne podstawy.", "5.0"),
]

TEAM = [
    ("michal", "Michał Kociankowski", "Założyciel i strateg badań", True),
    ("malgorzata", "Małgorzata Kowalewska", "Psycholożka, badaczka postaw i motywacji", False),
    ("magdalena", "Magdalena Kępka", "Badaczka jakościowa, moderatorka", False),
    ("justyna", "Justyna", "Analityczka danych i AI", False),
    ("maja", "Maja", "Koordynatorka projektów badawczych", False),
]

FAQ = [
    ("Jak wygląda współpraca z Synergionem?", "Zaczynamy od bezpłatnej rozmowy o decyzji, którą chcesz podjąć. W ciągu kilku dni dostajesz propozycję badania z harmonogramem i wyceną. Przez cały projekt masz jedną osobę kontaktową i wgląd w postęp prac."),
    ("Ile trwa typowy projekt badawczy?", "Test komunikacji zamykamy w 2–3 tygodnie, projekt jakościowy zwykle w 4–8 tygodni. Przy badaniach falowych raport z każdej fali jest gotowy dzień po zamknięciu pola."),
    ("Jak korzystacie z AI i co z bezpieczeństwem danych?", "AI transkrybuje nagrania, koduje odpowiedzi, liczy tabele i przygotowuje szkic raportu. Każdy wniosek sprawdza badacz. Dane respondentów przetwarzamy zgodnie z RODO, anonimizujemy je i nie używamy do trenowania publicznych modeli."),
    ("Jak wyceniacie projekty?", "Każdy projekt wyceniamy indywidualnie — cena zależy od metody, wielkości próby i liczby fal. Przy stałej współpracy proponujemy stałą miesięczną opłatę."),
    ("Czy prowadzicie badania falowe (trackingowe)?", "Tak. Budujemy stały szablon analizy, dzięki któremu wyniki kolejnych fal aktualizują się same, a zmiany istotne statystycznie od razu widać w panelu."),
    ("Czy pomagacie wdrożyć wnioski po badaniu?", "Tak. Prowadzimy warsztaty decyzyjne z zespołem klienta, pomagamy ułożyć plan działań i wracamy z badaniem kontrolnym, żeby sprawdzić efekty."),
]


def contact_form(dark=True):
    return f'''<form class="form rv d1" data-demo novalidate>
        <label>Imię i nazwisko<input name="n" placeholder="Anna Kowalska" required></label>
        <label>Adres e-mail<input name="e" type="email" placeholder="anna@firma.pl" required></label>
        <label>Czego dotyczy zapytanie?<select name="t"><option>Wybierz…</option><option>Badanie jakościowe</option><option>Badanie ilościowe / fale</option><option>Strategia i warsztaty</option><option>Inny temat</option></select></label>
        <label>Wiadomość<textarea name="m" placeholder="Opisz krótko, jaką decyzję chcesz podjąć…"></textarea></label>
        <button type="submit">Wyślij wiadomość</button>
        <div class="form-ok" role="status">Dziękujemy! To wersja pokazowa strony — wiadomość nie została wysłana. Zadzwoń: {PHONE}.</div>
      </form>'''


# --- strona główna -----------------------------------------------------------
def index():
    stars = "".join([STAR] * 5)
    trust_items = ["Zarząd PTBRiO", "Komitet Effie Awards", "Szkoła Strategii Marki SAR", "MBS by Effie", "New Europe 100", "Szkoła Insightów PTBRiO", "INSUMMIT"]
    trust = "".join(f"<span><i></i>{t}</span>" for t in trust_items) * 2

    svcs = ""
    for i, (img, t, d, items, cls) in enumerate(SERVICES):
        lis = "".join(f"<li>{x}</li>" for x in items)
        svcs += f'''<article class="svc {cls} rv d{i+1}" tabindex="0">
        <img src="assets/img/{img}.webp" alt="" loading="lazy">
        <div class="svc-body">
          <div class="svc-top"><h3>{t}</h3><span class="svc-arrow">{ARROW}</span></div>
          <div class="svc-more"><div><p>{d}</p><ul>{lis}</ul>{btn("Zapytaj o badanie", "kontakt.html", "light")}</div></div>
        </div>
      </article>'''

    why = "".join(f'''<div class="card rv d{i+1}"><div class="ic">{WHY_IC[k]}</div><h3>{t}</h3><p>{d}</p></div>''' for i, (k, t, d) in enumerate(WHY))

    ch1 = "".join(f'<span class="chip{" o" if i % 2 else ""}">{c}</span>' for i, c in enumerate(CHIPS1)) * 2
    ch2 = "".join(f'<span class="chip{"" if i % 2 else " o"}">{c}</span>' for i, c in enumerate(CHIPS2)) * 2

    steps = ""
    for i, (t, d, items, ai) in enumerate(STEPS):
        lis = "".join(f"<li>{x}</li>" for x in items)
        steps += f'''<div class="step{" on" if i == 0 else ""}"><div class="step-no">KROK 0{i+1}</div><span class="ai">{SPARK}{ai}</span><h3>{t}</h3><p>{d}</p><ul>{lis}</ul></div>'''

    cases = ""
    for c in CASES:
        tags = "".join(f"<span>{t}</span>" for t in c["tags"])
        checks = "".join(f"<li>{CHECK}{x}</li>" for x in c["checks"])
        cases += f'''<article class="case rv">
        <a class="case-img" href="projekty/{c["slug"]}.html"><img src="assets/img/{c["img"]}.webp" alt="" loading="lazy"></a>
        <div class="case-body">
          <h3>{c["short"]}</h3>
          <p>{c["lead"]}</p>
          <div class="tags">{tags}</div>
          <ul class="checks">{checks}</ul>
          {btn("Zobacz projekt", "projekty/" + c["slug"] + ".html", "dark")}
        </div>
      </article>'''

    revs = ""
    for n, r, ini, col, q, s in REVIEWS:
        revs += f'''<div class="review"><div class="review-who"><span class="avatar" style="background:{col}">{ini}</span><div><b>{n}</b><span>{r}</span></div></div><p>„{q}”</p><div class="review-score">{s}<span class="stars">{stars}</span></div></div>'''
    revs *= 2

    team = ""
    for i, (img, n, r, lead) in enumerate(TEAM):
        badge = '<span class="lead-badge">Założyciel</span>' if lead else ""
        team += f'''<div class="member rv d{(i % 4) + 1}"><div class="member-ph">{badge}<img src="assets/team/{img}.webp" alt="{n}" loading="lazy"></div><h3>{n}</h3><p>{r}</p></div>'''

    faq = "".join(f'<details{" open" if i == 0 else ""}><summary>{q}<i></i></summary><div class="ans">{a}</div></details>' for i, (q, a) in enumerate(FAQ))

    plan1 = "".join(f"<li>{CHECK_O}{x}</li>" for x in ["Rozmowa o celu i pytaniu badawczym", "Dobór metody: jakościowej, ilościowej lub mieszanej", "Realizacja pola i kontrola jakości", "Analiza wspierana AI z weryfikacją badacza", "Raport z rekomendacjami", "Spotkanie podsumowujące"])
    plan2 = "".join(f"<li>{CHECK_O}{x}</li>" for x in ["Dedykowany zespół badawczy", "Szablon analizy dla kolejnych fal", "Raport dzień po zamknięciu pola", "Panel wyników dla zespołu klienta", "Alerty o istotnych zmianach", "Warsztat decyzyjny co pół roku"])

    return head("Synergion — pracownia badań i strategii", "Synergion łączy 30 lat doświadczenia w badaniach rynku z nowoczesnymi narzędziami AI. Badania jakościowe, ilościowe i strategia marki.") + nav() + f'''
<main>
<section class="hero" id="start">
  <div class="hero-bg" role="img" aria-label="Michał Kociankowski podczas wystąpienia"></div>
  <div class="wrap">
    <div class="hero-inner">
      <div class="rating rv"><span class="stars">{stars}</span>200+ projektów badawczych od 2010 roku</div>
      <h1 class="rv d1">Od rozmowy<br><em>do decyzji</em></h1>
      <p class="lead rv d2">Jesteśmy pracownią badań i strategii. Łączymy 30 lat doświadczenia w badaniach rynku z narzędziami AI, dzięki którym szybciej słyszymy, co naprawdę mówią Twoi klienci, i zamieniamy to w decyzje.</p>
      <div class="hero-ctas rv d3">{btn("Umów rozmowę", "kontakt.html", "light")}<a class="btn btn-ghost" href="#uslugi">Zobacz usługi</a></div>
      <div class="hero-points rv d4"><span>Badania jakościowe i ilościowe</span><span>Analiza wspierana AI</span><span>Strategia oparta na danych</span></div>
    </div>
  </div>
  <div class="ai-chip rv d4"><span class="pulse"></span><div><b>Fala 4 · raport gotowy</b><small>24 h po zamknięciu pola</small></div></div>
</section>

<section class="trust" aria-label="Doświadczenie">
  <div class="wrap">
    <div class="trust-label">Doświadczenie, które zna polska branża badań</div>
    <div class="marquee"><div class="marquee-track">{trust}</div></div>
  </div>
</section>

<section class="sec" id="uslugi">
  <div class="wrap">
    <div class="head rv">{tag("uslugi", "Usługi")}<h2>Jak pomagamy <em>widzieć więcej</em></h2><p>Badania i doradztwo, które zamieniają głos klientów w konkretne kierunki działania.</p></div>
    <div class="services">{svcs}</div>
  </div>
</section>

<section class="sec sec-soft" id="dlaczego">
  <div class="wrap">
    <div class="head rv">{tag("why", "Dlaczego Synergion")}<h2>Doświadczenie, które <em>wyprzedza zmiany</em></h2><p>Łączymy metodologię, wiedzę o ludziach i nowoczesne narzędzia, żeby dostarczać wnioski, na których można oprzeć decyzje.</p></div>
    <div class="why">
      <div class="why-photo rv"><img src="assets/img/dlaczego.webp" alt="" loading="lazy"><div class="why-stat"><strong><span data-count="30">30</span>+</strong><span>lat doświadczenia w badaniach</span>{btn("Umów rozmowę", "kontakt.html", "light")}</div></div>
      {why}
    </div>
  </div>
</section>

<section class="sec" id="opinia">
  <div class="wrap">
    <div class="story">
      <div class="rv">{tag("story", "Historia klienta")}<blockquote>„<em>Synergion pokazał nam,</em> dlaczego klienci odchodzą, zanim zobaczyliśmy to w sprzedaży. Raport z drugiej fali mieliśmy dzień po zamknięciu badania.”</blockquote>{btn("Pracujmy razem", "kontakt.html", "grey")}</div>
      <figure class="rv d2"><img src="assets/img/opinia.webp" alt="" loading="lazy"><figcaption><b>Anna Wiśniewska</b><span>Dyrektorka marketingu, sieć handlowa</span></figcaption></figure>
    </div>
  </div>
  <div class="chips">
    <div class="marquee"><div class="marquee-track">{ch1}</div></div>
    <div class="marquee row2"><div class="marquee-track">{ch2}</div></div>
  </div>
</section>

<section class="sec sec-soft" id="wspolpraca">
  <div class="wrap">
    <div class="head rv">{tag("plans", "Formy współpracy")}<h2>Współpraca dopasowana <em>do Twojego pytania</em></h2><p>Jednorazowy projekt albo stały program badań. Wycenę przygotujemy po pierwszej rozmowie.</p></div>
    <div class="plans">
      <div class="plan rv d1"><div class="plan-name"><i>{TAGI["plans"]}</i>Projekt badawczy</div><div class="plan-price">Indywidualnie<small>/ projekt</small></div><p>Dla firm, które stoją przed konkretną decyzją: nowy produkt, zmiana komunikacji, wejście na rynek.</p>{btn("Zapytaj o wycenę", "kontakt.html", "dark")}<ul>{plan1}</ul></div>
      <div class="plan hot rv d2"><span class="badge">Najczęściej wybierane</span><div class="plan-name"><i>{SPARK}</i>Stały program badań</div><div class="plan-price">Abonament<small>/ miesiąc</small></div><p>Dla firm, które chcą regularnie mierzyć markę, satysfakcję klientów albo nastroje pracowników.</p>{btn("Porozmawiajmy", "kontakt.html", "dark")}<ul>{plan2}</ul></div>
    </div>
  </div>
</section>

<section class="sec sec-dark" id="jak-pracujemy">
  <div class="wrap">
    <div class="head rv">{tag("proc", "Nasz proces")}<h2>Jak <em>pracujemy</em></h2><p>Jasna droga od pytania badawczego do decyzji. AI przejmuje powtarzalną pracę, a badacz odpowiada za wnioski.</p></div>
    <div class="process">
      <div class="steps">{steps}</div>
      <div class="proc-media">
        <img src="assets/img/proces.webp" alt="" loading="lazy">
        <div class="proc-panel">
          <div class="proc-panel-top"><b>Tracking marki · fala 4</b><span>aktualizacja 06:12</span></div>
          <div class="bars"><i style="height:40%"></i><i style="height:55%"></i><i style="height:48%"></i><i style="height:66%"></i><i style="height:58%"></i><i style="height:74%"></i><i style="height:70%"></i><i style="height:88%"></i><i style="height:80%"></i><i style="height:96%"></i></div>
          <div class="proc-status"><span class="pulse"></span>Istotny wzrost zaufania do marki (+6 pkt) · do weryfikacji badacza</div>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="sec" id="projekty">
  <div class="wrap">
    <div class="head rv">{tag("cases", "Projekty")}<h2>Zobacz efekty <em>naszej pracy</em></h2><p>Wybrane projekty, w których badanie zamieniło się w decyzję.</p></div>
    <div class="cases">{cases}</div>
  </div>
</section>

<section class="sec sec-soft" id="opinie">
  <div class="wrap">
    <div class="head rv">{tag("reviews", "Opinie")}<h2>Dlaczego klienci <em>nam ufają</em></h2><p>Kilka słów od osób, z którymi pracowaliśmy.</p></div>
    <div class="reviews marquee"><div class="marquee-track">{revs}</div></div>
    <div class="stats rv">
      <div class="stat"><b><span data-count="200">200</span>+</b><span>projektów badawczych</span></div>
      <div class="stat"><b><span data-count="96">96</span>%</b><span>klientów wraca</span></div>
      <div class="stat"><b><span data-count="25">25</span>+</b><span>branż</span></div>
    </div>
    <div class="center rv">{btn("Umów bezpłatną konsultację", "kontakt.html", "dark", "").replace('btn btn-dark', 'btn btn-dark btn-big')}</div>
  </div>
</section>

<section class="sec" id="zespol">
  <div class="wrap">
    <div class="head rv">{tag("team", "Zespół")}<h2>Poznaj ludzi, którzy <em>zadają właściwe pytania</em></h2><p>Badacze, psycholożka i analitycy. Łączy nas ciekawość ludzi i rzetelność w pracy z danymi.</p></div>
    <div class="team">{team}</div>
  </div>
</section>

<section class="sec sec-soft" id="faq">
  <div class="wrap">
    <div class="head rv">{tag("faq", "FAQ")}<h2>Pytania i odpowiedzi</h2><p>Najważniejsze informacje, zanim zaczniemy współpracę.</p></div>
    <div class="faq rv">{faq}</div>
  </div>
</section>

<section class="contact" id="kontakt">
  <div class="contact-bg"></div>
  <div class="wrap">
    <div class="contact-info rv">
      <div>{tag("kontakt", "Kontakt")}<h2>Porozmawiajmy</h2><p>Masz pytanie, które nie daje Ci spokoju? Opowiedz nam o nim — wspólnie znajdziemy sposób, żeby na nie odpowiedzieć.</p></div>
      <div class="contact-lines">
        <a href="mailto:{MAIL}">{MAIL_I}{MAIL}</a>
        <a href="tel:{PHONE_HREF}">{PHONE_I}{PHONE}</a>
      </div>
    </div>
    {contact_form()}
  </div>
</section>
</main>
''' + footer()


# --- podstrona projektu -------------------------------------------------------
def case_page(i):
    c = CASES[i]
    nxt = CASES[(i + 1) % len(CASES)]
    p = "../"
    tags = "".join(f"<span>{t}</span>" for t in c["tags"])
    meta = "".join(f"<div><span>{k}</span><b>{v}</b></div>" for k, v in c["meta"])
    ch = "".join(f"<p>{x}</p>" for x in c["challenge"])
    ap = "".join(f"<p>{x}</p>" for x in c["approach"])
    res = "".join(f"<div class='rv'><b>{a}</b><span>{b}</span></div>" for a, b in c["results"])
    q, who = c["quote"]
    return head(f"{c['short']} — Synergion", c["lead"], p) + nav(p, solid=False, home=False) + f'''
<main>
<section class="page-hero">
  <div class="wrap">
    <div class="crumbs"><a href="{p}index.html">Strona główna</a> / <a href="{p}index.html#projekty">Projekty</a> / {c["tags"][0]}</div>
    <h1 class="rv">{c["title"]}</h1>
    <p class="rv d1">{c["lead"]}</p>
    <div class="tags rv d2" style="margin-top:26px">{tags}</div>
  </div>
</section>
<div class="wrap">
  <div class="cs-cover rv"><img src="{p}assets/img/{c["img"]}.webp" alt=""></div>
  <div class="cs-meta rv">{meta}</div>
  <div class="cs-body rv"><h2>Wyzwanie</h2><div class="txt">{ch}</div></div>
  <div class="cs-body rv"><h2>Jak to zrobiliśmy</h2><div class="txt">{ap}</div></div>
  <div class="cs-results">{res}</div>
  <div class="cs-quote rv"><blockquote>„{q}”</blockquote><cite>— {who}</cite></div>
  <div class="cs-next">
    <div><small>Następny projekt</small><a class="nx" href="{nxt["slug"]}.html">{nxt["short"]} →</a></div>
    {btn("Porozmawiajmy o Twoim projekcie", p + "kontakt.html", "dark")}
  </div>
</div>
</main>
''' + footer(p, home=False)


# --- kontakt -------------------------------------------------------------------
def kontakt():
    p = ""
    return head("Kontakt — Synergion", "Skontaktuj się z Synergionem: telefon, e-mail, adres pracowni w Bliznem Jasińskiego.") + nav(p, home=False) + f'''
<main>
<section class="page-hero">
  <div class="wrap">
    <div class="crumbs"><a href="index.html">Strona główna</a> / Kontakt</div>
    <h1 class="rv">Opowiedz nam o decyzji, <em>przed którą stoisz</em></h1>
    <p class="rv d1">Odpowiadamy w ciągu jednego dnia roboczego. Pierwsza rozmowa jest bezpłatna i do niczego nie zobowiązuje.</p>
  </div>
</section>
<div class="wrap">
  <div class="contact-page">
    <div class="info-cards">
      <div class="info-card rv"><span class="ic">{PHONE_I}</span><div><span>Telefon</span><a href="tel:{PHONE_HREF}">{PHONE}</a></div></div>
      <div class="info-card rv d1"><span class="ic">{MAIL_I}</span><div><span>E-mail</span><a href="mailto:{MAIL}">{MAIL}</a></div></div>
      <div class="info-card rv d2"><span class="ic">{PIN_I}</span><div><span>Adres</span><b>ul. Kościuszki 23, Blizne Jasińskiego</b></div></div>
      <div class="info-card rv d3"><span class="ic">{DOC_I}</span><div><span>Dane firmy</span><b>Synergion Michał Kociankowski sp.k.</b><span>KRS 0000394354</span></div></div>
      <div class="map rv"><iframe title="Mapa dojazdu" loading="lazy" src="https://www.openstreetmap.org/export/embed.html?bbox=20.845%2C52.238%2C20.895%2C52.262&amp;layer=mapnik&amp;marker=52.250%2C20.870"></iframe></div>
    </div>
    <div>
      <h2 class="h2 rv" style="font-size:32px">Napisz do nas</h2>
      {contact_form(False)}
    </div>
  </div>
</div>
</main>
''' + footer(p, home=False)


if __name__ == "__main__":
    (ROOT / "index.html").write_text(index(), encoding="utf-8")
    (ROOT / "kontakt.html").write_text(kontakt(), encoding="utf-8")
    (ROOT / "projekty").mkdir(exist_ok=True)
    for i, c in enumerate(CASES):
        (ROOT / "projekty" / f"{c['slug']}.html").write_text(case_page(i), encoding="utf-8")
    print("OK:", 2 + len(CASES), "stron")
