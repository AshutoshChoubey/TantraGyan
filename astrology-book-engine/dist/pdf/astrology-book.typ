
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
  font: ("Noto Sans Devanagari", "Devanagari MT", "Kohinoor Devanagari", "Georgia", "Palatino"),
  size: 9.0pt,
  lang: "hi"
)

#set par(justify: true, leading: 0.68em)

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
      *उच्च / नीच:* मेष १०° / तुला १०° | *कारकत्व:* आत्मा, पिता, राजसत्ता
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
      *उच्च / नीच:* वृषभ ३° / वृश्चिक ३° | *कारकत्व:* मन, माता, मानसिक शांति
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
      *उच्च / नीच:* मकर २८° / कर्क २८° | *कारकत्व:* पराक्रम, भ्राता, शौर्य
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
      *उच्च / नीच:* कन्या १५° / मीन १५° | *कारकत्व:* बुद्धि, वाणी, व्यापार
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
      *उच्च / नीच:* कर्क ५° / मकर ५° | *कारकत्व:* ज्ञान, धर्म, संतान, विवेक
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
      *उच्च / नीच:* मीन २७° / कन्या २७° | *कारकत्व:* प्रेम, ऐश्वर्य, कला, दांपत्य
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
      *उच्च / नीच:* तुला २०° / मेष २०° | *कारकत्व:* कर्म, न्याय, वैराग्य, दीर्घायु
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

= अध्याय १: वैदिक ज्योतिष आधार, दर्शन एवं भाव कारकत्व
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
  #align(center)[#text(size: 10.5pt, weight: "bold", fill: rgb("#451a03"))[यथा शिखा मयूराणां नागानां मणयो यथा।]]
  #align(center)[#text(size: 10.5pt, weight: "bold", fill: rgb("#451a03"))[तद्वद्वेदांगशास्त्राणां ज्योतिषं मूर्धनि स्थितम्॥]]
]

वैदिक ज्योतिष (Jyotish Shastra) केवल भाग्य बताने का माध्यम नहीं है, अपितु यह काल-विधान, कर्म-सिद्धांत और चेतना के विकास का गूढ़ विज्ञान है। जिस प्रकार मयूरों के सिर पर शिखा और नागों के सिर पर मणि सर्वोच्च स्थान पर सुशोभित होती है, उसी प्रकार समस्त वेदांगों (शिक्षा, कल्प, व्याकरण, निरुक्त, छंद, ज्योतिष) में ज्योतिष शास्त्र को सर्वोच्च "वेद का चक्षु" (Eye of the Veda) कहा गया है।

मानव जीवन में पूर्वजन्म-संचित कर्मों (प्रारब्ध) का प्रकटीकरण जन्म समय के आकाशीय ग्रहीय विन्यास के माध्यम से होता है। लग्न (Ascendant) आत्मा के इस देह में अवतरण का क्षणिक बिंदु है, जहां से संपूर्ण जीवन का खाका १२ भावों में विभाजित हो जाता है।


#v(0.3cm)
#align(center)[#line(length: 60%, stroke: 0.6pt + rgb("#d97706"))]
#v(0.3cm)

=== १.१ कालपुरुष कुण्डली एवं भाव व्यवस्था (The 12 Houses / Bhavas)

जन्म कुण्डली में १२ भाव होते हैं, जो जीवन के समस्त आयामों (शारीरिक, मानसिक, आर्थिक, वैवाहिक, आध्यात्मिक) का संचालन करते हैं। नीचे दिए गए कालपुरुष चक्र में मेष राशि लग्न (प्रथम भाव) में स्थित होकर प्राकृतिक कारकत्व दर्शाती है:


#align(center)[
  #image("assets/icons/lagna_chart.svg", width: 85%)
]
#align(center)[#text(size: 8pt, style: "italic", fill: rgb("#64748b"))[चित्र १.१: कालपुरुष कुण्डली (Kaalpurusha Kundli) — उच्च ग्रह एवं केन्द्र-त्रिकोण भाव विन्यास]]

प्रत्येक भाव का शास्त्रीय नाम, उसका जीवन कारकत्व तथा प्राकृतिक स्वामी ग्रह नीचे दी गई सारणी में स्पष्ट किया गया है:


#align(center)[
  #text(size: 7.2pt)[
    #table(
      columns: (0.9fr, 1.4fr, 1.6fr, 1.3fr, 1.8fr),
      fill: (x, y) => if y == 0 { rgb("#fef3c7") } else if calc.odd(y) { rgb("#f8fafc") } else { rgb("#ffffff") },
      stroke: (x, y) => if y == 0 { (bottom: 1.2pt + rgb("#b45309"), rest: 0.4pt + rgb("#cbd5e1")) } else { 0.4pt + rgb("#cbd5e1") },
      inset: (x: 3.2pt, y: 4.2pt),
      align: (x, y) => if y == 0 { center + horizon } else { left + horizon },
      [#text(weight: "bold", fill: rgb("#78350f"))[भाव क्रम]], [#text(weight: "bold", fill: rgb("#78350f"))[शास्त्रीय नाम]], [#text(weight: "bold", fill: rgb("#78350f"))[मुख्य जीवन कारकत्व (Significations)]], [#text(weight: "bold", fill: rgb("#78350f"))[प्राकृतिक स्वामी]], [#text(weight: "bold", fill: rgb("#78350f"))[श्रेणी]], [#strong[१ (प्रथम)]], [तनु भाव (Lagna)], [देह, वर्ण, रूप, आत्मबल, स्वास्थ्य, दीर्घायु, स्वभाव], [मेष (#box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#fee2e2"), stroke: 0.35pt + rgb("#ef4444"))[#image("/assets/images/planets/mars.png", width: 7pt) #h(1pt)#text(fill: rgb("#dc2626"), weight: "bold")[मंगल]])], [केन्द्र / त्रिकोण], [#strong[२ (द्वितीय)]], [धन भाव (Dhana)], [संचित धन, कुटुंब, वाणी, प्रारंभिक शिक्षा, दाहिनी आँख], [वृषभ (#box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#fce7f3"), stroke: 0.35pt + rgb("#f43f5e"))[#image("/assets/images/planets/venus.png", width: 7pt) #h(1pt)#text(fill: rgb("#be185d"), weight: "bold")[शुक्र]])], [मारक भाव], [#strong[३ (तृतीय)]], [सहज भाव (Sahaja)], [अनुज (छोटे भाई-बहन), पराक्रम, साहस, लेखन, लघु यात्राएं], [मिथुन (#box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#d1fae5"), stroke: 0.35pt + rgb("#10b981"))[#image("/assets/images/planets/mercury.png", width: 7pt) #h(1pt)#text(fill: rgb("#047857"), weight: "bold")[बुध]])], [उपचय भाव], [#strong[४ (चतुर्थ)]], [सुख भाव (Sukha)], [माता, गृह, भूमि, वाहन, अंतःकरण, मानसिक शांति, छाती], [कर्क (#box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#f1f5f9"), stroke: 0.35pt + rgb("#94a3b8"))[#image("/assets/images/planets/moon.png", width: 7pt) #h(1pt)#text(fill: rgb("#334155"), weight: "bold")[चन्द्रमा]])], [केन्द्र भाव], [#strong[५ (पंचम)]], [पुत्र भाव (Putra)], [संतान, पूर्वपुण्य, बुद्धि, मंत्र साधना, #box(baseline: 15%, inset: (x: 1.8pt, y: 0.8pt), radius: 2pt, fill: rgb("#d1fae5"), stroke: 0.35pt + rgb("#10b981"))[#text(fill: rgb("#047857"), weight: "bold", size: 0.85em)[उच्च]] विवेक, प्रेम], [सिंह (#box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#ffedd5"), stroke: 0.35pt + rgb("#ea580c"))[#image("/assets/images/planets/sun.png", width: 7pt) #h(1pt)#text(fill: rgb("#c2410c"), weight: "bold")[सूर्य]])], [त्रिकोण भाव], [#strong[६ (षष्ठ)]], [शत्रु / रोग भाव (Ari)], [रोग, ऋण, शत्रु, प्रतिस्पर्धा, मामा, सेवा, दैनिक कार्य], [कन्या (#box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#d1fae5"), stroke: 0.35pt + rgb("#10b981"))[#image("/assets/images/planets/mercury.png", width: 7pt) #h(1pt)#text(fill: rgb("#047857"), weight: "bold")[बुध]])], [त्रिक / उपचय], [#strong[७ (सप्तम)]], [जाया / कलत्र (Yuvati)], [जीवनसाथी, साझेदारी, व्यापार, विदेश गमन, काम-वासना], [तुला (#box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#fce7f3"), stroke: 0.35pt + rgb("#f43f5e"))[#image("/assets/images/planets/venus.png", width: 7pt) #h(1pt)#text(fill: rgb("#be185d"), weight: "bold")[शुक्र]])], [केन्द्र / मारक], [#strong[८ (अष्टम)]], [आयु / रन्ध्र (Randhra)], [आयु, मृत्यु का कारण, गुप्त विद्याएं, आकस्मिक धन, संकट], [वृश्चिक (#box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#fee2e2"), stroke: 0.35pt + rgb("#ef4444"))[#image("/assets/images/planets/mars.png", width: 7pt) #h(1pt)#text(fill: rgb("#dc2626"), weight: "bold")[मंगल]])], [त्रिक भाव], [#strong[९ (नवम)]], [भाग्य / धर्म (Dharma)], [धर्म, #box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#fef3c7"), stroke: 0.35pt + rgb("#f59e0b"))[#image("/assets/images/planets/jupiter.png", width: 7pt) #h(1pt)#text(fill: rgb("#b45309"), weight: "bold")[गुरु]], पिता, #box(baseline: 15%, inset: (x: 1.8pt, y: 0.8pt), radius: 2pt, fill: rgb("#d1fae5"), stroke: 0.35pt + rgb("#10b981"))[#text(fill: rgb("#047857"), weight: "bold", size: 0.85em)[उच्च]] शिक्षा, तीर्थाटन, ईश्वरीय कृपा], [धनु (#box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#fef3c7"), stroke: 0.35pt + rgb("#f59e0b"))[#image("/assets/images/planets/jupiter.png", width: 7pt) #h(1pt)#text(fill: rgb("#b45309"), weight: "bold")[गुरु]])], [परम त्रिकोण], [#strong[१० (दशम)]], [कर्म भाव (Karma)], [आजीविका, प्रतिष्ठा, राज्य पद, सामाजिक अधिकार, घुटने], [मकर (#box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#dbeafe"), stroke: 0.35pt + rgb("#3b82f6"))[#image("/assets/images/planets/saturn.png", width: 7pt) #h(1pt)#text(fill: rgb("#1d4ed8"), weight: "bold")[शनि]])], [परम केन्द्र], [#strong[११ (एकादश)]], [लाभ भाव (Labha)], [आय, ज्येष्ठ भ्राता, मित्र मंडली, महत्वाकांक्षा पूर्ति], [कुंभ (#box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#dbeafe"), stroke: 0.35pt + rgb("#3b82f6"))[#image("/assets/images/planets/saturn.png", width: 7pt) #h(1pt)#text(fill: rgb("#1d4ed8"), weight: "bold")[शनि]])], [उपचय भाव], [#strong[१२ (द्वादश)]], [व्यय भाव (Vyaya)], [व्यय, मोक्ष, विदेश वास, शयन सुख, अस्पताल, जेल, हानि], [मीन (#box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#fef3c7"), stroke: 0.35pt + rgb("#f59e0b"))[#image("/assets/images/planets/jupiter.png", width: 7pt) #h(1pt)#text(fill: rgb("#b45309"), weight: "bold")[गुरु]])], [त्रिक भाव]
    )
  ]
]


#v(0.3cm)
#align(center)[#line(length: 60%, stroke: 0.6pt + rgb("#d97706"))]
#v(0.3cm)

=== १.२ भावों का शास्त्रीय वर्गीकरण (Functional Classification of Houses)

महर्षि पराशर ने फलित के गहन विश्लेषण हेतु भावों को चार प्रमुख आध्यात्मिक व भौतिक श्रेणियों में विभाजित किया है:


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
केन्द्र भाव (१, ४, ७, १०) भगवान विष्णु के स्वरूप हैं (संरक्षण एवं भौतिक विस्तार)।
त्रिकोण भाव (१, ५, ९) देवी महालक्ष्मी के स्वरूप हैं (सौभाग्य एवं दैवीय कृपा)।
जब केन्द्र और त्रिकोण के स्वामियों का युति, दृष्टि अथवा राशि-परिवर्तन संबंध बनता है, तब प्रबल राजयोग की उत्पत्ति होती है।
]

