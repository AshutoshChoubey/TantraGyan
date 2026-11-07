
// ==============================================================================
// TANTRA GYAN VEDIC ASTROLOGY COMPENDIUM - TYPST MASTERWORK ACADEMIC EDITION
// ==============================================================================

#set page(
  paper: "a5",
  margin: (top: 1.2cm, bottom: 1.2cm, inside: 1.2cm, outside: 1.2cm),
  header: context {
    let page_num = counter(page).get().first()
    if page_num > 4 {
      if calc.odd(page_num) {
        align(right)[
          #text(size: 7.5pt, fill: rgb("#78350f"), font: ("Cinzel", "Georgia", "Noto Sans Devanagari"))[
            TANTRA GYAN • VEDIC ASTROLOGY #h(1fr) #page_num
          ]
          #v(-3pt)
          #line(length: 100%, stroke: 0.4pt + rgb("#cbd5e1"))
        ]
      } else {
        align(left)[
          #text(size: 7.5pt, fill: rgb("#78350f"), font: ("Cinzel", "Georgia", "Noto Sans Devanagari"))[
            #page_num #h(1fr) Tantra Gyan: Complete Vedic Astrology Compendium
          ]
          #v(-3pt)
          #line(length: 100%, stroke: 0.4pt + rgb("#cbd5e1"))
        ]
      }
    }
  },
  footer: context {
    let page_num = counter(page).get().first()
    if page_num > 4 {
      align(center)[
        #text(size: 7.5pt, fill: rgb("#94a3b8"))[— पृष्ठ #page_num —]
      ]
    }
  }
)

#set text(
  font: ("Noto Serif Devanagari", "Noto Sans Devanagari", "Devanagari MT", "Georgia", "Palatino"),
  size: 9.2pt,
  lang: "hi"
)

#set par(justify: true, leading: 0.70em)

// Masterwork Show Rules for Headings
#show heading.where(level: 1): it => {
  v(0.8cm)
  align(center)[
    #rect(fill: rgb("#fef3c7"), stroke: 0.6pt + rgb("#d97706"), radius: 3pt, inset: (x: 8pt, y: 3.5pt))[
      #text(size: 8pt, weight: "bold", fill: rgb("#78350f"))[TANTRA GYAN • VEDIC COMPENDIUM]
    ]
    #v(0.35cm)
    #text(size: 16pt, weight: "bold", fill: rgb("#78350f"))[#it.body]
    #v(0.2cm)
    #line(length: 45%, stroke: 1.2pt + rgb("#d97706"))
    #v(0.5cm)
  ]
}

#show heading.where(level: 2): it => {
  v(0.5cm)
  text(size: 11pt, weight: "bold", fill: rgb("#92400e"), style: "italic")[#it.body]
  v(0.2cm)
}

#show heading.where(level: 3): it => {
  v(0.45cm)
  rect(fill: rgb("#fffdf5"), stroke: (left: 3pt + rgb("#d97706")), inset: (left: 6pt, y: 2pt))[
    #text(size: 10pt, weight: "bold", fill: rgb("#78350f"))[#it.body]
  ]
  v(0.2cm)
}

#show heading.where(level: 4): it => {
  v(0.35cm)
  text(size: 9.5pt, weight: "bold", fill: rgb("#451a03"))[#it.body]
  v(0.15cm)
}

// --- FRONT MATTER: GRAND COVER PAGE ---
#align(center + horizon)[
  #block(
    stroke: 1.8pt + rgb("#b45309"),
    inset: 14pt,
    radius: 4pt,
    width: 100%,
    [
      #block(
        stroke: 0.6pt + rgb("#d97706"),
        inset: 12pt,
        width: 100%,
        [
          #v(0.2cm)
          #image("assets/icons/yantra.svg", width: 38%)
          #v(0.6cm)
          #text(size: 19pt, weight: "bold", fill: rgb("#78350f"))[तंत्र ज्ञान: वैदिक ज्योतिष महाग्रंथ]
          #v(0.2cm)
          #text(size: 10.5pt, weight: "bold", fill: rgb("#b45309"), font: ("Cinzel", "Georgia"))[Tantra Gyan: Complete Vedic Astrology Compendium]
          #v(0.35cm)
          #line(length: 60%, stroke: 1pt + rgb("#d97706"))
          #v(0.3cm)
          #text(size: 9pt, style: "italic", fill: rgb("#57534e"))[सम्पूर्ण प्रामाणिक शास्त्रीय फलित ज्ञानकोश एवं प्रेक्टिशनर नोटबुक]
          #v(0.8cm)
          #text(size: 8pt, fill: rgb("#78350f"), tracking: 1pt)[ग्रंथकार एवं ज्योतिषाचार्य] \
          #v(0.12cm)
          #text(size: 13pt, weight: "bold", fill: rgb("#78350f"))[आशुतोष कुमार चौबे] \
          #text(size: 9.5pt, fill: rgb("#57534e"), font: ("Cinzel", "Georgia"))[(Ashutosh Kumar Choubey)] \
          #text(size: 8pt, fill: rgb("#71717a"))[Vedic Astrologer & Publishing Systems Architect]
          #v(0.7cm)
          #rect(fill: rgb("#fef3c7"), stroke: 0.6pt + rgb("#d97706"), radius: 3pt, inset: (x: 8pt, y: 3pt))[
            #text(size: 7.5pt, weight: "bold", fill: rgb("#78350f"))[प्रथम शास्त्रीय मुद्रण संस्करण • Trade Paperback Masterwork Edition]
          ]
          #v(0.35cm)
          #text(size: 8pt, fill: rgb("#64748b"))[तंत्र ज्ञान शोध संस्थान (Tantra Gyan Research Center) • WorldGyan • 2026]
        ]
      )
    ]
  )
]

#pagebreak()

// Copyright & Dedication
#text(size: 8.5pt, fill: rgb("#475569"))[
  #strong[तंत्र ज्ञान: वैदिक ज्योतिष महाग्रंथ] \
  #emph[Tantra Gyan: Complete Vedic Astrology Compendium] \
  © 2026 Ashutosh Kumar Choubey & Tantra Gyan Research Center. All rights reserved. \
  ISBN: 978-93-5912-108-0 \
  प्रकाशक: तंत्र ज्ञान शोध संस्थान (Tantra Gyan Research Center) • WorldGyan \
  वेबसाइट: https://t.worldgyan.com • यूट्यूब: https://www.youtube.com/\@TantraGyan108
]

#v(2cm)
#align(center)[
  #image("assets/icons/ganesha.svg", width: 14%)
  #v(0.4cm)
  #text(size: 11pt, weight: "bold", fill: rgb("#78350f"), style: "italic")[
    वक्रतुण्ड महाकाय सूर्यकोटि समप्रभ। \
    निर्विघ्नं कुरु मे देव सर्वकार्येषु सर्वदा॥
  ]
  #v(0.4cm)
  #text(size: 9.5pt, fill: rgb("#57534e"))[
    यह ग्रंथ समस्त गुरुजनों, वैदिक ऋषियों एवं जिज्ञासुओं को सप्रेम समर्पित है।
  ]
]

#pagebreak()

// Table of Contents
#outline(title: "ग्रंथ अनुक्रमणिका • Table of Contents", depth: 2, indent: auto)

#pagebreak()

// Dedicated Full-Color Navagraha Reference Plate
#align(center)[
  #rect(fill: rgb("#fef3c7"), stroke: 0.6pt + rgb("#d97706"), radius: 3pt, inset: (x: 8pt, y: 3pt))[
    #text(size: 7.5pt, weight: "bold", fill: rgb("#78350f"))[शास्त्रीय ग्रह स्वरूप चक्र • PARASHARI COLOR PALETTE]
  ]
  #v(0.2cm)
  #text(size: 14pt, weight: "bold", fill: rgb("#78350f"))[नवग्रह शास्त्रीय स्वरूप, वर्ण एवं प्रतीक परिचय]
  #v(0.12cm)
  #text(size: 8pt, style: "italic", fill: rgb("#57534e"))[बृहत्पाराशर होरा शास्त्र एवं फलदीपिका अनुसार नवग्रहों का खगोलीय स्वरूप, रत्न, धातु, वर्ण एवं उच्च-नीच मर्यादा]
  #v(0.35cm)
]

#grid(
  columns: (1fr, 1fr),
  gutter: 7pt,
  // 1. Sun
  rect(fill: rgb("#fff7ed"), stroke: 0.6pt + rgb("#ea580c"), radius: 4pt, inset: 6pt)[
    #grid(columns: (18pt, 1fr, 12pt), gutter: 3pt,
      image("/assets/images/planets/sun.png", width: 16pt),
      [#text(weight: "bold", fill: rgb("#c2410c"), size: 8pt)[सूर्य • Sun (Su)] \ #text(size: 6.5pt, fill: rgb("#7c2d12"))[शास्त्रीय वर्ण: रक्त / ताम्रवर्ण]],
      [#align(right)[#text(size: 10pt, fill: rgb("#ea580c"))[☉]]]
    )
    #v(2pt)
    #text(size: 6.5pt, fill: rgb("#451a03"))[
      *देवता / तत्व:* अग्नि • तेजस | *रत्न:* माणिक्य • तांबा \
      *उच्च / नीच:* मेष 10° / तुला 10° | *कारकत्व:* आत्मा, पिता, राजसत्ता
    ]
  ],
  // 2. Moon
  rect(fill: rgb("#f8fafc"), stroke: 0.6pt + rgb("#94a3b8"), radius: 4pt, inset: 6pt)[
    #grid(columns: (18pt, 1fr, 12pt), gutter: 3pt,
      image("/assets/images/planets/moon.png", width: 16pt),
      [#text(weight: "bold", fill: rgb("#334155"), size: 8pt)[चन्द्र • Moon (Mo)] \ #text(size: 6.5pt, fill: rgb("#475569"))[शास्त्रीय वर्ण: श्वेत / चन्द्रकान्ति]],
      [#align(right)[#text(size: 10pt, fill: rgb("#94a3b8"))[☽]]]
    )
    #v(2pt)
    #text(size: 6.5pt, fill: rgb("#1e293b"))[
      *देवता / तत्व:* वरुण • जल तत्व | *रत्न:* मोती • चांदी \
      *उच्च / नीच:* वृषभ 3° / वृश्चिक 3° | *कारकत्व:* मन, माता, मानसिक शांति
    ]
  ],
  // 3. Mars
  rect(fill: rgb("#fef2f2"), stroke: 0.6pt + rgb("#ef4444"), radius: 4pt, inset: 6pt)[
    #grid(columns: (18pt, 1fr, 12pt), gutter: 3pt,
      image("/assets/images/planets/mars.png", width: 16pt),
      [#text(weight: "bold", fill: rgb("#dc2626"), size: 8pt)[मंगल • Mars (Ma)] \ #text(size: 6.5pt, fill: rgb("#991b1b"))[शास्त्रीय वर्ण: रक्तवर्ण (कुज)]],
      [#align(right)[#text(size: 10pt, fill: rgb("#ef4444"))[♂]]]
    )
    #v(2pt)
    #text(size: 6.5pt, fill: rgb("#7f1d1d"))[
      *देवता / तत्व:* कार्तिकेय • अग्नि | *रत्न:* मूंगा • तांबा \
      *उच्च / नीच:* मकर 28° / कर्क 28° | *कारकत्व:* पराक्रम, भ्राता, शौर्य
    ]
  ],
  // 4. Mercury
  rect(fill: rgb("#f0fdf4"), stroke: 0.6pt + rgb("#10b981"), radius: 4pt, inset: 6pt)[
    #grid(columns: (18pt, 1fr, 12pt), gutter: 3pt,
      image("/assets/images/planets/mercury.png", width: 16pt),
      [#text(weight: "bold", fill: rgb("#047857"), size: 8pt)[बुध • Mercury (Me)] \ #text(size: 6.5pt, fill: rgb("#065f46"))[शास्त्रीय वर्ण: हरित / श्याम]],
      [#align(right)[#text(size: 10pt, fill: rgb("#10b981"))[☿]]]
    )
    #v(2pt)
    #text(size: 6.5pt, fill: rgb("#064e3b"))[
      *देवता / तत्व:* विष्णु • पृथ्वी | *रत्न:* पन्ना • कांसा \
      *उच्च / नीच:* कन्या 15° / मीन 15° | *कारकत्व:* बुद्धि, वाणी, व्यापार
    ]
  ],
  // 5. Jupiter
  rect(fill: rgb("#fffbeb"), stroke: 0.6pt + rgb("#f59e0b"), radius: 4pt, inset: 6pt)[
    #grid(columns: (18pt, 1fr, 12pt), gutter: 3pt,
      image("/assets/images/planets/jupiter.png", width: 16pt),
      [#text(weight: "bold", fill: rgb("#b45309"), size: 8pt)[गुरु • Jupiter (Ju)] \ #text(size: 6.5pt, fill: rgb("#92400e"))[शास्त्रीय वर्ण: पीत / कनकवर्ण]],
      [#align(right)[#text(size: 10pt, fill: rgb("#f59e0b"))[♃]]]
    )
    #v(2pt)
    #text(size: 6.5pt, fill: rgb("#78350f"))[
      *देवता / तत्व:* इन्द्र / ब्रह्मा • आकाश | *रत्न:* पुखराज • स्वर्ण \
      *उच्च / नीच:* कर्क 5° / मकर 5° | *कारकत्व:* ज्ञान, धर्म, संतान, विवेक
    ]
  ],
  // 6. Venus
  rect(fill: rgb("#fdf2f8"), stroke: 0.6pt + rgb("#f43f5e"), radius: 4pt, inset: 6pt)[
    #grid(columns: (18pt, 1fr, 12pt), gutter: 3pt,
      image("/assets/images/planets/venus.png", width: 16pt),
      [#text(weight: "bold", fill: rgb("#be185d"), size: 8pt)[शुक्र • Venus (Ve)] \ #text(size: 6.5pt, fill: rgb("#9d174d"))[शास्त्रीय वर्ण: चित्र / शुभ्र श्वेत]],
      [#align(right)[#text(size: 10pt, fill: rgb("#f43f5e"))[♀]]]
    )
    #v(2pt)
    #text(size: 6.5pt, fill: rgb("#831843"))[
      *देवता / तत्व:* इंद्राणी • जल तत्व | *रत्न:* हीरा • चांदी \
      *उच्च / नीच:* मीन 27° / कन्या 27° | *कारकत्व:* प्रेम, ऐश्वर्य, कला, दांपत्य
    ]
  ],
  // 7. Saturn
  rect(fill: rgb("#eff6ff"), stroke: 0.6pt + rgb("#3b82f6"), radius: 4pt, inset: 6pt)[
    #grid(columns: (18pt, 1fr, 12pt), gutter: 3pt,
      image("/assets/images/planets/saturn.png", width: 16pt),
      [#text(weight: "bold", fill: rgb("#1d4ed8"), size: 8pt)[शनि • Saturn (Sa)] \ #text(size: 6.5pt, fill: rgb("#1e40af"))[शास्त्रीय वर्ण: कृष्ण / नीलवर्ण]],
      [#align(right)[#text(size: 11pt, fill: rgb("#3b82f6"))[♄]]]
    )
    #v(2pt)
    #text(size: 6.5pt, fill: rgb("#1e3a8a"))[
      *देवता / तत्व:* यमराज • वायु तत्व | *रत्न:* नीलम • लोहा \
      *उच्च / नीच:* तुला 20° / मेष 20° | *कारकत्व:* कर्म, न्याय, वैराग्य, दीर्घायु
    ]
  ],
  // 8. Rahu
  rect(fill: rgb("#f4f4f5"), stroke: 0.6pt + rgb("#27272a"), radius: 4pt, inset: 6pt)[
    #grid(columns: (18pt, 1fr, 12pt), gutter: 3pt,
      image("/assets/images/planets/rahu.png", width: 16pt),
      [#text(weight: "bold", fill: rgb("#09090b"), size: 8pt)[राहु • Rahu (Ra)] \ #text(size: 6.5pt, fill: rgb("#27272a"))[शास्त्रीय स्वरूप: धूम्रवर्ण (तमोगुणी)]],
      [#align(right)[#text(size: 10pt, fill: rgb("#27272a"))[☊]]]
    )
    #v(2pt)
    #text(size: 6.5pt, fill: rgb("#09090b"))[
      *देवता / तत्व:* सर्प • तमोगुण (छाया) | *रत्न:* गोमेद • सीसा \
      *उच्च / नीच:* मिथुन / धनु | *कारकत्व:* कूटनीति, विद्रोही भाव, विदेश
    ]
  ],
  // 9. Ketu
  rect(fill: rgb("#f4f4f5"), stroke: 0.6pt + rgb("#71717a"), radius: 4pt, inset: 6pt)[
    #grid(columns: (18pt, 1fr, 12pt), gutter: 3pt,
      image("/assets/images/planets/ketu.png", width: 16pt),
      [#text(weight: "bold", fill: rgb("#52525b"), size: 8pt)[केतु • Ketu (Ke)] \ #text(size: 6.5pt, fill: rgb("#52525b"))[शास्त्रीय स्वरूप: चित्र / धूम्रवर्ण]],
      [#align(right)[#text(size: 10pt, fill: rgb("#71717a"))[☋]]]
    )
    #v(2pt)
    #text(size: 6.5pt, fill: rgb("#27272a"))[
      *देवता / तत्व:* चित्रगुप्त • तमोगुण (छाया) | *रत्न:* लहसुनिया • मिश्र धातु \
      *उच्च / नीच:* धनु / मिथुन | *कारकत्व:* मोक्ष, अंतर्ज्ञान, वैराग्य, मौन
    ]
  ],
  // 10. Lagna
  rect(fill: rgb("#faf5ff"), stroke: 0.6pt + rgb("#a855f7"), radius: 4pt, inset: 6pt)[
    #grid(columns: (18pt, 1fr, 12pt), gutter: 3pt,
      image("/assets/images/planets/lagna.png", width: 16pt),
      [#text(weight: "bold", fill: rgb("#6b21a8"), size: 8pt)[लग्न • Ascendant (Asc)] \ #text(size: 6.5pt, fill: rgb("#7e22ce"))[शास्त्रीय स्वरूप: उदित लग्न (तनु भाव)]],
      [#align(right)[#text(size: 10pt, fill: rgb("#a855f7"))[✦]]]
    )
    #v(2pt)
    #text(size: 6.5pt, fill: rgb("#581c87"))[
      *स्वरूप:* कालपुरुष प्रथम भाव (तनु भाव) | *दिग्बल:* पूर्व क्षितिज \
      *मर्यादा:* देह सौष्ठव, तेज, आत्मबल, जीवन गति
    ]
  ]
)

#pagebreak()

= अध्याय 1: वैदिक ज्योतिष आधार, दर्शन एवं भाव कारकत्व
== Chapter 1: Foundations, Cosmic Philosophy, 12 Bhavas & Aspects


#rect(
  fill: rgb("#fffdf7"),
  stroke: (left: 3.5pt + rgb("#b45309"), rest: 0.5pt + rgb("#e2e8f0")),
  radius: (right: 4pt),
  width: 100%,
  inset: (x: 12pt, y: 10pt)
)[
  #align(center)[
    #rect(fill: rgb("#fef3c7"), stroke: 0.5pt + rgb("#d97706"), radius: 3pt, inset: (x: 6pt, y: 2pt))[
      #text(size: 8pt, weight: "bold", fill: rgb("#78350f"))[ॐ बृहत्पाराशर होरा शास्त्र — सृष्टि क्रम एवं वेदान्त]
    ]
  ]
  #v(0.2cm)
  #align(center)[#text(font: ("Noto Serif Devanagari", "Devanagari MT", "Georgia"), size: 10.5pt, weight: "bold", style: "italic", fill: rgb("#451a03"))[यथा शिखा मयूराणां नागानां मणयो यथा।]]
  #align(center)[#text(font: ("Noto Serif Devanagari", "Devanagari MT", "Georgia"), size: 10.5pt, weight: "bold", style: "italic", fill: rgb("#451a03"))[तद्वद्वेदांगशास्त्राणां ज्योतिषं मूर्धनि स्थितम्॥]]
]

वैदिक ज्योतिष (Jyotish Shastra) केवल भाग्य बताने का माध्यम नहीं है, अपितु यह काल-विधान, कर्म-सिद्धांत और चेतना के विकास का गूढ़ विज्ञान है। जिस प्रकार मयूरों के सिर पर शिखा और नागों के सिर पर मणि सर्वोच्च स्थान पर सुशोभित होती है, उसी प्रकार समस्त वेदांगों (शिक्षा, कल्प, व्याकरण, निरुक्त, छंद, ज्योतिष) में ज्योतिष शास्त्र को सर्वोच्च "वेद का चक्षु" (Eye of the Veda) कहा गया है।

मानव जीवन में पूर्वजन्म-संचित कर्मों (प्रारब्ध) का प्रकटीकरण जन्म समय के आकाशीय ग्रहीय विन्यास के माध्यम से होता है। लग्न (Ascendant) आत्मा के इस देह में अवतरण का क्षणिक बिंदु है, जहां से संपूर्ण जीवन का खाका 12 भावों में विभाजित हो जाता है।


#v(0.3cm)
#align(center)[#line(length: 60%, stroke: 0.6pt + rgb("#d97706"))]
#v(0.3cm)

=== 1.1 कालपुरुष कुण्डली एवं भाव व्यवस्था (The 12 Houses / Bhavas)

जन्म कुण्डली में 12 भाव होते हैं, जो जीवन के समस्त आयामों (शारीरिक, मानसिक, आर्थिक, वैवाहिक, आध्यात्मिक) का संचालन करते हैं। नीचे दिए गए कालपुरुष चक्र में मेष राशि लग्न (प्रथम भाव) में स्थित होकर प्राकृतिक कारकत्व दर्शाती है:


#align(center)[
  #image("assets/icons/lagna_chart.svg", width: 85%)
]
#align(center)[#text(size: 8pt, style: "italic", fill: rgb("#64748b"))[चित्र 1.1: कालपुरुष कुण्डली (Kaalpurusha Kundli) — उच्च ग्रह एवं केन्द्र-त्रिकोण भाव विन्यास]]

प्रत्येक भाव का शास्त्रीय नाम, उसका जीवन कारकत्व तथा प्राकृतिक स्वामी ग्रह नीचे दी गई सारणी में स्पष्ट किया गया है:


