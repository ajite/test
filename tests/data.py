"""Test data from wanikani API."""

API_KEY = 'API_KEY'

get_summary = {
  "object": "report",
  "url": "https://api.wanikani.com/v2/summary",
  "data_updated_at": "2018-04-11T21:00:00.000000Z",
  "data": {
    "lessons": [
      {
        "available_at": "2018-04-11T21:00:00.000000Z",
        "subject_ids": [
          25,
          26
        ]
      }
    ],
    "next_reviews_at": "2018-04-11T21:00:00.000000Z",
    "reviews": [
      {
        "available_at": "2018-04-11T21:00:00.000000Z",
        "subject_ids": [
          21,
          23,
          24
        ]
      },
      {
        "available_at": "2018-04-11T22:00:00.000000Z",
        "subject_ids": []
      }
    ]
  }
}

get_specific_subjects = {
  "object": "collection",
  "url": "https://api.wanikani.com/v2/subjects?types=kanji",
  "pages": {
    "per_page": 1000,
    "next_url": "https://api.wanikani.com/v2/subjects?page_after_id=1439\u0026types=kanji",
    "previous_url": None
  },
  "total_count": 2027,
  "data_updated_at": "2018-04-09T18:08:59.946969Z",
  "data": [
    {
      "id": 440,
      "object": "kanji",
      "url": "https://api.wanikani.com/v2/subjects/440",
      "data_updated_at": "2018-03-29T23:14:30.805034Z",
      "data": {
        "created_at": "2012-02-27T19:55:19.000000Z",
        "level": 1,
        "slug": "一",
        "hidden_at": None,
        "document_url": "https://www.wanikani.com/kanji/%E4%B8%80",
        "characters": "一",
        "meanings": [
          {
            "meaning": "One",
            "primary": True,
            "accepted_answer": True
          }
        ],
        "readings": [
          {
            "type": "onyomi",
            "primary": True,
            "accepted_answer": True,
            "reading": "いち"
          },
          {
            "type": "kunyomi",
            "primary": False,
            "accepted_answer": False,
            "reading": "ひと"
          },
          {
            "type": "nanori",
            "primary": False,
            "accepted_answer": False,
            "reading": "かず"
          }
        ],
        "component_subject_ids": [
          1
        ],
        "amalgamation_subject_ids": [
          56,
          88,
          91
        ],
        "visually_similar_subject_ids": [],
        "meaning_mnemonic": "Lying on the <radical>ground</radical> is something that looks just like the ground, the number <kanji>One</kanji>. Why is this One lying down? It's been shot by the number two. It's lying there, bleeding out and dying. The number One doesn't have long to live.",
        "meaning_hint": "To remember the meaning of <kanji>One</kanji>, imagine yourself there at the scene of the crime. You grab <kanji>One</kanji> in your arms, trying to prop it up, trying to hear its last words. Instead, it just splatters some blood on your face. \"Who did this to you?\" you ask. The number One points weakly, and you see number Two running off into an alleyway. He's always been jealous of number One and knows he can be number one now that he's taken the real number one out.",
        "reading_mnemonic": "As you're sitting there next to <kanji>One</kanji>, holding him up, you start feeling a weird sensation all over your skin. From the wound comes a fine powder (obviously coming from the special bullet used to kill One) that causes the person it touches to get extremely <reading>itchy</reading> (いち)",
        "reading_hint": "Make sure you feel the ridiculously <reading>itchy</reading> sensation covering your body. It climbs from your hands, where you're holding the number <kanji>One</kanji> up, and then goes through your arms, crawls up your neck, goes down your body, and then covers everything. It becomes uncontrollable, and you're scratching everywhere, writhing on the ground. It's so itchy that it's the most painful thing you've ever experienced (you should imagine this vividly, so you remember the reading of this kanji).",
        "lesson_position": 2,
        "spaced_repetition_system_id": 1
      }
    }
  ]
}

get_subject_without_utf_entry = {
    "object": "collection",
    "url": "https://api.wanikani.com/v2/subjects?ids=8769",
    "pages": {
        "per_page": 1000,
        "next_url": None,
        "previous_url": None
    },
    "total_count": 1,
    "data_updated_at": "2022-05-02T19:28:05.752635Z",
    "data": [
        {
            "id": 8769,
            "object": "radical",
            "url": "https://api.wanikani.com/v2/subjects/8769",
            "data_updated_at": "2021-10-11T22:20:15.393206Z",
            "data": {
                "created_at": "2012-03-03T04:09:15.000000Z",
                "level": 5,
                "slug": "viking",
                "hidden_at": None,
                "document_url": "https://www.wanikani.com/radicals/fake_meaning",
                "characters": None,
                "character_images": [
                    {
                        "url": "fake_path",
                        "metadata": {
                            "color": "#000000",
                            "dimensions": "1024x1024",
                            "style_name": "original"
                        },
                        "content_type": "image/png"
                    },
                    {
                        "url": "fake_path",
                        "metadata": {
                            "color": "#000000",
                            "dimensions": "1024x1024",
                            "style_name": "1024px"
                        },
                        "content_type": "image/png"
                    },
                    {
                        "url": "fake_path",
                        "metadata": {
                            "color": "#000000",
                            "dimensions": "512x512",
                            "style_name": "512px"
                        },
                        "content_type": "image/png"
                    },
                    {
                        "url": "fake_path",
                        "metadata": {
                            "color": "#000000",
                            "dimensions": "256x256",
                            "style_name": "256px"
                        },
                        "content_type": "image/png"
                    },
                    {
                        "url": "fake_path",
                        "metadata": {
                            "color": "#000000",
                            "dimensions": "128x128",
                            "style_name": "128px"
                        },
                        "content_type": "image/png"
                    },
                    {
                        "url": "fake_path",
                        "metadata": {
                            "color": "#000000",
                            "dimensions": "64x64",
                            "style_name": "64px"
                        },
                        "content_type": "image/png"
                    },
                    {
                        "url": "fake_path",
                        "metadata": {
                            "color": "#000000",
                            "dimensions": "32x32",
                            "style_name": "32px"
                        },
                        "content_type": "image/png"
                    },
                    {
                        "url": "fake_path",
                        "metadata": {
                            "inline_styles": False
                        },
                        "content_type": "image/svg+xml"
                    },
                    {
                        "url": "fake_path",
                        "metadata": {
                            "inline_styles": True
                        },
                        "content_type": "image/svg+xml"
                    }
                ],
                "meanings": [
                    {
                        "meaning": "Fake meaning",
                        "primary": True,
                        "accepted_answer": True
                    }
                ],
                "auxiliary_meanings": [],
                "amalgamation_subject_ids": [
                    29492329,
                ],
                "meaning_mnemonic": "Lorem Ipsum Dolor Sit Amet",
                "lesson_position": 3909,
                "spaced_repetition_system_id": 1
            }
        }
    ]
}