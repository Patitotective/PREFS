
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
    component: ComponentCreator('/PREFS/docs','a07'),
    routes: [
      {
        path: '/PREFS/docs/about/about',
        component: ComponentCreator('/PREFS/docs/about/about','742'),
        exact: true,
        'sidebar': "version-0.2.55/about"
      },
      {
        path: '/PREFS/docs/about/changelog',
        component: ComponentCreator('/PREFS/docs/about/changelog','ceb'),
        exact: true,
        'sidebar': "version-0.2.55/about"
      },
      {
        path: '/PREFS/docs/about/license',
        component: ComponentCreator('/PREFS/docs/about/license','120'),
        exact: true,
        'sidebar': "version-0.2.55/about"
      },
      {
        path: '/PREFS/docs/about/support',
        component: ComponentCreator('/PREFS/docs/about/support','cdd'),
        exact: true,
        'sidebar': "version-0.2.55/about"
      },
      {
        path: '/PREFS/docs/api/cli',
        component: ComponentCreator('/PREFS/docs/api/cli','2a4'),
        exact: true,
        'sidebar': "version-0.2.55/api"
      },
      {
        path: '/PREFS/docs/api/functions',
        component: ComponentCreator('/PREFS/docs/api/functions','657'),
        exact: true,
        'sidebar': "version-0.2.55/api"
      },
      {
        path: '/PREFS/docs/api/prefs-class',
        component: ComponentCreator('/PREFS/docs/api/prefs-class','288'),
        exact: true,
        'sidebar': "version-0.2.55/api"
      },
      {
        path: '/PREFS/docs/resources',
        component: ComponentCreator('/PREFS/docs/resources','fcb'),
        exact: true,
        'sidebar': "version-0.2.55/docs"
      },
      {
        path: '/PREFS/docs/start',
        component: ComponentCreator('/PREFS/docs/start','dd9'),
        exact: true,
        'sidebar': "version-0.2.55/docs"
      }
    ]
  },
  {
    path: '*',
    component: ComponentCreator('*')
  }
];