#align(center)[
  #text(font: ("Noto Sans Devanagari", "Noto Serif Devanagari"), size: 7.2pt)[
    #table(
      columns: (0.9fr, 1.4fr, 1.6fr, 1.3fr, 1.8fr),
      fill: (x, y) => if y == 0 { rgb("#fef3c7") } else if calc.odd(y) { rgb("#f8fafc") } else { rgb("#ffffff") },
      stroke: (x, y) => if y == 0 { (bottom: 1.2pt + rgb("#b45309"), rest: 0.4pt + rgb("#cbd5e1")) } else { 0.4pt + rgb("#cbd5e1") },
      inset: (x: 3.2pt, y: 4.2pt),
      align: (x, y) => if y == 0 { center + horizon } else { left + horizon },
      [#text(weight: "bold", fill: rgb("#78350f"))[भाव क्रम]], [#text(weight: "bold", fill: rgb("#78350f"))[शास्त्रीय नाम]], [#text(weight: "bold", fill: rgb("#78350f"))[मुख्य जीवन कारकत्व (Significations)]], [#text(weight: "bold", fill: rgb("#78350f"))[प्राकृतिक स्वामी]], [#text(weight: "bold", fill: rgb("#78350f"))[श्रेणी]], [#strong[1 (प्रथम)]], [तनु भाव (Lagna)], [देह, वर्ण, रूप, आत्मबल, स्वास्थ्य, दीर्घायु, स्वभाव], [मेष (#box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#fee2e2"), stroke: 0.35pt + rgb("#ef4444"))[#image("/assets/images/planets/mars.png", width: 7pt) #h(1pt)#text(fill: rgb("#dc2626"), weight: "bold")[मंगल]])], [केन्द्र / त्रिकोण], [#strong[2 (द्वितीय)]], [धन भाव (Dhana)], [संचित धन, कुटुंब, वाणी, प्रारंभिक शिक्षा, दाहिनी आँख], [वृषभ (#box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#fce7f3"), stroke: 0.35pt + rgb("#f43f5e"))[#image("/assets/images/planets/venus.png", width: 7pt) #h(1pt)#text(fill: rgb("#be185d"), weight: "bold")[शुक्र]])], [मारक भाव], [#strong[3 (तृतीय)]], [सहज भाव (Sahaja)], [अनुज (छोटे भाई-बहन), पराक्रम, साहस, लेखन, लघु यात्राएं], [मिथुन (#box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#d1fae5"), stroke: 0.35pt + rgb("#10b981"))[#image("/assets/images/planets/mercury.png", width: 7pt) #h(1pt)#text(fill: rgb("#047857"), weight: "bold")[बुध]])], [उपचय भाव], [#strong[4 (चतुर्थ)]], [सुख भाव (Sukha)], [माता, गृह, भूमि, वाहन, अंतःकरण, मानसिक शांति, छाती], [कर्क (#box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#f1f5f9"), stroke: 0.35pt + rgb("#94a3b8"))[#image("/assets/images/planets/moon.png", width: 7pt) #h(1pt)#text(fill: rgb("#334155"), weight: "bold")[चन्द्रमा]])], [केन्द्र भाव], [#strong[5 (पंचम)]], [पुत्र भाव (Putra)], [संतान, पूर्वपुण्य, बुद्धि, मंत्र साधना, #box(baseline: 15%, inset: (x: 1.8pt, y: 0.8pt), radius: 2pt, fill: rgb("#d1fae5"), stroke: 0.35pt + rgb("#10b981"))[#text(fill: rgb("#047857"), weight: "bold", size: 0.85em)[उच्च]] विवेक, प्रेम], [सिंह (#box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#ffedd5"), stroke: 0.35pt + rgb("#ea580c"))[#image("/assets/images/planets/sun.png", width: 7pt) #h(1pt)#text(fill: rgb("#c2410c"), weight: "bold")[सूर्य]])], [त्रिकोण भाव], [#strong[6 (षष्ठ)]], [शत्रु / रोग भाव (Ari)], [रोग, ऋण, शत्रु, प्रतिस्पर्धा, मामा, सेवा, दैनिक कार्य], [कन्या (#box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#d1fae5"), stroke: 0.35pt + rgb("#10b981"))[#image("/assets/images/planets/mercury.png", width: 7pt) #h(1pt)#text(fill: rgb("#047857"), weight: "bold")[बुध]])], [त्रिक / उपचय], [#strong[7 (सप्तम)]], [जाया / कलत्र (Yuvati)], [जीवनसाथी, साझेदारी, व्यापार, विदेश गमन, काम-वासना], [तुला (#box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#fce7f3"), stroke: 0.35pt + rgb("#f43f5e"))[#image("/assets/images/planets/venus.png", width: 7pt) #h(1pt)#text(fill: rgb("#be185d"), weight: "bold")[शुक्र]])], [केन्द्र / मारक], [#strong[8 (अष्टम)]], [आयु / रन्ध्र (Randhra)], [आयु, मृत्यु का कारण, गुप्त विद्याएं, आकस्मिक धन, संकट], [वृश्चिक (#box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#fee2e2"), stroke: 0.35pt + rgb("#ef4444"))[#image("/assets/images/planets/mars.png", width: 7pt) #h(1pt)#text(fill: rgb("#dc2626"), weight: "bold")[मंगल]])], [त्रिक भाव], [#strong[9 (नवम)]], [भाग्य / धर्म (Dharma)], [धर्म, #box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#fef3c7"), stroke: 0.35pt + rgb("#f59e0b"))[#image("/assets/images/planets/jupiter.png", width: 7pt) #h(1pt)#text(fill: rgb("#b45309"), weight: "bold")[गुरु]], पिता, #box(baseline: 15%, inset: (x: 1.8pt, y: 0.8pt), radius: 2pt, fill: rgb("#d1fae5"), stroke: 0.35pt + rgb("#10b981"))[#text(fill: rgb("#047857"), weight: "bold", size: 0.85em)[उच्च]] शिक्षा, तीर्थाटन, ईश्वरीय कृपा], [धनु (#box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#fef3c7"), stroke: 0.35pt + rgb("#f59e0b"))[#image("/assets/images/planets/jupiter.png", width: 7pt) #h(1pt)#text(fill: rgb("#b45309"), weight: "bold")[गुरु]])], [परम त्रिकोण], [#strong[10 (दशम)]], [कर्म भाव (Karma)], [आजीविका, प्रतिष्ठा, राज्य पद, सामाजिक अधिकार, घुटने], [मकर (#box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#dbeafe"), stroke: 0.35pt + rgb("#3b82f6"))[#image("/assets/images/planets/saturn.png", width: 7pt) #h(1pt)#text(fill: rgb("#1d4ed8"), weight: "bold")[शनि]])], [परम केन्द्र], [#strong[11 (एकादश)]], [लाभ भाव (Labha)], [आय, ज्येष्ठ भ्राता, मित्र मंडली, महत्वाकांक्षा पूर्ति], [कुंभ (#box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#dbeafe"), stroke: 0.35pt + rgb("#3b82f6"))[#image("/assets/images/planets/saturn.png", width: 7pt) #h(1pt)#text(fill: rgb("#1d4ed8"), weight: "bold")[शनि]])], [उपचय भाव], [#strong[12 (द्वादश)]], [व्यय भाव (Vyaya)], [व्यय, मोक्ष, विदेश वास, शयन सुख, अस्पताल, जेल, हानि], [मीन (#box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#fef3c7"), stroke: 0.35pt + rgb("#f59e0b"))[#image("/assets/images/planets/jupiter.png", width: 7pt) #h(1pt)#text(fill: rgb("#b45309"), weight: "bold")[गुरु]])], [त्रिक भाव]
    )
  ]
]


#v(0.3cm)
#align(center)[#line(length: 60%, stroke: 0.6pt + rgb("#d97706"))]
#v(0.3cm)

=== 1.2 भावों का शास्त्रीय वर्गीकरण (Functional Classification of Houses)

महर्षि पराशर ने फलित के गहन विश्लेषण हेतु भावों को पांच प्रमुख आध्यात्मिक व भौतिक श्रेणियों में विभाजित किया है:


#align(center)[
  #image("assets/icons/kalpurush_bhavas_diamond_chart.svg", width: 85%)
]
#align(center)[#text(size: 8pt, style: "italic", fill: rgb("#64748b"))[चित्र 1.2: कालपुरुष कुण्डली भाव वर्गीकरण महाचक्र — केन्द्र (विष्णु), त्रिकोण (लक्ष्मी), उपचय (वृद्धि), त्रिक (दुःस्थान) एवं मारक भाव व्यवस्था]]


#rect(
  fill: rgb("#f8fafc"),
  stroke: (left: 3.5pt + rgb("#334155"), rest: 0.5pt + rgb("#cbd5e1")),
  radius: (right: 4pt),
  width: 100%,
  inset: (x: 12pt, y: 10pt)
)[
  #rect(fill: rgb("#f1f5f9"), stroke: 0.6pt + rgb("#64748b"), radius: 3pt, inset: (x: 6pt, y: 2pt))[
    #text(size: 8pt, weight: "bold", fill: rgb("#1e293b"))[SUTRA • केन्द्र एवं त्रिकोण का राजयोग सिद्धांत]
  ]
  #v(0.2cm)
केन्द्र भाव (1, 4, 7, 10) भगवान विष्णु के स्वरूप हैं (संरक्षण एवं भौतिक विस्तार)।
त्रिकोण भाव (1, 5, 9) देवी महालक्ष्मी के स्वरूप हैं (सौभाग्य एवं दैवीय कृपा)।
जब केन्द्र और त्रिकोण के स्वामियों का युति, दृष्टि अथवा राशि-परिवर्तन संबंध बनता है, तब प्रबल राजयोग की उत्पत्ति होती है।
]

1. #strong[केन्द्र भाव (1, 4, 7, 10):] कुण्डली के चार मुख्य स्तंभ। ये जातक को भौतिक संसार में शक्ति, स्थिरता एवं सामाजिक संप्रभुता प्रदान करते हैं।
2. #strong[त्रिकोण भाव (1, 5, 9):] सर्वाधिक शुभ एवं सात्विक भाव। नवम भाव परम भाग्य एवं पंचम भाव पूर्वजन्म की संचित मेधा है। प्रथम भाव केन्द्र और त्रिकोण दोनों होने से सर्वोत्कृष्ट है।
3. #strong[उपचय भाव (3, 6, 10, 11):] वृद्धि के भाव। इन भावों में पापी ग्रह (#box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#ffedd5"), stroke: 0.35pt + rgb("#ea580c"))[#image("/assets/images/planets/sun.png", width: 7pt) #h(1pt)#text(fill: rgb("#c2410c"), weight: "bold")[सूर्य]], #box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#fee2e2"), stroke: 0.35pt + rgb("#ef4444"))[#image("/assets/images/planets/mars.png", width: 7pt) #h(1pt)#text(fill: rgb("#dc2626"), weight: "bold")[मंगल]], #box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#dbeafe"), stroke: 0.35pt + rgb("#3b82f6"))[#image("/assets/images/planets/saturn.png", width: 7pt) #h(1pt)#text(fill: rgb("#1d4ed8"), weight: "bold")[शनि]], #box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#f4f4f5"), stroke: 0.35pt + rgb("#27272a"))[#image("/assets/images/planets/rahu.png", width: 7pt) #h(1pt)#text(fill: rgb("#09090b"), weight: "bold")[राहु]]) समय के साथ जातक को संघर्ष के पश्चात विजय और अपार सफलता दिलाते हैं।
4. #strong[त्रिक भाव (6, 8, 12):] कष्ट, विघ्न एवं विसर्जन के भाव। 6ठा भाव रोग व ऋण का है, 8वां भाव मृत्यु व अप्रत्याशित परिवर्तनों का है, और 12वां भाव व्यय व मोक्ष का है।
5. #strong[मारक भाव (2, 7):] जीवन ऊर्जा को सीमित करने वाले भाव। मारक दशा में स्वास्थ्य एवं आयु का विशेष विचार किया जाता है।


#v(0.3cm)
#align(center)[#line(length: 60%, stroke: 0.6pt + rgb("#d97706"))]
#v(0.3cm)

=== 1.3 ग्रहों की दृष्टियां (Planetary Aspects / Drishti)

वैदिक ज्योतिष में ग्रह अपने स्थान के अतिरिक्त अन्य भावों को भी पूर्ण दृष्टि से देखते हैं:


#align(center)[
  #image("assets/icons/aspect_wheel.svg", width: 85%)
]
#align(center)[#text(size: 8pt, style: "italic", fill: rgb("#64748b"))[चित्र 1.3: ग्रहीय दृष्टि चक्र (Planetary Aspects & Drishti Matrix)]]

- #strong[सर्वग्रह दृष्टि:] समस्त ग्रह अपने स्थित भाव से #strong[7वें भाव] को पूर्ण (100%) दृष्टि से देखते हैं।
- #strong[#box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#fee2e2"), stroke: 0.35pt + rgb("#ef4444"))[#image("/assets/images/planets/mars.png", width: 7pt) #h(1pt)#text(fill: rgb("#dc2626"), weight: "bold")[मंगल]] की विशेष दृष्टियां:] 7वें भाव के अतिरिक्त #strong[4थे] एवं #strong[8वें] भाव पर पूर्ण दृष्टि।
- #strong[#box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#fef3c7"), stroke: 0.35pt + rgb("#f59e0b"))[#image("/assets/images/planets/jupiter.png", width: 7pt) #h(1pt)#text(fill: rgb("#b45309"), weight: "bold")[बृहस्पति]] (#box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#fef3c7"), stroke: 0.35pt + rgb("#f59e0b"))[#image("/assets/images/planets/jupiter.png", width: 7pt) #h(1pt)#text(fill: rgb("#b45309"), weight: "bold")[गुरु]]), #box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#f4f4f5"), stroke: 0.35pt + rgb("#27272a"))[#image("/assets/images/planets/rahu.png", width: 7pt) #h(1pt)#text(fill: rgb("#09090b"), weight: "bold")[राहु]] एवं #box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#f4f4f5"), stroke: 0.35pt + rgb("#71717a"))[#image("/assets/images/planets/ketu.png", width: 7pt) #h(1pt)#text(fill: rgb("#52525b"), weight: "bold")[केतु]] की विशेष दृष्टियां:] 7वें भाव के अतिरिक्त #strong[5वें] एवं #strong[9वें] भाव पर अमृतमय पूर्ण दृष्टि।
- #strong[#box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#dbeafe"), stroke: 0.35pt + rgb("#3b82f6"))[#image("/assets/images/planets/saturn.png", width: 7pt) #h(1pt)#text(fill: rgb("#1d4ed8"), weight: "bold")[शनि]] की विशेष दृष्टियां:] 7वें भाव के अतिरिक्त #strong[3रे] एवं #strong[10वें] भाव पर तीक्ष्ण पूर्ण दृष्टि।


#rect(
  fill: rgb("#fff1f2"),
  stroke: (left: 3.5pt + rgb("#dc2626"), rest: 0.5pt + rgb("#fecaca")),
  radius: (right: 4pt),
  width: 100%,
  inset: (x: 12pt, y: 10pt)
)[
  #rect(fill: rgb("#fee2e2"), stroke: 0.6pt + rgb("#ef4444"), radius: 3pt, inset: (x: 6pt, y: 2pt))[
    #text(size: 8pt, weight: "bold", fill: rgb("#991b1b"))[CAVEAT • दृष्टि फल का नियम]
  ]
  #v(0.2cm)
शुभ ग्रहों (#box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#fef3c7"), stroke: 0.35pt + rgb("#f59e0b"))[#image("/assets/images/planets/jupiter.png", width: 7pt) #h(1pt)#text(fill: rgb("#b45309"), weight: "bold")[गुरु]], #box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#fce7f3"), stroke: 0.35pt + rgb("#f43f5e"))[#image("/assets/images/planets/venus.png", width: 7pt) #h(1pt)#text(fill: rgb("#be185d"), weight: "bold")[शुक्र]], बली #box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#d1fae5"), stroke: 0.35pt + rgb("#10b981"))[#image("/assets/images/planets/mercury.png", width: 7pt) #h(1pt)#text(fill: rgb("#047857"), weight: "bold")[बुध]], पूर्ण #box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#f1f5f9"), stroke: 0.35pt + rgb("#94a3b8"))[#image("/assets/images/planets/moon.png", width: 7pt) #h(1pt)#text(fill: rgb("#334155"), weight: "bold")[चन्द्र]]) की दृष्टि जिस भाव या ग्रह पर पड़ती है, वह उस भाव के फलों में वृद्धि एवं दोषों का शमन करती है। इसके विपरीत, पापी ग्रहों (#box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#dbeafe"), stroke: 0.35pt + rgb("#3b82f6"))[#image("/assets/images/planets/saturn.png", width: 7pt) #h(1pt)#text(fill: rgb("#1d4ed8"), weight: "bold")[शनि]], #box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#f4f4f5"), stroke: 0.35pt + rgb("#27272a"))[#image("/assets/images/planets/rahu.png", width: 7pt) #h(1pt)#text(fill: rgb("#09090b"), weight: "bold")[राहु]], #box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#f4f4f5"), stroke: 0.35pt + rgb("#71717a"))[#image("/assets/images/planets/ketu.png", width: 7pt) #h(1pt)#text(fill: rgb("#52525b"), weight: "bold")[केतु]], क्रूर #box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#fee2e2"), stroke: 0.35pt + rgb("#ef4444"))[#image("/assets/images/planets/mars.png", width: 7pt) #h(1pt)#text(fill: rgb("#dc2626"), weight: "bold")[मंगल]]) की दृष्टि अलगाव, विलंब अथवा व्याधि उत्पन्न करती है, किंतु आध्यात्मिक दृष्टि से वैराग्य प्रदान करती है।
]




#pagebreak()

= अध्याय 2: नवग्रह कारकत्व, 17 शास्त्रीय राजयोग एवं पंच महापुरुष
== Chapter 2: Navagraha Karakatva, 17 Classical Raja Yogas & Transits


#rect(
  fill: rgb("#fffdf7"),
  stroke: (left: 3.5pt + rgb("#b45309"), rest: 0.5pt + rgb("#e2e8f0")),
  radius: (right: 4pt),
  width: 100%,
  inset: (x: 12pt, y: 10pt)
)[
  #align(center)[
    #rect(fill: rgb("#fef3c7"), stroke: 0.5pt + rgb("#d97706"), radius: 3pt, inset: (x: 6pt, y: 2pt))[
      #text(size: 8pt, weight: "bold", fill: rgb("#78350f"))[ॐ फलदीपिका — मन्त्रेश्वर विरचित — ग्रह स्वरूप]
    ]
  ]
  #v(0.2cm)
  #align(center)[#text(font: ("Noto Serif Devanagari", "Devanagari MT", "Georgia"), size: 10.5pt, weight: "bold", style: "italic", fill: rgb("#451a03"))[सूर्योऽऽत्मा जगतस्तस्थुषश्चन्द्रमा मन उच्यते।]]
  #align(center)[#text(font: ("Noto Serif Devanagari", "Devanagari MT", "Georgia"), size: 10.5pt, weight: "bold", style: "italic", fill: rgb("#451a03"))[सत्त्वं कुजः सोमसुतो वाणी वाचस्पतिर्धियम्॥]]
]

नौ आकाशीय शक्तियां (#box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#ffedd5"), stroke: 0.35pt + rgb("#ea580c"))[#image("/assets/images/planets/sun.png", width: 7pt) #h(1pt)#text(fill: rgb("#c2410c"), weight: "bold")[सूर्य]], #box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#f1f5f9"), stroke: 0.35pt + rgb("#94a3b8"))[#image("/assets/images/planets/moon.png", width: 7pt) #h(1pt)#text(fill: rgb("#334155"), weight: "bold")[चन्द्रमा]], #box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#fee2e2"), stroke: 0.35pt + rgb("#ef4444"))[#image("/assets/images/planets/mars.png", width: 7pt) #h(1pt)#text(fill: rgb("#dc2626"), weight: "bold")[मंगल]], #box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#d1fae5"), stroke: 0.35pt + rgb("#10b981"))[#image("/assets/images/planets/mercury.png", width: 7pt) #h(1pt)#text(fill: rgb("#047857"), weight: "bold")[बुध]], #box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#fef3c7"), stroke: 0.35pt + rgb("#f59e0b"))[#image("/assets/images/planets/jupiter.png", width: 7pt) #h(1pt)#text(fill: rgb("#b45309"), weight: "bold")[गुरु]], #box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#fce7f3"), stroke: 0.35pt + rgb("#f43f5e"))[#image("/assets/images/planets/venus.png", width: 7pt) #h(1pt)#text(fill: rgb("#be185d"), weight: "bold")[शुक्र]], #box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#dbeafe"), stroke: 0.35pt + rgb("#3b82f6"))[#image("/assets/images/planets/saturn.png", width: 7pt) #h(1pt)#text(fill: rgb("#1d4ed8"), weight: "bold")[शनि]], #box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#f4f4f5"), stroke: 0.35pt + rgb("#27272a"))[#image("/assets/images/planets/rahu.png", width: 7pt) #h(1pt)#text(fill: rgb("#09090b"), weight: "bold")[राहु]], #box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#f4f4f5"), stroke: 0.35pt + rgb("#71717a"))[#image("/assets/images/planets/ketu.png", width: 7pt) #h(1pt)#text(fill: rgb("#52525b"), weight: "bold")[केतु]]) मानव चेतना, देह, विचार एवं कर्मफलों के प्रतिनिधि हैं। #box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#ffedd5"), stroke: 0.35pt + rgb("#ea580c"))[#image("/assets/images/planets/sun.png", width: 7pt) #h(1pt)#text(fill: rgb("#c2410c"), weight: "bold")[सूर्य]] आत्मा है, #box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#f1f5f9"), stroke: 0.35pt + rgb("#94a3b8"))[#image("/assets/images/planets/moon.png", width: 7pt) #h(1pt)#text(fill: rgb("#334155"), weight: "bold")[चन्द्रमा]] मन है, #box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#fee2e2"), stroke: 0.35pt + rgb("#ef4444"))[#image("/assets/images/planets/mars.png", width: 7pt) #h(1pt)#text(fill: rgb("#dc2626"), weight: "bold")[मंगल]] पराक्रम व रक्त है, #box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#d1fae5"), stroke: 0.35pt + rgb("#10b981"))[#image("/assets/images/planets/mercury.png", width: 7pt) #h(1pt)#text(fill: rgb("#047857"), weight: "bold")[बुध]] वाणी व विवेक है, #box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#fef3c7"), stroke: 0.35pt + rgb("#f59e0b"))[#image("/assets/images/planets/jupiter.png", width: 7pt) #h(1pt)#text(fill: rgb("#b45309"), weight: "bold")[बृहस्पति]] ज्ञान व प्रज्ञा है, #box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#fce7f3"), stroke: 0.35pt + rgb("#f43f5e"))[#image("/assets/images/planets/venus.png", width: 7pt) #h(1pt)#text(fill: rgb("#be185d"), weight: "bold")[शुक्र]] वीर्य व सौंदर्य है, #box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#dbeafe"), stroke: 0.35pt + rgb("#3b82f6"))[#image("/assets/images/planets/saturn.png", width: 7pt) #h(1pt)#text(fill: rgb("#1d4ed8"), weight: "bold")[शनि]] आयु व कर्मदंड है, तथा #box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#f4f4f5"), stroke: 0.35pt + rgb("#27272a"))[#image("/assets/images/planets/rahu.png", width: 7pt) #h(1pt)#text(fill: rgb("#09090b"), weight: "bold")[राहु]] व #box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#f4f4f5"), stroke: 0.35pt + rgb("#71717a"))[#image("/assets/images/planets/ketu.png", width: 7pt) #h(1pt)#text(fill: rgb("#52525b"), weight: "bold")[केतु]] प्रारब्ध के कर्म-बंधन हैं।


#v(0.3cm)
#align(center)[#line(length: 60%, stroke: 0.6pt + rgb("#d97706"))]
#v(0.3cm)

=== 2.1 नवग्रह शास्त्रीय कारकत्व सारणी (Navagraha Significator Matrix)

नीचे दी गई सारणियों में नवग्रहों के संपूर्ण शास्त्रीय कारकत्व, देह अवयव, #box(baseline: 15%, inset: (x: 1.8pt, y: 0.8pt), radius: 2pt, fill: rgb("#d1fae5"), stroke: 0.35pt + rgb("#10b981"))[#text(fill: rgb("#047857"), weight: "bold", size: 0.85em)[उच्च]]-#box(baseline: 15%, inset: (x: 1.8pt, y: 0.8pt), radius: 2pt, fill: rgb("#fee2e2"), stroke: 0.35pt + rgb("#ef4444"))[#text(fill: rgb("#dc2626"), weight: "bold", size: 0.85em)[नीच]] अंश तथा ग्रंथ संदर्भ दो सुव्यवस्थित भागों में संकलित किए गए हैं:

==== तालिका 2.1 (क): प्रत्यक्ष एवं देव-गुरु ग्रह कारकत्व (सूर्य, चन्द्र, मंगल, बुध, गुरु)


#align(center)[
  #text(font: ("Noto Sans Devanagari", "Noto Serif Devanagari"), size: 6.8pt)[
    #table(
      columns: (1.0fr, 1.5fr, 1.5fr, 1.2fr, 1.0fr, 1.0fr, 1.0fr),
      fill: (x, y) => if y == 0 { rgb("#fef3c7") } else if calc.odd(y) { rgb("#f8fafc") } else { rgb("#ffffff") },
      stroke: (x, y) => if y == 0 { (bottom: 1.2pt + rgb("#b45309"), rest: 0.4pt + rgb("#cbd5e1")) } else { 0.4pt + rgb("#cbd5e1") },
      inset: (x: 2.8pt, y: 3.5pt),
      align: (x, y) => if y == 0 { center + horizon } else { left + horizon },
      [#text(weight: "bold", fill: rgb("#78350f"))[ग्रह]], [#text(weight: "bold", fill: rgb("#78350f"))[देह व अवयव]], [#text(weight: "bold", fill: rgb("#78350f"))[स्वभाव व मानसिक वृत्ति]], [#text(weight: "bold", fill: rgb("#78350f"))[संबंध व स्वजन]], [#text(weight: "bold", fill: rgb("#78350f"))[#box(baseline: 15%, inset: (x: 1.8pt, y: 0.8pt), radius: 2pt, fill: rgb("#d1fae5"), stroke: 0.35pt + rgb("#10b981"))[#text(fill: rgb("#047857"), weight: "bold", size: 0.85em)[उच्च]] राशि (अंश)]], [#text(weight: "bold", fill: rgb("#78350f"))[#box(baseline: 15%, inset: (x: 1.8pt, y: 0.8pt), radius: 2pt, fill: rgb("#fee2e2"), stroke: 0.35pt + rgb("#ef4444"))[#text(fill: rgb("#dc2626"), weight: "bold", size: 0.85em)[नीच]] राशि (अंश)]], [#text(weight: "bold", fill: rgb("#78350f"))[#box(baseline: 15%, inset: (x: 1.8pt, y: 0.8pt), radius: 2pt, fill: rgb("#f3e8ff"), stroke: 0.35pt + rgb("#c084fc"))[#text(fill: rgb("#6b21a8"), weight: "bold", size: 0.85em)[मूलत्रिकोण]]]], [#strong[#box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#ffedd5"), stroke: 0.35pt + rgb("#ea580c"))[#image("/assets/images/planets/sun.png", width: 7pt) #h(1pt)#text(fill: rgb("#c2410c"), weight: "bold")[सूर्य (Sun)]]]], [हृदय, अस्थि, नेत्र तेज, प्राण-शक्ति], [आत्मसम्मान, राजसी तेज, नेतृत्व], [पिता, शासक, नरेश], [मेष (10°)], [तुला (10°)], [सिंह (0°-20°)], [#strong[#box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#f1f5f9"), stroke: 0.35pt + rgb("#94a3b8"))[#image("/assets/images/planets/moon.png", width: 7pt) #h(1pt)#text(fill: rgb("#334155"), weight: "bold")[चन्द्र (Moon)]]]], [रक्त संचार, शारीरिक द्रव, आमाशय, मन], [संवेदनशीलता, शांति, कल्पनाशक्ति], [माता, राजसी स्त्रियां], [वृषभ (3°)], [वृश्चिक (3°)], [वृषभ (4°-30°)], [#strong[#box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#fee2e2"), stroke: 0.35pt + rgb("#ef4444"))[#image("/assets/images/planets/mars.png", width: 7pt) #h(1pt)#text(fill: rgb("#dc2626"), weight: "bold")[मंगल (Mars)]]]], [मज्जा, रक्त कणिकाएं, मांसपेशियां, पित्त], [पराक्रम, क्रोध, त्वरित निर्णय, साहस], [अनुज (छोटा भाई), सेनापति], [मकर (28°)], [कर्क (28°)], [मेष (0°-12°)], [#strong[#box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#d1fae5"), stroke: 0.35pt + rgb("#10b981"))[#image("/assets/images/planets/mercury.png", width: 7pt) #h(1pt)#text(fill: rgb("#047857"), weight: "bold")[बुध (Mercury)]]]], [तंत्रिका तंत्र, त्वचा, वाणी, मस्तिष्क], [तर्क, हास्य-विनोद, व्यापारिक बुद्धि], [मामा, मित्र, बहन, दूत], [कन्या (15°)], [मीन (15°)], [कन्या (16°-20°)], [#strong[#box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#fef3c7"), stroke: 0.35pt + rgb("#f59e0b"))[#image("/assets/images/planets/jupiter.png", width: 7pt) #h(1pt)#text(fill: rgb("#b45309"), weight: "bold")[गुरु (Jupiter)]]]], [यकृत (लिवर), वसा, कान, धमनियां], [सात्विकता, दया, धर्म-निष्ठा, विवेक], [#box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#fef3c7"), stroke: 0.35pt + rgb("#f59e0b"))[#image("/assets/images/planets/jupiter.png", width: 7pt) #h(1pt)#text(fill: rgb("#b45309"), weight: "bold")[गुरु]], पुत्र, विद्वान, ब्राह्मण], [कर्क (5°)], [मकर (5°)], [धनु (0°-10°)]
    )
  ]
]

