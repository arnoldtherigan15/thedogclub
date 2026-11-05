// Single source for the client progress page (client/progress/) and the internal tracker (docs/tracker.html).
// To update the client: edit this file, then commit and push. The page refreshes in about a minute.
//
// status for phases:  'done' | 'active' | 'todo'
// status for needs:   'done' | 'todo'
// status for payments: 'paid' | 'due' | 'upcoming'
// health:             'on-track' | 'waiting' | 'delayed'
window.PROJECT = {
  updated: '2026-11-05',
  start: '2026-11-02',
  target: '2026-11-23',
  health: 'on-track',
  healthNote: 'All 11 sections are built and live on the preview link, ahead of schedule. Next: your feedback and payment 2, then SEO and testing.',
  pagesBuilt: 11,
  pagesTotal: 11,
  // Fixed on the new site and checked: Pawsi sign-up (1), clickable locations (2), homepage text (4),
  // one H1 per page (7), alt text (10), no empty slider (14). The rest are covered in SEO & testing.
  auditFixed: 6,
  auditTotal: 14,

  phases: [
    { name: 'Kickoff & your design', from: '2026-11-02', to: '2026-11-04', status: 'done',
      text: 'Down payment received. You shared your Canva design, brand files, photos, price list, FAQ and house rules.' },
    { name: 'Design', from: '2026-11-04', to: '2026-11-05', status: 'done',
      text: 'Your Canva design turned into the website, with the header, footer, mobile version and animations that Canva does not cover.' },
    { name: 'Build', from: '2026-11-04', to: '2026-11-05', status: 'done',
      text: 'All 11 sections are built on the preview link with your real content: Services, Facility, Locations, House Rules, FAQ, Book a Visit, Partnership, Loyalty Program, About Us and the footer.',
      gate: 'Payment 2, once all pages are built' },
    { name: 'Your feedback', from: '2026-11-05', to: '2026-11-13', status: 'active',
      text: 'You check the preview on phone and laptop and add your feedback in the shared spreadsheet. We work through it as it comes in.' },
    { name: 'SEO & testing', from: '2026-11-16', to: '2026-11-17', status: 'todo',
      text: 'Search optimisation, speed, old-link redirects, and checks on phone and laptop.' },
    { name: 'Final review', from: '2026-11-17', to: '2026-11-19', status: 'todo',
      text: 'You check every section one last time and send any final corrections.',
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
    { title: 'Share your website design', due: '2026-11-04', status: 'done',
      text: 'Canva design with 12 screens.' },
    { title: 'Share your logo, brand files and photos', due: '2026-11-04', status: 'done',
      text: 'Logo, fonts, colour codes and photos for every page.' },
    { title: 'Answer the design questions', due: '2026-11-05', status: 'done',
      text: 'Addresses, opening hours, FAQ, footer, loyalty design and the referral form. Thank you.' },
    { title: 'Payment 2: IDR 2,250,000', due: '2026-11-12', status: 'todo', link: '../invoice-2/', linkText: 'View invoice',
      text: 'All pages are built, so payment 2 is now due. SEO and testing start once it is received.' },
    { title: 'Add your feedback in the shared spreadsheet', due: '2026-11-13', status: 'todo',
      text: 'Open the preview at develop--thedogclub-staging.netlify.app on phone and laptop, then add one row per change in the "Design feedback" tab.' },
    { title: 'Answer the open questions in the spreadsheet', due: '2026-11-13', status: 'todo',
      text: 'The "Open questions" tab lists what is still needed, for example the referral rewards, TikTok link and Booking & Refunds text.' },
    { title: 'Create a GitHub account', due: '2026-11-13', status: 'todo', link: '../onboarding/#github', linkText: 'Step-by-step guide',
      text: 'This is where your website code will live, in your name.' },
    { title: 'Give access to Google Search Console', due: '2026-11-13', status: 'todo', optional: true, link: '../onboarding/#search-console', linkText: 'Step-by-step guide',
      text: 'Helps protect your Google ranking during the move and gives us a before-and-after report.' },
    { title: 'Final check of every section', due: '2026-11-19', status: 'todo',
      text: 'One last look at content and details, with any final corrections in the spreadsheet.' },
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
    { name: 'Payment 2: progress', when: 'All pages built, before SEO & testing', amount: 'IDR 2,250,000', status: 'due' },
    { name: 'Payment 3: final', when: 'Before go-live', amount: 'IDR 1,500,000', status: 'upcoming' },
  ],

  // Newest first. Add one every Friday and at each milestone.
  updates: [
    { date: '2026-11-05', title: 'All sections built',
      done: [
        'All 11 sections built from your Canva design, on desktop and phone',
        'Addresses, opening hours, FAQ, footer and Loyalty Program (option B) added from your answers',
        'Preview online at develop--thedogclub-staging.netlify.app, hidden from Google',
      ],
      next: ['Work through your feedback', 'SEO and testing once payment 2 is received'],
      need: ['Payment 2', 'Your feedback and answers in the shared spreadsheet'] },
    { date: '2026-11-04', title: 'Your design is in',
      done: ['Received your Canva design, logo, photos, price list, FAQ and house rules', 'Received your answers on Ungasan, Seseh, Berawa, Pawsi registration and the Book a Visit contacts', 'Page list set: 11 pages based on your design, with Friends of The Dog Club and a short refund section added'],
      next: ['Build the homepage, header and footer on desktop and mobile for your approval'],
      need: ['Answers to the questions under "Needed from you next"'] },
    { date: '2026-11-02', title: 'Project started',
      done: ['Down payment received', 'Website audit completed'],
      next: ['Prepare the design'],
      need: [] },
  ],
};