1. #strong[केन्द्र भाव (१, ४, ७, १०):] कुण्डली के चार मुख्य स्तंभ। ये जातक को भौतिक संसार में शक्ति, स्थिरता एवं सामाजिक संप्रभुता प्रदान करते हैं।
2. #strong[त्रिकोण भाव (१, ५, ९):] सर्वाधिक शुभ एवं सात्विक भाव। नवम भाव परम भाग्य एवं पंचम भाव पूर्वजन्म की संचित मेधा है। प्रथम भाव केन्द्र और त्रिकोण दोनों होने से सर्वोत्कृष्ट है।
3. #strong[उपचय भाव (३, ६, १०, ११):] वृद्धि के भाव। इन भावों में पापी ग्रह (#box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#ffedd5"), stroke: 0.35pt + rgb("#ea580c"))[#image("/assets/images/planets/sun.png", width: 7pt) #h(1pt)#text(fill: rgb("#c2410c"), weight: "bold")[सूर्य]], #box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#fee2e2"), stroke: 0.35pt + rgb("#ef4444"))[#image("/assets/images/planets/mars.png", width: 7pt) #h(1pt)#text(fill: rgb("#dc2626"), weight: "bold")[मंगल]], #box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#dbeafe"), stroke: 0.35pt + rgb("#3b82f6"))[#image("/assets/images/planets/saturn.png", width: 7pt) #h(1pt)#text(fill: rgb("#1d4ed8"), weight: "bold")[शनि]], #box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#f4f4f5"), stroke: 0.35pt + rgb("#27272a"))[#image("/assets/images/planets/rahu.png", width: 7pt) #h(1pt)#text(fill: rgb("#09090b"), weight: "bold")[राहु]]) समय के साथ जातक को संघर्ष के पश्चात विजय और अपार सफलता दिलाते हैं।
4. #strong[त्रिक भाव (६, ८, १२):] कष्ट, विघ्न एवं विसर्जन के भाव। ६ठा भाव रोग व ऋण का है, ८वां भाव मृत्यु व अप्रत्याशित परिवर्तनों का है, और १२वां भाव व्यय व मोक्ष का है।
5. #strong[मारक भाव (२, ७):] जीवन ऊर्जा को सीमित करने वाले भाव। मारक दशा में स्वास्थ्य एवं आयु का विशेष विचार किया जाता है।


#v(0.3cm)
#align(center)[#line(length: 60%, stroke: 0.6pt + rgb("#d97706"))]
#v(0.3cm)

=== १.३ ग्रहों की दृष्टियां (Planetary Aspects / Drishti)

वैदिक ज्योतिष में ग्रह अपने स्थान के अतिरिक्त अन्य भावों को भी पूर्ण दृष्टि से देखते हैं:


#align(center)[
  #image("assets/icons/aspect_wheel.svg", width: 85%)
]
#align(center)[#text(size: 8pt, style: "italic", fill: rgb("#64748b"))[चित्र १.२: ग्रहीय दृष्टि चक्र (Planetary Aspects & Drishti Matrix)]]

- #strong[सर्वग्रह दृष्टि:] समस्त ग्रह अपने स्थित भाव से #strong[७वें भाव] को पूर्ण (१००%) दृष्टि से देखते हैं।
- #strong[#box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#fee2e2"), stroke: 0.35pt + rgb("#ef4444"))[#image("/assets/images/planets/mars.png", width: 7pt) #h(1pt)#text(fill: rgb("#dc2626"), weight: "bold")[मंगल]] की विशेष दृष्टियां:] ७वें भाव के अतिरिक्त #strong[४थे] एवं #strong[८वें] भाव पर पूर्ण दृष्टि।
- #strong[#box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#fef3c7"), stroke: 0.35pt + rgb("#f59e0b"))[#image("/assets/images/planets/jupiter.png", width: 7pt) #h(1pt)#text(fill: rgb("#b45309"), weight: "bold")[बृहस्पति]] (#box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#fef3c7"), stroke: 0.35pt + rgb("#f59e0b"))[#image("/assets/images/planets/jupiter.png", width: 7pt) #h(1pt)#text(fill: rgb("#b45309"), weight: "bold")[गुरु]]), #box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#f4f4f5"), stroke: 0.35pt + rgb("#27272a"))[#image("/assets/images/planets/rahu.png", width: 7pt) #h(1pt)#text(fill: rgb("#09090b"), weight: "bold")[राहु]] एवं #box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#f4f4f5"), stroke: 0.35pt + rgb("#71717a"))[#image("/assets/images/planets/ketu.png", width: 7pt) #h(1pt)#text(fill: rgb("#52525b"), weight: "bold")[केतु]] की विशेष दृष्टियां:] ७वें भाव के अतिरिक्त #strong[५वें] एवं #strong[९वें] भाव पर अमृतमय पूर्ण दृष्टि।
- #strong[#box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#dbeafe"), stroke: 0.35pt + rgb("#3b82f6"))[#image("/assets/images/planets/saturn.png", width: 7pt) #h(1pt)#text(fill: rgb("#1d4ed8"), weight: "bold")[शनि]] की विशेष दृष्टियां:] ७वें भाव के अतिरिक्त #strong[३रे] एवं #strong[१०वें] भाव पर तीक्ष्ण पूर्ण दृष्टि।


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

= अध्याय २: नवग्रह कारकत्व, १७ शास्त्रीय राजयोग एवं पंच महापुरुष
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
  #align(center)[#text(size: 10.5pt, weight: "bold", fill: rgb("#451a03"))[सूर्योऽऽत्मा जगतस्तस्थुषश्चन्द्रमा मन उच्यते।]]
  #align(center)[#text(size: 10.5pt, weight: "bold", fill: rgb("#451a03"))[सत्त्वं कुजः सोमसुतो वाणी वाचस्पतिर्धियम्॥]]
]

नौ आकाशीय शक्तियां (#box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#ffedd5"), stroke: 0.35pt + rgb("#ea580c"))[#image("/assets/images/planets/sun.png", width: 7pt) #h(1pt)#text(fill: rgb("#c2410c"), weight: "bold")[सूर्य]], #box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#f1f5f9"), stroke: 0.35pt + rgb("#94a3b8"))[#image("/assets/images/planets/moon.png", width: 7pt) #h(1pt)#text(fill: rgb("#334155"), weight: "bold")[चन्द्रमा]], #box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#fee2e2"), stroke: 0.35pt + rgb("#ef4444"))[#image("/assets/images/planets/mars.png", width: 7pt) #h(1pt)#text(fill: rgb("#dc2626"), weight: "bold")[मंगल]], #box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#d1fae5"), stroke: 0.35pt + rgb("#10b981"))[#image("/assets/images/planets/mercury.png", width: 7pt) #h(1pt)#text(fill: rgb("#047857"), weight: "bold")[बुध]], #box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#fef3c7"), stroke: 0.35pt + rgb("#f59e0b"))[#image("/assets/images/planets/jupiter.png", width: 7pt) #h(1pt)#text(fill: rgb("#b45309"), weight: "bold")[गुरु]], #box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#fce7f3"), stroke: 0.35pt + rgb("#f43f5e"))[#image("/assets/images/planets/venus.png", width: 7pt) #h(1pt)#text(fill: rgb("#be185d"), weight: "bold")[शुक्र]], #box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#dbeafe"), stroke: 0.35pt + rgb("#3b82f6"))[#image("/assets/images/planets/saturn.png", width: 7pt) #h(1pt)#text(fill: rgb("#1d4ed8"), weight: "bold")[शनि]], #box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#f4f4f5"), stroke: 0.35pt + rgb("#27272a"))[#image("/assets/images/planets/rahu.png", width: 7pt) #h(1pt)#text(fill: rgb("#09090b"), weight: "bold")[राहु]], #box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#f4f4f5"), stroke: 0.35pt + rgb("#71717a"))[#image("/assets/images/planets/ketu.png", width: 7pt) #h(1pt)#text(fill: rgb("#52525b"), weight: "bold")[केतु]]) मानव चेतना, देह, विचार एवं कर्मफलों के प्रतिनिधि हैं। #box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#ffedd5"), stroke: 0.35pt + rgb("#ea580c"))[#image("/assets/images/planets/sun.png", width: 7pt) #h(1pt)#text(fill: rgb("#c2410c"), weight: "bold")[सूर्य]] आत्मा है, #box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#f1f5f9"), stroke: 0.35pt + rgb("#94a3b8"))[#image("/assets/images/planets/moon.png", width: 7pt) #h(1pt)#text(fill: rgb("#334155"), weight: "bold")[चन्द्रमा]] मन है, #box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#fee2e2"), stroke: 0.35pt + rgb("#ef4444"))[#image("/assets/images/planets/mars.png", width: 7pt) #h(1pt)#text(fill: rgb("#dc2626"), weight: "bold")[मंगल]] पराक्रम व रक्त है, #box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#d1fae5"), stroke: 0.35pt + rgb("#10b981"))[#image("/assets/images/planets/mercury.png", width: 7pt) #h(1pt)#text(fill: rgb("#047857"), weight: "bold")[बुध]] वाणी व विवेक है, #box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#fef3c7"), stroke: 0.35pt + rgb("#f59e0b"))[#image("/assets/images/planets/jupiter.png", width: 7pt) #h(1pt)#text(fill: rgb("#b45309"), weight: "bold")[बृहस्पति]] ज्ञान व प्रज्ञा है, #box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#fce7f3"), stroke: 0.35pt + rgb("#f43f5e"))[#image("/assets/images/planets/venus.png", width: 7pt) #h(1pt)#text(fill: rgb("#be185d"), weight: "bold")[शुक्र]] वीर्य व सौंदर्य है, #box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#dbeafe"), stroke: 0.35pt + rgb("#3b82f6"))[#image("/assets/images/planets/saturn.png", width: 7pt) #h(1pt)#text(fill: rgb("#1d4ed8"), weight: "bold")[शनि]] आयु व कर्मदंड है, तथा #box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#f4f4f5"), stroke: 0.35pt + rgb("#27272a"))[#image("/assets/images/planets/rahu.png", width: 7pt) #h(1pt)#text(fill: rgb("#09090b"), weight: "bold")[राहु]] व #box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#f4f4f5"), stroke: 0.35pt + rgb("#71717a"))[#image("/assets/images/planets/ketu.png", width: 7pt) #h(1pt)#text(fill: rgb("#52525b"), weight: "bold")[केतु]] प्रारब्ध के कर्म-बंधन हैं।


#v(0.3cm)
#align(center)[#line(length: 60%, stroke: 0.6pt + rgb("#d97706"))]
#v(0.3cm)

=== २.१ नवग्रह शास्त्रीय कारकत्व सारणी (Navagraha Significator Matrix)

नीचे दी गई सारणी में नवग्रहों के संपूर्ण शास्त्रीय कारकत्व, #box(baseline: 15%, inset: (x: 1.8pt, y: 0.8pt), radius: 2pt, fill: rgb("#d1fae5"), stroke: 0.35pt + rgb("#10b981"))[#text(fill: rgb("#047857"), weight: "bold", size: 0.85em)[उच्च]]-#box(baseline: 15%, inset: (x: 1.8pt, y: 0.8pt), radius: 2pt, fill: rgb("#fee2e2"), stroke: 0.35pt + rgb("#ef4444"))[#text(fill: rgb("#dc2626"), weight: "bold", size: 0.85em)[नीच]] अंश तथा ग्रंथ संदर्भ संकलित किए गए हैं:


#align(center)[
  #text(size: 6.8pt)[
    #table(
      columns: (1.0fr, 1.5fr, 1.5fr, 1.2fr, 1.0fr, 1.0fr, 1.0fr),
      fill: (x, y) => if y == 0 { rgb("#fef3c7") } else if calc.odd(y) { rgb("#f8fafc") } else { rgb("#ffffff") },
      stroke: (x, y) => if y == 0 { (bottom: 1.2pt + rgb("#b45309"), rest: 0.4pt + rgb("#cbd5e1")) } else { 0.4pt + rgb("#cbd5e1") },
      inset: (x: 2.8pt, y: 3.5pt),
      align: (x, y) => if y == 0 { center + horizon } else { left + horizon },
      [#text(weight: "bold", fill: rgb("#78350f"))[ग्रह]], [#text(weight: "bold", fill: rgb("#78350f"))[देह व अवयव]], [#text(weight: "bold", fill: rgb("#78350f"))[स्वभाव व मानसिक वृत्ति]], [#text(weight: "bold", fill: rgb("#78350f"))[संबंध व स्वजन]], [#text(weight: "bold", fill: rgb("#78350f"))[#box(baseline: 15%, inset: (x: 1.8pt, y: 0.8pt), radius: 2pt, fill: rgb("#d1fae5"), stroke: 0.35pt + rgb("#10b981"))[#text(fill: rgb("#047857"), weight: "bold", size: 0.85em)[उच्च]] राशि (अंश)]], [#text(weight: "bold", fill: rgb("#78350f"))[#box(baseline: 15%, inset: (x: 1.8pt, y: 0.8pt), radius: 2pt, fill: rgb("#fee2e2"), stroke: 0.35pt + rgb("#ef4444"))[#text(fill: rgb("#dc2626"), weight: "bold", size: 0.85em)[नीच]] राशि (अंश)]], [#text(weight: "bold", fill: rgb("#78350f"))[#box(baseline: 15%, inset: (x: 1.8pt, y: 0.8pt), radius: 2pt, fill: rgb("#f3e8ff"), stroke: 0.35pt + rgb("#c084fc"))[#text(fill: rgb("#6b21a8"), weight: "bold", size: 0.85em)[मूलत्रिकोण]]]], [#strong[#box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#ffedd5"), stroke: 0.35pt + rgb("#ea580c"))[#image("/assets/images/planets/sun.png", width: 7pt) #h(1pt)#text(fill: rgb("#c2410c"), weight: "bold")[सूर्य (Sun)]]]], [हृदय, अस्थि, नेत्र तेज, प्राण-शक्ति], [आत्मसम्मान, राजसी तेज, नेतृत्व], [पिता, शासक, नरेश], [मेष (१०°)], [तुला (१०°)], [सिंह (०°-२०°)], [#strong[#box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#f1f5f9"), stroke: 0.35pt + rgb("#94a3b8"))[#image("/assets/images/planets/moon.png", width: 7pt) #h(1pt)#text(fill: rgb("#334155"), weight: "bold")[चन्द्र (Moon)]]]], [रक्त संचार, शारीरिक द्रव, आमाशय, मन], [संवेदनशीलता, शांति, कल्पनाशक्ति], [माता, राजसी स्त्रियां], [वृषभ (३°)], [वृश्चिक (३°)], [वृषभ (४°-३०°)], [#strong[#box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#fee2e2"), stroke: 0.35pt + rgb("#ef4444"))[#image("/assets/images/planets/mars.png", width: 7pt) #h(1pt)#text(fill: rgb("#dc2626"), weight: "bold")[मंगल (Mars)]]]], [मज्जा, रक्त कणिकाएं, मांसपेशियां, पित्त], [पराक्रम, क्रोध, त्वरित निर्णय, साहस], [अनुज (छोटा भाई), सेनापति], [मकर (२८°)], [कर्क (२८°)], [मेष (०°-१२°)], [#strong[#box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#d1fae5"), stroke: 0.35pt + rgb("#10b981"))[#image("/assets/images/planets/mercury.png", width: 7pt) #h(1pt)#text(fill: rgb("#047857"), weight: "bold")[बुध (Mercury)]]]], [तंत्रिका तंत्र, त्वचा, वाणी, मस्तिष्क], [तर्क, हास्य-विनोद, व्यापारिक बुद्धि], [मामा, मित्र, बहन, दूत], [कन्या (१५°)], [मीन (१५°)], [कन्या (१६°-२०°)], [#strong[#box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#fef3c7"), stroke: 0.35pt + rgb("#f59e0b"))[#image("/assets/images/planets/jupiter.png", width: 7pt) #h(1pt)#text(fill: rgb("#b45309"), weight: "bold")[गुरु (Jupiter)]]]], [यकृत (लिवर), वसा, कान, धमनियां], [सात्विकता, दया, धर्म-निष्ठा, विवेक], [#box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#fef3c7"), stroke: 0.35pt + rgb("#f59e0b"))[#image("/assets/images/planets/jupiter.png", width: 7pt) #h(1pt)#text(fill: rgb("#b45309"), weight: "bold")[गुरु]], पुत्र, विद्वान, ब्राह्मण], [कर्क (५°)], [मकर (५°)], [धनु (०°-१०°)], [#strong[#box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#fce7f3"), stroke: 0.35pt + rgb("#f43f5e"))[#image("/assets/images/planets/venus.png", width: 7pt) #h(1pt)#text(fill: rgb("#be185d"), weight: "bold")[शुक्र (Venus)]]]], [वीर्य, प्रजनन अंग, सौंदर्य, नेत्र ज्योति], [रसिकता, कला, परिष्कार, ऐश्वर्य], [पत्नी, प्रेमिका, कलाकार], [मीन (२७°)], [कन्या (२७°)], [तुला (०°-१५°)], [#strong[#box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#dbeafe"), stroke: 0.35pt + rgb("#3b82f6"))[#image("/assets/images/planets/saturn.png", width: 7pt) #h(1pt)#text(fill: rgb("#1d4ed8"), weight: "bold")[शनि (Saturn)]]]], [स्नायु, पैर, दांत, अस्थि संधियां (जोड़)], [धैर्य, वैराग्य, अनुशासन, कर्मठता], [सेवक, श्रमिक, वृद्ध जन], [तुला (२०°)], [मेष (२०°)], [कुंभ (०°-२०°)], [#strong[#box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#f4f4f5"), stroke: 0.35pt + rgb("#27272a"))[#image("/assets/images/planets/rahu.png", width: 7pt) #h(1pt)#text(fill: rgb("#09090b"), weight: "bold")[राहु (Rahu)]]]], [श्वसन तंत्र, त्वचा रोग, विषाक्तता], [महत्वाकांक्षा, कूटनीति, विद्रोही भाव], [दादा, विदेशी जन, विधर्मी], [मिथुन / वृषभ], [धनु / वृश्चिक], [कुंभ], [#strong[#box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#f4f4f5"), stroke: 0.35pt + rgb("#71717a"))[#image("/assets/images/planets/ketu.png", width: 7pt) #h(1pt)#text(fill: rgb("#52525b"), weight: "bold")[केतु (Ketu)]]]], [रीढ़, सूक्ष्म नाड़ियां, मोक्ष द्वार], [वैराग्य, अंतर्ज्ञान, मौन, संन्यास], [नाना, तपस्वी, गुप्त शत्रु], [धनु / वृश्चिक], [मिथुन / वृषभ], [मीन]
    )
  ]
]