==== तालिका 2.1 (ख): ऐश्वर्य, कर्मदंड एवं छाया ग्रह कारकत्व (शुक्र, शनि, राहु, केतु)


#align(center)[
  #text(font: ("Noto Sans Devanagari", "Noto Serif Devanagari"), size: 6.8pt)[
    #table(
      columns: (1.0fr, 1.5fr, 1.5fr, 1.2fr, 1.0fr, 1.0fr, 1.0fr),
      fill: (x, y) => if y == 0 { rgb("#fef3c7") } else if calc.odd(y) { rgb("#f8fafc") } else { rgb("#ffffff") },
      stroke: (x, y) => if y == 0 { (bottom: 1.2pt + rgb("#b45309"), rest: 0.4pt + rgb("#cbd5e1")) } else { 0.4pt + rgb("#cbd5e1") },
      inset: (x: 2.8pt, y: 3.5pt),
      align: (x, y) => if y == 0 { center + horizon } else { left + horizon },
      [#text(weight: "bold", fill: rgb("#78350f"))[ग्रह]], [#text(weight: "bold", fill: rgb("#78350f"))[देह व अवयव]], [#text(weight: "bold", fill: rgb("#78350f"))[स्वभाव व मानसिक वृत्ति]], [#text(weight: "bold", fill: rgb("#78350f"))[संबंध व स्वजन]], [#text(weight: "bold", fill: rgb("#78350f"))[#box(baseline: 15%, inset: (x: 1.8pt, y: 0.8pt), radius: 2pt, fill: rgb("#d1fae5"), stroke: 0.35pt + rgb("#10b981"))[#text(fill: rgb("#047857"), weight: "bold", size: 0.85em)[उच्च]] राशि (अंश)]], [#text(weight: "bold", fill: rgb("#78350f"))[#box(baseline: 15%, inset: (x: 1.8pt, y: 0.8pt), radius: 2pt, fill: rgb("#fee2e2"), stroke: 0.35pt + rgb("#ef4444"))[#text(fill: rgb("#dc2626"), weight: "bold", size: 0.85em)[नीच]] राशि (अंश)]], [#text(weight: "bold", fill: rgb("#78350f"))[#box(baseline: 15%, inset: (x: 1.8pt, y: 0.8pt), radius: 2pt, fill: rgb("#f3e8ff"), stroke: 0.35pt + rgb("#c084fc"))[#text(fill: rgb("#6b21a8"), weight: "bold", size: 0.85em)[मूलत्रिकोण]]]], [#strong[#box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#fce7f3"), stroke: 0.35pt + rgb("#f43f5e"))[#image("/assets/images/planets/venus.png", width: 7pt) #h(1pt)#text(fill: rgb("#be185d"), weight: "bold")[शुक्र (Venus)]]]], [वीर्य, प्रजनन अंग, सौंदर्य, नेत्र ज्योति], [रसिकता, कला, परिष्कार, ऐश्वर्य], [पत्नी, प्रेमिका, कलाकार], [मीन (27°)], [कन्या (27°)], [तुला (0°-15°)], [#strong[#box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#dbeafe"), stroke: 0.35pt + rgb("#3b82f6"))[#image("/assets/images/planets/saturn.png", width: 7pt) #h(1pt)#text(fill: rgb("#1d4ed8"), weight: "bold")[शनि (Saturn)]]]], [स्नायु, पैर, दांत, अस्थि संधियां (जोड़)], [धैर्य, वैराग्य, अनुशासन, कर्मठता], [सेवक, श्रमिक, वृद्ध जन], [तुला (20°)], [मेष (20°)], [कुंभ (0°-20°)], [#strong[#box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#f4f4f5"), stroke: 0.35pt + rgb("#27272a"))[#image("/assets/images/planets/rahu.png", width: 7pt) #h(1pt)#text(fill: rgb("#09090b"), weight: "bold")[राहु (Rahu)]]]], [श्वसन तंत्र, त्वचा रोग, विषाक्तता], [महत्वाकांक्षा, कूटनीति, विद्रोही भाव], [दादा, विदेशी जन, विधर्मी], [मिथुन / वृषभ], [धनु / वृश्चिक], [कुंभ], [#strong[#box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#f4f4f5"), stroke: 0.35pt + rgb("#71717a"))[#image("/assets/images/planets/ketu.png", width: 7pt) #h(1pt)#text(fill: rgb("#52525b"), weight: "bold")[केतु (Ketu)]]]], [रीढ़, सूक्ष्म नाड़ियां, मोक्ष द्वार], [वैराग्य, अंतर्ज्ञान, मौन, संन्यास], [नाना, तपस्वी, गुप्त शत्रु], [धनु / वृश्चिक], [मिथुन / वृषभ], [मीन]
    )
  ]
]


#v(0.3cm)
#align(center)[#line(length: 60%, stroke: 0.6pt + rgb("#d97706"))]
#v(0.3cm)

=== 2.2 17 शास्त्रीय राजयोग एवं पंच महापुरुष (17 Classical Raja Yogas)

शास्त्रीय ग्रंथों (बृहत्पाराशर, सारावली, फलदीपिका एवं जातक पारिजात) में वर्णित 17 प्रमुख राजयोग जातक को विपुल धन, सामाजिक ख्याति, राज्य सत्ता एवं अखंड अधिकार प्रदान करते हैं:


#align(center)[
  #image("assets/icons/raja_yogas_chart.svg", width: 85%)
]
#align(center)[#text(size: 8pt, style: "italic", fill: rgb("#64748b"))[चित्र 2.1: पंच महापुरुष एवं गजकेसरी राजयोग — केन्द्र-त्रिकोण भाव विन्यास (कर्क लग्न)]]

==== 1. पंच महापुरुष योग (The 5 Imperial Yogas)
जब भौमादि पांच ग्रह (#box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#fee2e2"), stroke: 0.35pt + rgb("#ef4444"))[#image("/assets/images/planets/mars.png", width: 7pt) #h(1pt)#text(fill: rgb("#dc2626"), weight: "bold")[मंगल]], #box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#d1fae5"), stroke: 0.35pt + rgb("#10b981"))[#image("/assets/images/planets/mercury.png", width: 7pt) #h(1pt)#text(fill: rgb("#047857"), weight: "bold")[बुध]], #box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#fef3c7"), stroke: 0.35pt + rgb("#f59e0b"))[#image("/assets/images/planets/jupiter.png", width: 7pt) #h(1pt)#text(fill: rgb("#b45309"), weight: "bold")[गुरु]], #box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#fce7f3"), stroke: 0.35pt + rgb("#f43f5e"))[#image("/assets/images/planets/venus.png", width: 7pt) #h(1pt)#text(fill: rgb("#be185d"), weight: "bold")[शुक्र]], #box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#dbeafe"), stroke: 0.35pt + rgb("#3b82f6"))[#image("/assets/images/planets/saturn.png", width: 7pt) #h(1pt)#text(fill: rgb("#1d4ed8"), weight: "bold")[शनि]]) अपनी #strong[#box(baseline: 15%, inset: (x: 1.8pt, y: 0.8pt), radius: 2pt, fill: rgb("#fef3c7"), stroke: 0.35pt + rgb("#f59e0b"))[#text(fill: rgb("#b45309"), weight: "bold", size: 0.85em)[स्वराशि]], #box(baseline: 15%, inset: (x: 1.8pt, y: 0.8pt), radius: 2pt, fill: rgb("#f3e8ff"), stroke: 0.35pt + rgb("#c084fc"))[#text(fill: rgb("#6b21a8"), weight: "bold", size: 0.85em)[मूलत्रिकोण]] या #box(baseline: 15%, inset: (x: 1.8pt, y: 0.8pt), radius: 2pt, fill: rgb("#d1fae5"), stroke: 0.35pt + rgb("#10b981"))[#text(fill: rgb("#047857"), weight: "bold", size: 0.85em)[उच्च]] राशि] में होकर #strong[केन्द्र भाव (1, 4, 7, 10)] में स्थित हों:

1. #strong[रुचक योग (#box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#fee2e2"), stroke: 0.35pt + rgb("#ef4444"))[#image("/assets/images/planets/mars.png", width: 7pt) #h(1pt)#text(fill: rgb("#dc2626"), weight: "bold")[मंगल]]):] पराक्रमी, साहसी, सेनाध्यक्ष या पुलिस प्रमुख, तेजस्वी देह, भू-स्वामी।
2. #strong[भद्र योग (#box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#d1fae5"), stroke: 0.35pt + rgb("#10b981"))[#image("/assets/images/planets/mercury.png", width: 7pt) #h(1pt)#text(fill: rgb("#047857"), weight: "bold")[बुध]]):] प्रखर विद्वान, अद्वितीय वक्ता, व्यापार में निपुण, दीर्घायु, तीव्र स्मरण शक्ति।
3. #strong[हंस योग (#box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#fef3c7"), stroke: 0.35pt + rgb("#f59e0b"))[#image("/assets/images/planets/jupiter.png", width: 7pt) #h(1pt)#text(fill: rgb("#b45309"), weight: "bold")[गुरु]]):] धार्मिक, निष्कलंक चरित्र, शास्त्रवेत्ता, राजा या राष्ट्रपति द्वारा सम्मानित, सात्विक जीवन।
4. #strong[मालव्य योग (#box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#fce7f3"), stroke: 0.35pt + rgb("#f43f5e"))[#image("/assets/images/planets/venus.png", width: 7pt) #h(1pt)#text(fill: rgb("#be185d"), weight: "bold")[शुक्र]]):] वैभवशाली, वाहनों व भवनों का स्वामी, कला-पारखी, सुखी दांपत्य, कामाकर्षक व्यक्तित्व।
5. #strong[शश योग (#box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#dbeafe"), stroke: 0.35pt + rgb("#3b82f6"))[#image("/assets/images/planets/saturn.png", width: 7pt) #h(1pt)#text(fill: rgb("#1d4ed8"), weight: "bold")[शनि]]):] न्यायप्रिय, जन-समूह का नेता, दीर्घायु, कूटनीतिज्ञ, गुप्त साधनों से अपार धनार्जन।


#rect(
  fill: rgb("#fffbeb"),
  stroke: (left: 3.5pt + rgb("#d97706"), rest: 0.5pt + rgb("#fde68a")),
  radius: (right: 4pt),
  width: 100%,
  inset: (x: 12pt, y: 10pt)
)[
  #rect(fill: rgb("#fef3c7"), stroke: 0.6pt + rgb("#ca8a04"), radius: 3pt, inset: (x: 6pt, y: 2pt))[
    #text(size: 8pt, weight: "bold", fill: rgb("#78350f"))[RAJA YOGA • गजकेसरी राजयोग (Gajakesari Yoga)]
  ]
  #v(0.2cm)
#strong[निर्माण नियम:] जब #box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#fef3c7"), stroke: 0.35pt + rgb("#f59e0b"))[#image("/assets/images/planets/jupiter.png", width: 7pt) #h(1pt)#text(fill: rgb("#b45309"), weight: "bold")[बृहस्पति]] #box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#f1f5f9"), stroke: 0.35pt + rgb("#94a3b8"))[#image("/assets/images/planets/moon.png", width: 7pt) #h(1pt)#text(fill: rgb("#334155"), weight: "bold")[चन्द्रमा]] से केन्द्र भाव (1, 4, 7, 10) में स्थित हो, और पाप ग्रहों से दृष्ट या अस्त न हो।
#strong[शास्त्रीय फल:] गज (हाथी) के समान प्रचंड बल एवं केसरी (सिंह) के समान अदम्य शौर्य। जातक समाज में सम्मानित, नीतिवान, अमर कीर्ति प्राप्त करने वाला होता है।
]


#rect(
  fill: rgb("#fffbeb"),
  stroke: (left: 3.5pt + rgb("#d97706"), rest: 0.5pt + rgb("#fde68a")),
  radius: (right: 4pt),
  width: 100%,
  inset: (x: 12pt, y: 10pt)
)[
  #rect(fill: rgb("#fef3c7"), stroke: 0.6pt + rgb("#ca8a04"), radius: 3pt, inset: (x: 6pt, y: 2pt))[
    #text(size: 8pt, weight: "bold", fill: rgb("#78350f"))[RAJA YOGA • बुधादित्य योग (Budhaditya Yoga)]
  ]
  #v(0.2cm)
#strong[निर्माण नियम:] #box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#ffedd5"), stroke: 0.35pt + rgb("#ea580c"))[#image("/assets/images/planets/sun.png", width: 7pt) #h(1pt)#text(fill: rgb("#c2410c"), weight: "bold")[सूर्य]] और #box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#d1fae5"), stroke: 0.35pt + rgb("#10b981"))[#image("/assets/images/planets/mercury.png", width: 7pt) #h(1pt)#text(fill: rgb("#047857"), weight: "bold")[बुध]] की किसी शुभ भाव (विशेषकर 1, 5, 9, 10, 11) में युति हो, और #box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#d1fae5"), stroke: 0.35pt + rgb("#10b981"))[#image("/assets/images/planets/mercury.png", width: 7pt) #h(1pt)#text(fill: rgb("#047857"), weight: "bold")[बुध]] #box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#ffedd5"), stroke: 0.35pt + rgb("#ea580c"))[#image("/assets/images/planets/sun.png", width: 7pt) #h(1pt)#text(fill: rgb("#c2410c"), weight: "bold")[सूर्य]] के अत्यंत निकट होकर पूर्णतः अस्त न हो।
#strong[शास्त्रीय फल:] कुशाग्र बुद्धि, प्रशासनिक कौशल, राजदरबार या कॉरपोरेट में सर्वोच्च पद, तार्किक विश्लेषण क्षमता।
]


#rect(
  fill: rgb("#fffbeb"),
  stroke: (left: 3.5pt + rgb("#d97706"), rest: 0.5pt + rgb("#fde68a")),
  radius: (right: 4pt),
  width: 100%,
  inset: (x: 12pt, y: 10pt)
)[
  #rect(fill: rgb("#fef3c7"), stroke: 0.6pt + rgb("#ca8a04"), radius: 3pt, inset: (x: 6pt, y: 2pt))[
    #text(size: 8pt, weight: "bold", fill: rgb("#78350f"))[RAJA YOGA • धर्म-कर्माधिपति राजयोग (Dharma-Karmadhipati Yoga)]
  ]
  #v(0.2cm)
#strong[निर्माण नियम:] नवमेश (भाग्य भाव का स्वामी) एवं दशमेश (कर्म भाव का स्वामी) की युति, दृष्टि संबंध अथवा परस्पर राशि-परिवर्तन हो।
#strong[शास्त्रीय फल:] वैदिक ज्योतिष का सर्वोत्तम राजयोग। जातक धर्मपूर्वक राज्य संचालन करता है, विपुल ऐश्वर्य भोगता है और लोक-कल्याणकारी कार्यों से अमर हो जाता है।
]


#rect(
  fill: rgb("#fffbeb"),
  stroke: (left: 3.5pt + rgb("#d97706"), rest: 0.5pt + rgb("#fde68a")),
  radius: (right: 4pt),
  width: 100%,
  inset: (x: 12pt, y: 10pt)
)[
  #rect(fill: rgb("#fef3c7"), stroke: 0.6pt + rgb("#ca8a04"), radius: 3pt, inset: (x: 6pt, y: 2pt))[
    #text(size: 8pt, weight: "bold", fill: rgb("#78350f"))[RAJA YOGA • नीचभंग राजयोग (Neechabhanga Raja Yoga)]
  ]
  #v(0.2cm)
#strong[शास्त्रीय नियम:] #box(baseline: 15%, inset: (x: 1.8pt, y: 0.8pt), radius: 2pt, fill: rgb("#fee2e2"), stroke: 0.35pt + rgb("#ef4444"))[#text(fill: rgb("#dc2626"), weight: "bold", size: 0.85em)[नीच]] राशि में स्थित ग्रह का नीचत्व निम्न 4 नियमों से भंग होता है:
1. #box(baseline: 15%, inset: (x: 1.8pt, y: 0.8pt), radius: 2pt, fill: rgb("#fee2e2"), stroke: 0.35pt + rgb("#ef4444"))[#text(fill: rgb("#dc2626"), weight: "bold", size: 0.85em)[नीच]] ग्रह जिस राशि में बैठा है, उसका स्वामी केन्द्र में हो।
2. #box(baseline: 15%, inset: (x: 1.8pt, y: 0.8pt), radius: 2pt, fill: rgb("#fee2e2"), stroke: 0.35pt + rgb("#ef4444"))[#text(fill: rgb("#dc2626"), weight: "bold", size: 0.85em)[नीच]] ग्रह जिस राशि में #box(baseline: 15%, inset: (x: 1.8pt, y: 0.8pt), radius: 2pt, fill: rgb("#d1fae5"), stroke: 0.35pt + rgb("#10b981"))[#text(fill: rgb("#047857"), weight: "bold", size: 0.85em)[उच्च]] होता है, उसका स्वामी लग्न या #box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#f1f5f9"), stroke: 0.35pt + rgb("#94a3b8"))[#image("/assets/images/planets/moon.png", width: 7pt) #h(1pt)#text(fill: rgb("#334155"), weight: "bold")[चन्द्र]] से केन्द्र में हो।
3. #box(baseline: 15%, inset: (x: 1.8pt, y: 0.8pt), radius: 2pt, fill: rgb("#fee2e2"), stroke: 0.35pt + rgb("#ef4444"))[#text(fill: rgb("#dc2626"), weight: "bold", size: 0.85em)[नीच]] ग्रह पर उसकी #box(baseline: 15%, inset: (x: 1.8pt, y: 0.8pt), radius: 2pt, fill: rgb("#d1fae5"), stroke: 0.35pt + rgb("#10b981"))[#text(fill: rgb("#047857"), weight: "bold", size: 0.85em)[उच्च]] राशि के स्वामी की पूर्ण दृष्टि हो।
4. #box(baseline: 15%, inset: (x: 1.8pt, y: 0.8pt), radius: 2pt, fill: rgb("#fee2e2"), stroke: 0.35pt + rgb("#ef4444"))[#text(fill: rgb("#dc2626"), weight: "bold", size: 0.85em)[नीच]] ग्रह #box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#f1f5f9"), stroke: 0.35pt + rgb("#94a3b8"))[#image("/assets/images/planets/moon.png", width: 7pt) #h(1pt)#text(fill: rgb("#334155"), weight: "bold")[चन्द्र]] लग्न से केन्द्र भाव में स्थित हो।
#strong[फल:] प्रारंभिक जीवन में तीव्र संघर्ष, तत्पश्चात चक्रवर्ती सम्राट या उद्योगपति के समान अप्रत्याशित उत्थान।
]


