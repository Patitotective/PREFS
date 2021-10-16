export default {
  "title": "PREFS",
  "tagline": "Manage your app preferences with PREFS.",
  "url": "https://patitotective.github.io",
  "baseUrl": "/PREFS/",
  "onBrokenLinks": "throw",
  "onBrokenMarkdownLinks": "warn",
  "favicon": "img/favicon.png",
  "organizationName": "Patitotective",
  "projectName": "PREFS",
  "presets": [
    [
      "@docusaurus/preset-classic",
      {
        "docs": {
          "sidebarPath": "/home/cristobal/Documents/Projects/PREFS/website/sidebars.js",
          "editUrl": "https://github.com/Patitotective/PREFS/tree/main/website",
          "showLastUpdateAuthor": true,
          "showLastUpdateTime": true
        },
        "blog": {
          "showReadingTime": true,
          "editUrl": "https://github.com/Patitotective/PREFS"
        },
        "theme": {
          "customCss": "/home/cristobal/Documents/Projects/PREFS/website/src/css/custom.css"
        }
      }
    ]
  ],
  "themeConfig": {
    "image": "img/dark_logo.png",
    "colorMode": {
      "defaultMode": "dark",
      "disableSwitch": false,
      "respectPrefersColorScheme": false,
      "switchConfig": {
        "darkIcon": "🌜",
        "darkIconStyle": {},
        "lightIcon": "🌞",
        "lightIconStyle": {}
      }
    },
    "announcementBar": {
      "id": "github_star",
      "content": "<b>⭐ If you like PREFS, please consider giving a star on <a href=\"https://github.com/Patitotective/PREFS\">GitHub</a> ❤️</b>",
      "backgroundColor": "#fafbfc",
      "textColor": "#091E42",
      "isCloseable": true
    },
    "navbar": {
      "title": "PREFS",
      "logo": {
        "alt": "PREFS logo",
        "src": "img/navbar_logo.png"
      },
      "items": [
        {
          "type": "doc",
          "position": "left",
          "docId": "start",
          "label": "Docs"
        },
        {
          "type": "doc",
          "position": "left",
          "docId": "api/prefs-class",
          "label": "API Reference"
        },
        {
          "type": "doc",
          "position": "left",
          "docId": "about/about",
          "label": "About"
        },
        {
          "type": "docsVersionDropdown",
          "position": "right",
          "dropdownItemsBefore": [],
          "dropdownItemsAfter": []
        }
      ],
      "hideOnScroll": false
    },
    "footer": {
      "style": "dark",
      "links": [
        {
          "title": "Links",
          "items": [
            {
              "label": "Source code",
              "href": "https://github.com/Patitotective/PREFS"
            },
            {
              "label": "Pypi page",
              "href": "https://pypi.org/project/PREFS/"
            },
            {
              "label": "Documentation",
              "href": "https://patitotective.github.io/PREFS/"
            }
          ]
        },
        {
          "title": "Contact me",
          "items": [
            {
              "label": "Discord: Patitotective#0127",
              "href": "https://patitotective.github.io/PREFS/About/about"
            },
            {
              "label": "Mail: cristobalriaga@gmail.com",
              "href": "mailto:cristobalriaga@gmail.com"
            }
          ]
        }
      ],
      "copyright": "Copyright © 2021 My Project, Inc. Built with Docusaurus."
    },
    "prism": {
      "theme": {
        "plain": {
          "color": "#403f53",
          "backgroundColor": "#FBFBFB"
        },
        "styles": [
          {
            "types": [
              "changed"
            ],
            "style": {
              "color": "rgb(162, 191, 252)",
              "fontStyle": "italic"
            }
          },
          {
            "types": [
              "deleted"
            ],
            "style": {
              "color": "rgba(239, 83, 80, 0.56)",
              "fontStyle": "italic"
            }
          },
          {
            "types": [
              "inserted",
              "attr-name"
            ],
            "style": {
              "color": "rgb(72, 118, 214)",
              "fontStyle": "italic"
            }
          },
          {
            "types": [
              "comment"
            ],
            "style": {
              "color": "rgb(152, 159, 177)",
              "fontStyle": "italic"
            }
          },
          {
            "types": [
              "string",
              "builtin",
              "char",
              "constant",
              "url"
            ],
            "style": {
              "color": "rgb(72, 118, 214)"
            }
          },
          {
            "types": [
              "variable"
            ],
            "style": {
              "color": "rgb(201, 103, 101)"
            }
          },
          {
            "types": [
              "number"
            ],
            "style": {
              "color": "rgb(170, 9, 130)"
            }
          },
          {
            "types": [
              "punctuation"
            ],
            "style": {
              "color": "rgb(153, 76, 195)"
            }
          },
          {
            "types": [
              "function",
              "selector",
              "doctype"
            ],
            "style": {
              "color": "rgb(153, 76, 195)",
              "fontStyle": "italic"
            }
          },
          {
            "types": [
              "class-name"
            ],
            "style": {
              "color": "rgb(17, 17, 17)"
            }
          },
          {
            "types": [
              "tag"
            ],
            "style": {
              "color": "rgb(153, 76, 195)"
            }
          },
          {
            "types": [
              "operator",
              "property",
              "keyword",
              "namespace"
            ],
            "style": {
              "color": "rgb(12, 150, 155)"
            }
          },
          {
            "types": [
              "boolean"
            ],
            "style": {
              "color": "rgb(188, 84, 84)"
            }
          }
        ]
      },
      "darkTheme": {
        "plain": {
          "color": "#f8f8f2",
          "backgroundColor": "#272822"
        },
        "styles": [
          {
            "types": [
              "changed"
            ],
            "style": {
              "color": "rgb(162, 191, 252)",
              "fontStyle": "italic"
            }
          },
          {
            "types": [
              "deleted"
            ],
            "style": {
              "color": "#f92672",
              "fontStyle": "italic"
            }
          },
          {
            "types": [
              "inserted"
            ],
            "style": {
              "color": "rgb(173, 219, 103)",
              "fontStyle": "italic"
            }
          },
          {
            "types": [
              "comment"
            ],
            "style": {
              "color": "#8292a2",
              "fontStyle": "italic"
            }
          },
          {
            "types": [
              "string",
              "url"
            ],
            "style": {
              "color": "#a6e22e"
            }
          },
          {
            "types": [
              "variable"
            ],
            "style": {
              "color": "#f8f8f2"
            }
          },
          {
            "types": [
              "number"
            ],
            "style": {
              "color": "#ae81ff"
            }
          },
          {
            "types": [
              "builtin",
              "char",
              "constant",
              "function",
              "class-name"
            ],
            "style": {
              "color": "#e6db74"
            }
          },
          {
            "types": [
              "punctuation"
            ],
            "style": {
              "color": "#f8f8f2"
            }
          },
          {
            "types": [
              "selector",
              "doctype"
            ],
            "style": {
              "color": "#a6e22e",
              "fontStyle": "italic"
            }
          },
          {
            "types": [
              "tag",
              "operator",
              "keyword"
            ],
            "style": {
              "color": "#66d9ef"
            }
          },
          {
            "types": [
              "boolean"
            ],
            "style": {
              "color": "#ae81ff"
            }
          },
          {
            "types": [
              "namespace"
            ],
            "style": {
              "color": "rgb(178, 204, 214)",
              "opacity": 0.7
            }
          },
          {
            "types": [
              "tag",
              "property"
            ],
            "style": {
              "color": "#f92672"
            }
          },
          {
            "types": [
              "attr-name"
            ],
            "style": {
              "color": "#a6e22e !important"
            }
          },
          {
            "types": [
              "doctype"
            ],
            "style": {
              "color": "#8292a2"
            }
          },
          {
            "types": [
              "rule"
            ],
            "style": {
              "color": "#e6db74"
            }
          }
        ]
      },
      "additionalLanguages": []
    },
    "docs": {
      "versionPersistence": "localStorage"
    },
    "metadatas": [],
    "hideableSidebar": false,
    "tableOfContents": {
      "minHeadingLevel": 2,
      "maxHeadingLevel": 3
    }
  },
  "baseUrlIssueBanner": true,
  "i18n": {
    "defaultLocale": "en",
    "locales": [
      "en"
    ],
    "localeConfigs": {}
  },
  "onDuplicateRoutes": "warn",
  "customFields": {},
  "plugins": [],
  "themes": [],
  "titleDelimiter": "|",
  "noIndex": false
};