#v(0.3cm)
#align(center)[#line(length: 60%, stroke: 0.6pt + rgb("#d97706"))]
#v(0.3cm)

=== २.२ १७ शास्त्रीय राजयोग एवं पंच महापुरुष (17 Classical Raja Yogas)

शास्त्रीय ग्रंथों (बृहत्पाराशर, सारावली, फलदीपिका एवं जातक पारिजात) में वर्णित १७ प्रमुख राजयोग जातक को विपुल धन, सामाजिक ख्याति, राज्य सत्ता एवं अखंड अधिकार प्रदान करते हैं:


#align(center)[
  #image("assets/icons/raja_yogas_chart.svg", width: 85%)
]
#align(center)[#text(size: 8pt, style: "italic", fill: rgb("#64748b"))[चित्र २.१: पंच महापुरुष एवं गजकेसरी राजयोग — केन्द्र-त्रिकोण भाव विन्यास (कर्क लग्न)]]

==== १. पंच महापुरुष योग (The 5 Imperial Yogas)
जब भौमादि पांच ग्रह (#box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#fee2e2"), stroke: 0.35pt + rgb("#ef4444"))[#image("/assets/images/planets/mars.png", width: 7pt) #h(1pt)#text(fill: rgb("#dc2626"), weight: "bold")[मंगल]], #box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#d1fae5"), stroke: 0.35pt + rgb("#10b981"))[#image("/assets/images/planets/mercury.png", width: 7pt) #h(1pt)#text(fill: rgb("#047857"), weight: "bold")[बुध]], #box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#fef3c7"), stroke: 0.35pt + rgb("#f59e0b"))[#image("/assets/images/planets/jupiter.png", width: 7pt) #h(1pt)#text(fill: rgb("#b45309"), weight: "bold")[गुरु]], #box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#fce7f3"), stroke: 0.35pt + rgb("#f43f5e"))[#image("/assets/images/planets/venus.png", width: 7pt) #h(1pt)#text(fill: rgb("#be185d"), weight: "bold")[शुक्र]], #box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#dbeafe"), stroke: 0.35pt + rgb("#3b82f6"))[#image("/assets/images/planets/saturn.png", width: 7pt) #h(1pt)#text(fill: rgb("#1d4ed8"), weight: "bold")[शनि]]) अपनी #strong[#box(baseline: 15%, inset: (x: 1.8pt, y: 0.8pt), radius: 2pt, fill: rgb("#fef3c7"), stroke: 0.35pt + rgb("#f59e0b"))[#text(fill: rgb("#b45309"), weight: "bold", size: 0.85em)[स्वराशि]], #box(baseline: 15%, inset: (x: 1.8pt, y: 0.8pt), radius: 2pt, fill: rgb("#f3e8ff"), stroke: 0.35pt + rgb("#c084fc"))[#text(fill: rgb("#6b21a8"), weight: "bold", size: 0.85em)[मूलत्रिकोण]] या #box(baseline: 15%, inset: (x: 1.8pt, y: 0.8pt), radius: 2pt, fill: rgb("#d1fae5"), stroke: 0.35pt + rgb("#10b981"))[#text(fill: rgb("#047857"), weight: "bold", size: 0.85em)[उच्च]] राशि] में होकर #strong[केन्द्र भाव (१, ४, ७, १०)] में स्थित हों:

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
#strong[निर्माण नियम:] जब #box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#fef3c7"), stroke: 0.35pt + rgb("#f59e0b"))[#image("/assets/images/planets/jupiter.png", width: 7pt) #h(1pt)#text(fill: rgb("#b45309"), weight: "bold")[बृहस्पति]] #box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#f1f5f9"), stroke: 0.35pt + rgb("#94a3b8"))[#image("/assets/images/planets/moon.png", width: 7pt) #h(1pt)#text(fill: rgb("#334155"), weight: "bold")[चन्द्रमा]] से केन्द्र भाव (१, ४, ७, १०) में स्थित हो, और पाप ग्रहों से दृष्ट या अस्त न हो।
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
#strong[निर्माण नियम:] #box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#ffedd5"), stroke: 0.35pt + rgb("#ea580c"))[#image("/assets/images/planets/sun.png", width: 7pt) #h(1pt)#text(fill: rgb("#c2410c"), weight: "bold")[सूर्य]] और #box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#d1fae5"), stroke: 0.35pt + rgb("#10b981"))[#image("/assets/images/planets/mercury.png", width: 7pt) #h(1pt)#text(fill: rgb("#047857"), weight: "bold")[बुध]] की किसी शुभ भाव (विशेषकर १, ५, ९, १०, ११) में युति हो, और #box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#d1fae5"), stroke: 0.35pt + rgb("#10b981"))[#image("/assets/images/planets/mercury.png", width: 7pt) #h(1pt)#text(fill: rgb("#047857"), weight: "bold")[बुध]] #box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#ffedd5"), stroke: 0.35pt + rgb("#ea580c"))[#image("/assets/images/planets/sun.png", width: 7pt) #h(1pt)#text(fill: rgb("#c2410c"), weight: "bold")[सूर्य]] के अत्यंत निकट होकर पूर्णतः अस्त न हो।
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
#strong[शास्त्रीय नियम:] #box(baseline: 15%, inset: (x: 1.8pt, y: 0.8pt), radius: 2pt, fill: rgb("#fee2e2"), stroke: 0.35pt + rgb("#ef4444"))[#text(fill: rgb("#dc2626"), weight: "bold", size: 0.85em)[नीच]] राशि में स्थित ग्रह का नीचत्व निम्न ४ नियमों से भंग होता है:
१. #box(baseline: 15%, inset: (x: 1.8pt, y: 0.8pt), radius: 2pt, fill: rgb("#fee2e2"), stroke: 0.35pt + rgb("#ef4444"))[#text(fill: rgb("#dc2626"), weight: "bold", size: 0.85em)[नीच]] ग्रह जिस राशि में बैठा है, उसका स्वामी केन्द्र में हो।
२. #box(baseline: 15%, inset: (x: 1.8pt, y: 0.8pt), radius: 2pt, fill: rgb("#fee2e2"), stroke: 0.35pt + rgb("#ef4444"))[#text(fill: rgb("#dc2626"), weight: "bold", size: 0.85em)[नीच]] ग्रह जिस राशि में #box(baseline: 15%, inset: (x: 1.8pt, y: 0.8pt), radius: 2pt, fill: rgb("#d1fae5"), stroke: 0.35pt + rgb("#10b981"))[#text(fill: rgb("#047857"), weight: "bold", size: 0.85em)[उच्च]] होता है, उसका स्वामी लग्न या #box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#f1f5f9"), stroke: 0.35pt + rgb("#94a3b8"))[#image("/assets/images/planets/moon.png", width: 7pt) #h(1pt)#text(fill: rgb("#334155"), weight: "bold")[चन्द्र]] से केन्द्र में हो।
३. #box(baseline: 15%, inset: (x: 1.8pt, y: 0.8pt), radius: 2pt, fill: rgb("#fee2e2"), stroke: 0.35pt + rgb("#ef4444"))[#text(fill: rgb("#dc2626"), weight: "bold", size: 0.85em)[नीच]] ग्रह पर उसकी #box(baseline: 15%, inset: (x: 1.8pt, y: 0.8pt), radius: 2pt, fill: rgb("#d1fae5"), stroke: 0.35pt + rgb("#10b981"))[#text(fill: rgb("#047857"), weight: "bold", size: 0.85em)[उच्च]] राशि के स्वामी की पूर्ण दृष्टि हो।
४. #box(baseline: 15%, inset: (x: 1.8pt, y: 0.8pt), radius: 2pt, fill: rgb("#fee2e2"), stroke: 0.35pt + rgb("#ef4444"))[#text(fill: rgb("#dc2626"), weight: "bold", size: 0.85em)[नीच]] ग्रह #box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#f1f5f9"), stroke: 0.35pt + rgb("#94a3b8"))[#image("/assets/images/planets/moon.png", width: 7pt) #h(1pt)#text(fill: rgb("#334155"), weight: "bold")[चन्द्र]] लग्न से केन्द्र भाव में स्थित हो।
#strong[फल:] प्रारंभिक जीवन में तीव्र संघर्ष, तत्पश्चात चक्रवर्ती सम्राट या उद्योगपति के समान अप्रत्याशित उत्थान।
]


#v(0.3cm)
#align(center)[#line(length: 60%, stroke: 0.6pt + rgb("#d97706"))]
#v(0.3cm)

=== २.३ विपरीत राजयोग (Viparita Raja Yogas: Harsha, Sarala, Vimala)


#align(center)[
  #image("assets/icons/viparita_chart.svg", width: 85%)
]
#align(center)[#text(size: 8pt, style: "italic", fill: rgb("#64748b"))[चित्र २.२: त्रिक भावों (६, ८, १२) से निर्मित हर्ष, सरल एवं विमल विपरीत राजयोग (तुला लग्न)]]

त्रिक भाव (६, ८, १२) सामान्यतः विनाशकारी माने जाते हैं, किंतु जब इन अशुभ भावों के स्वामी परस्पर केवल त्रिक भावों में ही स्थित हों और किसी शुभ भाव के स्वामी से युत न हों, तो यह "माइनस गुणा माइनस बराबर प्लस" के नियम से प्रचंड राजयोग उत्पन्न करते हैं:


#align(center)[
  #text(size: 7.8pt)[
    #table(
      columns: (1.1fr, 1.4fr, 3.5fr),
      fill: (x, y) => if y == 0 { rgb("#fef3c7") } else if calc.odd(y) { rgb("#f8fafc") } else { rgb("#ffffff") },
      stroke: (x, y) => if y == 0 { (bottom: 1.2pt + rgb("#b45309"), rest: 0.4pt + rgb("#cbd5e1")) } else { 0.4pt + rgb("#cbd5e1") },
      inset: (x: 4.2pt, y: 5.0pt),
      align: (x, y) => if y == 0 { center + horizon } else { left + horizon },
      [#text(weight: "bold", fill: rgb("#78350f"))[विपरीत राजयोग]], [#text(weight: "bold", fill: rgb("#78350f"))[निर्माण नियम (Formation Rule)]], [#text(weight: "bold", fill: rgb("#78350f"))[शास्त्रीय फल (Predictive Outcome)]], [#strong[हर्ष योग (Harsha Yoga)]], [६ठे भाव का स्वामी केवल ६ठे, ८वें या १२वें भाव में स्थित हो।], [शत्रुओं का समूल नाश, अटूट स्वास्थ्य, विपत्तियों में दैवीय रक्षा, न्यायालय में विजय।], [#strong[सरल योग (Sarala Yoga)]], [८वें भाव का स्वामी केवल ६ठे, ८वें या १२वें भाव में स्थित हो।], [जातक निर्भय, दीर्घायु, अकूत गुप्त संपत्ति का स्वामी, संकटों को अवसर में बदलने वाला।], [#strong[विमल योग (Vimala Yoga)]], [१२वें भाव का स्वामी केवल ६ठे, ८वें या १२वें भाव में स्थित हो।], [स्वतंत्र विचार, अपार आध्यात्मिक शांति, न्यूनतम व्यय से महान साम्राज्य की स्थापना।]
    )
  ]
]




#pagebreak()

= अध्याय ३: राशि चक्र, २७ नक्षत्र एवं विंशोत्तरी महादशा
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
  #align(center)[#text(size: 10.5pt, weight: "bold", fill: rgb("#451a03"))[क्षेत्राणि भानि भवनानि च राशयश्च।]]
  #align(center)[#text(size: 10.5pt, weight: "bold", fill: rgb("#451a03"))[मेषादयो नवभिरंघ्रिभिरृक्षमेकम्॥]]
]

आकाश मंडल ३६० अंश (Degrees) का एक पूर्ण वृत्त है, जिसे १२ राशियों (प्रत्येक ३० अंश) तथा २७ नक्षत्रों (प्रत्येक १३ अंश २० कला) में विभाजित किया गया है। प्रत्येक नक्षत्र में ४ चरण या पद होते हैं (प्रत्येक पद ३ अंश २० कला)। संपूर्ण राशि चक्र में कुल १०८ नक्षत्र पद होते हैं (२७ × ४ = १०८), जो भारतीय वैदिक गणित का आधार हैं।


#v(0.3cm)
#align(center)[#line(length: 60%, stroke: 0.6pt + rgb("#d97706"))]
#v(0.3cm)

=== ३.१ द्वादश राशि तत्व एवं गति स्वभाव (12 Zodiac Signs Matrix)


#align(center)[
  #text(size: 7.0pt)[
    #table(
      columns: (0.8fr, 1.2fr, 1.2fr, 1.2fr, 1.4fr, 1.4fr),
      fill: (x, y) => if y == 0 { rgb("#fef3c7") } else if calc.odd(y) { rgb("#f8fafc") } else { rgb("#ffffff") },
      stroke: (x, y) => if y == 0 { (bottom: 1.2pt + rgb("#b45309"), rest: 0.4pt + rgb("#cbd5e1")) } else { 0.4pt + rgb("#cbd5e1") },
      inset: (x: 3.0pt, y: 4.0pt),
      align: (x, y) => if y == 0 { center + horizon } else { left + horizon },
      [#text(weight: "bold", fill: rgb("#78350f"))[राशि क्रम]], [#text(weight: "bold", fill: rgb("#78350f"))[नाम (Sanskrit / English)]], [#text(weight: "bold", fill: rgb("#78350f"))[तत्व (Element)]], [#text(weight: "bold", fill: rgb("#78350f"))[स्वभाव (Modality)]], [#text(weight: "bold", fill: rgb("#78350f"))[स्वामी ग्रह]], [#text(weight: "bold", fill: rgb("#78350f"))[शरीर का अंग]], [#strong[१]], [मेष (Aries)], [अग्नि (Fire)], [चर (Movable)], [#box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#fee2e2"), stroke: 0.35pt + rgb("#ef4444"))[#image("/assets/images/planets/mars.png", width: 7pt) #h(1pt)#text(fill: rgb("#dc2626"), weight: "bold")[मंगल (Mars)]]], [मस्तक, कपाल], [#strong[२]], [वृषभ (Taurus)], [पृथ्वी (Earth)], [स्थिर (Fixed)], [#box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#fce7f3"), stroke: 0.35pt + rgb("#f43f5e"))[#image("/assets/images/planets/venus.png", width: 7pt) #h(1pt)#text(fill: rgb("#be185d"), weight: "bold")[शुक्र (Venus)]]], [मुख, गला, वाणी], [#strong[३]], [मिथुन (Gemini)], [वायु (Air)], [द्विस्वभाव (Dual)], [#box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#d1fae5"), stroke: 0.35pt + rgb("#10b981"))[#image("/assets/images/planets/mercury.png", width: 7pt) #h(1pt)#text(fill: rgb("#047857"), weight: "bold")[बुध (Mercury)]]], [कंधे, हाथ, श्वसन नलिका], [#strong[४]], [कर्क (Cancer)], [जल (Water)], [चर (Movable)], [#box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#f1f5f9"), stroke: 0.35pt + rgb("#94a3b8"))[#image("/assets/images/planets/moon.png", width: 7pt) #h(1pt)#text(fill: rgb("#334155"), weight: "bold")[चन्द्रमा]] (#box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#f1f5f9"), stroke: 0.35pt + rgb("#94a3b8"))[#image("/assets/images/planets/moon.png", width: 7pt) #h(1pt)#text(fill: rgb("#334155"), weight: "bold")[Moon]])], [छाती, स्तन, हृदय], [#strong[५]], [सिंह (Leo)], [अग्नि (Fire)], [स्थिर (Fixed)], [#box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#ffedd5"), stroke: 0.35pt + rgb("#ea580c"))[#image("/assets/images/planets/sun.png", width: 7pt) #h(1pt)#text(fill: rgb("#c2410c"), weight: "bold")[सूर्य (Sun)]]], [पेट, रीढ़ की हड्डी], [#strong[६]], [कन्या (Virgo)], [पृथ्वी (Earth)], [द्विस्वभाव (Dual)], [#box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#d1fae5"), stroke: 0.35pt + rgb("#10b981"))[#image("/assets/images/planets/mercury.png", width: 7pt) #h(1pt)#text(fill: rgb("#047857"), weight: "bold")[बुध (Mercury)]]], [आंतें, कमर, उदर गुहा], [#strong[७]], [तुला (Libra)], [वायु (Air)], [चर (Movable)], [#box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#fce7f3"), stroke: 0.35pt + rgb("#f43f5e"))[#image("/assets/images/planets/venus.png", width: 7pt) #h(1pt)#text(fill: rgb("#be185d"), weight: "bold")[शुक्र (Venus)]]], [गुर्दे (Kidneys), कटि प्रदेश], [#strong[८]], [वृश्चिक (Scorpio)], [जल (Water)], [स्थिर (Fixed)], [#box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#fee2e2"), stroke: 0.35pt + rgb("#ef4444"))[#image("/assets/images/planets/mars.png", width: 7pt) #h(1pt)#text(fill: rgb("#dc2626"), weight: "bold")[मंगल (Mars)]]], [जननांग, गुदा, मूत्राशय], [#strong[९]], [धनु (Sagittarius)], [अग्नि (Fire)], [द्विस्वभाव (Dual)], [#box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#fef3c7"), stroke: 0.35pt + rgb("#f59e0b"))[#image("/assets/images/planets/jupiter.png", width: 7pt) #h(1pt)#text(fill: rgb("#b45309"), weight: "bold")[गुरु (Jupiter)]]], [जंघाएं (Thighs), नितंब], [#strong[१०]], [मकर (Capricorn)], [पृथ्वी (Earth)], [चर (Movable)], [#box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#dbeafe"), stroke: 0.35pt + rgb("#3b82f6"))[#image("/assets/images/planets/saturn.png", width: 7pt) #h(1pt)#text(fill: rgb("#1d4ed8"), weight: "bold")[शनि (Saturn)]]], [घुटने, कंकाल संधि], [#strong[११]], [कुंभ (Aquarius)], [वायु (Air)], [स्थिर (Fixed)], [#box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#dbeafe"), stroke: 0.35pt + rgb("#3b82f6"))[#image("/assets/images/planets/saturn.png", width: 7pt) #h(1pt)#text(fill: rgb("#1d4ed8"), weight: "bold")[शनि (Saturn)]]], [पिंडलियां, टखने], [#strong[१२]], [मीन (Pisces)], [जल (Water)], [द्विस्वभाव (Dual)], [#box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#fef3c7"), stroke: 0.35pt + rgb("#f59e0b"))[#image("/assets/images/planets/jupiter.png", width: 7pt) #h(1pt)#text(fill: rgb("#b45309"), weight: "bold")[गुरु (Jupiter)]]], [पैर के तलवे, अंगूठे]
    )
  ]
]


#v(0.3cm)
#align(center)[#line(length: 60%, stroke: 0.6pt + rgb("#d97706"))]
#v(0.3cm)

=== ३.२ २७ नक्षत्र, उनके स्वामी एवं अधिष्ठाता देवता (The 27 Nakshatras)

प्रत्येक नक्षत्र के स्वामी ग्रह विंशोत्तरी दशा का आरंभ बिंदु निर्धारित करते हैं:


#align(center)[
  #text(size: 7.0pt)[
    #table(
      columns: (0.8fr, 1.2fr, 1.2fr, 1.2fr, 1.4fr, 1.4fr),
      fill: (x, y) => if y == 0 { rgb("#fef3c7") } else if calc.odd(y) { rgb("#f8fafc") } else { rgb("#ffffff") },
      stroke: (x, y) => if y == 0 { (bottom: 1.2pt + rgb("#b45309"), rest: 0.4pt + rgb("#cbd5e1")) } else { 0.4pt + rgb("#cbd5e1") },
      inset: (x: 3.0pt, y: 4.0pt),
      align: (x, y) => if y == 0 { center + horizon } else { left + horizon },
      [#text(weight: "bold", fill: rgb("#78350f"))[नक्षत्र क्रम]], [#text(weight: "bold", fill: rgb("#78350f"))[नक्षत्र नाम]], [#text(weight: "bold", fill: rgb("#78350f"))[विस्तार (Degrees)]], [#text(weight: "bold", fill: rgb("#78350f"))[नक्षत्र स्वामी ग्रह]], [#text(weight: "bold", fill: rgb("#78350f"))[अधिष्ठाता देवता]], [#text(weight: "bold", fill: rgb("#78350f"))[प्रतीक]], [#strong[१]], [अश्विनी (Ashwini)], [०°००' - १३°२०' मेष], [#box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#f4f4f5"), stroke: 0.35pt + rgb("#71717a"))[#image("/assets/images/planets/ketu.png", width: 7pt) #h(1pt)#text(fill: rgb("#52525b"), weight: "bold")[केतु]]], [अश्विनी कुमार (देव-वैद्य)], [अश्व का मुख], [#strong[२]], [भरणी (Bharani)], [१३°२०' - २६°४०' मेष], [#box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#fce7f3"), stroke: 0.35pt + rgb("#f43f5e"))[#image("/assets/images/planets/venus.png", width: 7pt) #h(1pt)#text(fill: rgb("#be185d"), weight: "bold")[शुक्र]]], [यमराज (न्याय व धर्म)], [योनि / त्रिकोण], [#strong[३]], [कृत्तिका (Krittika)], [२६°४०' मेष - १०°००' वृषभ], [#box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#ffedd5"), stroke: 0.35pt + rgb("#ea580c"))[#image("/assets/images/planets/sun.png", width: 7pt) #h(1pt)#text(fill: rgb("#c2410c"), weight: "bold")[सूर्य]]], [अग्नि देव (तेज व शुद्धि)], [उस्तरा / ज्वाला], [#strong[४]], [रोहिणी (Rohini)], [१०°००' - २३°२०' वृषभ], [#box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#f1f5f9"), stroke: 0.35pt + rgb("#94a3b8"))[#image("/assets/images/planets/moon.png", width: 7pt) #h(1pt)#text(fill: rgb("#334155"), weight: "bold")[चन्द्रमा]]], [ब्रह्मा / प्रजापति], [रथ / बैलगाड़ी], [#strong[५]], [मृगशिरा (Mrigashira)], [२३°२०' वृषभ - ६°४०' मिथुन], [#box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#fee2e2"), stroke: 0.35pt + rgb("#ef4444"))[#image("/assets/images/planets/mars.png", width: 7pt) #h(1pt)#text(fill: rgb("#dc2626"), weight: "bold")[मंगल]]], [सोम (अमृत व #box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#f1f5f9"), stroke: 0.35pt + rgb("#94a3b8"))[#image("/assets/images/planets/moon.png", width: 7pt) #h(1pt)#text(fill: rgb("#334155"), weight: "bold")[चन्द्र]])], [हिरण का सिर], [#strong[६]], [आर्द्रा (Ardra)], [६°४०' - २०°००' मिथुन], [#box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#f4f4f5"), stroke: 0.35pt + rgb("#27272a"))[#image("/assets/images/planets/rahu.png", width: 7pt) #h(1pt)#text(fill: rgb("#09090b"), weight: "bold")[राहु]]], [रुद्र (तूफान व प्रलय)], [अश्रु बिंदु / मणि], [#strong[७]], [पुनर्वसु (Punarvasu)], [२०°००' मिथुन - ३°२०' कर्क], [#box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#fef3c7"), stroke: 0.35pt + rgb("#f59e0b"))[#image("/assets/images/planets/jupiter.png", width: 7pt) #h(1pt)#text(fill: rgb("#b45309"), weight: "bold")[गुरु]]], [अदिति (देवमाता)], [बाणों का तरकश], [#strong[८]], [पुष्य (Pushya)], [३°२०' - १६°४०' कर्क], [#box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#dbeafe"), stroke: 0.35pt + rgb("#3b82f6"))[#image("/assets/images/planets/saturn.png", width: 7pt) #h(1pt)#text(fill: rgb("#1d4ed8"), weight: "bold")[शनि]]], [#box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#fef3c7"), stroke: 0.35pt + rgb("#f59e0b"))[#image("/assets/images/planets/jupiter.png", width: 7pt) #h(1pt)#text(fill: rgb("#b45309"), weight: "bold")[बृहस्पति]] (दिव्य ज्ञान)], [गाय का थन / कमल], [#strong[९]], [आश्लेषा (Ashlesha)], [१६°४०' - ३०°००' कर्क], [#box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#d1fae5"), stroke: 0.35pt + rgb("#10b981"))[#image("/assets/images/planets/mercury.png", width: 7pt) #h(1pt)#text(fill: rgb("#047857"), weight: "bold")[बुध]]], [सर्प / नागराज], [कुण्डलित सर्प], [#strong[१०]], [मघा (Magha)], [०°००' - १३°२०' सिंह], [#box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#f4f4f5"), stroke: 0.35pt + rgb("#71717a"))[#image("/assets/images/planets/ketu.png", width: 7pt) #h(1pt)#text(fill: rgb("#52525b"), weight: "bold")[केतु]]], [पितृ गण (पूर्वज)], [राज सिंहासन], [#strong[११]], [पूर्वाफाल्गुनी (Purva Phalguni)], [१३°२०' - २६°४०' सिंह], [#box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#fce7f3"), stroke: 0.35pt + rgb("#f43f5e"))[#image("/assets/images/planets/venus.png", width: 7pt) #h(1pt)#text(fill: rgb("#be185d"), weight: "bold")[शुक्र]]], [भग (ऐश्वर्य व सौभाग्य)], [शय्या (झूला)], [#strong[१२]], [उत्तराफाल्गुनी (Uttara Phalguni)], [२६°४०' सिंह - १०°००' कन्या], [#box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#ffedd5"), stroke: 0.35pt + rgb("#ea580c"))[#image("/assets/images/planets/sun.png", width: 7pt) #h(1pt)#text(fill: rgb("#c2410c"), weight: "bold")[सूर्य]]], [अर्यमा (सत्य व न्याय)], [मंच / शैय्या], [#strong[१३]], [हस्त (Hasta)], [१०°००' - २३°२०' कन्या], [#box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#f1f5f9"), stroke: 0.35pt + rgb("#94a3b8"))[#image("/assets/images/planets/moon.png", width: 7pt) #h(1pt)#text(fill: rgb("#334155"), weight: "bold")[चन्द्रमा]]], [सविता (#box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#ffedd5"), stroke: 0.35pt + rgb("#ea580c"))[#image("/assets/images/planets/sun.png", width: 7pt) #h(1pt)#text(fill: rgb("#c2410c"), weight: "bold")[सूर्य]] की जीवन ऊर्जा)], [खुला हुआ हाथ], [#strong[१४]], [चित्रा (Chitra)], [२३°२०' कन्या - ६°४०' तुला], [#box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#fee2e2"), stroke: 0.35pt + rgb("#ef4444"))[#image("/assets/images/planets/mars.png", width: 7pt) #h(1pt)#text(fill: rgb("#dc2626"), weight: "bold")[मंगल]]], [त्वष्टा / विश्वकर्मा], [चमकीला रत्न], [#strong[१५]], [स्वाति (Swati)], [६°४०' - २०°००' तुला], [#box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#f4f4f5"), stroke: 0.35pt + rgb("#27272a"))[#image("/assets/images/planets/rahu.png", width: 7pt) #h(1pt)#text(fill: rgb("#09090b"), weight: "bold")[राहु]]], [वायु देव (गति व स्वतंत्रता)], [मूंगे का पौधा], [#strong[१६]], [विशाखा (Vishakha)], [२०°००' तुला - ३°२०' वृश्चिक], [#box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#fef3c7"), stroke: 0.35pt + rgb("#f59e0b"))[#image("/assets/images/planets/jupiter.png", width: 7pt) #h(1pt)#text(fill: rgb("#b45309"), weight: "bold")[गुरु]]], [इंद्राग्नि (इंद्र व अग्नि)], [तोरण द्वार], [#strong[१७]], [अनुराधा (Anuradha)], [३°२०' - १६°४०' वृश्चिक], [#box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#dbeafe"), stroke: 0.35pt + rgb("#3b82f6"))[#image("/assets/images/planets/saturn.png", width: 7pt) #h(1pt)#text(fill: rgb("#1d4ed8"), weight: "bold")[शनि]]], [मित्र देव (मैत्री व सहयोग)], [विजय पताका], [#strong[१८]], [ज्येष्ठा (Jyeshtha)], [१६°४०' - ३०°००' वृश्चिक], [#box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#d1fae5"), stroke: 0.35pt + rgb("#10b981"))[#image("/assets/images/planets/mercury.png", width: 7pt) #h(1pt)#text(fill: rgb("#047857"), weight: "bold")[बुध]]], [इंद्र (देवराज)], [कुंडल / छत्र], [#strong[१९]], [मूल (Moola)], [०°००' - १३°२०' धनु], [#box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#f4f4f5"), stroke: 0.35pt + rgb("#71717a"))[#image("/assets/images/planets/ketu.png", width: 7pt) #h(1pt)#text(fill: rgb("#52525b"), weight: "bold")[केतु]]], [निर्ऋति (विनाश व पुनरुत्थान)], [जड़ों का गुच्छा], [#strong[२०]], [पूर्वाषाढ़ा (Purva Ashadha)], [१३°२०' - २६°४०' धनु], [#box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#fce7f3"), stroke: 0.35pt + rgb("#f43f5e"))[#image("/assets/images/planets/venus.png", width: 7pt) #h(1pt)#text(fill: rgb("#be185d"), weight: "bold")[शुक्र]]], [अपः (जल देव)], [पंखा / सूप], [#strong[२१]], [उत्तराषाढ़ा (Uttara Ashadha)], [२६°४०' धनु - १०°००' मकर], [#box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#ffedd5"), stroke: 0.35pt + rgb("#ea580c"))[#image("/assets/images/planets/sun.png", width: 7pt) #h(1pt)#text(fill: rgb("#c2410c"), weight: "bold")[सूर्य]]], [विश्वेदेव (समस्त देवता)], [हाथी का दांत], [#strong[२२]], [श्रवण (Shravana)], [१०°००' - २३°२०' मकर], [#box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#f1f5f9"), stroke: 0.35pt + rgb("#94a3b8"))[#image("/assets/images/planets/moon.png", width: 7pt) #h(1pt)#text(fill: rgb("#334155"), weight: "bold")[चन्द्रमा]]], [भगवान विष्णु (संरक्षक)], [तीन पद / कान], [#strong[२३]], [धनिष्ठा (Dhanishta)], [२३°२०' मकर - ६°४०' कुंभ], [#box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#fee2e2"), stroke: 0.35pt + rgb("#ef4444"))[#image("/assets/images/planets/mars.png", width: 7pt) #h(1pt)#text(fill: rgb("#dc2626"), weight: "bold")[मंगल]]], [अष्ट वसु (भौतिक समृद्धि)], [मृदंग / ढोल], [#strong[२४]], [शतभिषा (Shatabhisha)], [६°४०' - २०°००' कुंभ], [#box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#f4f4f5"), stroke: 0.35pt + rgb("#27272a"))[#image("/assets/images/planets/rahu.png", width: 7pt) #h(1pt)#text(fill: rgb("#09090b"), weight: "bold")[राहु]]], [वरुण (सागर व अंतरिक्ष)], [१०० चिकित्सकों का वृत्त], [#strong[२५]], [पूर्वाभाद्रपद (Purva Bhadrapada)], [२०°००' कुंभ - ३°२०' मीन], [#box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#fef3c7"), stroke: 0.35pt + rgb("#f59e0b"))[#image("/assets/images/planets/jupiter.png", width: 7pt) #h(1pt)#text(fill: rgb("#b45309"), weight: "bold")[गुरु]]], [अज एकपाद (अग्नि नाग)], [तलवार / दो मुख], [#strong[२६]], [उत्तराभाद्रपद (Uttara Bhadrapada)], [३°२०' - १६°४०' मीन], [#box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#dbeafe"), stroke: 0.35pt + rgb("#3b82f6"))[#image("/assets/images/planets/saturn.png", width: 7pt) #h(1pt)#text(fill: rgb("#1d4ed8"), weight: "bold")[शनि]]], [अहिर्बुध्न्य (समुद्री शेषनाग)], [जुड़वां / सर्प], [#strong[२७]], [रेवती (Revati)], [१६°४०' - ३०°००' मीन], [#box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#d1fae5"), stroke: 0.35pt + rgb("#10b981"))[#image("/assets/images/planets/mercury.png", width: 7pt) #h(1pt)#text(fill: rgb("#047857"), weight: "bold")[बुध]]], [पूषा (पोषण व मार्गदर्शक)], [मछली का युगल]
    )
  ]
]


#v(0.3cm)
#align(center)[#line(length: 60%, stroke: 0.6pt + rgb("#d97706"))]
#v(0.3cm)

=== ३.३ १२० वर्षीय विंशोत्तरी महादशा चक्र (120-Year Vimshottari Mahadasha)

वैदिक ज्योतिष में काल-गणना एवं फलित समय-निर्धारण (Timing of Events) का मुख्य आधार #strong[विंशोत्तरी महादशा] है। मानव की पूर्ण आयु १२० वर्ष मानकर इसे ९ ग्रहों में शास्त्रीय अनुपात में बांटा गया है:


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
#box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#f4f4f5"), stroke: 0.35pt + rgb("#71717a"))[#image("/assets/images/planets/ketu.png", width: 7pt) #h(1pt)#text(fill: rgb("#52525b"), weight: "bold")[केतु]] (७ वर्ष) → #box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#fce7f3"), stroke: 0.35pt + rgb("#f43f5e"))[#image("/assets/images/planets/venus.png", width: 7pt) #h(1pt)#text(fill: rgb("#be185d"), weight: "bold")[शुक्र]] (२० वर्ष) → #box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#ffedd5"), stroke: 0.35pt + rgb("#ea580c"))[#image("/assets/images/planets/sun.png", width: 7pt) #h(1pt)#text(fill: rgb("#c2410c"), weight: "bold")[सूर्य]] (६ वर्ष) → #box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#f1f5f9"), stroke: 0.35pt + rgb("#94a3b8"))[#image("/assets/images/planets/moon.png", width: 7pt) #h(1pt)#text(fill: rgb("#334155"), weight: "bold")[चन्द्रमा]] (१० वर्ष) → #box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#fee2e2"), stroke: 0.35pt + rgb("#ef4444"))[#image("/assets/images/planets/mars.png", width: 7pt) #h(1pt)#text(fill: rgb("#dc2626"), weight: "bold")[मंगल]] (७ वर्ष) → #box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#f4f4f5"), stroke: 0.35pt + rgb("#27272a"))[#image("/assets/images/planets/rahu.png", width: 7pt) #h(1pt)#text(fill: rgb("#09090b"), weight: "bold")[राहु]] (१८ वर्ष) → #box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#fef3c7"), stroke: 0.35pt + rgb("#f59e0b"))[#image("/assets/images/planets/jupiter.png", width: 7pt) #h(1pt)#text(fill: rgb("#b45309"), weight: "bold")[गुरु]] (१६ वर्ष) → #box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#dbeafe"), stroke: 0.35pt + rgb("#3b82f6"))[#image("/assets/images/planets/saturn.png", width: 7pt) #h(1pt)#text(fill: rgb("#1d4ed8"), weight: "bold")[शनि]] (१९ वर्ष) → #box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#d1fae5"), stroke: 0.35pt + rgb("#10b981"))[#image("/assets/images/planets/mercury.png", width: 7pt) #h(1pt)#text(fill: rgb("#047857"), weight: "bold")[बुध]] (१७ वर्ष)
कुल योग = १२० वर्ष
]