#v(0.3cm)
#align(center)[#line(length: 60%, stroke: 0.6pt + rgb("#d97706"))]
#v(0.3cm)

=== 2.3 विपरीत राजयोग (Viparita Raja Yogas: Harsha, Sarala, Vimala)


#align(center)[
  #image("assets/icons/viparita_chart.svg", width: 85%)
]
#align(center)[#text(size: 8pt, style: "italic", fill: rgb("#64748b"))[चित्र 2.2: त्रिक भावों (6, 8, 12) से निर्मित हर्ष, सरल एवं विमल विपरीत राजयोग (तुला लग्न)]]

त्रिक भाव (6, 8, 12) सामान्यतः विनाशकारी माने जाते हैं, किंतु जब इन अशुभ भावों के स्वामी परस्पर केवल त्रिक भावों में ही स्थित हों और किसी शुभ भाव के स्वामी से युत न हों, तो यह "माइनस गुणा माइनस बराबर प्लस" के नियम से प्रचंड राजयोग उत्पन्न करते हैं:


#align(center)[
  #text(font: ("Noto Sans Devanagari", "Noto Serif Devanagari"), size: 7.8pt)[
    #table(
      columns: (1.1fr, 1.4fr, 3.5fr),
      fill: (x, y) => if y == 0 { rgb("#fef3c7") } else if calc.odd(y) { rgb("#f8fafc") } else { rgb("#ffffff") },
      stroke: (x, y) => if y == 0 { (bottom: 1.2pt + rgb("#b45309"), rest: 0.4pt + rgb("#cbd5e1")) } else { 0.4pt + rgb("#cbd5e1") },
      inset: (x: 4.2pt, y: 5.0pt),
      align: (x, y) => if y == 0 { center + horizon } else { left + horizon },
      [#text(weight: "bold", fill: rgb("#78350f"))[विपरीत राजयोग]], [#text(weight: "bold", fill: rgb("#78350f"))[निर्माण नियम (Formation Rule)]], [#text(weight: "bold", fill: rgb("#78350f"))[शास्त्रीय फल (Predictive Outcome)]], [#strong[हर्ष योग (Harsha Yoga)]], [6ठे भाव का स्वामी केवल 6ठे, 8वें या 12वें भाव में स्थित हो।], [शत्रुओं का समूल नाश, अटूट स्वास्थ्य, विपत्तियों में दैवीय रक्षा, न्यायालय में विजय।], [#strong[सरल योग (Sarala Yoga)]], [8वें भाव का स्वामी केवल 6ठे, 8वें या 12वें भाव में स्थित हो।], [जातक निर्भय, दीर्घायु, अकूत गुप्त संपत्ति का स्वामी, संकटों को अवसर में बदलने वाला।], [#strong[विमल योग (Vimala Yoga)]], [12वें भाव का स्वामी केवल 6ठे, 8वें या 12वें भाव में स्थित हो।], [स्वतंत्र विचार, अपार आध्यात्मिक शांति, न्यूनतम व्यय से महान साम्राज्य की स्थापना।]
    )
  ]
]




#pagebreak()

= अध्याय 3: राशि चक्र, 27 नक्षत्र एवं विंशोत्तरी महादशा
== Chapter 3: Zodiac Signs, 27 Lunar Mansions & Vimshottari Mahadasha


#rect(
  fill: rgb("#fffdf7"),
  stroke: (left: 3.5pt + rgb("#b45309"), rest: 0.5pt + rgb("#e2e8f0")),
  radius: (right: 4pt),
  width: 100%,
  inset: (x: 12pt, y: 10pt)
)[
  #align(center)[
    #rect(fill: rgb("#fef3c7"), stroke: 0.5pt + rgb("#d97706"), radius: 3pt, inset: (x: 6pt, y: 2pt))[
      #text(size: 8pt, weight: "bold", fill: rgb("#78350f"))[ॐ बृहज्जातकम् — वराहमिहिर — राशि स्वरूप]
    ]
  ]
  #v(0.2cm)
  #align(center)[#text(font: ("Noto Serif Devanagari", "Devanagari MT", "Georgia"), size: 10.5pt, weight: "bold", style: "italic", fill: rgb("#451a03"))[क्षेत्राणि भानि भवनानि च राशयश्च।]]
  #align(center)[#text(font: ("Noto Serif Devanagari", "Devanagari MT", "Georgia"), size: 10.5pt, weight: "bold", style: "italic", fill: rgb("#451a03"))[मेषादयो नवभिरंघ्रिभिरृक्षमेकम्॥]]
]

आकाश मंडल 360 अंश (Degrees) का एक पूर्ण वृत्त है, जिसे 12 राशियों (प्रत्येक 30 अंश) तथा 27 नक्षत्रों (प्रत्येक 13 अंश 20 कला) में विभाजित किया गया है। प्रत्येक नक्षत्र में 4 चरण या पद होते हैं (प्रत्येक पद 3 अंश 20 कला)। संपूर्ण राशि चक्र में कुल 108 नक्षत्र पद होते हैं (27 × 4 = 108), जो भारतीय वैदिक गणित का आधार हैं।


#v(0.3cm)
#align(center)[#line(length: 60%, stroke: 0.6pt + rgb("#d97706"))]
#v(0.3cm)

=== 3.1 द्वादश राशि तत्व एवं गति स्वभाव (12 Zodiac Signs Matrix)


#align(center)[
  #text(font: ("Noto Sans Devanagari", "Noto Serif Devanagari"), size: 7.0pt)[
    #table(
      columns: (0.8fr, 1.2fr, 1.2fr, 1.2fr, 1.4fr, 1.4fr),
      fill: (x, y) => if y == 0 { rgb("#fef3c7") } else if calc.odd(y) { rgb("#f8fafc") } else { rgb("#ffffff") },
      stroke: (x, y) => if y == 0 { (bottom: 1.2pt + rgb("#b45309"), rest: 0.4pt + rgb("#cbd5e1")) } else { 0.4pt + rgb("#cbd5e1") },
      inset: (x: 3.0pt, y: 4.0pt),
      align: (x, y) => if y == 0 { center + horizon } else { left + horizon },
      [#text(weight: "bold", fill: rgb("#78350f"))[राशि क्रम]], [#text(weight: "bold", fill: rgb("#78350f"))[नाम (Sanskrit / English)]], [#text(weight: "bold", fill: rgb("#78350f"))[तत्व (Element)]], [#text(weight: "bold", fill: rgb("#78350f"))[स्वभाव (Modality)]], [#text(weight: "bold", fill: rgb("#78350f"))[स्वामी ग्रह]], [#text(weight: "bold", fill: rgb("#78350f"))[शरीर का अंग]], [#strong[1]], [मेष (Aries)], [अग्नि (Fire)], [चर (Movable)], [#box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#fee2e2"), stroke: 0.35pt + rgb("#ef4444"))[#image("/assets/images/planets/mars.png", width: 7pt) #h(1pt)#text(fill: rgb("#dc2626"), weight: "bold")[मंगल (Mars)]]], [मस्तक, कपाल], [#strong[2]], [वृषभ (Taurus)], [पृथ्वी (Earth)], [स्थिर (Fixed)], [#box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#fce7f3"), stroke: 0.35pt + rgb("#f43f5e"))[#image("/assets/images/planets/venus.png", width: 7pt) #h(1pt)#text(fill: rgb("#be185d"), weight: "bold")[शुक्र (Venus)]]], [मुख, गला, वाणी], [#strong[3]], [मिथुन (Gemini)], [वायु (Air)], [द्विस्वभाव (Dual)], [#box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#d1fae5"), stroke: 0.35pt + rgb("#10b981"))[#image("/assets/images/planets/mercury.png", width: 7pt) #h(1pt)#text(fill: rgb("#047857"), weight: "bold")[बुध (Mercury)]]], [कंधे, हाथ, श्वसन नलिका], [#strong[4]], [कर्क (Cancer)], [जल (Water)], [चर (Movable)], [#box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#f1f5f9"), stroke: 0.35pt + rgb("#94a3b8"))[#image("/assets/images/planets/moon.png", width: 7pt) #h(1pt)#text(fill: rgb("#334155"), weight: "bold")[चन्द्रमा]] (#box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#f1f5f9"), stroke: 0.35pt + rgb("#94a3b8"))[#image("/assets/images/planets/moon.png", width: 7pt) #h(1pt)#text(fill: rgb("#334155"), weight: "bold")[Moon]])], [छाती, स्तन, हृदय], [#strong[5]], [सिंह (Leo)], [अग्नि (Fire)], [स्थिर (Fixed)], [#box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#ffedd5"), stroke: 0.35pt + rgb("#ea580c"))[#image("/assets/images/planets/sun.png", width: 7pt) #h(1pt)#text(fill: rgb("#c2410c"), weight: "bold")[सूर्य (Sun)]]], [पेट, रीढ़ की हड्डी], [#strong[6]], [कन्या (Virgo)], [पृथ्वी (Earth)], [द्विस्वभाव (Dual)], [#box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#d1fae5"), stroke: 0.35pt + rgb("#10b981"))[#image("/assets/images/planets/mercury.png", width: 7pt) #h(1pt)#text(fill: rgb("#047857"), weight: "bold")[बुध (Mercury)]]], [आंतें, कमर, उदर गुहा], [#strong[7]], [तुला (Libra)], [वायु (Air)], [चर (Movable)], [#box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#fce7f3"), stroke: 0.35pt + rgb("#f43f5e"))[#image("/assets/images/planets/venus.png", width: 7pt) #h(1pt)#text(fill: rgb("#be185d"), weight: "bold")[शुक्र (Venus)]]], [गुर्दे (Kidneys), कटि प्रदेश], [#strong[8]], [वृश्चिक (Scorpio)], [जल (Water)], [स्थिर (Fixed)], [#box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#fee2e2"), stroke: 0.35pt + rgb("#ef4444"))[#image("/assets/images/planets/mars.png", width: 7pt) #h(1pt)#text(fill: rgb("#dc2626"), weight: "bold")[मंगल (Mars)]]], [जननांग, गुदा, मूत्राशय], [#strong[9]], [धनु (Sagittarius)], [अग्नि (Fire)], [द्विस्वभाव (Dual)], [#box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#fef3c7"), stroke: 0.35pt + rgb("#f59e0b"))[#image("/assets/images/planets/jupiter.png", width: 7pt) #h(1pt)#text(fill: rgb("#b45309"), weight: "bold")[गुरु (Jupiter)]]], [जंघाएं (Thighs), नितंब], [#strong[10]], [मकर (Capricorn)], [पृथ्वी (Earth)], [चर (Movable)], [#box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#dbeafe"), stroke: 0.35pt + rgb("#3b82f6"))[#image("/assets/images/planets/saturn.png", width: 7pt) #h(1pt)#text(fill: rgb("#1d4ed8"), weight: "bold")[शनि (Saturn)]]], [घुटने, कंकाल संधि], [#strong[11]], [कुंभ (Aquarius)], [वायु (Air)], [स्थिर (Fixed)], [#box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#dbeafe"), stroke: 0.35pt + rgb("#3b82f6"))[#image("/assets/images/planets/saturn.png", width: 7pt) #h(1pt)#text(fill: rgb("#1d4ed8"), weight: "bold")[शनि (Saturn)]]], [पिंडलियां, टखने], [#strong[12]], [मीन (Pisces)], [जल (Water)], [द्विस्वभाव (Dual)], [#box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#fef3c7"), stroke: 0.35pt + rgb("#f59e0b"))[#image("/assets/images/planets/jupiter.png", width: 7pt) #h(1pt)#text(fill: rgb("#b45309"), weight: "bold")[गुरु (Jupiter)]]], [पैर के तलवे, अंगूठे]
    )
  ]
]


#v(0.3cm)
#align(center)[#line(length: 60%, stroke: 0.6pt + rgb("#d97706"))]
#v(0.3cm)

=== 3.2 27 नक्षत्र, उनके स्वामी एवं अधिष्ठाता देवता (The 27 Nakshatras)

प्रत्येक नक्षत्र के स्वामी ग्रह विंशोत्तरी दशा का आरंभ बिंदु निर्धारित करते हैं:


#align(center)[
  #text(font: ("Noto Sans Devanagari", "Noto Serif Devanagari"), size: 7.0pt)[
    #table(
      columns: (0.8fr, 1.2fr, 1.2fr, 1.2fr, 1.4fr, 1.4fr),
      fill: (x, y) => if y == 0 { rgb("#fef3c7") } else if calc.odd(y) { rgb("#f8fafc") } else { rgb("#ffffff") },
      stroke: (x, y) => if y == 0 { (bottom: 1.2pt + rgb("#b45309"), rest: 0.4pt + rgb("#cbd5e1")) } else { 0.4pt + rgb("#cbd5e1") },
      inset: (x: 3.0pt, y: 4.0pt),
      align: (x, y) => if y == 0 { center + horizon } else { left + horizon },
      [#text(weight: "bold", fill: rgb("#78350f"))[नक्षत्र क्रम]], [#text(weight: "bold", fill: rgb("#78350f"))[नक्षत्र नाम]], [#text(weight: "bold", fill: rgb("#78350f"))[विस्तार (Degrees)]], [#text(weight: "bold", fill: rgb("#78350f"))[नक्षत्र स्वामी ग्रह]], [#text(weight: "bold", fill: rgb("#78350f"))[अधिष्ठाता देवता]], [#text(weight: "bold", fill: rgb("#78350f"))[प्रतीक]], [#strong[1]], [अश्विनी (Ashwini)], [0°00' - 13°20' मेष], [#box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#f4f4f5"), stroke: 0.35pt + rgb("#71717a"))[#image("/assets/images/planets/ketu.png", width: 7pt) #h(1pt)#text(fill: rgb("#52525b"), weight: "bold")[केतु]]], [अश्विनी कुमार (देव-वैद्य)], [अश्व का मुख], [#strong[2]], [भरणी (Bharani)], [13°20' - 26°40' मेष], [#box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#fce7f3"), stroke: 0.35pt + rgb("#f43f5e"))[#image("/assets/images/planets/venus.png", width: 7pt) #h(1pt)#text(fill: rgb("#be185d"), weight: "bold")[शुक्र]]], [यमराज (न्याय व धर्म)], [योनि / त्रिकोण], [#strong[3]], [कृत्तिका (Krittika)], [26°40' मेष - 10°00' वृषभ], [#box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#ffedd5"), stroke: 0.35pt + rgb("#ea580c"))[#image("/assets/images/planets/sun.png", width: 7pt) #h(1pt)#text(fill: rgb("#c2410c"), weight: "bold")[सूर्य]]], [अग्नि देव (तेज व शुद्धि)], [उस्तरा / ज्वाला], [#strong[4]], [रोहिणी (Rohini)], [10°00' - 23°20' वृषभ], [#box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#f1f5f9"), stroke: 0.35pt + rgb("#94a3b8"))[#image("/assets/images/planets/moon.png", width: 7pt) #h(1pt)#text(fill: rgb("#334155"), weight: "bold")[चन्द्रमा]]], [ब्रह्मा / प्रजापति], [रथ / बैलगाड़ी], [#strong[5]], [मृगशिरा (Mrigashira)], [23°20' वृषभ - 6°40' मिथुन], [#box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#fee2e2"), stroke: 0.35pt + rgb("#ef4444"))[#image("/assets/images/planets/mars.png", width: 7pt) #h(1pt)#text(fill: rgb("#dc2626"), weight: "bold")[मंगल]]], [सोम (अमृत व #box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#f1f5f9"), stroke: 0.35pt + rgb("#94a3b8"))[#image("/assets/images/planets/moon.png", width: 7pt) #h(1pt)#text(fill: rgb("#334155"), weight: "bold")[चन्द्र]])], [हिरण का सिर], [#strong[6]], [आर्द्रा (Ardra)], [6°40' - 20°00' मिथुन], [#box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#f4f4f5"), stroke: 0.35pt + rgb("#27272a"))[#image("/assets/images/planets/rahu.png", width: 7pt) #h(1pt)#text(fill: rgb("#09090b"), weight: "bold")[राहु]]], [रुद्र (तूफान व प्रलय)], [अश्रु बिंदु / मणि], [#strong[7]], [पुनर्वसु (Punarvasu)], [20°00' मिथुन - 3°20' कर्क], [#box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#fef3c7"), stroke: 0.35pt + rgb("#f59e0b"))[#image("/assets/images/planets/jupiter.png", width: 7pt) #h(1pt)#text(fill: rgb("#b45309"), weight: "bold")[गुरु]]], [अदिति (देवमाता)], [बाणों का तरकश], [#strong[8]], [पुष्य (Pushya)], [3°20' - 16°40' कर्क], [#box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#dbeafe"), stroke: 0.35pt + rgb("#3b82f6"))[#image("/assets/images/planets/saturn.png", width: 7pt) #h(1pt)#text(fill: rgb("#1d4ed8"), weight: "bold")[शनि]]], [#box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#fef3c7"), stroke: 0.35pt + rgb("#f59e0b"))[#image("/assets/images/planets/jupiter.png", width: 7pt) #h(1pt)#text(fill: rgb("#b45309"), weight: "bold")[बृहस्पति]] (दिव्य ज्ञान)], [गाय का थन / कमल], [#strong[9]], [आश्लेषा (Ashlesha)], [16°40' - 30°00' कर्क], [#box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#d1fae5"), stroke: 0.35pt + rgb("#10b981"))[#image("/assets/images/planets/mercury.png", width: 7pt) #h(1pt)#text(fill: rgb("#047857"), weight: "bold")[बुध]]], [सर्प / नागराज], [कुण्डलित सर्प], [#strong[10]], [मघा (Magha)], [0°00' - 13°20' सिंह], [#box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#f4f4f5"), stroke: 0.35pt + rgb("#71717a"))[#image("/assets/images/planets/ketu.png", width: 7pt) #h(1pt)#text(fill: rgb("#52525b"), weight: "bold")[केतु]]], [पितृ गण (पूर्वज)], [राज सिंहासन], [#strong[11]], [पूर्वाफाल्गुनी (Purva Phalguni)], [13°20' - 26°40' सिंह], [#box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#fce7f3"), stroke: 0.35pt + rgb("#f43f5e"))[#image("/assets/images/planets/venus.png", width: 7pt) #h(1pt)#text(fill: rgb("#be185d"), weight: "bold")[शुक्र]]], [भग (ऐश्वर्य व सौभाग्य)], [शय्या (झूला)], [#strong[12]], [उत्तराफाल्गुनी (Uttara Phalguni)], [26°40' सिंह - 10°00' कन्या], [#box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#ffedd5"), stroke: 0.35pt + rgb("#ea580c"))[#image("/assets/images/planets/sun.png", width: 7pt) #h(1pt)#text(fill: rgb("#c2410c"), weight: "bold")[सूर्य]]], [अर्यमा (सत्य व न्याय)], [मंच / शैय्या], [#strong[13]], [हस्त (Hasta)], [10°00' - 23°20' कन्या], [#box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#f1f5f9"), stroke: 0.35pt + rgb("#94a3b8"))[#image("/assets/images/planets/moon.png", width: 7pt) #h(1pt)#text(fill: rgb("#334155"), weight: "bold")[चन्द्रमा]]], [सविता (#box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#ffedd5"), stroke: 0.35pt + rgb("#ea580c"))[#image("/assets/images/planets/sun.png", width: 7pt) #h(1pt)#text(fill: rgb("#c2410c"), weight: "bold")[सूर्य]] की जीवन ऊर्जा)], [खुला हुआ हाथ], [#strong[14]], [चित्रा (Chitra)], [23°20' कन्या - 6°40' तुला], [#box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#fee2e2"), stroke: 0.35pt + rgb("#ef4444"))[#image("/assets/images/planets/mars.png", width: 7pt) #h(1pt)#text(fill: rgb("#dc2626"), weight: "bold")[मंगल]]], [त्वष्टा / विश्वकर्मा], [चमकीला रत्न], [#strong[15]], [स्वाति (Swati)], [6°40' - 20°00' तुला], [#box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#f4f4f5"), stroke: 0.35pt + rgb("#27272a"))[#image("/assets/images/planets/rahu.png", width: 7pt) #h(1pt)#text(fill: rgb("#09090b"), weight: "bold")[राहु]]], [वायु देव (गति व स्वतंत्रता)], [मूंगे का पौधा], [#strong[16]], [विशाखा (Vishakha)], [20°00' तुला - 3°20' वृश्चिक], [#box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#fef3c7"), stroke: 0.35pt + rgb("#f59e0b"))[#image("/assets/images/planets/jupiter.png", width: 7pt) #h(1pt)#text(fill: rgb("#b45309"), weight: "bold")[गुरु]]], [इंद्राग्नि (इंद्र व अग्नि)], [तोरण द्वार], [#strong[17]], [अनुराधा (Anuradha)], [3°20' - 16°40' वृश्चिक], [#box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#dbeafe"), stroke: 0.35pt + rgb("#3b82f6"))[#image("/assets/images/planets/saturn.png", width: 7pt) #h(1pt)#text(fill: rgb("#1d4ed8"), weight: "bold")[शनि]]], [मित्र देव (मैत्री व सहयोग)], [विजय पताका], [#strong[18]], [ज्येष्ठा (Jyeshtha)], [16°40' - 30°00' वृश्चिक], [#box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#d1fae5"), stroke: 0.35pt + rgb("#10b981"))[#image("/assets/images/planets/mercury.png", width: 7pt) #h(1pt)#text(fill: rgb("#047857"), weight: "bold")[बुध]]], [इंद्र (देवराज)], [कुंडल / छत्र], [#strong[19]], [मूल (Moola)], [0°00' - 13°20' धनु], [#box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#f4f4f5"), stroke: 0.35pt + rgb("#71717a"))[#image("/assets/images/planets/ketu.png", width: 7pt) #h(1pt)#text(fill: rgb("#52525b"), weight: "bold")[केतु]]], [निर्ऋति (विनाश व पुनरुत्थान)], [जड़ों का गुच्छा], [#strong[20]], [पूर्वाषाढ़ा (Purva Ashadha)], [13°20' - 26°40' धनु], [#box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#fce7f3"), stroke: 0.35pt + rgb("#f43f5e"))[#image("/assets/images/planets/venus.png", width: 7pt) #h(1pt)#text(fill: rgb("#be185d"), weight: "bold")[शुक्र]]], [अपः (जल देव)], [पंखा / सूप], [#strong[21]], [उत्तराषाढ़ा (Uttara Ashadha)], [26°40' धनु - 10°00' मकर], [#box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#ffedd5"), stroke: 0.35pt + rgb("#ea580c"))[#image("/assets/images/planets/sun.png", width: 7pt) #h(1pt)#text(fill: rgb("#c2410c"), weight: "bold")[सूर्य]]], [विश्वेदेव (समस्त देवता)], [हाथी का दांत], [#strong[22]], [श्रवण (Shravana)], [10°00' - 23°20' मकर], [#box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#f1f5f9"), stroke: 0.35pt + rgb("#94a3b8"))[#image("/assets/images/planets/moon.png", width: 7pt) #h(1pt)#text(fill: rgb("#334155"), weight: "bold")[चन्द्रमा]]], [भगवान विष्णु (संरक्षक)], [तीन पद / कान], [#strong[23]], [धनिष्ठा (Dhanishta)], [23°20' मकर - 6°40' कुंभ], [#box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#fee2e2"), stroke: 0.35pt + rgb("#ef4444"))[#image("/assets/images/planets/mars.png", width: 7pt) #h(1pt)#text(fill: rgb("#dc2626"), weight: "bold")[मंगल]]], [अष्ट वसु (भौतिक समृद्धि)], [मृदंग / ढोल], [#strong[24]], [शतभिषा (Shatabhisha)], [6°40' - 20°00' कुंभ], [#box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#f4f4f5"), stroke: 0.35pt + rgb("#27272a"))[#image("/assets/images/planets/rahu.png", width: 7pt) #h(1pt)#text(fill: rgb("#09090b"), weight: "bold")[राहु]]], [वरुण (सागर व अंतरिक्ष)], [100 चिकित्सकों का वृत्त], [#strong[25]], [पूर्वाभाद्रपद (Purva Bhadrapada)], [20°00' कुंभ - 3°20' मीन], [#box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#fef3c7"), stroke: 0.35pt + rgb("#f59e0b"))[#image("/assets/images/planets/jupiter.png", width: 7pt) #h(1pt)#text(fill: rgb("#b45309"), weight: "bold")[गुरु]]], [अज एकपाद (अग्नि नाग)], [तलवार / दो मुख], [#strong[26]], [उत्तराभाद्रपद (Uttara Bhadrapada)], [3°20' - 16°40' मीन], [#box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#dbeafe"), stroke: 0.35pt + rgb("#3b82f6"))[#image("/assets/images/planets/saturn.png", width: 7pt) #h(1pt)#text(fill: rgb("#1d4ed8"), weight: "bold")[शनि]]], [अहिर्बुध्न्य (समुद्री शेषनाग)], [जुड़वां / सर्प], [#strong[27]], [रेवती (Revati)], [16°40' - 30°00' मीन], [#box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#d1fae5"), stroke: 0.35pt + rgb("#10b981"))[#image("/assets/images/planets/mercury.png", width: 7pt) #h(1pt)#text(fill: rgb("#047857"), weight: "bold")[बुध]]], [पूषा (पोषण व मार्गदर्शक)], [मछली का युगल]
    )
  ]
]


