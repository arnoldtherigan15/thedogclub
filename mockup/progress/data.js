// Single source for the client progress page (mockup/progress/) and the internal tracker (docs/tracker.html).
// To update the client: edit this file, then commit and push. The page refreshes in about a minute.
//
// status for phases:  'done' | 'active' | 'todo'
// status for needs:   'done' | 'todo'
// status for payments: 'paid' | 'due' | 'upcoming'
// health:             'on-track' | 'waiting' | 'delayed'
window.PROJECT = {
  updated: '2026-11-02',
  start: '2026-11-02',
  target: '2026-11-23',
  health: 'waiting',
  healthNote: 'We are waiting for your choice of design direction, the next step in week 1.',
  pagesBuilt: 0,
  pagesTotal: 27,
  auditFixed: 0,
  auditTotal: 14,

  phases: [
    { name: 'Kickoff & design choice', from: '2026-11-02', to: '2026-11-02', status: 'active',
      text: 'You choose one of the four design directions. We collect your brand files, photos and latest prices.' },
    { name: 'Design', from: '2026-11-03', to: '2026-11-06', status: 'todo',
      text: 'Homepage and Dog Daycare page in the chosen direction, on desktop and mobile. Up to 2 rounds of major revisions.',
      gate: 'Design approved in writing' },
    { name: 'Build', from: '2026-11-09', to: '2026-11-13', status: 'todo',
      text: 'All 27 pages are built on a private preview link, with your real content and prices.',
      gate: 'Payment 2, once all pages are built' },
    { name: 'SEO & testing', from: '2026-11-16', to: '2026-11-17', status: 'todo',
      text: 'Search optimisation, speed, old-link redirects, and checks on phone and laptop.' },
    { name: 'Your review', from: '2026-11-17', to: '2026-11-19', status: 'todo',
      text: 'You check every page on the preview link and send one combined list of corrections.',
      gate: 'One list of corrections' },
    { name: 'Fixes & final payment', from: '2026-11-20', to: '2026-11-20', status: 'todo',
      text: 'We apply the corrections. You confirm the site is ready to go live.',
      gate: 'Written go-live confirmation and payment 3' },
    { name: 'Go live', from: '2026-11-23', to: '2026-11-23', status: 'todo',
      text: 'The new website goes live on thedogclub.id. Your @thedogclub.id email is not affected.' },
    { name: '30-day warranty', from: '2026-11-23', to: '2026-12-23', status: 'todo',
      text: 'Any bug in our work is fixed free of charge. Search Console is monitored and a short report follows.' },
  ],

  needs: [
    { title: 'Choose a design direction', due: '2026-11-02', status: 'todo', link: '../design/', linkText: 'View the options',
      text: 'Pick one of the four options, or tell us which parts you like from each.' },
    { title: 'Share a Google Drive folder with your logo and brand files', due: '2026-11-04', status: 'todo', link: '../onboarding/#drive', linkText: 'How to set it up',
      text: 'The original logo file (SVG, AI, PDF or large PNG), plus colour codes and fonts if you have them.' },
    { title: 'Upload original photos', due: '2026-11-04', status: 'todo', link: '../onboarding/#drive', linkText: 'What to include',
      text: 'Park, pools, villa, spa, team and dogs. Original camera or phone files, not screenshots.' },
    { title: 'Confirm prices and schedule', due: '2026-11-04', status: 'todo',
      text: 'We are using your February 2026 price list. Please confirm it is still current and clarify these points:',
      points: [
        'Monday opening hours: 9am–6pm, 10am–4pm or 9am–4pm?',
        'Hotel check-in and check-out times',
        'Current prices for pet taxi, in-house vet and dog walking',
      ] },
    { title: 'Answer 7 short questions', due: '2026-11-04', status: 'todo', link: '../onboarding/#info', linkText: 'See the questions',
      text: 'Locations, member sign-up, policies and the invoice name. A WhatsApp reply is fine.' },
    { title: 'Send design feedback', due: '2026-11-05', status: 'todo',
      text: 'One combined list per round, so nothing gets lost.' },
    { title: 'Share customer reviews', due: '2026-11-06', status: 'todo', optional: true,
      text: 'Any reviews you are happy to show on the website.' },
    { title: 'Approve the design in writing', due: '2026-11-06', status: 'todo',
      text: 'A WhatsApp message saying "Design approved" is enough. The build starts after this.' },
    { title: 'Create a GitHub account', due: '2026-11-09', status: 'todo', link: '../onboarding/#github', linkText: 'Step-by-step guide',
      text: 'After the design is final. This is where your website code will live, in your name.' },
    { title: 'Give access to Google Search Console', due: '2026-11-09', status: 'todo', optional: true, link: '../onboarding/#search-console', linkText: 'Step-by-step guide',
      text: 'Helps protect your Google ranking during the move and gives us a before-and-after report.' },
    { title: 'Share the old WordPress admin', due: '2026-11-09', status: 'todo', optional: true,
      text: 'Lets us recover original images from the current website. Please do not send passwords over WhatsApp.' },
    { title: 'Payment 2: IDR 2,250,000', due: '2026-11-13', status: 'todo',
      text: 'Due once all pages are built, before SEO and testing start. An invoice will be sent then.' },
    { title: 'Review all pages on the preview link', due: '2026-11-19', status: 'todo',
      text: 'Check content and prices, then send one combined list of corrections.' },
    { title: 'Create a Netlify account', due: '2026-11-20', status: 'todo', link: '../onboarding/#netlify', linkText: 'Step-by-step guide',
      text: 'Free hosting for the new website, with no monthly fee.' },
    { title: 'Confirm go-live and make payment 3: IDR 1,500,000', due: '2026-11-20', status: 'todo',
      text: 'The website goes live after the final payment is received.' },
    { title: 'Be ready for a 15-minute call with your DomaiNesia login', due: '2026-11-23', status: 'todo', link: '../onboarding/#domain', linkText: 'What happens',
      text: 'On the morning of go-live, someone logs in to my.domainesia.com and shares their screen while we switch the domain.' },
    { title: 'Keep the old website hosting active', due: '2026-11-30', status: 'todo',
      text: 'Please do not cancel it until we confirm the new website has been stable for at least one week.' },
  ],

  payments: [
    { name: 'Payment 1: down payment', when: 'Project start', amount: 'IDR 3,750,000', status: 'paid' },
    { name: 'Payment 2: progress', when: 'All pages built, before SEO & testing', amount: 'IDR 2,250,000', status: 'upcoming' },
    { name: 'Payment 3: final', when: 'Before go-live', amount: 'IDR 1,500,000', status: 'upcoming' },
  ],

  // Newest first. Add one every Friday and at each milestone.
  updates: [
    { date: '2026-11-02', title: 'Project started',
      done: ['Down payment received', 'Website audit completed', 'Four design directions shared'],
      next: ['Develop the chosen direction into the homepage and Dog Daycare page'],
      need: ['Your choice of design direction'] },
  ],
};
