
import React from 'react';
import ComponentCreator from '@docusaurus/ComponentCreator';

export default [
  {
    path: '/PREFS/',
    component: ComponentCreator('/PREFS/','d35'),
    exact: true
  },
  {
    path: '/PREFS/__docusaurus/debug',
    component: ComponentCreator('/PREFS/__docusaurus/debug','477'),
    exact: true
  },
  {
    path: '/PREFS/__docusaurus/debug/config',
    component: ComponentCreator('/PREFS/__docusaurus/debug/config','d2e'),
    exact: true
  },
  {
    path: '/PREFS/__docusaurus/debug/content',
    component: ComponentCreator('/PREFS/__docusaurus/debug/content','c23'),
    exact: true
  },
  {
    path: '/PREFS/__docusaurus/debug/globalData',
    component: ComponentCreator('/PREFS/__docusaurus/debug/globalData','dce'),
    exact: true
  },
  {
    path: '/PREFS/__docusaurus/debug/metadata',
    component: ComponentCreator('/PREFS/__docusaurus/debug/metadata','553'),
    exact: true
  },
  {
    path: '/PREFS/__docusaurus/debug/registry',
    component: ComponentCreator('/PREFS/__docusaurus/debug/registry','091'),
    exact: true
  },
  {
    path: '/PREFS/__docusaurus/debug/routes',
    component: ComponentCreator('/PREFS/__docusaurus/debug/routes','553'),
    exact: true
  },
  {
    path: '/PREFS/blog/archive',
    component: ComponentCreator('/PREFS/blog/archive','5d9'),
    exact: true
  },
  {
    path: '/PREFS/docs',
    component: ComponentCreator('/PREFS/docs','d9f'),
    routes: [
      {
        path: '/PREFS/docs/about/about',
        component: ComponentCreator('/PREFS/docs/about/about','a3a'),
        exact: true,
        'sidebar': "about"
      },
      {
        path: '/PREFS/docs/about/changelog',
        component: ComponentCreator('/PREFS/docs/about/changelog','9c3'),
        exact: true,
        'sidebar': "about"
      },
      {
        path: '/PREFS/docs/about/license',
        component: ComponentCreator('/PREFS/docs/about/license','8a0'),
        exact: true,
        'sidebar': "about"
      },
      {
        path: '/PREFS/docs/about/support',
        component: ComponentCreator('/PREFS/docs/about/support','333'),
        exact: true,
        'sidebar': "about"
      },
      {
        path: '/PREFS/docs/api/cli',
        component: ComponentCreator('/PREFS/docs/api/cli','ddb'),
        exact: true,
        'sidebar': "api"
      },
      {
        path: '/PREFS/docs/api/functions',
        component: ComponentCreator('/PREFS/docs/api/functions','899'),
        exact: true,
        'sidebar': "api"
      },
      {
        path: '/PREFS/docs/api/prefs-class',
        component: ComponentCreator('/PREFS/docs/api/prefs-class','088'),
        exact: true,
        'sidebar': "api"
      },
      {
        path: '/PREFS/docs/resources',
        component: ComponentCreator('/PREFS/docs/resources','bd8'),
        exact: true,
        'sidebar': "docs"
      },
      {
        path: '/PREFS/docs/start',
        component: ComponentCreator('/PREFS/docs/start','993'),
        exact: true,
        'sidebar': "docs"
      }
    ]
  },
  {
    path: '*',
    component: ComponentCreator('*')
  }
];