#v(0.3cm)
#align(center)[#line(length: 60%, stroke: 0.6pt + rgb("#d97706"))]
#v(0.3cm)

=== 3.3 120 वर्षीय विंशोत्तरी महादशा चक्र (120-Year Vimshottari Mahadasha)

वैदिक ज्योतिष में काल-गणना एवं फलित समय-निर्धारण (Timing of Events) का मुख्य आधार #strong[विंशोत्तरी महादशा] है। मानव की पूर्ण आयु 120 वर्ष मानकर इसे 9 ग्रहों में शास्त्रीय अनुपात में बांटा गया है:


#rect(
  fill: rgb("#f8fafc"),
  stroke: (left: 3.5pt + rgb("#334155"), rest: 0.5pt + rgb("#cbd5e1")),
  radius: (right: 4pt),
  width: 100%,
  inset: (x: 12pt, y: 10pt)
)[
  #rect(fill: rgb("#f1f5f9"), stroke: 0.6pt + rgb("#64748b"), radius: 3pt, inset: (x: 6pt, y: 2pt))[
    #text(size: 8pt, weight: "bold", fill: rgb("#1e293b"))[SUTRA • विंशोत्तरी दशा क्रम एवं भुक्ति काल]
  ]
  #v(0.2cm)
दशा क्रम निश्चित है:
#box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#f4f4f5"), stroke: 0.35pt + rgb("#71717a"))[#image("/assets/images/planets/ketu.png", width: 7pt) #h(1pt)#text(fill: rgb("#52525b"), weight: "bold")[केतु]] (7 वर्ष) → #box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#fce7f3"), stroke: 0.35pt + rgb("#f43f5e"))[#image("/assets/images/planets/venus.png", width: 7pt) #h(1pt)#text(fill: rgb("#be185d"), weight: "bold")[शुक्र]] (20 वर्ष) → #box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#ffedd5"), stroke: 0.35pt + rgb("#ea580c"))[#image("/assets/images/planets/sun.png", width: 7pt) #h(1pt)#text(fill: rgb("#c2410c"), weight: "bold")[सूर्य]] (6 वर्ष) → #box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#f1f5f9"), stroke: 0.35pt + rgb("#94a3b8"))[#image("/assets/images/planets/moon.png", width: 7pt) #h(1pt)#text(fill: rgb("#334155"), weight: "bold")[चन्द्रमा]] (10 वर्ष) → #box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#fee2e2"), stroke: 0.35pt + rgb("#ef4444"))[#image("/assets/images/planets/mars.png", width: 7pt) #h(1pt)#text(fill: rgb("#dc2626"), weight: "bold")[मंगल]] (7 वर्ष) → #box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#f4f4f5"), stroke: 0.35pt + rgb("#27272a"))[#image("/assets/images/planets/rahu.png", width: 7pt) #h(1pt)#text(fill: rgb("#09090b"), weight: "bold")[राहु]] (18 वर्ष) → #box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#fef3c7"), stroke: 0.35pt + rgb("#f59e0b"))[#image("/assets/images/planets/jupiter.png", width: 7pt) #h(1pt)#text(fill: rgb("#b45309"), weight: "bold")[गुरु]] (16 वर्ष) → #box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#dbeafe"), stroke: 0.35pt + rgb("#3b82f6"))[#image("/assets/images/planets/saturn.png", width: 7pt) #h(1pt)#text(fill: rgb("#1d4ed8"), weight: "bold")[शनि]] (19 वर्ष) → #box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#d1fae5"), stroke: 0.35pt + rgb("#10b981"))[#image("/assets/images/planets/mercury.png", width: 7pt) #h(1pt)#text(fill: rgb("#047857"), weight: "bold")[बुध]] (17 वर्ष)
कुल योग = 120 वर्ष
]


#align(center)[
  #text(font: ("Noto Sans Devanagari", "Noto Serif Devanagari"), size: 7.5pt)[
    #table(
      columns: (1.1fr, 1.3fr, 1.4fr, 3.2fr),
      fill: (x, y) => if y == 0 { rgb("#fef3c7") } else if calc.odd(y) { rgb("#f8fafc") } else { rgb("#ffffff") },
      stroke: (x, y) => if y == 0 { (bottom: 1.2pt + rgb("#b45309"), rest: 0.4pt + rgb("#cbd5e1")) } else { 0.4pt + rgb("#cbd5e1") },
      inset: (x: 3.8pt, y: 4.5pt),
      align: (x, y) => if y == 0 { center + horizon } else { left + horizon },
      [#text(weight: "bold", fill: rgb("#78350f"))[दशा क्रम]], [#text(weight: "bold", fill: rgb("#78350f"))[ग्रह]], [#text(weight: "bold", fill: rgb("#78350f"))[महादशा अवधि (वर्ष)]], [#text(weight: "bold", fill: rgb("#78350f"))[मुख्य प्रभाव एवं फलित दृष्टिकोण]], [#strong[1]], [#box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#f4f4f5"), stroke: 0.35pt + rgb("#71717a"))[#image("/assets/images/planets/ketu.png", width: 7pt) #h(1pt)#text(fill: rgb("#52525b"), weight: "bold")[केतु (Ketu)]]], [#strong[7 वर्ष]], [आध्यात्मिक उन्मेष, भौतिक विरक्ति, आकस्मिक परिवर्तन, गुप्त विद्याओं की ओर झुकाव], [#strong[2]], [#box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#fce7f3"), stroke: 0.35pt + rgb("#f43f5e"))[#image("/assets/images/planets/venus.png", width: 7pt) #h(1pt)#text(fill: rgb("#be185d"), weight: "bold")[शुक्र (Venus)]]], [#strong[20 वर्ष]], [भौतिक ऐश्वर्य, विवाह, वाहन, सौंदर्य, कला, व्यापारिक विस्तार, विलास], [#strong[3]], [#box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#ffedd5"), stroke: 0.35pt + rgb("#ea580c"))[#image("/assets/images/planets/sun.png", width: 7pt) #h(1pt)#text(fill: rgb("#c2410c"), weight: "bold")[सूर्य (Sun)]]], [#strong[6 वर्ष]], [आत्मबल, प्रशासनिक अधिकार, सरकारी सम्मान, पिता का सहयोग, नेत्र व स्वास्थ्य विचार], [#strong[4]], [#box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#f1f5f9"), stroke: 0.35pt + rgb("#94a3b8"))[#image("/assets/images/planets/moon.png", width: 7pt) #h(1pt)#text(fill: rgb("#334155"), weight: "bold")[चन्द्र (Moon)]]], [#strong[10 वर्ष]], [मानसिक शांति, माता का सुख, यात्राएं, कल्पनाशक्ति, जन-समर्थन, रचनात्मकता], [#strong[5]], [#box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#fee2e2"), stroke: 0.35pt + rgb("#ef4444"))[#image("/assets/images/planets/mars.png", width: 7pt) #h(1pt)#text(fill: rgb("#dc2626"), weight: "bold")[मंगल (Mars)]]], [#strong[7 वर्ष]], [साहस, भूमि क्रय-विक्रय, रक्त व मज्जा की सक्रियता, तकनीकी कार्य, विवाद अथवा विजय], [#strong[6]], [#box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#f4f4f5"), stroke: 0.35pt + rgb("#27272a"))[#image("/assets/images/planets/rahu.png", width: 7pt) #h(1pt)#text(fill: rgb("#09090b"), weight: "bold")[राहु (Rahu)]]], [#strong[18 वर्ष]], [तीव्र महत्वाकांक्षा, विदेशी यात्राएं, अकूत धनार्जन, अप्रत्याशित उत्थान-पतन, कूटनीति], [#strong[7]], [#box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#fef3c7"), stroke: 0.35pt + rgb("#f59e0b"))[#image("/assets/images/planets/jupiter.png", width: 7pt) #h(1pt)#text(fill: rgb("#b45309"), weight: "bold")[गुरु (Jupiter)]]], [#strong[16 वर्ष]], [ज्ञान, संतान प्राप्ति, धर्मानुष्ठान, #box(baseline: 15%, inset: (x: 1.8pt, y: 0.8pt), radius: 2pt, fill: rgb("#d1fae5"), stroke: 0.35pt + rgb("#10b981"))[#text(fill: rgb("#047857"), weight: "bold", size: 0.85em)[उच्च]] पद, #box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#fef3c7"), stroke: 0.35pt + rgb("#f59e0b"))[#image("/assets/images/planets/jupiter.png", width: 7pt) #h(1pt)#text(fill: rgb("#b45309"), weight: "bold")[गुरु]] कृपा, विवेक एवं आर्थिक स्थिरता], [#strong[8]], [#box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#dbeafe"), stroke: 0.35pt + rgb("#3b82f6"))[#image("/assets/images/planets/saturn.png", width: 7pt) #h(1pt)#text(fill: rgb("#1d4ed8"), weight: "bold")[शनि (Saturn)]]], [#strong[19 वर्ष]], [कठोर परिश्रम, अनुशासन, कर्मफल भुगतान, जन-सामान्य से जुड़ाव, दीर्घकालिक सफलता], [#strong[9]], [#box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#d1fae5"), stroke: 0.35pt + rgb("#10b981"))[#image("/assets/images/planets/mercury.png", width: 7pt) #h(1pt)#text(fill: rgb("#047857"), weight: "bold")[बुध (Mercury)]]], [#strong[17 वर्ष]], [व्यापारिक उन्नति, संचार, लेखा, लेखन, तार्किक विवेक, बौद्धिक शिखर]
    )
  ]
]




#pagebreak()

= अध्याय 4: दीप्तादि 9 अवस्थाएं एवं भावों में सूर्य फल
== Chapter 4: Deeptadi 9 Planetary States & Solar House Positions


#rect(
  fill: rgb("#fffdf7"),
  stroke: (left: 3.5pt + rgb("#b45309"), rest: 0.5pt + rgb("#e2e8f0")),
  radius: (right: 4pt),
  width: 100%,
  inset: (x: 12pt, y: 10pt)
)[
  #align(center)[
    #rect(fill: rgb("#fef3c7"), stroke: 0.5pt + rgb("#d97706"), radius: 3pt, inset: (x: 6pt, y: 2pt))[
      #text(size: 8pt, weight: "bold", fill: rgb("#78350f"))[ॐ सारावली — कल्याण वर्मा — दीप्तादि अवस्था फल]
    ]
  ]
  #v(0.2cm)
  #align(center)[#text(font: ("Noto Serif Devanagari", "Devanagari MT", "Georgia"), size: 10.5pt, weight: "bold", style: "italic", fill: rgb("#451a03"))[दीप्तः स्वोच्चे स्वस्थः स्वगृहे मुदितोऽधिमित्रे शान्तः सुहृदि।]]
  #align(center)[#text(font: ("Noto Serif Devanagari", "Devanagari MT", "Georgia"), size: 10.5pt, weight: "bold", style: "italic", fill: rgb("#451a03"))[दीनोऽसमर्थशत्रौ दुःखी विकलः खलोऽधमे कोपो रणे॥]]
]

कुण्डली में किसी ग्रह का केवल शुभ भाव में बैठना ही पर्याप्त नहीं होता, अपितु यह देखना अनिवार्य है कि वह ग्रह चेतना के किस स्तर पर कार्य कर रहा है। महर्षि पराशर एवं कल्याण वर्मा ने ग्रहों की #strong[9 दीप्तादि अवस्थाओं] का प्रतिपादन किया है, जो ग्रह के वास्तविक शुभाशुभ फल की तीव्रता और गुणवत्ता निर्धारित करती हैं।


#v(0.3cm)
#align(center)[#line(length: 60%, stroke: 0.6pt + rgb("#d97706"))]
#v(0.3cm)

=== 4.1 ग्रहों की दीप्तादि 9 अवस्थाएं (Deeptadi 9 Planetary Dignities)


#align(center)[
  #text(font: ("Noto Sans Devanagari", "Noto Serif Devanagari"), size: 7.2pt)[
    #table(
      columns: (0.9fr, 1.4fr, 1.6fr, 1.3fr, 1.8fr),
      fill: (x, y) => if y == 0 { rgb("#fef3c7") } else if calc.odd(y) { rgb("#f8fafc") } else { rgb("#ffffff") },
      stroke: (x, y) => if y == 0 { (bottom: 1.2pt + rgb("#b45309"), rest: 0.4pt + rgb("#cbd5e1")) } else { 0.4pt + rgb("#cbd5e1") },
      inset: (x: 3.2pt, y: 4.2pt),
      align: (x, y) => if y == 0 { center + horizon } else { left + horizon },
      [#text(weight: "bold", fill: rgb("#78350f"))[अवस्था क्रम]], [#text(weight: "bold", fill: rgb("#78350f"))[अवस्था नाम]], [#text(weight: "bold", fill: rgb("#78350f"))[स्थिति एवं खगोलीय मर्यादा (Astronomical Position)]], [#text(weight: "bold", fill: rgb("#78350f"))[फल की तीव्रता (Potency)]], [#text(weight: "bold", fill: rgb("#78350f"))[वास्तविक जीवन प्रभाव (Life Manifestation)]], [#strong[1]], [#strong[दीप्त (Deepta)]], [ग्रह अपनी परम #box(baseline: 15%, inset: (x: 1.8pt, y: 0.8pt), radius: 2pt, fill: rgb("#d1fae5"), stroke: 0.35pt + rgb("#10b981"))[#text(fill: rgb("#047857"), weight: "bold", size: 0.85em)[उच्च]] राशि (Exaltation) में स्थित हो।], [100% पूर्ण शुभ फल], [राज्य सम्मान, अदम्य आत्मविश्वास, सार्वभौम कीर्ति, विपुल ऐश्वर्य।], [#strong[2]], [#strong[स्वस्थ (Swastha)]], [ग्रह अपनी #box(baseline: 15%, inset: (x: 1.8pt, y: 0.8pt), radius: 2pt, fill: rgb("#fef3c7"), stroke: 0.35pt + rgb("#f59e0b"))[#text(fill: rgb("#b45309"), weight: "bold", size: 0.85em)[स्वराशि]] (Own Sign) या #box(baseline: 15%, inset: (x: 1.8pt, y: 0.8pt), radius: 2pt, fill: rgb("#f3e8ff"), stroke: 0.35pt + rgb("#c084fc"))[#text(fill: rgb("#6b21a8"), weight: "bold", size: 0.85em)[मूलत्रिकोण]] में हो।], [85% #box(baseline: 15%, inset: (x: 1.8pt, y: 0.8pt), radius: 2pt, fill: rgb("#d1fae5"), stroke: 0.35pt + rgb("#10b981"))[#text(fill: rgb("#047857"), weight: "bold", size: 0.85em)[उच्च]] शुभ फल], [स्थिरता, गृह-सुख, निष्कलंक स्वास्थ्य, स्वावलंबी जीवन, आत्म-संतोष।], [#strong[3]], [#strong[मुदित (Mudita)]], [ग्रह अपने अधिमित्र (Great Friend) की राशि में हो।], [75% शुभ फल], [प्रसन्नता, मित्रों व परिजनों का अटूट सहयोग, आर्थिक सुख, सुरुचिपूर्ण जीवन।], [#strong[4]], [#strong[शांत (Shanta)]], [ग्रह अपने मित्र (Friend) की राशि में स्थित हो।], [60% अनुकूल फल], [शांतिपूर्ण प्रगति, सहज कार्य सिद्धि, सामान्य सुख, धार्मिक अभिरुचि।], [#strong[5]], [#strong[दीन (Deena)]], [ग्रह अपने सम (Neutral) ग्रह की राशि में स्थित हो।], [40% मध्यम फल], [औसत जीवन, सामान्य संघर्ष, न विशेष हानि न विशेष लाभ।], [#strong[6]], [#strong[दुखित (Dukhita)]], [ग्रह अपने शत्रु (Enemy) की राशि में स्थित हो।], [25% कष्टप्रद फल], [मानसिक उद्वेग, पारिवारिक कलह, स्थान परिवर्तन, कार्यों में अकारण विघ्न।], [#strong[7]], [#strong[विकल (Vikala)]], [ग्रह #box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#ffedd5"), stroke: 0.35pt + rgb("#ea580c"))[#image("/assets/images/planets/sun.png", width: 7pt) #h(1pt)#text(fill: rgb("#c2410c"), weight: "bold")[सूर्य]] की किरणों से अत्यंत निकट होकर #strong[अस्त (Combust)] हो।], [10% क्षीण फल], [आत्मबल का अभाव, रोग, संबंधियों से उपेक्षा, प्रयासों का श्रेय न मिलना।], [#strong[8]], [#strong[खल (Khala)]], [ग्रह अपनी #box(baseline: 15%, inset: (x: 1.8pt, y: 0.8pt), radius: 2pt, fill: rgb("#fee2e2"), stroke: 0.35pt + rgb("#ef4444"))[#text(fill: rgb("#dc2626"), weight: "bold", size: 0.85em)[नीच]] राशि (Debilitation) में स्थित हो।], [0-15% दूषित फल], [संकीर्ण मनोवृत्ति, आर्थिक संकट, अपयश, #box(baseline: 15%, inset: (x: 1.8pt, y: 0.8pt), radius: 2pt, fill: rgb("#fee2e2"), stroke: 0.35pt + rgb("#ef4444"))[#text(fill: rgb("#dc2626"), weight: "bold", size: 0.85em)[नीच]] संगति, असाध्य रोग।], [#strong[9]], [#strong[कोप (Kopa)]], [ग्रह ग्रह-युद्ध (Planetary War) में अन्य ग्रह से पराजित हो।], [अत्यंत अनिष्ट फल], [धन-हानि, मानसिक अवसाद, पराजय का भय, परिजनों से घोर विछोह।]
    )
  ]
]


#v(0.3cm)
#align(center)[#line(length: 60%, stroke: 0.6pt + rgb("#d97706"))]
#v(0.3cm)

=== 4.2 पंचधा मैत्री सिद्धांत (The Five-Fold Relationship Matrix)

ग्रहों के आपसी संबंध केवल स्थायी (नैसर्गिक) नहीं होते, अपितु कुण्डली में उनकी तात्कालिक स्थिति भी मित्रता या शत्रुता तय करती है:


#rect(
  fill: rgb("#f8fafc"),
  stroke: (left: 3.5pt + rgb("#334155"), rest: 0.5pt + rgb("#cbd5e1")),
  radius: (right: 4pt),
  width: 100%,
  inset: (x: 12pt, y: 10pt)
)[
  #rect(fill: rgb("#f1f5f9"), stroke: 0.6pt + rgb("#64748b"), radius: 3pt, inset: (x: 6pt, y: 2pt))[
    #text(size: 8pt, weight: "bold", fill: rgb("#1e293b"))[SUTRA • पंचधा मैत्री गणना सूत्र]
  ]
  #v(0.2cm)
1. #strong[नैसर्गिक मित्र + तात्कालिक मित्र] = #strong[अधिमित्र (Great Friend)]
2. #strong[नैसर्गिक मित्र + तात्कालिक सम/शत्रु] = #strong[सम या मित्र]
3. #strong[नैसर्गिक शत्रु + तात्कालिक शत्रु] = #strong[अधिशत्रु (Great Enemy)]
4. #strong[नैसर्गिक सम + तात्कालिक मित्र] = #strong[मित्र]
5. #strong[नैसर्गिक शत्रु + तात्कालिक मित्र] = #strong[सम]
]


#v(0.3cm)
#align(center)[#line(length: 60%, stroke: 0.6pt + rgb("#d97706"))]
#v(0.3cm)

=== 4.3 सूर्य देव का द्वादश भावों में शास्त्रीय फल (Sun Across 12 Houses)

#box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#ffedd5"), stroke: 0.35pt + rgb("#ea580c"))[#image("/assets/images/planets/sun.png", width: 7pt) #h(1pt)#text(fill: rgb("#c2410c"), weight: "bold")[सूर्य]] संपूर्ण सौरमंडल की आत्मा एवं जीवन-ऊर्जा का मूल स्रोत हैं। 12 भावों में #box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#ffedd5"), stroke: 0.35pt + rgb("#ea580c"))[#image("/assets/images/planets/sun.png", width: 7pt) #h(1pt)#text(fill: rgb("#c2410c"), weight: "bold")[सूर्य]] का फल निम्नानुसार है:

1. #strong[प्रथम भाव (तनु):] जातक तेजस्वी, गौरवर्ण, स्वाभिमानी, क्रोधी, नेत्र ज्योति पर प्रभाव, नेतृत्व क्षमता से संपन्न।
2. #strong[द्वितीय भाव (धन):] मुख में तेज, स्पष्ट व कटु वाणी, पैतृक संपत्ति से लाभ अथवा विवाद, नेत्र विकार की संभावना।
3. #strong[तृतीय भाव (सहज):] प्रचंड पराक्रमी, शत्रुओं पर विजय, बंधु-बांधवों में प्रतिष्ठित, लेखन व युद्ध में अजेय।
4. #strong[चतुर्थ भाव (सुख):] मातृ-सुख में कमी, गृह से दूर वास, वाहनों का सुख, सीने में उष्णता या पित्त की अधिकता।
5. #strong[पंचम भाव (पुत्र):] तीक्ष्ण बुद्धि, मंत्र विद्या में सिद्धि, संतान की संख्या सीमित, पाचन तंत्र में पित्त प्रकोप।
6. #strong[षष्ठ भाव (शत्रु):] शत्रुओं का समूल नाश, प्रशासनिक विजय, ऋण से मुक्ति, उत्तम पाचन शक्ति, मामा पक्ष पर प्रभाव।
7. #strong[सप्तम भाव (जाया):] दांपत्य में अहं का टकराव, जीवनसाथी स्वाभिमानी, साझेदारी में सावधान रहने की आवश्यकता।
8. #strong[अष्टम भाव (आयु):] रहस्यमयी ज्ञान, नेत्र विकार की आशंका, गुप्त धन की प्राप्ति, पित्त विकार, दीर्घायु।
9. #strong[नवम भाव (भाग्य):] अत्यंत भाग्यशाली, पिता व #box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#fef3c7"), stroke: 0.35pt + rgb("#f59e0b"))[#image("/assets/images/planets/jupiter.png", width: 7pt) #h(1pt)#text(fill: rgb("#b45309"), weight: "bold")[गुरु]] का भक्त, धार्मिक अनुष्ठानकर्ता, समाज में पूज्य।
10. #strong[दशम भाव (कर्म):] #strong[दिग्बली #box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#ffedd5"), stroke: 0.35pt + rgb("#ea580c"))[#image("/assets/images/planets/sun.png", width: 7pt) #h(1pt)#text(fill: rgb("#c2410c"), weight: "bold")[सूर्य]] (Digbala)]। जातक राजा या सरकार का मुख्य अधिकारी, असीम प्रतिष्ठा, अटूट सत्ता।
11. #strong[एकादश भाव (लाभ):] अपार धन लाभ, #box(baseline: 15%, inset: (x: 1.8pt, y: 0.8pt), radius: 2pt, fill: rgb("#d1fae5"), stroke: 0.35pt + rgb("#10b981"))[#text(fill: rgb("#047857"), weight: "bold", size: 0.85em)[उच्च]] पदाधिकारियों से मित्रता, महत्वाकांक्षाओं की पूर्ण सिद्धि, निरोगी काया।
12. #strong[द्वादश भाव (व्यय):] आध्यात्मिक मुक्ति, विदेश यात्राएं, नेत्र दुर्बलता, अस्पताल या राजकीय व्यय, एकांतप्रियता।




#pagebreak()

= अध्याय 5: आयुर्-ज्योतिष (Medical Astrology) एवं अर्बुद (कैंसर) रोग विश्लेषण
== Chapter 5: Medical Astrology & Oncological Cellular Diagnostics


#rect(
  fill: rgb("#fffdf7"),
  stroke: (left: 3.5pt + rgb("#b45309"), rest: 0.5pt + rgb("#e2e8f0")),
  radius: (right: 4pt),
  width: 100%,
  inset: (x: 12pt, y: 10pt)
)[
  #align(center)[
    #rect(fill: rgb("#fef3c7"), stroke: 0.5pt + rgb("#d97706"), radius: 3pt, inset: (x: 6pt, y: 2pt))[
      #text(size: 8pt, weight: "bold", fill: rgb("#78350f"))[ॐ चरक संहिता — सूत्रस्थान — कर्मज व्याधि विचार]
    ]
  ]
  #v(0.2cm)
  #align(center)[#text(font: ("Noto Serif Devanagari", "Devanagari MT", "Georgia"), size: 10.5pt, weight: "bold", style: "italic", fill: rgb("#451a03"))[कर्मजा व्याधयो ये स्युर्न ते शाम्यन्ति भेषजैः।]]
  #align(center)[#text(font: ("Noto Serif Devanagari", "Devanagari MT", "Georgia"), size: 10.5pt, weight: "bold", style: "italic", fill: rgb("#451a03"))[प्रायश्चित्तैः प्रशाम्यन्ति जपहोमार्चनादिभिः॥]]
]

आयुर्-ज्योतिष (Medical Astrology) चरक, सुश्रुत और पराशर के ज्ञान का दिव्य समन्वय है। रोग केवल जैविक या भौतिक कारणों से ही नहीं होते, अपितु वे पूर्वजन्म-कृत अशुभ कर्मों (कर्मज व्याधि) के परिणाम होते हैं। जब कुण्डली में रोगकारक ग्रह सक्रिय होते हैं, तब शरीर के त्रिदोष (वात, पित्त, कफ) में असंतुलन उत्पन्न होकर असाध्य रोगों का रूप ले लेता है।


#v(0.3cm)
#align(center)[#line(length: 60%, stroke: 0.6pt + rgb("#d97706"))]
#v(0.3cm)

=== 5.1 आयुर्-ज्योतिष अंग एवं ग्रह अधिकार (Anatomical Rulerships)


#align(center)[
  #text(font: ("Noto Sans Devanagari", "Noto Serif Devanagari"), size: 7.5pt)[
    #table(
      columns: (1.1fr, 1.3fr, 1.4fr, 3.2fr),
      fill: (x, y) => if y == 0 { rgb("#fef3c7") } else if calc.odd(y) { rgb("#f8fafc") } else { rgb("#ffffff") },
      stroke: (x, y) => if y == 0 { (bottom: 1.2pt + rgb("#b45309"), rest: 0.4pt + rgb("#cbd5e1")) } else { 0.4pt + rgb("#cbd5e1") },
      inset: (x: 3.8pt, y: 4.5pt),
      align: (x, y) => if y == 0 { center + horizon } else { left + horizon },
      [#text(weight: "bold", fill: rgb("#78350f"))[ग्रह]], [#text(weight: "bold", fill: rgb("#78350f"))[शारीरिक धातु (Dhatu)]], [#text(weight: "bold", fill: rgb("#78350f"))[त्रिदोष प्रकृति]], [#text(weight: "bold", fill: rgb("#78350f"))[प्रभावित अंग एवं अवयव]], [#strong[#box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#ffedd5"), stroke: 0.35pt + rgb("#ea580c"))[#image("/assets/images/planets/sun.png", width: 7pt) #h(1pt)#text(fill: rgb("#c2410c"), weight: "bold")[सूर्य (Sun)]]]], [अस्थि (Bones)], [पित्त (Pitta)], [हृदय, दाहिना नेत्र, मस्तिष्क, जीवन-ऊर्जा (प्राण), रक्तचाप], [#strong[#box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#f1f5f9"), stroke: 0.35pt + rgb("#94a3b8"))[#image("/assets/images/planets/moon.png", width: 7pt) #h(1pt)#text(fill: rgb("#334155"), weight: "bold")[चन्द्र (Moon)]]]], [रस व रक्त द्रव (Plasma/Blood)], [कफ व वात], [फेफड़े, छाती, आमाशय, बायां नेत्र, लिंफेटिक तंत्र, गर्भाशय], [#strong[#box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#fee2e2"), stroke: 0.35pt + rgb("#ef4444"))[#image("/assets/images/planets/mars.png", width: 7pt) #h(1pt)#text(fill: rgb("#dc2626"), weight: "bold")[मंगल (Mars)]]]], [मज्जा व लाल रक्त कण (Bone Marrow/RBC)], [पित्त (Pitta)], [यकृत, पित्ताशय, मांसपेशियां, जननांग, सूजन, विद्रधि], [#strong[#box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#d1fae5"), stroke: 0.35pt + rgb("#10b981"))[#image("/assets/images/planets/mercury.png", width: 7pt) #h(1pt)#text(fill: rgb("#047857"), weight: "bold")[बुध (Mercury)]]]], [त्वचा (Skin)], [त्रिदोष (सम)], [तंत्रिका तंत्र (Nerves), मस्तिष्क के सेरिब्रम, फेफड़े की नलिकाएं], [#strong[#box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#fef3c7"), stroke: 0.35pt + rgb("#f59e0b"))[#image("/assets/images/planets/jupiter.png", width: 7pt) #h(1pt)#text(fill: rgb("#b45309"), weight: "bold")[गुरु (Jupiter)]]]], [वसा (Fat / Adipose Tissue)], [कफ (Kapha)], [यकृत (Liver), धमनियां, कान, अग्न्याशय (Pancreas)], [#strong[#box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#fce7f3"), stroke: 0.35pt + rgb("#f43f5e"))[#image("/assets/images/planets/venus.png", width: 7pt) #h(1pt)#text(fill: rgb("#be185d"), weight: "bold")[शुक्र (Venus)]]]], [#box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#fce7f3"), stroke: 0.35pt + rgb("#f43f5e"))[#image("/assets/images/planets/venus.png", width: 7pt) #h(1pt)#text(fill: rgb("#be185d"), weight: "bold")[शुक्र]] / वीर्य (Semen / Ovaries)], [वात व कफ], [वृक्क (Kidneys), मूत्र मार्ग, प्रजनन ग्रंथियां, हार्मोन संतुलन], [#strong[#box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#dbeafe"), stroke: 0.35pt + rgb("#3b82f6"))[#image("/assets/images/planets/saturn.png", width: 7pt) #h(1pt)#text(fill: rgb("#1d4ed8"), weight: "bold")[शनि (Saturn)]]]], [स्नायु व मांसपेशियां (Tendons/Nerves)], [वात (Vata)], [जोड़, अस्थि-संधि, पैर, बड़ी आंत, दीर्घकालिक क्षय, ट्यूमर], [#strong[#box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#f4f4f5"), stroke: 0.35pt + rgb("#27272a"))[#image("/assets/images/planets/rahu.png", width: 7pt) #h(1pt)#text(fill: rgb("#09090b"), weight: "bold")[राहु (Rahu)]]]], [विषाक्तता (Toxins / Mutagens)], [वात (Vata)], [अनियंत्रित कोशिका विभाजन, ऑटो-इम्यून विकार, रहस्यमयी संक्रमण], [#strong[#box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#f4f4f5"), stroke: 0.35pt + rgb("#71717a"))[#image("/assets/images/planets/ketu.png", width: 7pt) #h(1pt)#text(fill: rgb("#52525b"), weight: "bold")[केतु (Ketu)]]]], [सूक्ष्म नाड़ियां व कोशिकाएं], [पित्त (Pitta)], [शल्य क्रिया, फोड़े, कीटाणु संक्रमण, असाध्य अवरोध]
    )
  ]
]


#v(0.3cm)
#align(center)[#line(length: 60%, stroke: 0.6pt + rgb("#d97706"))]
#v(0.3cm)

=== 5.2 अर्बुद (कैंसर) रोग का ज्योतिषीय सूत्र विश्लेषण (Oncology / Arbuda Roga)


#align(center)[
  #image("assets/icons/medical_astrology_chart.svg", width: 85%)
]
#align(center)[#text(size: 8pt, style: "italic", fill: rgb("#64748b"))[चित्र 5.1: अर्बुद (कैंसर) रोग कारक कुण्डली विन्यास — त्रिक भावों (6, 8, 12) में चन्द्र-राहु एवं शनि-मंगल युति]]

अर्बुद (कैंसर) रोग का मूल कारण कोशिकाओं का अनियंत्रित, अनियोजित एवं आक्रामक रूप से विभाजित होना है। वैदिक ज्योतिष के अनुसार कैंसर का निर्माण किसी एक ग्रह से नहीं, बल्कि एक जटिल ग्रहीय सिंड्रोम से होता है:


#rect(
  fill: rgb("#f8fafc"),
  stroke: (left: 3.5pt + rgb("#334155"), rest: 0.5pt + rgb("#cbd5e1")),
  radius: (right: 4pt),
  width: 100%,
  inset: (x: 12pt, y: 10pt)
)[
  #rect(fill: rgb("#f1f5f9"), stroke: 0.6pt + rgb("#64748b"), radius: 3pt, inset: (x: 6pt, y: 2pt))[
    #text(size: 8pt, weight: "bold", fill: rgb("#1e293b"))[SUTRA • कैंसर निर्माण का चतुर्-सूत्रीय सिद्धांत]
  ]
  #v(0.2cm)
1. #strong[#box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#f4f4f5"), stroke: 0.35pt + rgb("#27272a"))[#image("/assets/images/planets/rahu.png", width: 7pt) #h(1pt)#text(fill: rgb("#09090b"), weight: "bold")[राहु]] की भूमिका:] #box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#f4f4f5"), stroke: 0.35pt + rgb("#27272a"))[#image("/assets/images/planets/rahu.png", width: 7pt) #h(1pt)#text(fill: rgb("#09090b"), weight: "bold")[राहु]] अनियंत्रित विस्तार, धुंधलापन, उत्परिवर्तन (Genetic Mutation) एवं असामान्य कोशिका गुणन का मुख्य अधिपति है।
2. #strong[#box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#dbeafe"), stroke: 0.35pt + rgb("#3b82f6"))[#image("/assets/images/planets/saturn.png", width: 7pt) #h(1pt)#text(fill: rgb("#1d4ed8"), weight: "bold")[शनि]] की भूमिका:] #box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#dbeafe"), stroke: 0.35pt + rgb("#3b82f6"))[#image("/assets/images/planets/saturn.png", width: 7pt) #h(1pt)#text(fill: rgb("#1d4ed8"), weight: "bold")[शनि]] दीर्घकालिक क्षय, रक्त में रुकावट, ऊतकों का सड़ना (Necrosis) और पुरानी गांठों (Tumors) का कारक है।
3. #strong[#box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#f1f5f9"), stroke: 0.35pt + rgb("#94a3b8"))[#image("/assets/images/planets/moon.png", width: 7pt) #h(1pt)#text(fill: rgb("#334155"), weight: "bold")[चन्द्रमा]] एवं #box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#fee2e2"), stroke: 0.35pt + rgb("#ef4444"))[#image("/assets/images/planets/mars.png", width: 7pt) #h(1pt)#text(fill: rgb("#dc2626"), weight: "bold")[मंगल]] का दूषित होना:] #box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#f1f5f9"), stroke: 0.35pt + rgb("#94a3b8"))[#image("/assets/images/planets/moon.png", width: 7pt) #h(1pt)#text(fill: rgb("#334155"), weight: "bold")[चन्द्रमा]] रस/जल का स्वामी है और #box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#fee2e2"), stroke: 0.35pt + rgb("#ef4444"))[#image("/assets/images/planets/mars.png", width: 7pt) #h(1pt)#text(fill: rgb("#dc2626"), weight: "bold")[मंगल]] रक्त व मज्जा का। जब जल और रक्त विषाक्त होते हैं, तब अर्बुद की नींव पड़ती है।
4. #strong[त्रिक भाव (6, 8, 12) एवं लग्न का पीड़ित होना:] 6ठा भाव रोग का, 8वां भाव असाध्य व्याधि का, 12वां भाव शय्याग्रस्त होने का, और लग्न रोग प्रतिरोधक क्षमता का है।
]

==== विभिन्न अंगों के कैंसर के विशिष्ट ग्रहीय योग:


#align(center)[
  #text(font: ("Noto Sans Devanagari", "Noto Serif Devanagari"), size: 7.8pt)[
    #table(
      columns: (1.1fr, 1.4fr, 3.5fr),
      fill: (x, y) => if y == 0 { rgb("#fef3c7") } else if calc.odd(y) { rgb("#f8fafc") } else { rgb("#ffffff") },
      stroke: (x, y) => if y == 0 { (bottom: 1.2pt + rgb("#b45309"), rest: 0.4pt + rgb("#cbd5e1")) } else { 0.4pt + rgb("#cbd5e1") },
      inset: (x: 4.2pt, y: 5.0pt),
      align: (x, y) => if y == 0 { center + horizon } else { left + horizon },
      [#text(weight: "bold", fill: rgb("#78350f"))[कैंसर का प्रकार]], [#text(weight: "bold", fill: rgb("#78350f"))[प्रभावित भाव व ग्रह]], [#text(weight: "bold", fill: rgb("#78350f"))[विशिष्ट शास्त्रीय ग्रहीय युति]], [#strong[रक्त कैंसर (Leukemia)]], [#box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#f1f5f9"), stroke: 0.35pt + rgb("#94a3b8"))[#image("/assets/images/planets/moon.png", width: 7pt) #h(1pt)#text(fill: rgb("#334155"), weight: "bold")[चन्द्रमा]], #box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#fee2e2"), stroke: 0.35pt + rgb("#ef4444"))[#image("/assets/images/planets/mars.png", width: 7pt) #h(1pt)#text(fill: rgb("#dc2626"), weight: "bold")[मंगल]] एवं षष्ठेश], [#box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#f1f5f9"), stroke: 0.35pt + rgb("#94a3b8"))[#image("/assets/images/planets/moon.png", width: 7pt) #h(1pt)#text(fill: rgb("#334155"), weight: "bold")[चन्द्रमा]] और #box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#fee2e2"), stroke: 0.35pt + rgb("#ef4444"))[#image("/assets/images/planets/mars.png", width: 7pt) #h(1pt)#text(fill: rgb("#dc2626"), weight: "bold")[मंगल]] पर #box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#f4f4f5"), stroke: 0.35pt + rgb("#27272a"))[#image("/assets/images/planets/rahu.png", width: 7pt) #h(1pt)#text(fill: rgb("#09090b"), weight: "bold")[राहु]] या #box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#dbeafe"), stroke: 0.35pt + rgb("#3b82f6"))[#image("/assets/images/planets/saturn.png", width: 7pt) #h(1pt)#text(fill: rgb("#1d4ed8"), weight: "bold")[शनि]] की कुदृष्टि, षष्ठ भाव में #box(baseline: 15%, inset: (x: 1.8pt, y: 0.8pt), radius: 2pt, fill: rgb("#fee2e2"), stroke: 0.35pt + rgb("#ef4444"))[#text(fill: rgb("#dc2626"), weight: "bold", size: 0.85em)[नीच]] का #box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#fee2e2"), stroke: 0.35pt + rgb("#ef4444"))[#image("/assets/images/planets/mars.png", width: 7pt) #h(1pt)#text(fill: rgb("#dc2626"), weight: "bold")[मंगल]] #box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#f4f4f5"), stroke: 0.35pt + rgb("#27272a"))[#image("/assets/images/planets/rahu.png", width: 7pt) #h(1pt)#text(fill: rgb("#09090b"), weight: "bold")[राहु]] से युक्त।], [#strong[स्तन एवं फेफड़े का कैंसर]], [चतुर्थ भाव एवं कर्क राशि], [चतुर्थेश का 6ठे या 8वें भाव में #box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#f4f4f5"), stroke: 0.35pt + rgb("#27272a"))[#image("/assets/images/planets/rahu.png", width: 7pt) #h(1pt)#text(fill: rgb("#09090b"), weight: "bold")[राहु]]-#box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#dbeafe"), stroke: 0.35pt + rgb("#3b82f6"))[#image("/assets/images/planets/saturn.png", width: 7pt) #h(1pt)#text(fill: rgb("#1d4ed8"), weight: "bold")[शनि]] से पीड़ित होना, कर्क राशि में पापी ग्रहों का जमावड़ा।], [#strong[मस्तिष्क का अर्बुद (Brain Tumor)]], [प्रथम भाव एवं मेष राशि], [लग्नेश मेष राशि में #box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#f4f4f5"), stroke: 0.35pt + rgb("#27272a"))[#image("/assets/images/planets/rahu.png", width: 7pt) #h(1pt)#text(fill: rgb("#09090b"), weight: "bold")[राहु]]-#box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#f4f4f5"), stroke: 0.35pt + rgb("#71717a"))[#image("/assets/images/planets/ketu.png", width: 7pt) #h(1pt)#text(fill: rgb("#52525b"), weight: "bold")[केतु]] अक्ष पर होकर #box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#dbeafe"), stroke: 0.35pt + rgb("#3b82f6"))[#image("/assets/images/planets/saturn.png", width: 7pt) #h(1pt)#text(fill: rgb("#1d4ed8"), weight: "bold")[शनि]] या वक्री #box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#fee2e2"), stroke: 0.35pt + rgb("#ef4444"))[#image("/assets/images/planets/mars.png", width: 7pt) #h(1pt)#text(fill: rgb("#dc2626"), weight: "bold")[मंगल]] द्वारा देखा जाना।], [#strong[त्वचा का कैंसर (Melanoma)]], [#box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#d1fae5"), stroke: 0.35pt + rgb("#10b981"))[#image("/assets/images/planets/mercury.png", width: 7pt) #h(1pt)#text(fill: rgb("#047857"), weight: "bold")[बुध]], षष्ठ भाव एवं कन्या राशि], [#box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#d1fae5"), stroke: 0.35pt + rgb("#10b981"))[#image("/assets/images/planets/mercury.png", width: 7pt) #h(1pt)#text(fill: rgb("#047857"), weight: "bold")[बुध]] का #box(baseline: 15%, inset: (x: 1.8pt, y: 0.8pt), radius: 2pt, fill: rgb("#fee2e2"), stroke: 0.35pt + rgb("#ef4444"))[#text(fill: rgb("#dc2626"), weight: "bold", size: 0.85em)[नीच]] राशि में #box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#f4f4f5"), stroke: 0.35pt + rgb("#27272a"))[#image("/assets/images/planets/rahu.png", width: 7pt) #h(1pt)#text(fill: rgb("#09090b"), weight: "bold")[राहु]] से युत होकर #box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#ffedd5"), stroke: 0.35pt + rgb("#ea580c"))[#image("/assets/images/planets/sun.png", width: 7pt) #h(1pt)#text(fill: rgb("#c2410c"), weight: "bold")[सूर्य]] द्वारा अत्यधिक दग्ध होना।], [#strong[उदर व आंतों का कैंसर]], [पंचम व षष्ठ भाव], [#box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#fef3c7"), stroke: 0.35pt + rgb("#f59e0b"))[#image("/assets/images/planets/jupiter.png", width: 7pt) #h(1pt)#text(fill: rgb("#b45309"), weight: "bold")[गुरु]] या #box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#d1fae5"), stroke: 0.35pt + rgb("#10b981"))[#image("/assets/images/planets/mercury.png", width: 7pt) #h(1pt)#text(fill: rgb("#047857"), weight: "bold")[बुध]] का #box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#f4f4f5"), stroke: 0.35pt + rgb("#27272a"))[#image("/assets/images/planets/rahu.png", width: 7pt) #h(1pt)#text(fill: rgb("#09090b"), weight: "bold")[राहु]] के साथ षष्ठ भाव में स्थित होकर पाप ग्रहों से पीड़ित होना।]
    )
  ]
]


#v(0.3cm)
#align(center)[#line(length: 60%, stroke: 0.6pt + rgb("#d97706"))]
#v(0.3cm)

=== 5.3 दशा-गोचर प्रकटीकरण एवं ज्योतिषीय निवारण (Timing & Remedies)

कैंसर रोग का प्रकटीकरण तभी होता है जब:
1. जातक की #strong[मारक (2, 7) अथवा त्रिक भावों (6, 8, 12)] के स्वामियों की विंशोत्तरी दशा चल रही हो।
2. गोचर में #box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#f4f4f5"), stroke: 0.35pt + rgb("#27272a"))[#image("/assets/images/planets/rahu.png", width: 7pt) #h(1pt)#text(fill: rgb("#09090b"), weight: "bold")[राहु]] अथवा #box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#dbeafe"), stroke: 0.35pt + rgb("#3b82f6"))[#image("/assets/images/planets/saturn.png", width: 7pt) #h(1pt)#text(fill: rgb("#1d4ed8"), weight: "bold")[शनि]] लग्न, लग्नेश अथवा #box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#f1f5f9"), stroke: 0.35pt + rgb("#94a3b8"))[#image("/assets/images/planets/moon.png", width: 7pt) #h(1pt)#text(fill: rgb("#334155"), weight: "bold")[चन्द्र]] राशि के ऊपर से या अष्टम भाव से भ्रमण कर रहे हों।


#rect(
  fill: rgb("#fff1f2"),
  stroke: (left: 3.5pt + rgb("#dc2626"), rest: 0.5pt + rgb("#fecaca")),
  radius: (right: 4pt),
  width: 100%,
  inset: (x: 12pt, y: 10pt)
)[
  #rect(fill: rgb("#fee2e2"), stroke: 0.6pt + rgb("#ef4444"), radius: 3pt, inset: (x: 6pt, y: 2pt))[
    #text(size: 8pt, weight: "bold", fill: rgb("#991b1b"))[CAVEAT • चिकित्सीय एवं आध्यात्मिक समन्वय]
  ]
  #v(0.2cm)
