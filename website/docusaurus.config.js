// @ts-check
// Note: type annotations allow type checking and IDEs autocompletion

const lightCodeTheme = require('prism-react-renderer/themes/nightOwlLight');
const darkCodeTheme = require('prism-react-renderer/themes/okaidia');

/** @type {import('@docusaurus/types').Config} */
const config = {
  title: 'PREFS',
  tagline: 'Manage your app preferences with PREFS.',
  url: 'https://patitotective.github.io',
  baseUrl: '/PREFS/', 
  onBrokenLinks: 'throw', 
  onBrokenMarkdownLinks: 'warn',
  favicon: 'img/favicon.png',
  organizationName: 'Patitotective', // Usually your GitHub org/user name.
  projectName: 'PREFS', // Usually your repo name.

  presets: [
    [
      '@docusaurus/preset-classic',
      /** @type {import('@docusaurus/preset-classic').Options} */
      ({
        docs: {
          sidebarPath: require.resolve('./sidebars.js'), 
          // Please change this to your repo.
          editUrl: 'https://github.com/Patitotective/PREFS/tree/main/website',
          showLastUpdateAuthor: true,
          showLastUpdateTime: true,          
        },
        blog: {
          showReadingTime: true,
          // Please change this to your repo.
          editUrl:
            'https://github.com/Patitotective/PREFS',
        }, 
        theme: {
          customCss: require.resolve('./src/css/custom.css'),
        },
      }),
    ],
  ],

  themeConfig:
    /** @type {import('@docusaurus/preset-classic').ThemeConfig} */
    ({
      image: 'img/dark_logo.png', 
      colorMode: {
        defaultMode: "dark", 
      }, 
      announcementBar: {
        id: 'github_star',
        content:
          '<b>⭐ If you like PREFS, please consider giving a star on <a href="https://github.com/Patitotective/PREFS">GitHub</a> ❤️</b>',
        backgroundColor: '#fafbfc',
        textColor: '#091E42',
        isCloseable: true,
      },       
      navbar: {
        title: 'PREFS', 
        logo: {
          alt: 'PREFS logo',
          src: 'img/navbar_logo.png', 
        },
        items: [
          {
            type: 'doc',
            position: 'left',
            docId: 'start',
            label: 'Docs',
          }, 
          {
            type: 'doc',
            position: 'left',
            docId: 'api/prefs-class',
            label: 'API Reference',
          }, 
          {
            type: 'doc',
            position: 'left', 
            docId: 'about/about', 
            label: 'About'
          }, 
          {
            type: 'docsVersionDropdown', 
            position: 'right', 
          },     
        ],
      
      },

      footer: {
        style: 'dark',
        links: [
          {
            title: 'Links',
            items: [
              {
                label: 'Source code',
                href: 'https://github.com/Patitotective/PREFS',
              },
              {
                label: 'Pypi page',
                href: 'https://pypi.org/project/PREFS/',
              },
              {
                label: 'Documentation',
                href: 'https://patitotective.github.io/PREFS/',
              }
            ],
          },
          {
            title: 'Contact me',
            items: [
              {
                label: 'Discord: Patitotective#0127',
                href: "https://patitotective.github.io/PREFS/About/about"
              },
              {
                label: 'Mail: cristobalriaga@gmail.com',
                href: 'mailto:cristobalriaga@gmail.com',
              },
            ],
          },
        ],
        
        copyright: `Copyright © ${new Date().getFullYear()} My Project, Inc. Built with Docusaurus.`,
      },
      prism: {
        theme: lightCodeTheme,
        darkTheme: darkCodeTheme,
      },
    }),
};

module.exports = config;