#align(center)[
  #text(size: 7.5pt)[
    #table(
      columns: (1.1fr, 1.3fr, 1.4fr, 3.2fr),
      fill: (x, y) => if y == 0 { rgb("#fef3c7") } else if calc.odd(y) { rgb("#f8fafc") } else { rgb("#ffffff") },
      stroke: (x, y) => if y == 0 { (bottom: 1.2pt + rgb("#b45309"), rest: 0.4pt + rgb("#cbd5e1")) } else { 0.4pt + rgb("#cbd5e1") },
      inset: (x: 3.8pt, y: 4.5pt),
      align: (x, y) => if y == 0 { center + horizon } else { left + horizon },
      [#text(weight: "bold", fill: rgb("#78350f"))[दशा क्रम]], [#text(weight: "bold", fill: rgb("#78350f"))[ग्रह]], [#text(weight: "bold", fill: rgb("#78350f"))[महादशा अवधि (वर्ष)]], [#text(weight: "bold", fill: rgb("#78350f"))[मुख्य प्रभाव एवं फलित दृष्टिकोण]], [#strong[१]], [#box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#f4f4f5"), stroke: 0.35pt + rgb("#71717a"))[#image("/assets/images/planets/ketu.png", width: 7pt) #h(1pt)#text(fill: rgb("#52525b"), weight: "bold")[केतु (Ketu)]]], [#strong[७ वर्ष]], [आध्यात्मिक उन्मेष, भौतिक विरक्ति, आकस्मिक परिवर्तन, गुप्त विद्याओं की ओर झुकाव], [#strong[२]], [#box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#fce7f3"), stroke: 0.35pt + rgb("#f43f5e"))[#image("/assets/images/planets/venus.png", width: 7pt) #h(1pt)#text(fill: rgb("#be185d"), weight: "bold")[शुक्र (Venus)]]], [#strong[२० वर्ष]], [भौतिक ऐश्वर्य, विवाह, वाहन, सौंदर्य, कला, व्यापारिक विस्तार, विलास], [#strong[३]], [#box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#ffedd5"), stroke: 0.35pt + rgb("#ea580c"))[#image("/assets/images/planets/sun.png", width: 7pt) #h(1pt)#text(fill: rgb("#c2410c"), weight: "bold")[सूर्य (Sun)]]], [#strong[६ वर्ष]], [आत्मबल, प्रशासनिक अधिकार, सरकारी सम्मान, पिता का सहयोग, नेत्र व स्वास्थ्य विचार], [#strong[४]], [#box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#f1f5f9"), stroke: 0.35pt + rgb("#94a3b8"))[#image("/assets/images/planets/moon.png", width: 7pt) #h(1pt)#text(fill: rgb("#334155"), weight: "bold")[चन्द्र (Moon)]]], [#strong[१० वर्ष]], [मानसिक शांति, माता का सुख, यात्राएं, कल्पनाशक्ति, जन-समर्थन, रचनात्मकता], [#strong[५]], [#box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#fee2e2"), stroke: 0.35pt + rgb("#ef4444"))[#image("/assets/images/planets/mars.png", width: 7pt) #h(1pt)#text(fill: rgb("#dc2626"), weight: "bold")[मंगल (Mars)]]], [#strong[७ वर्ष]], [साहस, भूमि क्रय-विक्रय, रक्त व मज्जा की सक्रियता, तकनीकी कार्य, विवाद अथवा विजय], [#strong[६]], [#box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#f4f4f5"), stroke: 0.35pt + rgb("#27272a"))[#image("/assets/images/planets/rahu.png", width: 7pt) #h(1pt)#text(fill: rgb("#09090b"), weight: "bold")[राहु (Rahu)]]], [#strong[१८ वर्ष]], [तीव्र महत्वाकांक्षा, विदेशी यात्राएं, अकूत धनार्जन, अप्रत्याशित उत्थान-पतन, कूटनीति], [#strong[७]], [#box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#fef3c7"), stroke: 0.35pt + rgb("#f59e0b"))[#image("/assets/images/planets/jupiter.png", width: 7pt) #h(1pt)#text(fill: rgb("#b45309"), weight: "bold")[गुरु (Jupiter)]]], [#strong[१६ वर्ष]], [ज्ञान, संतान प्राप्ति, धर्मानुष्ठान, #box(baseline: 15%, inset: (x: 1.8pt, y: 0.8pt), radius: 2pt, fill: rgb("#d1fae5"), stroke: 0.35pt + rgb("#10b981"))[#text(fill: rgb("#047857"), weight: "bold", size: 0.85em)[उच्च]] पद, #box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#fef3c7"), stroke: 0.35pt + rgb("#f59e0b"))[#image("/assets/images/planets/jupiter.png", width: 7pt) #h(1pt)#text(fill: rgb("#b45309"), weight: "bold")[गुरु]] कृपा, विवेक एवं आर्थिक स्थिरता], [#strong[८]], [#box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#dbeafe"), stroke: 0.35pt + rgb("#3b82f6"))[#image("/assets/images/planets/saturn.png", width: 7pt) #h(1pt)#text(fill: rgb("#1d4ed8"), weight: "bold")[शनि (Saturn)]]], [#strong[१९ वर्ष]], [कठोर परिश्रम, अनुशासन, कर्मफल भुगतान, जन-सामान्य से जुड़ाव, दीर्घकालिक सफलता], [#strong[९]], [#box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#d1fae5"), stroke: 0.35pt + rgb("#10b981"))[#image("/assets/images/planets/mercury.png", width: 7pt) #h(1pt)#text(fill: rgb("#047857"), weight: "bold")[बुध (Mercury)]]], [#strong[१७ वर्ष]], [व्यापारिक उन्नति, संचार, लेखा, लेखन, तार्किक विवेक, बौद्धिक शिखर]
    )
  ]
]




#pagebreak()

= अध्याय ४: दीप्तादि ९ अवस्थाएं एवं भावों में सूर्य फल
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
  #align(center)[#text(size: 10.5pt, weight: "bold", fill: rgb("#451a03"))[दीप्तः स्वोच्चे स्वस्थः स्वगृहे मुदितोऽधिमित्रे शान्तः सुहृदि।]]
  #align(center)[#text(size: 10.5pt, weight: "bold", fill: rgb("#451a03"))[दीनोऽसमर्थशत्रौ दुःखी विकलः खलोऽधमे कोपो रणे॥]]
]

कुण्डली में किसी ग्रह का केवल शुभ भाव में बैठना ही पर्याप्त नहीं होता, अपितु यह देखना अनिवार्य है कि वह ग्रह चेतना के किस स्तर पर कार्य कर रहा है। महर्षि पराशर एवं कल्याण वर्मा ने ग्रहों की #strong[९ दीप्तादि अवस्थाओं] का प्रतिपादन किया है, जो ग्रह के वास्तविक शुभाशुभ फल की तीव्रता और गुणवत्ता निर्धारित करती हैं।


#v(0.3cm)
#align(center)[#line(length: 60%, stroke: 0.6pt + rgb("#d97706"))]
#v(0.3cm)

=== ४.१ ग्रहों की दीप्तादि ९ अवस्थाएं (Deeptadi 9 Planetary Dignities)


#align(center)[
  #text(size: 7.2pt)[
    #table(
      columns: (0.9fr, 1.4fr, 1.6fr, 1.3fr, 1.8fr),
      fill: (x, y) => if y == 0 { rgb("#fef3c7") } else if calc.odd(y) { rgb("#f8fafc") } else { rgb("#ffffff") },
      stroke: (x, y) => if y == 0 { (bottom: 1.2pt + rgb("#b45309"), rest: 0.4pt + rgb("#cbd5e1")) } else { 0.4pt + rgb("#cbd5e1") },
      inset: (x: 3.2pt, y: 4.2pt),
      align: (x, y) => if y == 0 { center + horizon } else { left + horizon },
      [#text(weight: "bold", fill: rgb("#78350f"))[अवस्था क्रम]], [#text(weight: "bold", fill: rgb("#78350f"))[अवस्था नाम]], [#text(weight: "bold", fill: rgb("#78350f"))[स्थिति एवं खगोलीय मर्यादा (Astronomical Position)]], [#text(weight: "bold", fill: rgb("#78350f"))[फल की तीव्रता (Potency)]], [#text(weight: "bold", fill: rgb("#78350f"))[वास्तविक जीवन प्रभाव (Life Manifestation)]], [#strong[१]], [#strong[दीप्त (Deepta)]], [ग्रह अपनी परम #box(baseline: 15%, inset: (x: 1.8pt, y: 0.8pt), radius: 2pt, fill: rgb("#d1fae5"), stroke: 0.35pt + rgb("#10b981"))[#text(fill: rgb("#047857"), weight: "bold", size: 0.85em)[उच्च]] राशि (Exaltation) में स्थित हो।], [१००% पूर्ण शुभ फल], [राज्य सम्मान, अदम्य आत्मविश्वास, सार्वभौम कीर्ति, विपुल ऐश्वर्य।], [#strong[२]], [#strong[स्वस्थ (Swastha)]], [ग्रह अपनी #box(baseline: 15%, inset: (x: 1.8pt, y: 0.8pt), radius: 2pt, fill: rgb("#fef3c7"), stroke: 0.35pt + rgb("#f59e0b"))[#text(fill: rgb("#b45309"), weight: "bold", size: 0.85em)[स्वराशि]] (Own Sign) या #box(baseline: 15%, inset: (x: 1.8pt, y: 0.8pt), radius: 2pt, fill: rgb("#f3e8ff"), stroke: 0.35pt + rgb("#c084fc"))[#text(fill: rgb("#6b21a8"), weight: "bold", size: 0.85em)[मूलत्रिकोण]] में हो।], [८५% #box(baseline: 15%, inset: (x: 1.8pt, y: 0.8pt), radius: 2pt, fill: rgb("#d1fae5"), stroke: 0.35pt + rgb("#10b981"))[#text(fill: rgb("#047857"), weight: "bold", size: 0.85em)[उच्च]] शुभ फल], [स्थिरता, गृह-सुख, निष्कलंक स्वास्थ्य, स्वावलंबी जीवन, आत्म-संतोष।], [#strong[३]], [#strong[मुदित (Mudita)]], [ग्रह अपने अधिमित्र (Great Friend) की राशि में हो।], [७५% शुभ फल], [प्रसन्नता, मित्रों व परिजनों का अटूट सहयोग, आर्थिक सुख, सुरुचिपूर्ण जीवन।], [#strong[४]], [#strong[शांत (Shanta)]], [ग्रह अपने मित्र (Friend) की राशि में स्थित हो।], [६०% अनुकूल फल], [शांतिपूर्ण प्रगति, सहज कार्य सिद्धि, सामान्य सुख, धार्मिक अभिरुचि।], [#strong[५]], [#strong[दीन (Deena)]], [ग्रह अपने सम (Neutral) ग्रह की राशि में स्थित हो।], [४०% मध्यम फल], [औसत जीवन, सामान्य संघर्ष, न विशेष हानि न विशेष लाभ।], [#strong[६]], [#strong[दुखित (Dukhita)]], [ग्रह अपने शत्रु (Enemy) की राशि में स्थित हो।], [२५% कष्टप्रद फल], [मानसिक उद्वेग, पारिवारिक कलह, स्थान परिवर्तन, कार्यों में अकारण विघ्न।], [#strong[७]], [#strong[विकल (Vikala)]], [ग्रह #box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#ffedd5"), stroke: 0.35pt + rgb("#ea580c"))[#image("/assets/images/planets/sun.png", width: 7pt) #h(1pt)#text(fill: rgb("#c2410c"), weight: "bold")[सूर्य]] की किरणों से अत्यंत निकट होकर #strong[अस्त (Combust)] हो।], [१०% क्षीण फल], [आत्मबल का अभाव, रोग, संबंधियों से उपेक्षा, प्रयासों का श्रेय न मिलना।], [#strong[८]], [#strong[खल (Khala)]], [ग्रह अपनी #box(baseline: 15%, inset: (x: 1.8pt, y: 0.8pt), radius: 2pt, fill: rgb("#fee2e2"), stroke: 0.35pt + rgb("#ef4444"))[#text(fill: rgb("#dc2626"), weight: "bold", size: 0.85em)[नीच]] राशि (Debilitation) में स्थित हो।], [०-१५% दूषित फल], [संकीर्ण मनोवृत्ति, आर्थिक संकट, अपयश, #box(baseline: 15%, inset: (x: 1.8pt, y: 0.8pt), radius: 2pt, fill: rgb("#fee2e2"), stroke: 0.35pt + rgb("#ef4444"))[#text(fill: rgb("#dc2626"), weight: "bold", size: 0.85em)[नीच]] संगति, असाध्य रोग।], [#strong[९]], [#strong[कोप (Kopa)]], [ग्रह ग्रह-युद्ध (Planetary War) में अन्य ग्रह से पराजित हो।], [अत्यंत अनिष्ट फल], [धन-हानि, मानसिक अवसाद, पराजय का भय, परिजनों से घोर विछोह।]
    )
  ]
]


#v(0.3cm)
#align(center)[#line(length: 60%, stroke: 0.6pt + rgb("#d97706"))]
#v(0.3cm)

=== ४.२ पंचधा मैत्री सिद्धांत (The Five-Fold Relationship Matrix)

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
१. #strong[नैसर्गिक मित्र + तात्कालिक मित्र] = #strong[अधिमित्र (Great Friend)]
२. #strong[नैसर्गिक मित्र + तात्कालिक सम/शत्रु] = #strong[सम या मित्र]
३. #strong[नैसर्गिक शत्रु + तात्कालिक शत्रु] = #strong[अधिशत्रु (Great Enemy)]
४. #strong[नैसर्गिक सम + तात्कालिक मित्र] = #strong[मित्र]
५. #strong[नैसर्गिक शत्रु + तात्कालिक मित्र] = #strong[सम]
]


#v(0.3cm)
#align(center)[#line(length: 60%, stroke: 0.6pt + rgb("#d97706"))]
#v(0.3cm)

=== ४.३ सूर्य देव का द्वादश भावों में शास्त्रीय फल (Sun Across 12 Houses)

#box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#ffedd5"), stroke: 0.35pt + rgb("#ea580c"))[#image("/assets/images/planets/sun.png", width: 7pt) #h(1pt)#text(fill: rgb("#c2410c"), weight: "bold")[सूर्य]] संपूर्ण सौरमंडल की आत्मा एवं जीवन-ऊर्जा का मूल स्रोत हैं। १२ भावों में #box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#ffedd5"), stroke: 0.35pt + rgb("#ea580c"))[#image("/assets/images/planets/sun.png", width: 7pt) #h(1pt)#text(fill: rgb("#c2410c"), weight: "bold")[सूर्य]] का फल निम्नानुसार है:

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

