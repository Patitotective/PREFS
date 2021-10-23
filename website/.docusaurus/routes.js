
import React from 'react';
import ComponentCreator from '@docusaurus/ComponentCreator';

export default [
  {
    path: '/PREFS/',
    component: ComponentCreator('/PREFS/','d35'),
    exact: true
  },
  {
    path: '/PREFS/blog/archive',
    component: ComponentCreator('/PREFS/blog/archive','5d9'),
    exact: true
  },
  {
    path: '/PREFS/search',
    component: ComponentCreator('/PREFS/search','c99'),
    exact: true
  },
  {
    path: '/PREFS/docs/0.2.56',
    component: ComponentCreator('/PREFS/docs/0.2.56','ea0'),
    routes: [
      {
        path: '/PREFS/docs/0.2.56/about/about',
        component: ComponentCreator('/PREFS/docs/0.2.56/about/about','62b'),
        exact: true,
        'sidebar': "version-0.2.56/about"
      },
      {
        path: '/PREFS/docs/0.2.56/about/changelog',
        component: ComponentCreator('/PREFS/docs/0.2.56/about/changelog','332'),
        exact: true,
        'sidebar': "version-0.2.56/about"
      },
      {
        path: '/PREFS/docs/0.2.56/about/license',
        component: ComponentCreator('/PREFS/docs/0.2.56/about/license','580'),
        exact: true,
        'sidebar': "version-0.2.56/about"
      },
      {
        path: '/PREFS/docs/0.2.56/about/support',
        component: ComponentCreator('/PREFS/docs/0.2.56/about/support','252'),
        exact: true,
        'sidebar': "version-0.2.56/about"
      },
      {
        path: '/PREFS/docs/0.2.56/api/cli',
        component: ComponentCreator('/PREFS/docs/0.2.56/api/cli','7b4'),
        exact: true,
        'sidebar': "version-0.2.56/api"
      },
      {
        path: '/PREFS/docs/0.2.56/api/functions',
        component: ComponentCreator('/PREFS/docs/0.2.56/api/functions','d09'),
        exact: true,
        'sidebar': "version-0.2.56/api"
      },
      {
        path: '/PREFS/docs/0.2.56/api/prefs-class',
        component: ComponentCreator('/PREFS/docs/0.2.56/api/prefs-class','d91'),
        exact: true,
        'sidebar': "version-0.2.56/api"
      },
      {
        path: '/PREFS/docs/0.2.56/resources',
        component: ComponentCreator('/PREFS/docs/0.2.56/resources','502'),
        exact: true,
        'sidebar': "version-0.2.56/docs"
      },
      {
        path: '/PREFS/docs/0.2.56/start',
        component: ComponentCreator('/PREFS/docs/0.2.56/start','0af'),
        exact: true,
        'sidebar': "version-0.2.56/docs"
      }
    ]
  },
  {
    path: '/PREFS/docs/next',
    component: ComponentCreator('/PREFS/docs/next','6d5'),
    routes: [
      {
        path: '/PREFS/docs/next/about/about',
        component: ComponentCreator('/PREFS/docs/next/about/about','f55'),
        exact: true,
        'sidebar': "about"
      },
      {
        path: '/PREFS/docs/next/about/changelog',
        component: ComponentCreator('/PREFS/docs/next/about/changelog','129'),
        exact: true,
        'sidebar': "about"
      },
      {
        path: '/PREFS/docs/next/about/license',
        component: ComponentCreator('/PREFS/docs/next/about/license','d21'),
        exact: true,
        'sidebar': "about"
      },
      {
        path: '/PREFS/docs/next/about/support',
        component: ComponentCreator('/PREFS/docs/next/about/support','59f'),
        exact: true,
        'sidebar': "about"
      },
      {
        path: '/PREFS/docs/next/api/cli',
        component: ComponentCreator('/PREFS/docs/next/api/cli','177'),
        exact: true,
        'sidebar': "api"
      },
      {
        path: '/PREFS/docs/next/api/functions',
        component: ComponentCreator('/PREFS/docs/next/api/functions','3b4'),
        exact: true,
        'sidebar': "api"
      },
      {
        path: '/PREFS/docs/next/api/prefs-class',
        component: ComponentCreator('/PREFS/docs/next/api/prefs-class','43f'),
        exact: true,
        'sidebar': "api"
      },
      {
        path: '/PREFS/docs/next/resources',
        component: ComponentCreator('/PREFS/docs/next/resources','194'),
        exact: true,
        'sidebar': "docs"
      },
      {
        path: '/PREFS/docs/next/start',
        component: ComponentCreator('/PREFS/docs/next/start','fa7'),
        exact: true,
        'sidebar': "docs"
      }
    ]
  },
  {
    path: '/PREFS/docs',
    component: ComponentCreator('/PREFS/docs','a84'),
    routes: [
      {
        path: '/PREFS/docs/about/about',
        component: ComponentCreator('/PREFS/docs/about/about','14a'),
        exact: true,
        'sidebar': "version-0.2.65/about"
      },
      {
        path: '/PREFS/docs/about/changelog',
        component: ComponentCreator('/PREFS/docs/about/changelog','7ab'),
        exact: true,
        'sidebar': "version-0.2.65/about"
      },
      {
        path: '/PREFS/docs/about/license',
        component: ComponentCreator('/PREFS/docs/about/license','f6d'),
        exact: true,
        'sidebar': "version-0.2.65/about"
      },
      {
        path: '/PREFS/docs/about/support',
        component: ComponentCreator('/PREFS/docs/about/support','567'),
        exact: true,
        'sidebar': "version-0.2.65/about"
      },
      {
        path: '/PREFS/docs/api/cli',
        component: ComponentCreator('/PREFS/docs/api/cli','86a'),
        exact: true,
        'sidebar': "version-0.2.65/api"
      },
      {
        path: '/PREFS/docs/api/functions',
        component: ComponentCreator('/PREFS/docs/api/functions','2d0'),
        exact: true,
        'sidebar': "version-0.2.65/api"
      },
      {
        path: '/PREFS/docs/api/prefs-class',
        component: ComponentCreator('/PREFS/docs/api/prefs-class','a10'),
        exact: true,
        'sidebar': "version-0.2.65/api"
      },
      {
        path: '/PREFS/docs/resources',
        component: ComponentCreator('/PREFS/docs/resources','5f8'),
        exact: true,
        'sidebar': "version-0.2.65/docs"
      },
      {
        path: '/PREFS/docs/start',
        component: ComponentCreator('/PREFS/docs/start','920'),
        exact: true,
        'sidebar': "version-0.2.65/docs"
      }
    ]
  },
  {
    path: '*',
    component: ComponentCreator('*')
  }
];