ज्योतिषीय उपचार कभी भी आधुनिक एलोपैथी, कीमोथेरेपी अथवा शल्य चिकित्सा का विकल्प नहीं है। यह चिकित्सा के साथ-साथ जातक के आत्मबल, आभामंडल (Aura) एवं कर्मज दोषों को शांत करने में सहायक सिद्ध होता है:
1. #strong[महामृत्युंजय मंत्र जप:] सवा लाख महामृत्युंजय मंत्र का संपुटित जप प्राण-शक्ति का संवर्धन करता है।
2. #strong[रुद्राभिषेक अनुष्ठान:] कुशा रस एवं दूर्वा से भगवान शिव का अभिषेक रक्त शोधन में फलदायी है।
3. #strong[दान कर्म:] #box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#dbeafe"), stroke: 0.35pt + rgb("#3b82f6"))[#image("/assets/images/planets/saturn.png", width: 7pt) #h(1pt)#text(fill: rgb("#1d4ed8"), weight: "bold")[शनि]] व #box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#f4f4f5"), stroke: 0.35pt + rgb("#27272a"))[#image("/assets/images/planets/rahu.png", width: 7pt) #h(1pt)#text(fill: rgb("#09090b"), weight: "bold")[राहु]] की शांति हेतु काले तिल, कंबल, नारियल एवं रोगियों को निःशुल्क औषधि दान।
]




#pagebreak()

= अध्याय 6: नक्षत्र पद विभाजन, नवांश गणित एवं मंगल श्लोक
== Chapter 6: Nakshatra Pada Sub-Division, Navamsha & Concluding Shlokas


#rect(
  fill: rgb("#fffdf7"),
  stroke: (left: 3.5pt + rgb("#b45309"), rest: 0.5pt + rgb("#e2e8f0")),
  radius: (right: 4pt),
  width: 100%,
  inset: (x: 12pt, y: 10pt)
)[
  #align(center)[
    #rect(fill: rgb("#fef3c7"), stroke: 0.5pt + rgb("#d97706"), radius: 3pt, inset: (x: 6pt, y: 2pt))[
      #text(size: 8pt, weight: "bold", fill: rgb("#78350f"))[ॐ बृहत्पाराशर होरा शास्त्र — नवांश फल]
    ]
  ]
  #v(0.2cm)
  #align(center)[#text(font: ("Noto Serif Devanagari", "Devanagari MT", "Georgia"), size: 10.5pt, weight: "bold", style: "italic", fill: rgb("#451a03"))[नवांशाद्बलिनो ज्ञेयं कलत्रस्य बलाबलम्।]]
  #align(center)[#text(font: ("Noto Serif Devanagari", "Devanagari MT", "Georgia"), size: 10.5pt, weight: "bold", style: "italic", fill: rgb("#451a03"))[तथैव भाग्यवृद्धिश्च धर्ममार्गरतिस्तथा॥]]
]

कुण्डली का स्थूल शरीर लग्न कुण्डली (D1) है, किंतु उसकी सूक्ष्म आत्मा #strong[नवांश कुण्डली (D9)] है। नवांश का अर्थ है किसी राशि का 9वां भाग (3°20')। चूंकि 27 नक्षत्रों में प्रत्येक के 4 पद होते हैं, अतः संपूर्ण भचक्र में 108 नवांश पद होते हैं। नवांश से जातक के आंतरिक सामर्थ्य, दांपत्य जीवन, भाग्य की वास्तविकता तथा उत्तरार्ध जीवन का सटीक ज्ञान प्राप्त होता है।


#v(0.3cm)
#align(center)[#line(length: 60%, stroke: 0.6pt + rgb("#d97706"))]
#v(0.3cm)

=== 6.1 नवांश पद गणना सिद्धांत (Navamsha Mathematics)

नवांश की गणना राशियों के चर, स्थिर एवं द्विस्वभाव स्वभाव के अनुसार की जाती है:

1. #strong[चर राशियां (मेष, कर्क, तुला, मकर):] नवांश की गणना उसी राशि से प्रारंभ होती है (मेष का प्रथम नवांश मेष से, कर्क का कर्क से)।
2. #strong[स्थिर राशियां (वृषभ, सिंह, वृश्चिक, कुंभ):] नवांश की गणना उस राशि से 9वें स्थान से प्रारंभ होती है (वृषभ का प्रथम नवांश मकर से)।
3. #strong[द्विस्वभाव राशियां (मिथुन, कन्या, धनु, मीन):] नवांश की गणना उस राशि से 5वें स्थान से प्रारंभ होती है (मिथुन का प्रथम नवांश तुला से)।


#rect(
  fill: rgb("#f8fafc"),
  stroke: (left: 3.5pt + rgb("#334155"), rest: 0.5pt + rgb("#cbd5e1")),
  radius: (right: 4pt),
  width: 100%,
  inset: (x: 12pt, y: 10pt)
)[
  #rect(fill: rgb("#f1f5f9"), stroke: 0.6pt + rgb("#64748b"), radius: 3pt, inset: (x: 6pt, y: 2pt))[
    #text(size: 8pt, weight: "bold", fill: rgb("#1e293b"))[SUTRA • वर्गोत्तम नवांश का अमृत नियम]
  ]
  #v(0.2cm)
जब कोई ग्रह लग्न कुण्डली (D1) और नवांश कुण्डली (D9) दोनों में #strong[एक ही राशि] में स्थित होता है, तो वह #strong[वर्गोत्तम (Vargottama)] कहलाता है।
वर्गोत्तम ग्रह अपनी दशा में परम #box(baseline: 15%, inset: (x: 1.8pt, y: 0.8pt), radius: 2pt, fill: rgb("#d1fae5"), stroke: 0.35pt + rgb("#10b981"))[#text(fill: rgb("#047857"), weight: "bold", size: 0.85em)[उच्च]] ग्रह के समान शुभ, स्थायी एवं राजसी फल प्रदान करता है, भले ही वह स्थूल कुण्डली में मित्र या सम राशि में ही क्यों न हो।
]


#v(0.3cm)
#align(center)[#line(length: 60%, stroke: 0.6pt + rgb("#d97706"))]
#v(0.3cm)

=== 6.2 प्रमुख नक्षत्र पदों का सूक्ष्म फलित (Pada Micro-Analysis)

नीचे तीन महत्वपूर्ण नक्षत्रों के पदों का व्यावहारिक फलित दिया गया है:


#align(center)[
  #text(font: ("Noto Sans Devanagari", "Noto Serif Devanagari"), size: 7.5pt)[
    #table(
      columns: (1.1fr, 1.3fr, 1.4fr, 3.2fr),
      fill: (x, y) => if y == 0 { rgb("#fef3c7") } else if calc.odd(y) { rgb("#f8fafc") } else { rgb("#ffffff") },
      stroke: (x, y) => if y == 0 { (bottom: 1.2pt + rgb("#b45309"), rest: 0.4pt + rgb("#cbd5e1")) } else { 0.4pt + rgb("#cbd5e1") },
      inset: (x: 3.8pt, y: 4.5pt),
      align: (x, y) => if y == 0 { center + horizon } else { left + horizon },
      [#text(weight: "bold", fill: rgb("#78350f"))[नक्षत्र]], [#text(weight: "bold", fill: rgb("#78350f"))[पद क्रम]], [#text(weight: "bold", fill: rgb("#78350f"))[नवांश राशि व स्वामी]], [#text(weight: "bold", fill: rgb("#78350f"))[मनोवैज्ञानिक प्रवृत्ति व फलित संकेत]], [#strong[अश्विनी (Ashwini)]], [प्रथम पद (1)], [मेष (#box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#fee2e2"), stroke: 0.35pt + rgb("#ef4444"))[#image("/assets/images/planets/mars.png", width: 7pt) #h(1pt)#text(fill: rgb("#dc2626"), weight: "bold")[मंगल]])], [तीव्र ऊर्जा, साहसी, नेतृत्व क्षमता, त्वरित कार्य सिद्धि, अग्रणी स्वभाव।], [], [द्वितीय पद (2)], [वृषभ (#box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#fce7f3"), stroke: 0.35pt + rgb("#f43f5e"))[#image("/assets/images/planets/venus.png", width: 7pt) #h(1pt)#text(fill: rgb("#be185d"), weight: "bold")[शुक्र]])], [भौतिक स्थिरता, रूपवान, व्यावहारिक ज्ञान, कला व धन संचय की रुचि।], [], [तृतीय पद (3)], [मिथुन (#box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#d1fae5"), stroke: 0.35pt + rgb("#10b981"))[#image("/assets/images/planets/mercury.png", width: 7pt) #h(1pt)#text(fill: rgb("#047857"), weight: "bold")[बुध]])], [बौद्धिक चंचलता, संचार कला, हास्य-विनोद, बहुमुखी प्रतिभा।], [], [चतुर्थ पद (4)], [कर्क (#box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#f1f5f9"), stroke: 0.35pt + rgb("#94a3b8"))[#image("/assets/images/planets/moon.png", width: 7pt) #h(1pt)#text(fill: rgb("#334155"), weight: "bold")[चन्द्रमा]])], [संवेदनशील, दूसरों की सेवा करने वाला, उत्कृष्ट चिकित्सक, भावनात्मक मन।], [#strong[पुष्य (Pushya)]], [प्रथम पद (1)], [सिंह (#box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#ffedd5"), stroke: 0.35pt + rgb("#ea580c"))[#image("/assets/images/planets/sun.png", width: 7pt) #h(1pt)#text(fill: rgb("#c2410c"), weight: "bold")[सूर्य]])], [आध्यात्मिक तेज, पैतृक गौरव, न्यायप्रियता, राजदरबार में सम्मान।], [], [द्वितीय पद (2)], [कन्या (#box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#d1fae5"), stroke: 0.35pt + rgb("#10b981"))[#image("/assets/images/planets/mercury.png", width: 7pt) #h(1pt)#text(fill: rgb("#047857"), weight: "bold")[बुध]])], [सूक्ष्म विश्लेषण, सेवा भाव, व्यावहारिक योजनाकार, संयमित वाणी।], [], [तृतीय पद (3)], [तुला (#box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#fce7f3"), stroke: 0.35pt + rgb("#f43f5e"))[#image("/assets/images/planets/venus.png", width: 7pt) #h(1pt)#text(fill: rgb("#be185d"), weight: "bold")[शुक्र]])], [सामाजिक सौहार्द, सुरुचिपूर्ण जीवन, निष्पक्ष न्याय, व्यापारिक सफलता।], [], [चतुर्थ पद (4)], [वृश्चिक (#box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#fee2e2"), stroke: 0.35pt + rgb("#ef4444"))[#image("/assets/images/planets/mars.png", width: 7pt) #h(1pt)#text(fill: rgb("#dc2626"), weight: "bold")[मंगल]])], [गुप्त साधना, गूढ़ विद्याओं का ज्ञाता, गहन अंतर्दृष्टि, आक्रामक संकल्प।], [#strong[आश्लेषा (Ashlesha)]], [प्रथम पद (1)], [धनु (#box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#fef3c7"), stroke: 0.35pt + rgb("#f59e0b"))[#image("/assets/images/planets/jupiter.png", width: 7pt) #h(1pt)#text(fill: rgb("#b45309"), weight: "bold")[गुरु]])], [दार्शनिक सोच, #box(baseline: 15%, inset: (x: 1.8pt, y: 0.8pt), radius: 2pt, fill: rgb("#d1fae5"), stroke: 0.35pt + rgb("#10b981"))[#text(fill: rgb("#047857"), weight: "bold", size: 0.85em)[उच्च]] आकांक्षाएं, कूटनीति में दक्ष, शास्त्रों का अभ्यासी।], [], [द्वितीय पद (2)], [मकर (#box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#dbeafe"), stroke: 0.35pt + rgb("#3b82f6"))[#image("/assets/images/planets/saturn.png", width: 7pt) #h(1pt)#text(fill: rgb("#1d4ed8"), weight: "bold")[शनि]])], [कठोर परिश्रम, महत्वाकांक्षा, धैर्यपूर्वक लक्ष्य प्राप्ति, स्वार्थ नियंत्रण।], [], [तृतीय पद (3)], [कुंभ (#box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#dbeafe"), stroke: 0.35pt + rgb("#3b82f6"))[#image("/assets/images/planets/saturn.png", width: 7pt) #h(1pt)#text(fill: rgb("#1d4ed8"), weight: "bold")[शनि]])], [गुप्त अनुसंधान, जन-कल्याण, वैज्ञानिक दृष्टिकोण, अलौकिक आकर्षण।], [], [चतुर्थ पद (4)], [मीन (#box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#fef3c7"), stroke: 0.35pt + rgb("#f59e0b"))[#image("/assets/images/planets/jupiter.png", width: 7pt) #h(1pt)#text(fill: rgb("#b45309"), weight: "bold")[गुरु]])], [मोक्ष प्राप्ति की लालसा, मोह-माया से विरक्ति, पूर्ण समर्पण, तांत्रिक अंतःप्रेरणा।]
    )
  ]
]


#v(0.3cm)
#align(center)[#line(length: 60%, stroke: 0.6pt + rgb("#d97706"))]
#v(0.3cm)

=== 6.3 उपनिषद् मंगल कामना एवं शांति पाठ (Universal Benediction)


#rect(
  fill: rgb("#fffdf7"),
  stroke: (left: 3.5pt + rgb("#b45309"), rest: 0.5pt + rgb("#e2e8f0")),
  radius: (right: 4pt),
  width: 100%,
  inset: (x: 12pt, y: 10pt)
)[
  #align(center)[
    #rect(fill: rgb("#fef3c7"), stroke: 0.5pt + rgb("#d97706"), radius: 3pt, inset: (x: 6pt, y: 2pt))[
      #text(size: 8pt, weight: "bold", fill: rgb("#78350f"))[ॐ बृहदारण्यकोपनिषद् — शांति मंत्र]
    ]
  ]
  #v(0.2cm)
  #align(center)[#text(font: ("Noto Serif Devanagari", "Devanagari MT", "Georgia"), size: 10.5pt, weight: "bold", style: "italic", fill: rgb("#451a03"))[ॐ असतो मा सद्गमय।]]
  #align(center)[#text(font: ("Noto Serif Devanagari", "Devanagari MT", "Georgia"), size: 10.5pt, weight: "bold", style: "italic", fill: rgb("#451a03"))[तमसो मा ज्योतिर्गमय।]]
  #align(center)[#text(font: ("Noto Serif Devanagari", "Devanagari MT", "Georgia"), size: 10.5pt, weight: "bold", style: "italic", fill: rgb("#451a03"))[मृत्योर्मा अमृतं गमय॥]]
  #align(center)[#text(font: ("Noto Serif Devanagari", "Devanagari MT", "Georgia"), size: 10.5pt, weight: "bold", style: "italic", fill: rgb("#451a03"))[ॐ शान्तिः शान्तिः शान्तिः॥]]
]

हे परमात्मा! हमें असत्य से सत्य की ओर ले चलो, अंधकार से प्रकाश की ओर ले चलो, और मृत्यु से अमरत्व की ओर ले चलो। तीनों लोकों में दैहिक, दैविक और भौतिक तापों की पूर्ण शांति हो।


#rect(
  fill: rgb("#fffdf7"),
  stroke: (left: 3.5pt + rgb("#b45309"), rest: 0.5pt + rgb("#e2e8f0")),
  radius: (right: 4pt),
  width: 100%,
  inset: (x: 12pt, y: 10pt)
)[
  #align(center)[
    #rect(fill: rgb("#fef3c7"), stroke: 0.5pt + rgb("#d97706"), radius: 3pt, inset: (x: 6pt, y: 2pt))[
      #text(size: 8pt, weight: "bold", fill: rgb("#78350f"))[ॐ स्वस्ति प्रार्थना — लोक कल्याण श्लोक]
    ]
  ]
  #v(0.2cm)
  #align(center)[#text(font: ("Noto Serif Devanagari", "Devanagari MT", "Georgia"), size: 10.5pt, weight: "bold", style: "italic", fill: rgb("#451a03"))[सर्वे भवन्तु सुखिनः सर्वे सन्तु निरामयाः।]]
  #align(center)[#text(font: ("Noto Serif Devanagari", "Devanagari MT", "Georgia"), size: 10.5pt, weight: "bold", style: "italic", fill: rgb("#451a03"))[सर्वे भद्राणि पश्यन्तु मा कश्चिद्दुःखभाग्भवेत्॥]]
]

समस्त प्राणी सुखी हों, सभी रोगमुक्त व स्वस्थ रहें, सभी का कल्याण हो, और इस संसार में किसी को भी लेशमात्र भी दुःख न भोगना पड़े।


#v(0.3cm)
#align(center)[#line(length: 60%, stroke: 0.6pt + rgb("#d97706"))]
#v(0.3cm)

=== 6.4 ग्रंथ समापन एवं कृतज्ञता ज्ञापन (Colophon)

#strong[तंत्र ज्ञान: वैदिक ज्योतिष महाग्रंथ] का यह प्रथम ट्रेड पेपरबैक एवं डिजिटल ग्रंथ संस्करण प्रामाणिक संकलन, शास्त्रीय सूत्रों के अनुसंधान एवं आधुनिक विश्लेषणात्मक प्रारूप के साथ लोक-हितार्थ समर्पित किया जाता है।

- #strong[ग्रंथकार एवं शोधकर्ता:] ज्योतिषाचार्य आशुतोष कुमार चौबे (Ashutosh Kumar Choubey)
- #strong[आधिकारिक अनुसंधान केन्द्र:] तंत्र ज्ञान शोध संस्थान (Tantra Gyan Research Center)
- #strong[वेबसाइट:] [t.worldgyan.com](https://t.worldgyan.com)
- #strong[यूट्यूब शोध मंच:] [\@TantraGyan108](https://www.youtube.com/\@TantraGyan108)
- #strong[ईमेल:] [tantraresearchcenter\@gmail.com](mailto:tantraresearchcenter\@gmail.com)
- #strong[संस्करण वर्ष:] 2026 (Digital & Print Masterwork Edition)




#pagebreak()

= अध्याय 7: चित्रात्मक कुण्डली एटलस — महाभूत, उपचय एवं नक्षत्र मण्डल
== Chapter 7: Visual Kundali Atlas — Elements, Upachaya & Nakshatra Mandala


#rect(
  fill: rgb("#fffdf7"),
  stroke: (left: 3.5pt + rgb("#b45309"), rest: 0.5pt + rgb("#e2e8f0")),
  radius: (right: 4pt),
  width: 100%,
  inset: (x: 12pt, y: 10pt)
)[
  #align(center)[
    #rect(fill: rgb("#fef3c7"), stroke: 0.5pt + rgb("#d97706"), radius: 3pt, inset: (x: 6pt, y: 2pt))[
      #text(size: 8pt, weight: "bold", fill: rgb("#78350f"))[ॐ बृहत्पाराशर होरा शास्त्र — भाव स्वरूप एवं तत्त्व विचार]
    ]
  ]
  #v(0.2cm)
  #align(center)[#text(font: ("Noto Serif Devanagari", "Devanagari MT", "Georgia"), size: 10.5pt, weight: "bold", style: "italic", fill: rgb("#451a03"))[तत्रादौ पञ्चभूतानां पृथिव्यादीनां स्वभावतः।]]
  #align(center)[#text(font: ("Noto Serif Devanagari", "Devanagari MT", "Georgia"), size: 10.5pt, weight: "bold", style: "italic", fill: rgb("#451a03"))[शरीरं सर्वजन्तूनां जायते कालयोगतः॥]]
]

वैदिक ज्योतिष में फलित का आधार केवल गणितीय गणना नहीं, अपितु सम्पूर्ण ब्रह्माण्ड का प्रतीकात्मक ज्यामितीय प्रकटीकरण है। प्राचीन ऋषियों ने कुण्डली के 12 भावों और 27 नक्षत्रों को एक ऐसी ज्यामितीय संरचना (Diamond Chart एवं Circle Wheel) में ढाला है, जो जीवन के समस्त भौतिक, मानसिक एवं आध्यात्मिक आयामों का साक्षात् दर्शन कराती है।

इस अध्याय में सारणियों (Tables) के समस्त गूढ़ सिद्धांतों को 5 प्रमुख पूर्ण-पृष्ठ मास्टर चार्ट्स (Full-Page Vector Charts) के माध्यम से चित्रात्मक रूप में प्रस्तुत किया गया है।


#v(0.3cm)
#align(center)[#line(length: 60%, stroke: 0.6pt + rgb("#d97706"))]
#v(0.3cm)

=== 7.1 चतुर्विध महाभूत कुण्डली चक्र (The Four Elements Diamond Kundali)

सम्पूर्ण 12 भाव चार मूलभूत तत्वों — #strong[अग्नि (Fire), पृथ्वी (Earth), वायु (Air) एवं जल (Water)] में विभक्त हैं, जो पुरुषार्थ चतुष्टय (धर्म, अर्थ, काम, मोक्ष) का संचालन करते हैं:


#align(center)[
  #image("assets/icons/elements_diamond_chart.svg", width: 85%)
]
#align(center)[#text(size: 8pt, style: "italic", fill: rgb("#64748b"))[चित्र 7.1: चतुर्विध महाभूत कुण्डली चक्र (The Four Elements Diamond Kundali) — अग्नि, पृथ्वी, वायु एवं जल तत्वों का संपूर्ण भाव समन्वय]]

==== महाभूत एवं त्रिकोण फलित सारणी का चित्रात्मक विश्लेषण (Elemental Synthesis):

1. #strong[अग्नि तत्व (Fire Element — धर्म त्रिकोण: भाव 1, 5, 9):]
- #strong[भाव 1 (तनु):] मेष राशि का प्राकृतिक वास। जातक का आत्मबल, प्राण-ऊर्जा, नेतृत्व और शारीरिक पराक्रम।
- #strong[भाव 5 (पुत्र/धी):] सिंह राशि का प्राकृतिक वास। पूर्वजन्म के संचित संस्कार, अंतःप्रज्ञा, आध्यात्मिक विवेक और मंत्र सिद्धि।
- #strong[भाव 9 (भाग्य/धर्म):] धनु राशि का प्राकृतिक वास। ईश्वरीय कृपा, #box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#fef3c7"), stroke: 0.35pt + rgb("#f59e0b"))[#image("/assets/images/planets/jupiter.png", width: 7pt) #h(1pt)#text(fill: rgb("#b45309"), weight: "bold")[गुरु]]-आशीर्वाद, जीवन का अंतिम धर्म और परम पुरुषार्थ।
- #emph[ग्रहीय ऊर्जा:] #box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#ffedd5"), stroke: 0.35pt + rgb("#ea580c"))[#image("/assets/images/planets/sun.png", width: 7pt) #h(1pt)#text(fill: rgb("#c2410c"), weight: "bold")[सूर्य]], #box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#fee2e2"), stroke: 0.35pt + rgb("#ef4444"))[#image("/assets/images/planets/mars.png", width: 7pt) #h(1pt)#text(fill: rgb("#dc2626"), weight: "bold")[मंगल]] एवं #box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#fef3c7"), stroke: 0.35pt + rgb("#f59e0b"))[#image("/assets/images/planets/jupiter.png", width: 7pt) #h(1pt)#text(fill: rgb("#b45309"), weight: "bold")[बृहस्पति]] अग्नि तत्व के मुख्य संचालक हैं। जब अग्नि तत्व संतुलित होता है, तो जातक समाज का पथ-प्रदर्शक बनता है।