= अध्याय ५: आयुर्-ज्योतिष (Medical Astrology) एवं अर्बुद (कैंसर) रोग विश्लेषण
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
  #align(center)[#text(size: 10.5pt, weight: "bold", fill: rgb("#451a03"))[कर्मजा व्याधयो ये स्युर्न ते शाम्यन्ति भेषजैः।]]
  #align(center)[#text(size: 10.5pt, weight: "bold", fill: rgb("#451a03"))[प्रायश्चित्तैः प्रशाम्यन्ति जपहोमार्चनादिभिः॥]]
]

आयुर्-ज्योतिष (Medical Astrology) चरक, सुश्रुत और पराशर के ज्ञान का दिव्य समन्वय है। रोग केवल जैविक या भौतिक कारणों से ही नहीं होते, अपितु वे पूर्वजन्म-कृत अशुभ कर्मों (कर्मज व्याधि) के परिणाम होते हैं। जब कुण्डली में रोगकारक ग्रह सक्रिय होते हैं, तब शरीर के त्रिदोष (वात, पित्त, कफ) में असंतुलन उत्पन्न होकर असाध्य रोगों का रूप ले लेता है।


#v(0.3cm)
#align(center)[#line(length: 60%, stroke: 0.6pt + rgb("#d97706"))]
#v(0.3cm)

=== ५.१ आयुर्-ज्योतिष अंग एवं ग्रह अधिकार (Anatomical Rulerships)


#align(center)[
  #text(size: 7.5pt)[
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

=== ५.२ अर्बुद (कैंसर) रोग का ज्योतिषीय सूत्र विश्लेषण (Oncology / Arbuda Roga)


#align(center)[
  #image("assets/icons/medical_astrology_chart.svg", width: 85%)
]
#align(center)[#text(size: 8pt, style: "italic", fill: rgb("#64748b"))[चित्र ५.१: अर्बुद (कैंसर) रोग कारक कुण्डली विन्यास — त्रिक भावों (६, ८, १२) में चन्द्र-राहु एवं शनि-मंगल युति]]

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
१. #strong[#box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#f4f4f5"), stroke: 0.35pt + rgb("#27272a"))[#image("/assets/images/planets/rahu.png", width: 7pt) #h(1pt)#text(fill: rgb("#09090b"), weight: "bold")[राहु]] की भूमिका:] #box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#f4f4f5"), stroke: 0.35pt + rgb("#27272a"))[#image("/assets/images/planets/rahu.png", width: 7pt) #h(1pt)#text(fill: rgb("#09090b"), weight: "bold")[राहु]] अनियंत्रित विस्तार, धुंधलापन, उत्परिवर्तन (Genetic Mutation) एवं असामान्य कोशिका गुणन का मुख्य अधिपति है।
२. #strong[#box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#dbeafe"), stroke: 0.35pt + rgb("#3b82f6"))[#image("/assets/images/planets/saturn.png", width: 7pt) #h(1pt)#text(fill: rgb("#1d4ed8"), weight: "bold")[शनि]] की भूमिका:] #box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#dbeafe"), stroke: 0.35pt + rgb("#3b82f6"))[#image("/assets/images/planets/saturn.png", width: 7pt) #h(1pt)#text(fill: rgb("#1d4ed8"), weight: "bold")[शनि]] दीर्घकालिक क्षय, रक्त में रुकावट, ऊतकों का सड़ना (Necrosis) और पुरानी गांठों (Tumors) का कारक है।
३. #strong[#box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#f1f5f9"), stroke: 0.35pt + rgb("#94a3b8"))[#image("/assets/images/planets/moon.png", width: 7pt) #h(1pt)#text(fill: rgb("#334155"), weight: "bold")[चन्द्रमा]] एवं #box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#fee2e2"), stroke: 0.35pt + rgb("#ef4444"))[#image("/assets/images/planets/mars.png", width: 7pt) #h(1pt)#text(fill: rgb("#dc2626"), weight: "bold")[मंगल]] का दूषित होना:] #box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#f1f5f9"), stroke: 0.35pt + rgb("#94a3b8"))[#image("/assets/images/planets/moon.png", width: 7pt) #h(1pt)#text(fill: rgb("#334155"), weight: "bold")[चन्द्रमा]] रस/जल का स्वामी है और #box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#fee2e2"), stroke: 0.35pt + rgb("#ef4444"))[#image("/assets/images/planets/mars.png", width: 7pt) #h(1pt)#text(fill: rgb("#dc2626"), weight: "bold")[मंगल]] रक्त व मज्जा का। जब जल और रक्त विषाक्त होते हैं, तब अर्बुद की नींव पड़ती है।
४. #strong[त्रिक भाव (६, ८, १२) एवं लग्न का पीड़ित होना:] ६ठा भाव रोग का, ८वां भाव असाध्य व्याधि का, १२वां भाव शय्याग्रस्त होने का, और लग्न रोग प्रतिरोधक क्षमता का है।
]

==== विभिन्न अंगों के कैंसर के विशिष्ट ग्रहीय योग:


#align(center)[
  #text(size: 7.8pt)[
    #table(
      columns: (1.1fr, 1.4fr, 3.5fr),
      fill: (x, y) => if y == 0 { rgb("#fef3c7") } else if calc.odd(y) { rgb("#f8fafc") } else { rgb("#ffffff") },
      stroke: (x, y) => if y == 0 { (bottom: 1.2pt + rgb("#b45309"), rest: 0.4pt + rgb("#cbd5e1")) } else { 0.4pt + rgb("#cbd5e1") },
      inset: (x: 4.2pt, y: 5.0pt),
      align: (x, y) => if y == 0 { center + horizon } else { left + horizon },
      [#text(weight: "bold", fill: rgb("#78350f"))[कैंसर का प्रकार]], [#text(weight: "bold", fill: rgb("#78350f"))[प्रभावित भाव व ग्रह]], [#text(weight: "bold", fill: rgb("#78350f"))[विशिष्ट शास्त्रीय ग्रहीय युति]], [#strong[रक्त कैंसर (Leukemia)]], [#box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#f1f5f9"), stroke: 0.35pt + rgb("#94a3b8"))[#image("/assets/images/planets/moon.png", width: 7pt) #h(1pt)#text(fill: rgb("#334155"), weight: "bold")[चन्द्रमा]], #box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#fee2e2"), stroke: 0.35pt + rgb("#ef4444"))[#image("/assets/images/planets/mars.png", width: 7pt) #h(1pt)#text(fill: rgb("#dc2626"), weight: "bold")[मंगल]] एवं षष्ठेश], [#box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#f1f5f9"), stroke: 0.35pt + rgb("#94a3b8"))[#image("/assets/images/planets/moon.png", width: 7pt) #h(1pt)#text(fill: rgb("#334155"), weight: "bold")[चन्द्रमा]] और #box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#fee2e2"), stroke: 0.35pt + rgb("#ef4444"))[#image("/assets/images/planets/mars.png", width: 7pt) #h(1pt)#text(fill: rgb("#dc2626"), weight: "bold")[मंगल]] पर #box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#f4f4f5"), stroke: 0.35pt + rgb("#27272a"))[#image("/assets/images/planets/rahu.png", width: 7pt) #h(1pt)#text(fill: rgb("#09090b"), weight: "bold")[राहु]] या #box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#dbeafe"), stroke: 0.35pt + rgb("#3b82f6"))[#image("/assets/images/planets/saturn.png", width: 7pt) #h(1pt)#text(fill: rgb("#1d4ed8"), weight: "bold")[शनि]] की कुदृष्टि, षष्ठ भाव में #box(baseline: 15%, inset: (x: 1.8pt, y: 0.8pt), radius: 2pt, fill: rgb("#fee2e2"), stroke: 0.35pt + rgb("#ef4444"))[#text(fill: rgb("#dc2626"), weight: "bold", size: 0.85em)[नीच]] का #box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#fee2e2"), stroke: 0.35pt + rgb("#ef4444"))[#image("/assets/images/planets/mars.png", width: 7pt) #h(1pt)#text(fill: rgb("#dc2626"), weight: "bold")[मंगल]] #box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#f4f4f5"), stroke: 0.35pt + rgb("#27272a"))[#image("/assets/images/planets/rahu.png", width: 7pt) #h(1pt)#text(fill: rgb("#09090b"), weight: "bold")[राहु]] से युक्त।], [#strong[स्तन एवं फेफड़े का कैंसर]], [चतुर्थ भाव एवं कर्क राशि], [चतुर्थेश का ६ठे या ८वें भाव में #box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#f4f4f5"), stroke: 0.35pt + rgb("#27272a"))[#image("/assets/images/planets/rahu.png", width: 7pt) #h(1pt)#text(fill: rgb("#09090b"), weight: "bold")[राहु]]-#box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#dbeafe"), stroke: 0.35pt + rgb("#3b82f6"))[#image("/assets/images/planets/saturn.png", width: 7pt) #h(1pt)#text(fill: rgb("#1d4ed8"), weight: "bold")[शनि]] से पीड़ित होना, कर्क राशि में पापी ग्रहों का जमावड़ा।], [#strong[मस्तिष्क का अर्बुद (Brain Tumor)]], [प्रथम भाव एवं मेष राशि], [लग्नेश मेष राशि में #box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#f4f4f5"), stroke: 0.35pt + rgb("#27272a"))[#image("/assets/images/planets/rahu.png", width: 7pt) #h(1pt)#text(fill: rgb("#09090b"), weight: "bold")[राहु]]-#box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#f4f4f5"), stroke: 0.35pt + rgb("#71717a"))[#image("/assets/images/planets/ketu.png", width: 7pt) #h(1pt)#text(fill: rgb("#52525b"), weight: "bold")[केतु]] अक्ष पर होकर #box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#dbeafe"), stroke: 0.35pt + rgb("#3b82f6"))[#image("/assets/images/planets/saturn.png", width: 7pt) #h(1pt)#text(fill: rgb("#1d4ed8"), weight: "bold")[शनि]] या वक्री #box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#fee2e2"), stroke: 0.35pt + rgb("#ef4444"))[#image("/assets/images/planets/mars.png", width: 7pt) #h(1pt)#text(fill: rgb("#dc2626"), weight: "bold")[मंगल]] द्वारा देखा जाना।], [#strong[त्वचा का कैंसर (Melanoma)]], [#box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#d1fae5"), stroke: 0.35pt + rgb("#10b981"))[#image("/assets/images/planets/mercury.png", width: 7pt) #h(1pt)#text(fill: rgb("#047857"), weight: "bold")[बुध]], षष्ठ भाव एवं कन्या राशि], [#box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#d1fae5"), stroke: 0.35pt + rgb("#10b981"))[#image("/assets/images/planets/mercury.png", width: 7pt) #h(1pt)#text(fill: rgb("#047857"), weight: "bold")[बुध]] का #box(baseline: 15%, inset: (x: 1.8pt, y: 0.8pt), radius: 2pt, fill: rgb("#fee2e2"), stroke: 0.35pt + rgb("#ef4444"))[#text(fill: rgb("#dc2626"), weight: "bold", size: 0.85em)[नीच]] राशि में #box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#f4f4f5"), stroke: 0.35pt + rgb("#27272a"))[#image("/assets/images/planets/rahu.png", width: 7pt) #h(1pt)#text(fill: rgb("#09090b"), weight: "bold")[राहु]] से युत होकर #box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#ffedd5"), stroke: 0.35pt + rgb("#ea580c"))[#image("/assets/images/planets/sun.png", width: 7pt) #h(1pt)#text(fill: rgb("#c2410c"), weight: "bold")[सूर्य]] द्वारा अत्यधिक दग्ध होना।], [#strong[उदर व आंतों का कैंसर]], [पंचम व षष्ठ भाव], [#box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#fef3c7"), stroke: 0.35pt + rgb("#f59e0b"))[#image("/assets/images/planets/jupiter.png", width: 7pt) #h(1pt)#text(fill: rgb("#b45309"), weight: "bold")[गुरु]] या #box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#d1fae5"), stroke: 0.35pt + rgb("#10b981"))[#image("/assets/images/planets/mercury.png", width: 7pt) #h(1pt)#text(fill: rgb("#047857"), weight: "bold")[बुध]] का #box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#f4f4f5"), stroke: 0.35pt + rgb("#27272a"))[#image("/assets/images/planets/rahu.png", width: 7pt) #h(1pt)#text(fill: rgb("#09090b"), weight: "bold")[राहु]] के साथ षष्ठ भाव में स्थित होकर पाप ग्रहों से पीड़ित होना।]
    )
  ]
]


#v(0.3cm)
#align(center)[#line(length: 60%, stroke: 0.6pt + rgb("#d97706"))]
#v(0.3cm)

=== ५.३ दशा-गोचर प्रकटीकरण एवं ज्योतिषीय निवारण (Timing & Remedies)

