import { RouteRecordRaw } from 'vue-router';

const routes: RouteRecordRaw[] = [
  {
    path: '/',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      { path: '', name: 'IndexPage', component: () => import('pages/IndexPage.vue') },
      { path: '/measurements', name: 'MeasurementsPage', component: () => import('pages/MeasurementsPage.vue'), },
      { path: '/symptoms', name: 'SymptomsPage', component: () => import('pages/SymptomsPage.vue') },
      { path: '/activity', name: 'ActivityPage', component: () => import('pages/ActivityPage.vue') },
      { path: '/devices', name: 'DevicesPage', component: () => import('pages/DevicesPage.vue') },
      { path: '/family', name: 'FamilyPage', component: () => import('pages/FamilyPage.vue') },
      { path: '/documents', name: 'DocumentsPage', component: () => import('pages/DocumentsPage.vue') },
      { path: '/settings', name: 'SettingsPage', component: () => import('pages/SettingsPage.vue') }
    ],
  },
  {
    path: '/auth',
    component: () => import('layouts/UnauthLayout.vue'),
    children: [
      { path: '/auth', name: 'AuthPage', component: () => import('pages/AuthPage.vue') }
    ]
  },

  // Always leave this as last one,
  // but you can also remove it
  {
    path: '/:catchAll(.*)*',
    component: () => import('pages/ErrorNotFound.vue'),
  },
];

export default routes;