2. #strong[पृथ्वी तत्व (Earth Element — अर्थ त्रिकोण: भाव 2, 6, 10):]
- #strong[भाव 2 (धन):] वृषभ राशि का प्राकृतिक वास। भौतिक संपदा का संचय, पारिवारिक सुरक्षा और वाणी का प्रभाव।
- #strong[भाव 6 (ऋण/रोग/सेवा):] कन्या राशि का प्राकृतिक वास। दैनिक कार्य, सेवा, अनुशासन, प्रतिस्पर्धा और व्यावहारिक कौशल।
- #strong[भाव 10 (कर्म/साम्राज्य):] मकर राशि का प्राकृतिक वास। सामाजिक प्रतिष्ठा, राज्य सत्ता, करियर की पराकाष्ठा और उत्तरदायित्व।
- #emph[ग्रहीय ऊर्जा:] #box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#fce7f3"), stroke: 0.35pt + rgb("#f43f5e"))[#image("/assets/images/planets/venus.png", width: 7pt) #h(1pt)#text(fill: rgb("#be185d"), weight: "bold")[शुक्र]], #box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#d1fae5"), stroke: 0.35pt + rgb("#10b981"))[#image("/assets/images/planets/mercury.png", width: 7pt) #h(1pt)#text(fill: rgb("#047857"), weight: "bold")[बुध]] एवं #box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#dbeafe"), stroke: 0.35pt + rgb("#3b82f6"))[#image("/assets/images/planets/saturn.png", width: 7pt) #h(1pt)#text(fill: rgb("#1d4ed8"), weight: "bold")[शनि]] पृथ्वी तत्व को भौतिक रूप देते हैं। यह तत्व जातक को यथार्थवादी, परिश्रमी और स्थिर बनाता है।

3. #strong[वायु तत्व (Air Element — काम त्रिकोण: भाव 3, 7, 11):]
- #strong[भाव 3 (सहज):] मिथुन राशि का प्राकृतिक वास। साहस, लेखन, संवाद, मीडिया और बौद्धिक उद्यम।
- #strong[भाव 7 (जाया/व्यापार):] तुला राशि का प्राकृतिक वास। सामाजिक अनुबंध, साझेदारी, लोक-व्यवहार और वैवाहिक संतुलन।
- #strong[भाव 11 (लाभ):] कुंभ राशि का प्राकृतिक वास। जनसंपर्क तंत्र (Networking), दीर्घकालिक लाभ और समस्त इच्छाओं की पूर्ति।
- #emph[ग्रहीय ऊर्जा:] #box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#d1fae5"), stroke: 0.35pt + rgb("#10b981"))[#image("/assets/images/planets/mercury.png", width: 7pt) #h(1pt)#text(fill: rgb("#047857"), weight: "bold")[बुध]], #box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#fce7f3"), stroke: 0.35pt + rgb("#f43f5e"))[#image("/assets/images/planets/venus.png", width: 7pt) #h(1pt)#text(fill: rgb("#be185d"), weight: "bold")[शुक्र]] और #box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#dbeafe"), stroke: 0.35pt + rgb("#3b82f6"))[#image("/assets/images/planets/saturn.png", width: 7pt) #h(1pt)#text(fill: rgb("#1d4ed8"), weight: "bold")[शनि]] वायु तत्व के बौद्धिक प्रेरक हैं। यह तत्व नवीन विचारों और संपर्कों का विस्तार करता है।

4. #strong[जल तत्व (Water Element — मोक्ष त्रिकोण: भाव 4, 8, 12):]
- #strong[भाव 4 (सुख/मन):] कर्क राशि का प्राकृतिक वास। अंतःकरण, मातृ-प्रेम, मानसिक स्थिरता और आत्मिक शांति।
- #strong[भाव 8 (आयु/गूढ़):] वृश्चिक राशि का प्राकृतिक वास। मनोवैज्ञानिक गभीरता, कायाकल्प, गूढ़ तंत्र-विद्या और छिपे सत्य।
- #strong[भाव 12 (मोक्ष/व्यय):] मीन राशि का प्राकृतिक वास। भौतिक विसर्जन, ध्यान, समाधि, विदेश वास और परम मोक्ष।
- #emph[ग्रहीय ऊर्जा:] #box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#f1f5f9"), stroke: 0.35pt + rgb("#94a3b8"))[#image("/assets/images/planets/moon.png", width: 7pt) #h(1pt)#text(fill: rgb("#334155"), weight: "bold")[चन्द्रमा]], #box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#fee2e2"), stroke: 0.35pt + rgb("#ef4444"))[#image("/assets/images/planets/mars.png", width: 7pt) #h(1pt)#text(fill: rgb("#dc2626"), weight: "bold")[मंगल]]/#box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#f4f4f5"), stroke: 0.35pt + rgb("#71717a"))[#image("/assets/images/planets/ketu.png", width: 7pt) #h(1pt)#text(fill: rgb("#52525b"), weight: "bold")[केतु]] एवं #box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#fef3c7"), stroke: 0.35pt + rgb("#f59e0b"))[#image("/assets/images/planets/jupiter.png", width: 7pt) #h(1pt)#text(fill: rgb("#b45309"), weight: "bold")[बृहस्पति]] जल तत्व के भावात्मक नियामक हैं।


#v(0.3cm)
#align(center)[#line(length: 60%, stroke: 0.6pt + rgb("#d97706"))]
#v(0.3cm)

=== 7.2 उपचय भाव साधन एवं सतत वृद्धि चक्र (Upachaya Compounding Mandala)


#rect(
  fill: rgb("#f8fafc"),
  stroke: (left: 3.5pt + rgb("#334155"), rest: 0.5pt + rgb("#cbd5e1")),
  radius: (right: 4pt),
  width: 100%,
  inset: (x: 12pt, y: 10pt)
)[
  #rect(fill: rgb("#f1f5f9"), stroke: 0.6pt + rgb("#64748b"), radius: 3pt, inset: (x: 6pt, y: 2pt))[
    #text(size: 8pt, weight: "bold", fill: rgb("#1e293b"))[SUTRA • महर्षि पराशर उपचय सूत्र]
  ]
  #v(0.2cm)
"त्रिषडायैकादशे क्रूराः शुभाः" — भाव 3, 6, 10 एवं 11 में क्रूर व पापी ग्रह समय के साथ स्वर्ण-तुल्य फल देते हैं।
]

उपचय भाव वे भाव हैं जिनमें जातक की आयु और अनुभव बढ़ने के साथ-साथ फलों में सतत वृद्धि (Compounding) होती है:


#align(center)[
  #image("assets/icons/upachaya_diamond_chart.svg", width: 85%)
]
#align(center)[#text(size: 8pt, style: "italic", fill: rgb("#64748b"))[चित्र 7.2: उपचय भाव साधन चक्र (Upachaya Growth Mandala) — संघर्ष से विजय, आयु सोपान एवं क्रूर ग्रहों का सिद्धि योग]]

==== उपचय सोपान क्रम (The Compounding Stages of Life):
- #strong[भाव 3 (आयु 28+):] पराक्रम और नए उद्यम का समय। जातक पैतृक सीमाओं को तोड़कर अपनी भुजाओं के बल पर आजीविका स्थापित करता है। कारक: #box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#fee2e2"), stroke: 0.35pt + rgb("#ef4444"))[#image("/assets/images/planets/mars.png", width: 7pt) #h(1pt)#text(fill: rgb("#dc2626"), weight: "bold")[मंगल]]।
- #strong[भाव 6 (आयु 32+):] शत्रुओं और बाधाओं के पराभव का समय। षडरिपुओं (काम, क्रोध, मद, लोभ, मोह, मत्सर) पर विजय प्राप्त होती है। कारक: #box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#fee2e2"), stroke: 0.35pt + rgb("#ef4444"))[#image("/assets/images/planets/mars.png", width: 7pt) #h(1pt)#text(fill: rgb("#dc2626"), weight: "bold")[मंगल]] व #box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#dbeafe"), stroke: 0.35pt + rgb("#3b82f6"))[#image("/assets/images/planets/saturn.png", width: 7pt) #h(1pt)#text(fill: rgb("#1d4ed8"), weight: "bold")[शनि]]।
- #strong[भाव 10 (आयु 36+):] राज्य सत्ता और करियर की पराकाष्ठा। समाज में अधिकार और पद-प्रतिष्ठा का चरमोत्कर्ष होता है। कारक: #box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#ffedd5"), stroke: 0.35pt + rgb("#ea580c"))[#image("/assets/images/planets/sun.png", width: 7pt) #h(1pt)#text(fill: rgb("#c2410c"), weight: "bold")[सूर्य]], #box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#d1fae5"), stroke: 0.35pt + rgb("#10b981"))[#image("/assets/images/planets/mercury.png", width: 7pt) #h(1pt)#text(fill: rgb("#047857"), weight: "bold")[बुध]], #box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#dbeafe"), stroke: 0.35pt + rgb("#3b82f6"))[#image("/assets/images/planets/saturn.png", width: 7pt) #h(1pt)#text(fill: rgb("#1d4ed8"), weight: "bold")[शनि]]।
- #strong[भाव 11 (आयु 40+):] सर्व-मनोरथ सिद्धि। पूर्व में किए गए समस्त निवेशों और कर्मों का बहुगुणित लाभ (Compounded Returns) प्राप्त होता है। कारक: #box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#fef3c7"), stroke: 0.35pt + rgb("#f59e0b"))[#image("/assets/images/planets/jupiter.png", width: 7pt) #h(1pt)#text(fill: rgb("#b45309"), weight: "bold")[बृहस्पति]]।


#v(0.3cm)
#align(center)[#line(length: 60%, stroke: 0.6pt + rgb("#d97706"))]
#v(0.3cm)

=== 7.3 लक्ष्मी-नारायण राजयोग एवं केन्द्र-त्रिकोण ज्यामिति (Kendra & Trikona Architecture)


#rect(
  fill: rgb("#fffbeb"),
  stroke: (left: 3.5pt + rgb("#d97706"), rest: 0.5pt + rgb("#fde68a")),
  radius: (right: 4pt),
  width: 100%,
  inset: (x: 12pt, y: 10pt)
)[
  #rect(fill: rgb("#fef3c7"), stroke: 0.6pt + rgb("#ca8a04"), radius: 3pt, inset: (x: 6pt, y: 2pt))[
    #text(size: 8pt, weight: "bold", fill: rgb("#78350f"))[RAJA YOGA • धर्म-कर्माधिपति राजयोग]
  ]
  #v(0.2cm)
केन्द्र भाव (1, 4, 7, 10) साक्षात् भगवान विष्णु के स्वरूप हैं, जो सृष्टि का पालन और कर्म का विस्तार करते हैं।
त्रिकोण भाव (1, 5, 9) देवी महालक्ष्मी के स्वरूप हैं, जो सौभाग्य और दैवीय कृपा का वरदान देती हैं।
]


#align(center)[
  #image("assets/icons/kendra_trikona_diamond_chart.svg", width: 85%)
]
#align(center)[#text(size: 8pt, style: "italic", fill: rgb("#64748b"))[चित्र 7.3: लक्ष्मी-नारायण योग एवं केन्द्र-त्रिकोण ज्यामिति चक्र (Kendra-Trikona Divine Resonance)]]

- #strong[लग्न की अद्वितीय महिमा:] प्रथम भाव (Lagna) केन्द्र और त्रिकोण दोनों की श्रेणी में आने से कुण्डली का सर्वाधिक पवित्र व समर्थ बिंदु है।
- #strong[राजयोग का निर्माण:] जब किसी भी केन्द्रेश (विष्णु) का संबंध किसी भी त्रिकोणेश (लक्ष्मी) से दृष्टि, युति अथवा राशि-परिवर्तन द्वारा बनता है, तब जातक का जीवन साधारण से असाधारण की ओर रूपांतरित हो जाता है।


#v(0.3cm)
#align(center)[#line(length: 60%, stroke: 0.6pt + rgb("#d97706"))]
#v(0.3cm)

=== 7.4 सप्तविंशति नक्षत्र व 108 पद 360° महामण्डल (The 360° Nakshatra & Pada Mandala)

सम्पूर्ण भचक्र (360° Zodiac) 27 नक्षत्रों और 108 पदों में विभाजित है:


#align(center)[
  #image("assets/icons/nakshatra_mandala_wheel.svg", width: 85%)
]
#align(center)[#text(size: 8pt, style: "italic", fill: rgb("#64748b"))[चित्र 7.4: सप्तविंशति नक्षत्र व 108 पद 360° महामण्डल चक्र (The 360° Circular Nakshatra & Pada Wheel)]]

==== गणितीय अनुपात एवं प्रतिशत विभाजन (Mathematical Proportion):
- #strong[सम्पूर्ण भचक्र (Full Circle):] 360° = 100%
- #strong[12 राशियां (12 Rashis):] प्रत्येक राशि 30° = 8.333%
- #strong[27 नक्षत्र (27 Nakshatras):] प्रत्येक नक्षत्र 13°20′ = 3.704%
- #strong[108 पद (108 Padas):] प्रत्येक पद 3°20′ = 0.926%
- #strong[नक्षत्र स्वामी चक्र (3 चक्र):]
1. #emph[प्रथम चक्र (अश्विनी से आश्लेषा):] #box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#f4f4f5"), stroke: 0.35pt + rgb("#71717a"))[#image("/assets/images/planets/ketu.png", width: 7pt) #h(1pt)#text(fill: rgb("#52525b"), weight: "bold")[केतु]] → #box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#fce7f3"), stroke: 0.35pt + rgb("#f43f5e"))[#image("/assets/images/planets/venus.png", width: 7pt) #h(1pt)#text(fill: rgb("#be185d"), weight: "bold")[शुक्र]] → #box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#ffedd5"), stroke: 0.35pt + rgb("#ea580c"))[#image("/assets/images/planets/sun.png", width: 7pt) #h(1pt)#text(fill: rgb("#c2410c"), weight: "bold")[सूर्य]] → #box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#f1f5f9"), stroke: 0.35pt + rgb("#94a3b8"))[#image("/assets/images/planets/moon.png", width: 7pt) #h(1pt)#text(fill: rgb("#334155"), weight: "bold")[चन्द्र]] → #box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#fee2e2"), stroke: 0.35pt + rgb("#ef4444"))[#image("/assets/images/planets/mars.png", width: 7pt) #h(1pt)#text(fill: rgb("#dc2626"), weight: "bold")[मंगल]] → #box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#f4f4f5"), stroke: 0.35pt + rgb("#27272a"))[#image("/assets/images/planets/rahu.png", width: 7pt) #h(1pt)#text(fill: rgb("#09090b"), weight: "bold")[राहु]] → #box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#fef3c7"), stroke: 0.35pt + rgb("#f59e0b"))[#image("/assets/images/planets/jupiter.png", width: 7pt) #h(1pt)#text(fill: rgb("#b45309"), weight: "bold")[गुरु]] → #box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#dbeafe"), stroke: 0.35pt + rgb("#3b82f6"))[#image("/assets/images/planets/saturn.png", width: 7pt) #h(1pt)#text(fill: rgb("#1d4ed8"), weight: "bold")[शनि]] → #box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#d1fae5"), stroke: 0.35pt + rgb("#10b981"))[#image("/assets/images/planets/mercury.png", width: 7pt) #h(1pt)#text(fill: rgb("#047857"), weight: "bold")[बुध]]
2. #emph[द्वितीय चक्र (मघा से ज्येष्ठा):] #box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#f4f4f5"), stroke: 0.35pt + rgb("#71717a"))[#image("/assets/images/planets/ketu.png", width: 7pt) #h(1pt)#text(fill: rgb("#52525b"), weight: "bold")[केतु]] → #box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#fce7f3"), stroke: 0.35pt + rgb("#f43f5e"))[#image("/assets/images/planets/venus.png", width: 7pt) #h(1pt)#text(fill: rgb("#be185d"), weight: "bold")[शुक्र]] → #box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#ffedd5"), stroke: 0.35pt + rgb("#ea580c"))[#image("/assets/images/planets/sun.png", width: 7pt) #h(1pt)#text(fill: rgb("#c2410c"), weight: "bold")[सूर्य]] → #box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#f1f5f9"), stroke: 0.35pt + rgb("#94a3b8"))[#image("/assets/images/planets/moon.png", width: 7pt) #h(1pt)#text(fill: rgb("#334155"), weight: "bold")[चन्द्र]] → #box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#fee2e2"), stroke: 0.35pt + rgb("#ef4444"))[#image("/assets/images/planets/mars.png", width: 7pt) #h(1pt)#text(fill: rgb("#dc2626"), weight: "bold")[मंगल]] → #box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#f4f4f5"), stroke: 0.35pt + rgb("#27272a"))[#image("/assets/images/planets/rahu.png", width: 7pt) #h(1pt)#text(fill: rgb("#09090b"), weight: "bold")[राहु]] → #box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#fef3c7"), stroke: 0.35pt + rgb("#f59e0b"))[#image("/assets/images/planets/jupiter.png", width: 7pt) #h(1pt)#text(fill: rgb("#b45309"), weight: "bold")[गुरु]] → #box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#dbeafe"), stroke: 0.35pt + rgb("#3b82f6"))[#image("/assets/images/planets/saturn.png", width: 7pt) #h(1pt)#text(fill: rgb("#1d4ed8"), weight: "bold")[शनि]] → #box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#d1fae5"), stroke: 0.35pt + rgb("#10b981"))[#image("/assets/images/planets/mercury.png", width: 7pt) #h(1pt)#text(fill: rgb("#047857"), weight: "bold")[बुध]]
3. #emph[तृतीय चक्र (मूल से रेवती):] #box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#f4f4f5"), stroke: 0.35pt + rgb("#71717a"))[#image("/assets/images/planets/ketu.png", width: 7pt) #h(1pt)#text(fill: rgb("#52525b"), weight: "bold")[केतु]] → #box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#fce7f3"), stroke: 0.35pt + rgb("#f43f5e"))[#image("/assets/images/planets/venus.png", width: 7pt) #h(1pt)#text(fill: rgb("#be185d"), weight: "bold")[शुक्र]] → #box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#ffedd5"), stroke: 0.35pt + rgb("#ea580c"))[#image("/assets/images/planets/sun.png", width: 7pt) #h(1pt)#text(fill: rgb("#c2410c"), weight: "bold")[सूर्य]] → #box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#f1f5f9"), stroke: 0.35pt + rgb("#94a3b8"))[#image("/assets/images/planets/moon.png", width: 7pt) #h(1pt)#text(fill: rgb("#334155"), weight: "bold")[चन्द्र]] → #box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#fee2e2"), stroke: 0.35pt + rgb("#ef4444"))[#image("/assets/images/planets/mars.png", width: 7pt) #h(1pt)#text(fill: rgb("#dc2626"), weight: "bold")[मंगल]] → #box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#f4f4f5"), stroke: 0.35pt + rgb("#27272a"))[#image("/assets/images/planets/rahu.png", width: 7pt) #h(1pt)#text(fill: rgb("#09090b"), weight: "bold")[राहु]] → #box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#fef3c7"), stroke: 0.35pt + rgb("#f59e0b"))[#image("/assets/images/planets/jupiter.png", width: 7pt) #h(1pt)#text(fill: rgb("#b45309"), weight: "bold")[गुरु]] → #box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#dbeafe"), stroke: 0.35pt + rgb("#3b82f6"))[#image("/assets/images/planets/saturn.png", width: 7pt) #h(1pt)#text(fill: rgb("#1d4ed8"), weight: "bold")[शनि]] → #box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#d1fae5"), stroke: 0.35pt + rgb("#10b981"))[#image("/assets/images/planets/mercury.png", width: 7pt) #h(1pt)#text(fill: rgb("#047857"), weight: "bold")[बुध]]


#v(0.3cm)
#align(center)[#line(length: 60%, stroke: 0.6pt + rgb("#d97706"))]
#v(0.3cm)

=== 7.5 द्वादश भाव कारकत्व व स्थिर ग्रह चक्र (12 Houses Karakatva Diamond Chart)


#rect(
  fill: rgb("#fff1f2"),
  stroke: (left: 3.5pt + rgb("#dc2626"), rest: 0.5pt + rgb("#fecaca")),
  radius: (right: 4pt),
  width: 100%,
  inset: (x: 12pt, y: 10pt)
)[
  #rect(fill: rgb("#fee2e2"), stroke: 0.6pt + rgb("#ef4444"), radius: 3pt, inset: (x: 6pt, y: 2pt))[
    #text(size: 8pt, weight: "bold", fill: rgb("#991b1b"))[CAVEAT • भावेश बनाम कारक का सिद्धांत]
  ]
  #v(0.2cm)
केवल भावेश का बली होना पर्याप्त नहीं है; यदि भाव का स्थिर कारक ग्रह अस्त, #box(baseline: 15%, inset: (x: 1.8pt, y: 0.8pt), radius: 2pt, fill: rgb("#fee2e2"), stroke: 0.35pt + rgb("#ef4444"))[#text(fill: rgb("#dc2626"), weight: "bold", size: 0.85em)[नीच]] अथवा षष्ठ/अष्टम/द्वादश भाव में पीड़ित हो, तो उस भाव के प्राकृतिक सुखों में बाधा आती है।
]


#align(center)[
  #image("assets/icons/bhava_karaka_diamond_chart.svg", width: 85%)
]
#align(center)[#text(size: 8pt, style: "italic", fill: rgb("#64748b"))[चित्र 7.5: द्वादश भाव कारकत्व व स्थिर ग्रह चक्र (The 12 Houses Karakatva Diamond Chart)]]

- #strong[#box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#ffedd5"), stroke: 0.35pt + rgb("#ea580c"))[#image("/assets/images/planets/sun.png", width: 7pt) #h(1pt)#text(fill: rgb("#c2410c"), weight: "bold")[सूर्य]]:] प्रथम भाव (आत्मबल) एवं दशम भाव (राज्य प्रतिष्ठा) के स्थिर कारक।
- #strong[#box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#fef3c7"), stroke: 0.35pt + rgb("#f59e0b"))[#image("/assets/images/planets/jupiter.png", width: 7pt) #h(1pt)#text(fill: rgb("#b45309"), weight: "bold")[बृहस्पति]] (#box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#fef3c7"), stroke: 0.35pt + rgb("#f59e0b"))[#image("/assets/images/planets/jupiter.png", width: 7pt) #h(1pt)#text(fill: rgb("#b45309"), weight: "bold")[गुरु]]):] द्वितीय (धन), पंचम (संतान/धी), नवम (धर्म/भाग्य) एवं एकादश (लाभ) के सर्वाधिक व्यापक कारक।
- #strong[#box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#fee2e2"), stroke: 0.35pt + rgb("#ef4444"))[#image("/assets/images/planets/mars.png", width: 7pt) #h(1pt)#text(fill: rgb("#dc2626"), weight: "bold")[मंगल]]:] तृतीय (साहस/भ्राता) एवं षष्ठ (शत्रु विजय) के कारक।
- #strong[#box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#fce7f3"), stroke: 0.35pt + rgb("#f43f5e"))[#image("/assets/images/planets/venus.png", width: 7pt) #h(1pt)#text(fill: rgb("#be185d"), weight: "bold")[शुक्र]]:] चतुर्थ (वाहन/ऐश्वर्य) एवं सप्तम (वैवाहिक सुख) के कारक।
- #strong[#box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#dbeafe"), stroke: 0.35pt + rgb("#3b82f6"))[#image("/assets/images/planets/saturn.png", width: 7pt) #h(1pt)#text(fill: rgb("#1d4ed8"), weight: "bold")[शनि]]:] षष्ठ (रोग निवारण), अष्टम (दीर्घायु) एवं द्वादश (मोक्ष) के कारक।