कैंसर रोग का प्रकटीकरण तभी होता है जब:
१. जातक की #strong[मारक (२, ७) अथवा त्रिक भावों (६, ८, १२)] के स्वामियों की विंशोत्तरी दशा चल रही हो।
२. गोचर में #box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#f4f4f5"), stroke: 0.35pt + rgb("#27272a"))[#image("/assets/images/planets/rahu.png", width: 7pt) #h(1pt)#text(fill: rgb("#09090b"), weight: "bold")[राहु]] अथवा #box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#dbeafe"), stroke: 0.35pt + rgb("#3b82f6"))[#image("/assets/images/planets/saturn.png", width: 7pt) #h(1pt)#text(fill: rgb("#1d4ed8"), weight: "bold")[शनि]] लग्न, लग्नेश अथवा #box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#f1f5f9"), stroke: 0.35pt + rgb("#94a3b8"))[#image("/assets/images/planets/moon.png", width: 7pt) #h(1pt)#text(fill: rgb("#334155"), weight: "bold")[चन्द्र]] राशि के ऊपर से या अष्टम भाव से भ्रमण कर रहे हों।


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
१. #strong[महामृत्युंजय मंत्र जप:] सवा लाख महामृत्युंजय मंत्र का संपुटित जप प्राण-शक्ति का संवर्धन करता है।
२. #strong[रुद्राभिषेक अनुष्ठान:] कुशा रस एवं दूर्वा से भगवान शिव का अभिषेक रक्त शोधन में फलदायी है।
३. #strong[दान कर्म:] #box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#dbeafe"), stroke: 0.35pt + rgb("#3b82f6"))[#image("/assets/images/planets/saturn.png", width: 7pt) #h(1pt)#text(fill: rgb("#1d4ed8"), weight: "bold")[शनि]] व #box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#f4f4f5"), stroke: 0.35pt + rgb("#27272a"))[#image("/assets/images/planets/rahu.png", width: 7pt) #h(1pt)#text(fill: rgb("#09090b"), weight: "bold")[राहु]] की शांति हेतु काले तिल, कंबल, नारियल एवं रोगियों को निःशुल्क औषधि दान।
]




#pagebreak()

= अध्याय ६: नक्षत्र पद विभाजन, नवांश गणित एवं मंगल श्लोक
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
  #align(center)[#text(size: 10.5pt, weight: "bold", fill: rgb("#451a03"))[नवांशाद्बलिनो ज्ञेयं कलत्रस्य बलाबलम्।]]
  #align(center)[#text(size: 10.5pt, weight: "bold", fill: rgb("#451a03"))[तथैव भाग्यवृद्धिश्च धर्ममार्गरतिस्तथा॥]]
]

कुण्डली का स्थूल शरीर लग्न कुण्डली (D1) है, किंतु उसकी सूक्ष्म आत्मा #strong[नवांश कुण्डली (D9)] है। नवांश का अर्थ है किसी राशि का ९वां भाग (३°२०')। चूंकि २७ नक्षत्रों में प्रत्येक के ४ पद होते हैं, अतः संपूर्ण भचक्र में १०८ नवांश पद होते हैं। नवांश से जातक के आंतरिक सामर्थ्य, दांपत्य जीवन, भाग्य की वास्तविकता तथा उत्तरार्ध जीवन का सटीक ज्ञान प्राप्त होता है।


#v(0.3cm)
#align(center)[#line(length: 60%, stroke: 0.6pt + rgb("#d97706"))]
#v(0.3cm)

=== ६.१ नवांश पद गणना सिद्धांत (Navamsha Mathematics)

नवांश की गणना राशियों के चर, स्थिर एवं द्विस्वभाव स्वभाव के अनुसार की जाती है:

1. #strong[चर राशियां (मेष, कर्क, तुला, मकर):] नवांश की गणना उसी राशि से प्रारंभ होती है (मेष का प्रथम नवांश मेष से, कर्क का कर्क से)।
2. #strong[स्थिर राशियां (वृषभ, सिंह, वृश्चिक, कुंभ):] नवांश की गणना उस राशि से ९वें स्थान से प्रारंभ होती है (वृषभ का प्रथम नवांश मकर से)।
3. #strong[द्विस्वभाव राशियां (मिथुन, कन्या, धनु, मीन):] नवांश की गणना उस राशि से ५वें स्थान से प्रारंभ होती है (मिथुन का प्रथम नवांश तुला से)।


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

=== ६.२ प्रमुख नक्षत्र पदों का सूक्ष्म फलित (Pada Micro-Analysis)

नीचे तीन महत्वपूर्ण नक्षत्रों के पदों का व्यावहारिक फलित दिया गया है:


#align(center)[
  #text(size: 7.5pt)[
    #table(
      columns: (1.1fr, 1.3fr, 1.4fr, 3.2fr),
      fill: (x, y) => if y == 0 { rgb("#fef3c7") } else if calc.odd(y) { rgb("#f8fafc") } else { rgb("#ffffff") },
      stroke: (x, y) => if y == 0 { (bottom: 1.2pt + rgb("#b45309"), rest: 0.4pt + rgb("#cbd5e1")) } else { 0.4pt + rgb("#cbd5e1") },
      inset: (x: 3.8pt, y: 4.5pt),
      align: (x, y) => if y == 0 { center + horizon } else { left + horizon },
      [#text(weight: "bold", fill: rgb("#78350f"))[नक्षत्र]], [#text(weight: "bold", fill: rgb("#78350f"))[पद क्रम]], [#text(weight: "bold", fill: rgb("#78350f"))[नवांश राशि व स्वामी]], [#text(weight: "bold", fill: rgb("#78350f"))[मनोवैज्ञानिक प्रवृत्ति व फलित संकेत]], [#strong[अश्विनी (Ashwini)]], [प्रथम पद (१)], [मेष (#box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#fee2e2"), stroke: 0.35pt + rgb("#ef4444"))[#image("/assets/images/planets/mars.png", width: 7pt) #h(1pt)#text(fill: rgb("#dc2626"), weight: "bold")[मंगल]])], [तीव्र ऊर्जा, साहसी, नेतृत्व क्षमता, त्वरित कार्य सिद्धि, अग्रणी स्वभाव।], [], [द्वितीय पद (२)], [वृषभ (#box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#fce7f3"), stroke: 0.35pt + rgb("#f43f5e"))[#image("/assets/images/planets/venus.png", width: 7pt) #h(1pt)#text(fill: rgb("#be185d"), weight: "bold")[शुक्र]])], [भौतिक स्थिरता, रूपवान, व्यावहारिक ज्ञान, कला व धन संचय की रुचि।], [], [तृतीय पद (३)], [मिथुन (#box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#d1fae5"), stroke: 0.35pt + rgb("#10b981"))[#image("/assets/images/planets/mercury.png", width: 7pt) #h(1pt)#text(fill: rgb("#047857"), weight: "bold")[बुध]])], [बौद्धिक चंचलता, संचार कला, हास्य-विनोद, बहुमुखी प्रतिभा।], [], [चतुर्थ पद (४)], [कर्क (#box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#f1f5f9"), stroke: 0.35pt + rgb("#94a3b8"))[#image("/assets/images/planets/moon.png", width: 7pt) #h(1pt)#text(fill: rgb("#334155"), weight: "bold")[चन्द्रमा]])], [संवेदनशील, दूसरों की सेवा करने वाला, उत्कृष्ट चिकित्सक, भावनात्मक मन।], [#strong[पुष्य (Pushya)]], [प्रथम पद (१)], [सिंह (#box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#ffedd5"), stroke: 0.35pt + rgb("#ea580c"))[#image("/assets/images/planets/sun.png", width: 7pt) #h(1pt)#text(fill: rgb("#c2410c"), weight: "bold")[सूर्य]])], [आध्यात्मिक तेज, पैतृक गौरव, न्यायप्रियता, राजदरबार में सम्मान।], [], [द्वितीय पद (२)], [कन्या (#box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#d1fae5"), stroke: 0.35pt + rgb("#10b981"))[#image("/assets/images/planets/mercury.png", width: 7pt) #h(1pt)#text(fill: rgb("#047857"), weight: "bold")[बुध]])], [सूक्ष्म विश्लेषण, सेवा भाव, व्यावहारिक योजनाकार, संयमित वाणी।], [], [तृतीय पद (३)], [तुला (#box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#fce7f3"), stroke: 0.35pt + rgb("#f43f5e"))[#image("/assets/images/planets/venus.png", width: 7pt) #h(1pt)#text(fill: rgb("#be185d"), weight: "bold")[शुक्र]])], [सामाजिक सौहार्द, सुरुचिपूर्ण जीवन, निष्पक्ष न्याय, व्यापारिक सफलता।], [], [चतुर्थ पद (४)], [वृश्चिक (#box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#fee2e2"), stroke: 0.35pt + rgb("#ef4444"))[#image("/assets/images/planets/mars.png", width: 7pt) #h(1pt)#text(fill: rgb("#dc2626"), weight: "bold")[मंगल]])], [गुप्त साधना, गूढ़ विद्याओं का ज्ञाता, गहन अंतर्दृष्टि, आक्रामक संकल्प।], [#strong[आश्लेषा (Ashlesha)]], [प्रथम पद (१)], [धनु (#box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#fef3c7"), stroke: 0.35pt + rgb("#f59e0b"))[#image("/assets/images/planets/jupiter.png", width: 7pt) #h(1pt)#text(fill: rgb("#b45309"), weight: "bold")[गुरु]])], [दार्शनिक सोच, #box(baseline: 15%, inset: (x: 1.8pt, y: 0.8pt), radius: 2pt, fill: rgb("#d1fae5"), stroke: 0.35pt + rgb("#10b981"))[#text(fill: rgb("#047857"), weight: "bold", size: 0.85em)[उच्च]] आकांक्षाएं, कूटनीति में दक्ष, शास्त्रों का अभ्यासी।], [], [द्वितीय पद (२)], [मकर (#box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#dbeafe"), stroke: 0.35pt + rgb("#3b82f6"))[#image("/assets/images/planets/saturn.png", width: 7pt) #h(1pt)#text(fill: rgb("#1d4ed8"), weight: "bold")[शनि]])], [कठोर परिश्रम, महत्वाकांक्षा, धैर्यपूर्वक लक्ष्य प्राप्ति, स्वार्थ नियंत्रण।], [], [तृतीय पद (३)], [कुंभ (#box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#dbeafe"), stroke: 0.35pt + rgb("#3b82f6"))[#image("/assets/images/planets/saturn.png", width: 7pt) #h(1pt)#text(fill: rgb("#1d4ed8"), weight: "bold")[शनि]])], [गुप्त अनुसंधान, जन-कल्याण, वैज्ञानिक दृष्टिकोण, अलौकिक आकर्षण।], [], [चतुर्थ पद (४)], [मीन (#box(baseline: 15%, inset: (x: 2pt, y: 1pt), radius: 2pt, fill: rgb("#fef3c7"), stroke: 0.35pt + rgb("#f59e0b"))[#image("/assets/images/planets/jupiter.png", width: 7pt) #h(1pt)#text(fill: rgb("#b45309"), weight: "bold")[गुरु]])], [मोक्ष प्राप्ति की लालसा, मोह-माया से विरक्ति, पूर्ण समर्पण, तांत्रिक अंतःप्रेरणा।]
    )
  ]
]


#v(0.3cm)
#align(center)[#line(length: 60%, stroke: 0.6pt + rgb("#d97706"))]
#v(0.3cm)

=== ६.३ उपनिषद् मंगल कामना एवं शांति पाठ (Universal Benediction)


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
  #align(center)[#text(size: 10.5pt, weight: "bold", fill: rgb("#451a03"))[ॐ असतो मा सद्गमय।]]
  #align(center)[#text(size: 10.5pt, weight: "bold", fill: rgb("#451a03"))[तमसो मा ज्योतिर्गमय।]]
  #align(center)[#text(size: 10.5pt, weight: "bold", fill: rgb("#451a03"))[मृत्योर्मा अमृतं गमय॥]]
  #align(center)[#text(size: 10.5pt, weight: "bold", fill: rgb("#451a03"))[ॐ शान्तिः शान्तिः शान्तिः॥]]
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
  #align(center)[#text(size: 10.5pt, weight: "bold", fill: rgb("#451a03"))[सर्वे भवन्तु सुखिनः सर्वे सन्तु निरामयाः।]]
  #align(center)[#text(size: 10.5pt, weight: "bold", fill: rgb("#451a03"))[सर्वे भद्राणि पश्यन्तु मा कश्चिद्दुःखभाग्भवेत्॥]]
]

समस्त प्राणी सुखी हों, सभी रोगमुक्त व स्वस्थ रहें, सभी का कल्याण हो, और इस संसार में किसी को भी लेशमात्र भी दुःख न भोगना पड़े।


#v(0.3cm)
#align(center)[#line(length: 60%, stroke: 0.6pt + rgb("#d97706"))]
#v(0.3cm)

=== ६.४ ग्रंथ समापन एवं कृतज्ञता ज्ञापन (Colophon)

#strong[तंत्र ज्ञान: वैदिक ज्योतिष महाग्रंथ] का यह प्रथम ट्रेड पेपरबैक एवं डिजिटल ग्रंथ संस्करण प्रामाणिक संकलन, शास्त्रीय सूत्रों के अनुसंधान एवं आधुनिक विश्लेषणात्मक प्रारूप के साथ लोक-हितार्थ समर्पित किया जाता है।

- #strong[ग्रंथकार एवं शोधकर्ता:] ज्योतिषाचार्य आशुतोष कुमार चौबे (Ashutosh Kumar Choubey)
- #strong[आधिकारिक अनुसंधान केन्द्र:] तंत्र ज्ञान शोध संस्थान (Tantra Gyan Research Center)
- #strong[वेबसाइट:] [t.worldgyan.com](https://t.worldgyan.com)
- #strong[यूट्यूब शोध मंच:] [\@TantraGyan108](https://www.youtube.com/\@TantraGyan108)
- #strong[ईमेल:] [tantraresearchcenter\@gmail.com](mailto:tantraresearchcenter\@gmail.com)
- #strong[संस्करण वर्ष:] २०२६ (Digital & Print Masterwork Edition)



